---
name: relay-pa-merchant
description: Cashfree KYC workflow for PA Merchant Onboarding — mandatory under RBI PA Master Direction 2025 (RBI/DPSS/2025-26/141). CKYCR-first, tiered CDD by annual turnover (Simplified CDD ≤₹40L vs Full CDD >₹40L), background/antecedent verification, 10% beneficial ownership threshold, FIU-IND obligations, CKYCR upload within 10 days. Board-approved KYC policy required pre-go-live. Generates Node.js integration code and Relay workflow spec. ~₹20–35 per merchant onboarding.
triggers:
  - /relay-pa-merchant
  - merchant onboarding KYC
  - PA merchant verification
  - payment aggregator merchant KYC
  - merchant due diligence relay
tools:
  - Read/Write
---

# PA Merchant Onboarding KYC

> CKYCR-first · Tiered CDD by turnover (Simplified ≤₹40L / Full CDD >₹40L) · 10% UBO threshold · Antecedent check mandatory · CKYCR upload within 10 days · RBI PA MD 2025

---

## Regulatory context

This workflow implements merchant onboarding KYC as mandated by **RBI PA Master Direction 2025 (RBI/DPSS/2025-26/141, September 15, 2025)** — the operative document superseding all prior PA circulars (2020, 2021, 2023).

| Mandate | Threshold / Rule |
|---|---|
| CKYCR lookup | First port of call for ALL merchant onboarding |
| Simplified CDD | Available only for merchants with ≤₹40L annual turnover |
| Full CDD | Mandatory for >₹40L annual turnover or CKYCR record not found |
| Beneficial ownership disclosure | 10% shareholding threshold (Oct 2023 KYC MD amendment) |
| Background/antecedent check | Mandatory for all merchants (Clause 8.3, PA MD 2025) |
| CKYCR upload | Within 10 business days of KYC completion |
| STR/CTR filing | STR: 7 working days from suspicion; CTR: 15th of succeeding month for >₹10L |

> **Board-approved KYC/AML policy is a prerequisite.** Relay cannot substitute for a board-approved policy document. This must be in place before you onboard the first merchant.

---

## CDD tier quick guide

