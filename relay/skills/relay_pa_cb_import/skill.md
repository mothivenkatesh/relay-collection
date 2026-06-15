---
name: relay-pa-cb-import
description: Cashfree KYC workflow for PA-CB Import Direction — foreign merchant and cross-border buyer KYC under FEMA, RBI PA-CB guidelines, and IDPMS mandate. ₹25L per-transaction hard cap enforced at API layer, buyer due diligence triggered at ₹2.5L, IDPMS flagging, Small PPI instrument excluded from cross-border, foreign entity UBO at 10% with nationality. Generates Node.js integration code. ~₹30–50 per onboarding.
triggers:
  - /relay-pa-cb-import
  - cross-border import KYC
  - foreign merchant verification
  - PA-CB import direction
  - IDPMS flagging workflow
  - buyer due diligence workflow
  - cross-border buyer verification
tools:
  - Read/Write
---

# PA-CB Import Direction — Foreign Merchant / Buyer KYC

> ₹25L per-transaction hard cap · Buyer DD at ₹2.5L · IDPMS flagging · Small PPI excluded · Foreign entity UBO at 10% with nationality · FEMA + PA-CB compliant · ~₹30–50 per onboarding

---

## Regulatory context

This workflow covers Cashfree's **PA-CB licence — Import direction**: enabling Indian buyers to pay foreign merchants (imports of goods or services).

| Requirement | Rule |
|---|---|
| ₹25L per-transaction cap | Hard cap per PA-CB guidelines — no override possible |
| Buyer due diligence | Triggered at ₹2.5L per transaction unit (import direction) |
| IDPMS flagging | Mandatory for all cross-border import payments per FEMA 1999 |
| Small PPI exclusion | Small PPI wallets CANNOT be used as payment instrument for cross-border imports |
| Full KYC PPI only | Only Full KYC PPI (₹2L balance limit) permitted for cross-border transactions |
| Foreign entity UBO | 10% threshold — collect nationality + country of residence for all UBO ≥10% |
| FATF country risk | High/black-list countries trigger EDD — use relay-edd for those cases |

---

## Two flows this skill handles

**Flow A — Foreign merchant onboarding**: KYC the foreign entity selling into India. Done once; enables recurring Indian buyer payments to that merchant.

**Flow B — High-value buyer due diligence**: Triggered at ₹2.5L per transaction. Verifies Indian buyer's source of funds for the specific import payment.

---

## Quickstart — 20 minutes to live

### Environment variables