| Tier | Turnover | Verification required | Cost |
|---|---|---|---|
| Simplified CDD | ≤₹40L p.a. | PAN + CPV (Customer Personal Verification) + 1 OVD | ~₹20–25 |
| Full CDD | >₹40L p.a. | CKYCR lookup → fresh KYC if not found; PAN + OVD + face match + UBO declaration | ~₹30–35 |

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
CKYC_DOCKER_DEPLOYED=false          # true when CKYCR on-prem Docker is running
CKYC_ONPREM_URL=                    # http://your-ckycr-docker-host
ANTECEDENT_CHECK_API_URL=           # your background verification endpoint
CPV_SCHEDULING_URL=                 # physical CPV scheduler
SIMPLIFIED_CDD_TURNOVER_LIMIT=4000000   # ₹40L — adjust only if policy changes
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "pa_merchant_kyc",
  "description": "PA Merchant Onboarding — CKYCR-first, tiered CDD, 10% UBO, antecedent check",
  "trigger": "api",
  "inputs": ["merchant_id", "business_pan", "annual_turnover_inr", "mobile", "business_type"],
  "nodes": [
    { "id": "consent", "type": "ui", "template": "dpdp_consent",
      "msg": "We need to verify your business identity as required by RBI Payment Aggregator guidelines.",
      "on_denied": "REJECT" },

    { "id": "ckyc-gate", "type": "condition",
      "if": "CKYC_DOCKER_DEPLOYED == true", "then": "ckyc-lookup", "else": "turnover-gate",
      "note": "CKYCR is mandatory first step per PA MD 2025 — deploy CKYCR Docker to enable short path" },

    { "id": "ckyc-lookup", "type": "api", "call": "{{CKYC_ONPREM_URL}}/lookup",
      "in": { "pan": "{{business_pan}}", "entity_type": "BUSINESS" },
      "on_found_clean": "ubo-check",
      "on_found_stale": "turnover-gate",
      "on_not_found": "turnover-gate",
      "on_found_flagged": "full-cdd" },

    { "id": "turnover-gate", "type": "condition",
      "if": "annual_turnover_inr <= {{SIMPLIFIED_CDD_TURNOVER_LIMIT}}",
      "then": "simplified-cdd", "else": "full-cdd" },

    { "id": "simplified-cdd", "type": "sequence",
      "note": "Simplified CDD — ≤₹40L turnover. PAN + CPV + 1 OVD per PA MD 2025 Annex II.",
      "nodes": [
        { "id": "pan-simplified", "type": "api", "call": "POST /pan", "version": "2024-12-01",
          "on_invalid": "REJECT", "on_deleted": "REJECT" },
        { "id": "ovd-upload", "type": "ui", "template": "document_upload",
          "required_docs": ["GSTIN_certificate_or_shop_establishment_or_trade_licence"],
          "note": "1 OVD — any of: GSTIN certificate, shop & establishment certificate, or trade licence" },
        { "id": "cpv-schedule", "type": "api", "call": "{{CPV_SCHEDULING_URL}}/book",
          "in": { "merchant_id": "{{merchant_id}}", "urgency": "STANDARD" },
          "note": "CPV = Customer Personal Verification — mandatory for Simplified CDD" }
      ]},

    { "id": "full-cdd", "type": "sequence",
      "note": "Full CDD — >₹40L turnover or CKYCR not found.",
      "nodes": [
        { "id": "mob-send", "type": "api", "call": "POST /mobile360/otp/send" },
        { "id": "mob-verify", "type": "api", "call": "POST /mobile360/otp/verify",
          "prefill_outputs": ["name"] },
        { "id": "pan-full", "type": "api", "call": "POST /pan", "version": "2024-12-01",
          "on_invalid": "REJECT", "on_deleted": "REJECT",
          "note": "PAN advanced — includes director flag, filing status, income proxy" },
        { "id": "ovd-full", "type": "ui", "template": "document_upload",
          "required_docs": [
            "certificate_of_incorporation_or_partnership_deed",
            "GSTIN_certificate",
            "board_resolution_authorising_signatory"
          ]},
        { "id": "liveness-full", "type": "api", "call": "POST /face-liveness",
          "content_type": "multipart/form-data",
          "retry_flow": [
            { "attempt": 1, "on_fail": "liveness-guide-2" },
            { "attempt": 2, "on_fail": "liveness-guide-3" },
            { "attempt": 3, "on_fail": "vkyc-merchant" }
          ]},
        { "id": "liveness-guide-2", "type": "ui",
          "msg": "Liveness check failed. Try better lighting and a plain background.", "then": "liveness-full" },
        { "id": "liveness-guide-3", "type": "ui",
          "msg": "One more attempt. Full face visible, remove glasses.", "then": "liveness-full" },
        { "id": "vkyc-merchant", "type": "api", "call": "POST /vkyc",
          "meta": { "regulator": "PA", "geolocation_required": false },
          "note": "VKYC escape hatch — activated when 3 liveness attempts fail due to device-class SDK issues. Prevents genuine merchant rejection on incompatible hardware.",
          "states": { "APPROVE": "face-match-full", "REJECT": "REJECT",
                      "UNABLE_TO_VALIDATE": "MANUAL_REVIEW", "FAILED": "REJECT" }},
        { "id": "face-match-full", "type": "api", "call": "POST /face-match",
          "content_type": "multipart/form-data",
          "threshold": 0.75, "on_fail": "REJECT", "flag_if_below_80": "+1 AMBER" }
      ]},

    { "id": "ubo-check", "type": "ui", "template": "ubo_declaration",
      "threshold_pct": 10,
      "required_fields": ["shareholder_name", "shareholding_pct", "nationality", "pep_status"],
      "note": "10% beneficial ownership threshold per Oct 2023 KYC MD amendment. ALL shareholders ≥10% must be declared." },

    { "id": "antecedent-check", "type": "api", "call": "{{ANTECEDENT_CHECK_API_URL}}/screen",
      "in": {
        "merchant_id": "{{merchant_id}}",
        "pan": "{{business_pan}}",
        "entity_name": "{{name}}"
      },
      "on_adverse_HIGH": "REJECT",
      "on_adverse_MEDIUM": "+1 AMBER",
      "on_clear": "bav",
      "note": "Background/antecedent check mandatory per PA MD 2025 Clause 8.3" },

    { "id": "bav", "type": "api", "call": "POST /bank-account/sync",
      "on_fraud_account": "REJECT_AND_FLAG", "on_invalid": "REJECT",
      "flags": { "name_below_60": "REJECT", "name_60_to_84": "+1 AMBER" },
      "note": "Merchant settlement bank account — name must match entity PAN" },

    { "id": "ckyc-upload-gate", "type": "condition",
      "if": "CKYC_DOCKER_DEPLOYED == true", "then": "ckyc-push", "else": "risk-gate" },
    { "id": "ckyc-push", "type": "api", "call": "{{CKYC_ONPREM_URL}}/upload",
      "async": true, "mandate_days": 10,
      "note": "CKYCR upload within 10 business days — mandatory per PA MD 2025" },

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
} = process.env;

// Fix 2 — Idempotency store (use Redis in production)
const processedWebhooks = new Map(); // redis.set(key, '1', 'EX', 86400)

app.post('/api/merchant-kyc/start', async (req, res) => {
  const {
    merchantId,
    businessPan,
    annualTurnoverInr,
    mobile,
    businessType,   // SOLE_PROP | PARTNERSHIP | PVT_LTD | PUBLIC_LTD | LLP | TRUST | NGO
  } = req.body;

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
        merchant_id:         merchantId,
        business_pan:        businessPan,
        annual_turnover_inr: annualTurnoverInr,
        mobile,
        business_type:       businessType,
        redirect_url: `${BASE_URL}/merchant-kyc/done`,
        webhook_url:  `${BASE_URL}/api/merchant-kyc/webhook`,
      }),
    }
  );

  const { run_id, hosted_url } = await r.json();
  res.json({ kycUrl: hosted_url, runId: run_id });
});

app.post('/api/merchant-kyc/webhook', (req, res) => {
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

  const { merchant_id, status, flags, cdd_tier } = req.body;
  // cdd_tier: 'SIMPLIFIED' | 'FULL'

  switch (status) {
    case 'APPROVED':
      // ✅ Merchant verified — activate for transaction processing
      activateMerchant(merchant_id, cdd_tier);
      scheduleNextReKYC(merchant_id, cdd_tier); // set re-KYC by risk tier
      break;

    case 'REJECTED':
      // ❌ Hard reject — adverse antecedent, PAN invalid, forgery, fraud account
      // flags[]: 'antecedent_adverse_HIGH', 'pan_invalid', 'fraud_account', etc.
      rejectMerchant(merchant_id, flags);
      if (flags.some(f => f.includes('antecedent') || f.includes('fraud'))) {
        logToFIU(merchant_id, flags); // file STR if applicable
      }
      break;

    case 'MANUAL_REVIEW':
      // ⚠️ 1 amber flag — route to compliance ops
      queueForCompliance(merchant_id, flags, cdd_tier);
      break;

    case 'CPV_SCHEDULED':
      // 🏠 CPV booked (Simplified CDD path)
      notifyMerchantCPV(merchant_id);
      break;
  }

  res.json({ received: true });
});

async function activateMerchant(id, tier)        { /* activate settlement, set limits by tier */ }
async function scheduleNextReKYC(id, tier)        { /* LOW: 10yr, MEDIUM: 8yr, HIGH: 2yr */ }
async function rejectMerchant(id, flags)          { /* update DB, block account */ }
async function queueForCompliance(id, flags, tier){ /* compliance ops queue */ }
async function notifyMerchantCPV(id)              { /* send CPV appointment details */ }
async function logToFIU(id, flags)                { /* append to STR queue */ }

app.listen(3000);
```

---

### Step 3 — Test it

```bash
# Simplified CDD merchant (≤₹40L turnover)
curl -X POST http://localhost:3000/api/merchant-kyc/start \
  -H "Content-Type: application/json" \
  -d '{"merchantId":"merch_001","businessPan":"AABCE1234F","annualTurnoverInr":3000000,"mobile":"9999999999","businessType":"SOLE_PROP"}'

# Full CDD merchant (>₹40L turnover)
curl -X POST http://localhost:3000/api/merchant-kyc/start \
  -H "Content-Type: application/json" \
  -d '{"merchantId":"merch_002","businessPan":"AABCF5678G","annualTurnoverInr":10000000,"mobile":"9999999998","businessType":"PVT_LTD"}'

# Simulate APPROVED (Full CDD)
curl -X POST http://localhost:3000/api/merchant-kyc/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"merchant_id":"merch_002","status":"APPROVED","flags":[],"cdd_tier":"FULL"}'

# Simulate REJECTED (adverse antecedent)
curl -X POST http://localhost:3000/api/merchant-kyc/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"merchant_id":"merch_003","status":"REJECTED","flags":["antecedent_adverse_HIGH"],"cdd_tier":"FULL"}'
```

---

## Business type → document matrix

| Business type | Incorporation proof | Signatory authority |
|---|---|---|
| Sole Proprietor | Shop & establishment cert or trade licence | Self |
| Partnership | Partnership deed | All partners |
| Private Limited | Certificate of incorporation | Board resolution |
| Public Limited | Certificate of incorporation | Board resolution + MOA extract |
| LLP | LLP agreement | Designated partner authorisation |
| Trust | Trust deed + registration cert | Trustee authorisation |
| NGO / Society | Registration cert | Governing body resolution |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| DPDP consent (merchant-specific) | CKYCR on-prem Docker | AML/sanctions screening |
| CKYCR lookup + short path | Antecedent check API | FIU-IND STR/CTR filing system |
| Turnover-gated CDD routing | CPV scheduling system | Board-approved KYC policy |
| PAN Advanced (director flags, income proxy) | | |
| OVD upload (entity documents) | | |
| Face liveness + match (Full CDD) | | |
| 10% UBO declaration UI | | |
| BAV — merchant settlement account | | |
| CKYCR async upload (10-day mandate) | | |
| Amber flag risk gate | | |

**Regulation:** RBI PA Master Direction 2025 (RBI/DPSS/2025-26/141) · KYC Master Direction 2023 (Oct 2023 amendment — 10% UBO) · PMLA Section 11A · DPDP Act 2023

**Cost:** Simplified CDD ~₹20–25 · Full CDD ~₹30–35 per merchant

**FIU-IND:** STR within 7 working days of suspicion · CTR by 15th of succeeding month for >₹10L

---

## MCP — coming soon

```
/relay-pa-merchant

→ Claude: "Annual turnover bracket? CKYCR Docker deployed? Business type?"
→ Calls Relay MCP → creates PA merchant onboarding workflow
→ Returns RELAY_WORKFLOW_ID, already live
```