```env
CASHFREE_CLIENT_ID=
CASHFREE_CLIENT_SECRET=
CASHFREE_BASE_URL=https://sandbox.cashfree.com/verification
CASHFREE_WEBHOOK_SECRET=
BASE_URL=http://localhost:3000
RELAY_WORKFLOW_ID=
IDPMS_API_URL=            # Cashfree internal or your IDPMS integration endpoint
BUYER_DD_THRESHOLD=250000  # ₹2.5L — statutory buyer due diligence trigger
TXN_CAP_INR=2500000        # ₹25L — hard cap per PA-CB guidelines
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "pa_cb_import_kyc",
  "description": "PA-CB Import — foreign merchant KYC + buyer DD at ₹2.5L + IDPMS flagging",
  "trigger": "api",
  "inputs": ["entity_id", "flow_type", "entity_country", "mobile", "transaction_amount_inr"],
  "nodes": [
    { "id": "txn-cap-gate", "type": "condition",
      "if": "transaction_amount_inr > {{TXN_CAP_INR}}", "then": "REJECT",
      "note": "₹25L per-transaction hard cap — mandatory per PA-CB guidelines. No manual override." },

    { "id": "ppi-instrument-check", "type": "condition",
      "if": "payment_instrument == 'SMALL_PPI'", "then": "REJECT",
      "note": "Small PPI wallets are EXCLUDED from cross-border import payments per RBI PA-CB circular" },

    { "id": "flow-gate", "type": "condition",
      "switch": "flow_type",
      "cases": {
        "FOREIGN_MERCHANT": "foreign-merchant-kyc",
        "BUYER_DUE_DILIGENCE": "buyer-dd-gate"
      }
    },

    { "id": "foreign-merchant-kyc", "type": "sequence",
      "note": "Foreign entity onboarding — passport/equivalent OVD + entity docs + face match + UBO",
      "nodes": [
        { "id": "consent-fm", "type": "ui", "template": "dpdp_consent", "on_denied": "REJECT" },
        { "id": "entity-doc-upload", "type": "ui", "template": "document_upload",
          "required_docs": [
            "certificate_of_incorporation_or_equivalent",
            "authorised_signatory_passport_or_national_id",
            "proof_of_business_address"
          ],
          "note": "Foreign equivalent of Indian OVD — jurisdiction-specific documents accepted" },
        { "id": "foreign-ocr", "type": "api", "call": "POST /bharat-ocr", "doc": "PASSPORT",
          "content_type": "multipart/form-data",
          "on_forgery": "REJECT",
          "note": "Passport OCR for authorised signatory identity" },
        { "id": "liveness-fm", "type": "api", "call": "POST /face-liveness",
          "content_type": "multipart/form-data",
          "retry_flow": [
            { "attempt": 1, "on_fail": "liveness-guide-fm-2" },
            { "attempt": 2, "on_fail": "liveness-guide-fm-3" },
            { "attempt": 3, "on_fail": "vkyc-fm" }
          ]},
        { "id": "liveness-guide-fm-2", "type": "ui",
          "msg": "Liveness check failed. Better lighting and a plain background helps.", "then": "liveness-fm" },
        { "id": "liveness-guide-fm-3", "type": "ui",
          "msg": "One more attempt. Full face visible, no glasses.", "then": "liveness-fm" },
        { "id": "vkyc-fm", "type": "api", "call": "POST /vkyc",
          "meta": { "regulator": "PA-CB", "geolocation_required": true },
          "note": "VKYC escape hatch — triggered on device-class liveness failure (documented on Helio/Snapdragon 450 chipsets). Prevents hard-REJECT for a legitimate foreign merchant on a broken SDK environment.",
          "states": { "APPROVE": "face-match-fm", "REJECT": "REJECT",
                      "UNABLE_TO_VALIDATE": "MANUAL_REVIEW", "FAILED": "REJECT" }},
        { "id": "face-match-fm", "type": "api", "call": "POST /face-match",
          "content_type": "multipart/form-data",
          "threshold": 0.75, "on_fail": "REJECT" },
        { "id": "ubo-fm", "type": "ui", "template": "ubo_declaration",
          "threshold_pct": 10,
          "required_fields": ["shareholder_name", "shareholding_pct", "nationality", "country_of_residence", "pep_status"],
          "note": "Foreign entity UBO — nationality and country of residence mandatory for FATF risk scoring" }
      ]},

    { "id": "buyer-dd-gate", "type": "condition",
      "if": "transaction_amount_inr >= {{BUYER_DD_THRESHOLD}}", "then": "buyer-dd-flow",
      "else": "idpms-flag",
      "note": "Buyer DD only triggered at ₹2.5L and above" },

    { "id": "buyer-dd-flow", "type": "sequence",
      "note": "High-value buyer due diligence — source of funds for specific import transaction",
      "nodes": [
        { "id": "consent-buyer", "type": "ui", "template": "dpdp_consent", "on_denied": "REJECT" },
        { "id": "mob-send", "type": "api", "call": "POST /mobile360/otp/send" },
        { "id": "mob-verify", "type": "api", "call": "POST /mobile360/otp/verify",
          "prefill_outputs": ["pan", "name"] },
        { "id": "pan-buyer", "type": "api", "call": "POST /pan", "version": "2024-12-01",
          "on_invalid": "REJECT" },
        { "id": "sof-declaration", "type": "ui", "template": "source_of_funds_declaration",
          "required_fields": ["fund_source", "fund_origin_country", "purpose_of_import"],
          "note": "Source of funds declaration mandatory for import payments ≥₹2.5L" },
        { "id": "sof-docs", "type": "ui", "template": "document_upload",
          "required_docs": ["salary_slip_or_itr_or_bank_statement"],
          "note": "3 months bank statement or latest ITR accepted" }
      ]},

    { "id": "idpms-flag", "type": "api", "call": "{{IDPMS_API_URL}}/register",
      "in": {
        "entity_id": "{{entity_id}}",
        "flow_type": "{{flow_type}}",
        "transaction_amount_inr": "{{transaction_amount_inr}}",
        "entity_country": "{{entity_country}}"
      },
      "outputs": ["idpms_ref_number"],
      "note": "IDPMS flagging mandatory for all import payments per FEMA 1999" },

    { "id": "risk-gate", "type": "gate", "rules": [
        { "if": "amber_flags == 0", "out": "APPROVE" },
        { "if": "amber_flags == 1", "out": "MANUAL_REVIEW" },
        { "if": "amber_flags >= 2", "out": "REJECT" }
    ]}
  ]
}
```

---

### Step 2 — Backend (Node.js)

```javascript
// server.js
import express from 'express';
import crypto  from 'crypto';

const app = express();
app.use(express.json({ verify: (req, _, buf) => { req.rawBody = buf; } }));

const {
  CASHFREE_CLIENT_ID, CASHFREE_CLIENT_SECRET,
  CASHFREE_WEBHOOK_SECRET, RELAY_WORKFLOW_ID, BASE_URL,
  TXN_CAP_INR      = '2500000',
  BUYER_DD_THRESHOLD = '250000',
} = process.env;

// Fix 4 — Startup validation: statutory constants must not be overridden
// PA-CB guidelines set ₹25L hard cap with no exceptions
const TXN_CAP = parseInt(TXN_CAP_INR);
if (TXN_CAP !== 2500000) {
  throw new Error(`FATAL: TXN_CAP_INR must be 2500000 per PA-CB statutory cap. Got: ${TXN_CAP}. Do not change this value.`);
}

// Fix 2 — Idempotency store (use Redis in production; Map shown for clarity)
const processedWebhooks = new Map(); // replace with redis.set(key, '1', 'EX', 86400)

// Fix 5 — Aggregate transaction monitoring: structuring detection within 24h window
const entityTxnLog = new Map(); // replace with Redis sorted set keyed by entity_id
function checkStructuring(entityId, amountInr) {
  const now = Date.now();
  const window = 24 * 60 * 60 * 1000; // 24 hours
  const log = entityTxnLog.get(entityId) || [];
  const recent = log.filter(e => now - e.ts < window);
  const aggregate = recent.reduce((sum, e) => sum + e.amount, 0) + amountInr;
  if (aggregate > TXN_CAP) {
    return { structuring: true, aggregate24h: aggregate };
  }
  recent.push({ ts: now, amount: amountInr });
  entityTxnLog.set(entityId, recent);
  return { structuring: false, aggregate24h: aggregate };
}

// Enforce ₹25L cap before triggering any KYC workflow
function enforceTransactionCap(amountInr) {
  if (amountInr > TXN_CAP) {
    throw Object.assign(
      new Error(`Transaction ₹${amountInr} exceeds PA-CB cap of ₹25L`),
      { code: 'TXN_CAP_EXCEEDED' }
    );
  }
}

app.post('/api/cb-import/start', async (req, res) => {
  const {
    entityId,
    flowType,              // 'FOREIGN_MERCHANT' | 'BUYER_DUE_DILIGENCE'
    entityCountry,
    mobile,
    transactionAmountInr,
    paymentInstrument,     // required — must be one of ALLOWED_INSTRUMENTS
  } = req.body;

  // Fix 3 — Strict enum validation: default-deny on missing/unknown/wrong-case instrument
  const ALLOWED_INSTRUMENTS = ['UPI', 'CARD', 'NETBANKING', 'FULL_KYC_PPI'];
  if (!paymentInstrument || !ALLOWED_INSTRUMENTS.includes(paymentInstrument)) {
    return res.status(400).json({
      error: `paymentInstrument is required and must be one of: ${ALLOWED_INSTRUMENTS.join(', ')}`,
      code: 'INSTRUMENT_REQUIRED',
      received: paymentInstrument ?? null,
    });
  }
  // SMALL_PPI is blocked by the allowlist above — no separate check needed

  // Hard cap: reject before even opening KYC session
  try {
    enforceTransactionCap(transactionAmountInr);
  } catch (err) {
    return res.status(400).json({ error: err.message, code: err.code });
  }

  // Fix 5 — Structuring detection: aggregate within 24h before starting KYC
  const { structuring, aggregate24h } = checkStructuring(entityId, transactionAmountInr);
  if (structuring) {
    return res.status(400).json({
      error: `Aggregate transactions for entity ${entityId} exceed ₹25L within 24h (₹${aggregate24h}). Possible structuring — flagged for review.`,
      code: 'STRUCTURING_DETECTED',
    });
  }

  const r = await fetch(
    `https://api.cashfree.com/relay/v1/workflows/${RELAY_WORKFLOW_ID}/runs`,
    {
      method: 'POST',
      headers: {
        'x-client-id':     CASHFREE_CLIENT_ID,
        'x-client-secret': CASHFREE_CLIENT_SECRET,
        'Content-Type':    'application/json',
      },
      body: JSON.stringify({
        entity_id:              entityId,
        flow_type:              flowType,
        entity_country:         entityCountry,
        mobile,
        transaction_amount_inr: transactionAmountInr,
        payment_instrument:     paymentInstrument,
        redirect_url: `${BASE_URL}/cb-import/done`,
        webhook_url:  `${BASE_URL}/api/cb-import/webhook`,
      }),
    }
  );

  const { run_id, hosted_url } = await r.json();
  res.json({ kycUrl: hosted_url, runId: run_id });
});

app.post('/api/cb-import/webhook', (req, res) => {
  const sig = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody).digest('base64');
  if (sig !== expected) return res.status(401).send('Bad signature');

  // Fix 2 — Idempotency: deduplicate retried webhook deliveries
  const idempotencyKey = req.body.run_id || req.headers['x-cashfree-idempotency-key'];
  if (idempotencyKey && processedWebhooks.has(idempotencyKey)) {
    return res.json({ received: true, duplicate: true });
  }
  if (idempotencyKey) processedWebhooks.set(idempotencyKey, Date.now());

  const { entity_id, status, flags, flow_type, idpms_ref_number } = req.body;

  switch (status) {
    case 'APPROVED':
      if (flow_type === 'FOREIGN_MERCHANT') {
        activateForeignMerchant(entity_id, idpms_ref_number);
      } else {
        approveImportTransaction(entity_id, idpms_ref_number);
      }
      break;

    case 'REJECTED':
      // ❌ Forgery, face mismatch, ₹25L cap exceeded
      rejectEntity(entity_id, flags);
      if (flags.includes('fraud_account') || flags.includes('pep_confirmed')) {
        logToFIU(entity_id, flags); // STR filing
      }
      break;

    case 'MANUAL_REVIEW':
      queueForCompliance(entity_id, flags, flow_type);
      break;
  }

  res.json({ received: true });
});

async function activateForeignMerchant(id, idpmsRef)  { /* enable for Indian buyer payments */ }
async function approveImportTransaction(id, idpmsRef)  { /* allow import payment to proceed */ }
async function rejectEntity(id, flags)                { /* block entity */ }
async function queueForCompliance(id, flags, type)    { /* ops queue */ }
async function logToFIU(id, flags)                    { /* STR queue */ }

app.listen(3000);
```

---

### Step 3 — Test it

```bash
# Foreign merchant onboarding
curl -X POST http://localhost:3000/api/cb-import/start \
  -H "Content-Type: application/json" \
  -d '{"entityId":"fm_001","flowType":"FOREIGN_MERCHANT","entityCountry":"US","mobile":"9999999999","transactionAmountInr":0,"paymentInstrument":"CARD"}'

# High-value buyer DD (₹3L transaction)
curl -X POST http://localhost:3000/api/cb-import/start \
  -H "Content-Type: application/json" \
  -d '{"entityId":"buyer_001","flowType":"BUYER_DUE_DILIGENCE","entityCountry":"US","mobile":"9999999998","transactionAmountInr":300000,"paymentInstrument":"NETBANKING"}'

# Blocked — Small PPI instrument (returns 400)
curl -X POST http://localhost:3000/api/cb-import/start \
  -H "Content-Type: application/json" \
  -d '{"entityId":"buyer_002","flowType":"BUYER_DUE_DILIGENCE","entityCountry":"UK","mobile":"9999999997","transactionAmountInr":100000,"paymentInstrument":"SMALL_PPI"}'

# Blocked — ₹25L cap exceeded (returns 400)
curl -X POST http://localhost:3000/api/cb-import/start \
  -H "Content-Type: application/json" \
  -d '{"entityId":"buyer_003","flowType":"BUYER_DUE_DILIGENCE","entityCountry":"DE","mobile":"9999999996","transactionAmountInr":2600000,"paymentInstrument":"NETBANKING"}'
```

---

## FATF country risk routing

| FATF tier | UBO requirements | Monitoring | Escalation |
|---|---|---|---|
| Low (FATF member, white-list) | Standard 10% UBO | Monthly | None |
| Medium (grey-list adjacent) | 10% UBO + enhanced source of funds | Weekly | Soft review |
| High (FATF grey-list) | Full EDD — use `/relay-edd` | Daily + STR review | relay-edd |
| Prohibited (FATF black-list) | REJECT immediately | N/A | REJECT |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| ₹25L per-transaction hard cap (API layer) | IDPMS API integration | AD Bank portal filing |
| Small PPI instrument exclusion | | FEMA compliance monitoring |
| Foreign merchant KYC (passport OCR + face match) | | Sanctions screening — use relay-edd |
| Buyer due diligence at ₹2.5L threshold | | FATF country risk data |
| Source of funds declaration UI | | |
| 10% UBO declaration (nationality + country) | | |
| IDPMS registration flag | | |

**Regulation:** FEMA 1999 · RBI AP (DIR Series) · RBI PA-CB Guidelines · PMLA Section 11A · DPDP Act 2023

**Cost:** Foreign merchant onboarding ~₹35–50 · Buyer DD ~₹30–40 per transaction

---

## MCP — coming soon

```
/relay-pa-cb-import

→ Claude: "Foreign merchant or buyer DD? Entity country? Transaction amount?"
→ Calls Relay MCP → creates PA-CB import workflow with IDPMS flagging
→ Returns RELAY_WORKFLOW_ID
```
