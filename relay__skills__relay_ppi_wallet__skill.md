---
name: relay-ppi-wallet
description: Cashfree KYC workflow for PPI Wallet Onboarding — Small PPI (OTP + self-declaration, ₹10K balance) and Full KYC PPI (OVD + PAN + face match, ₹2L balance) with automatic upgrade path. KYC expiry tracking (2 years for Full KYC). Cross-border eligibility gate (Small PPI excluded from imports/exports). Generates Node.js integration code and Relay workflow spec. ~₹8–25 per onboarding.
triggers:
  - /relay-ppi-wallet
  - PPI wallet onboarding
  - prepaid payment instrument KYC
  - wallet KYC relay
  - Small PPI onboarding
  - Full KYC PPI upgrade
tools:
  - Read/Write
---

# PPI Wallet Onboarding (Small PPI + Full KYC PPI)

> Small PPI (OTP + self-declaration, ₹10K) → Full KYC PPI (OVD + PAN + face, ₹2L) · Auto-upgrade trigger · KYC expiry tracking (2 years) · Cross-border eligibility gate · RBI PPI Master Circular

---

## Regulatory context

This workflow implements wallet onboarding per **RBI PPI Master Circular (RBI/2017-18/153)** and its amendments.

| PPI type | Verification | Balance limit | Monthly load limit | Cross-border | Cost |
|---|---|---|---|---|---|
| Small PPI | OTP + self-declaration | ₹10,000 | ₹10,000 | ❌ Not allowed | ~₹8–12 |
| Full KYC PPI | OVD + PAN + face match | ₹2,00,000 | ₹10,00,000 | ✅ Allowed | ~₹20–25 |

> **Critical rule**: Small PPI CANNOT be used for cross-border transactions (PA-CB import or export). Full KYC PPI is the minimum for cross-border eligibility.

---

## Upgrade path

```
Customer approaches ₹8K balance (configurable upgrade trigger)
  → System prompts upgrade
    → Customer completes Full KYC (OVD + PAN + face match)
      → Balance limit raised to ₹2L
      → Monthly load raised to ₹10L
      → Cross-border eligibility unlocked
      → KYC expiry set: 2 years from completion
```

---

## Quickstart — 15 minutes to live

### Environment variables

```env
CASHFREE_CLIENT_ID=
CASHFREE_CLIENT_SECRET=
CASHFREE_BASE_URL=https://sandbox.cashfree.com/verification
CASHFREE_WEBHOOK_SECRET=
BASE_URL=http://localhost:3000
RELAY_WORKFLOW_ID=
SMALL_PPI_BALANCE_LIMIT=10000      # ₹10,000 — statutory, do not change
FULL_KYC_BALANCE_LIMIT=200000      # ₹2,00,000 — statutory, do not change
UPGRADE_TRIGGER_THRESHOLD=8000     # prompt upgrade at ₹8K (80% of Small PPI limit)
KYC_EXPIRY_MONTHS=24               # Full KYC PPI valid for 2 years per RBI PPI MC
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "ppi_wallet_onboarding",
  "description": "PPI wallet — Small PPI OTP path + Full KYC upgrade + expiry tracking",
  "trigger": "api",
  "inputs": ["customer_id", "mobile", "ppi_type"],
  "nodes": [
    { "id": "consent", "type": "ui", "template": "dpdp_consent",
      "msg": "We need your consent to set up your wallet as required by RBI PPI guidelines.",
      "on_denied": "REJECT" },

    { "id": "ppi-route", "type": "condition",
      "switch": "ppi_type",
      "cases": {
        "SMALL":    "small-ppi-flow",
        "FULL_KYC": "full-kyc-flow",
        "UPGRADE":  "upgrade-confirmation"
      }
    },

    { "id": "small-ppi-flow", "type": "sequence",
      "note": "Small PPI — OTP + self-declaration. No OVD required.",
      "nodes": [
        { "id": "mob-send", "type": "api", "call": "POST /mobile360/otp/send" },
        { "id": "mob-verify", "type": "api", "call": "POST /mobile360/otp/verify" },
        { "id": "self-declaration", "type": "ui", "template": "self_declaration",
          "required_fields": ["name", "dob", "address"],
          "note": "Customer declares details — RBI PPI MC: no OVD required at Small PPI tier" },
        { "id": "upgrade-nudge", "type": "ui",
          "msg": "Wallet ready with ₹10,000 limit. Upgrade with full KYC to get ₹2,00,000 limit and cross-border payments.",
          "options": ["Upgrade now", "Skip for now"],
          "on_upgrade_now": "full-kyc-flow",
          "on_skip": "APPROVE_SMALL" }
      ]},

    { "id": "upgrade-confirmation", "type": "ui",
      "msg": "Your wallet is approaching its ₹10,000 limit. Complete KYC to unlock ₹2,00,000 and cross-border payments.",
      "options": ["Upgrade now"],
      "then": "full-kyc-flow" },

    { "id": "full-kyc-flow", "type": "sequence",
      "note": "Full KYC PPI — OVD + PAN + face match. Required for ₹2L limit and cross-border.",
      "nodes": [
        { "id": "mob-send-full", "type": "api", "call": "POST /mobile360/otp/send" },
        { "id": "mob-verify-full", "type": "api", "call": "POST /mobile360/otp/verify",
          "prefill_outputs": ["pan", "name"] },
        { "id": "pan-full", "type": "api", "call": "POST /pan", "version": "2024-12-01",
          "on_invalid": "REJECT", "on_deleted": "REJECT" },
        { "id": "digilocker-full", "type": "api", "call": "POST /digilocker", "doc": "AADHAAR",
          "timeout_min": 10, "on_timeout": "ovd-ocr", "on_denied": "ovd-ocr" },
        { "id": "ovd-ocr", "type": "api", "call": "POST /bharat-ocr", "doc": "AADHAAR",
          "content_type": "multipart/form-data",
          "on_forgery": "REJECT",
          "note": "Aadhaar OCR fallback — Voter ID or Passport accepted as alternate OVD" },
        { "id": "liveness-full", "type": "api", "call": "POST /face-liveness",
          "content_type": "multipart/form-data",
          "retry_flow": [
            { "attempt": 1, "on_fail": "liveness-retry-2" },
            { "attempt": 2, "on_fail": "liveness-retry-3" },
            { "attempt": 3, "on_fail": "vkyc-ppi" }
          ]},
        { "id": "liveness-retry-2", "type": "ui",
          "msg": "Liveness check failed. Better lighting + plain background helps.", "then": "liveness-full" },
        { "id": "liveness-retry-3", "type": "ui",
          "msg": "Last attempt. Full face visible, remove glasses.", "then": "liveness-full" },
        { "id": "vkyc-ppi", "type": "api", "call": "POST /vkyc",
          "meta": { "regulator": "PPI", "geolocation_required": false },
          "note": "VKYC escape hatch — device-class liveness failure. Full KYC PPI upgrade blocked only if VKYC also fails; user retains Small PPI tier.",
          "states": { "APPROVE": "face-match-full", "REJECT": "REJECT",
                      "UNABLE_TO_VALIDATE": "MANUAL_REVIEW", "FAILED": "REJECT" }},
        { "id": "face-match-full", "type": "api", "call": "POST /face-match",
          "content_type": "multipart/form-data",
          "threshold": 0.75, "on_fail": "REJECT", "flag_if_below_80": "+1 AMBER" },
        { "id": "kyc-expiry-set", "type": "internal",
          "action": "set_expiry",
          "expiry_months": "{{KYC_EXPIRY_MONTHS}}",
          "note": "Full KYC PPI expiry — 2 years from completion. Re-KYC required at expiry." }
      ]},

    { "id": "risk-gate", "type": "gate", "rules": [
        { "if": "amber_flags == 0 && ppi_type == 'SMALL'",    "out": "APPROVE_SMALL" },
        { "if": "amber_flags == 0 && ppi_type != 'SMALL'",    "out": "APPROVE_FULL" },
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
  UPGRADE_TRIGGER_THRESHOLD = '8000',
  SMALL_PPI_BALANCE_LIMIT   = '10000',
  FULL_KYC_BALANCE_LIMIT    = '200000',
} = process.env;

// Fix 4 — Startup validation: statutory PPI balance limits must not be overridden
if (parseInt(SMALL_PPI_BALANCE_LIMIT) !== 10000) {
  throw new Error(`FATAL: SMALL_PPI_BALANCE_LIMIT must be 10000 per RBI PPI Master Circular. Got: ${SMALL_PPI_BALANCE_LIMIT}`);
}
if (parseInt(FULL_KYC_BALANCE_LIMIT) !== 200000) {
  throw new Error(`FATAL: FULL_KYC_BALANCE_LIMIT must be 200000 per RBI PPI Master Circular. Got: ${FULL_KYC_BALANCE_LIMIT}`);
}

// Fix 2 — Idempotency store (use Redis in production)
const processedWebhooks = new Map(); // redis.set(key, '1', 'EX', 86400)

app.post('/api/ppi/start', async (req, res) => {
  const {
    customerId,
    mobile,
    ppiType = 'SMALL',  // 'SMALL' | 'FULL_KYC' | 'UPGRADE'
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
        customer_id: customerId,
        mobile,
        ppi_type:    ppiType,
        redirect_url: `${BASE_URL}/ppi/done`,
        webhook_url:  `${BASE_URL}/api/ppi/webhook`,
      }),
    }
  );

  const { run_id, hosted_url } = await r.json();
  res.json({ kycUrl: hosted_url, runId: run_id });
});

// Call this from your wallet balance-check middleware on every transaction
app.post('/api/ppi/check-upgrade', async (req, res) => {
  const { customerId, currentBalanceInr, mobile } = req.body;
  const threshold = parseInt(UPGRADE_TRIGGER_THRESHOLD);

  if (currentBalanceInr >= threshold) {
    const upgradeRes = await fetch('/api/ppi/start', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ customerId, mobile, ppiType: 'UPGRADE' }),
    });
    const { kycUrl } = await upgradeRes.json();
    return res.json({ upgradeRequired: true, kycUrl });
  }

  res.json({ upgradeRequired: false });
});

app.post('/api/ppi/webhook', (req, res) => {
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

  const { customer_id, status, ppi_tier, kyc_expiry_date } = req.body;
  // ppi_tier: 'SMALL' | 'FULL_KYC'

  switch (status) {
    case 'APPROVE_SMALL':
      // ✅ Small PPI activated — ₹10K balance, no cross-border
      activateSmallPPI(customer_id);
      setWalletLimits(customer_id, { balance: 10000, monthlyLoad: 10000 });
      break;

    case 'APPROVE_FULL':
      // ✅ Full KYC PPI — ₹2L balance, cross-border eligible, 2yr KYC expiry
      activateFullKYCPPI(customer_id);
      setWalletLimits(customer_id, { balance: 200000, monthlyLoad: 1000000 });
      enableCrossBorder(customer_id);
      scheduleKYCExpiry(customer_id, kyc_expiry_date);
      break;

    case 'REJECTED':
      // ❌ Forgery, face mismatch, or PAN invalid
      rejectWallet(customer_id);
      break;

    case 'MANUAL_REVIEW':
      queueForReview(customer_id);
      break;
  }

  res.json({ received: true });
});

async function activateSmallPPI(id)           { /* create wallet, Small PPI tier */ }
async function activateFullKYCPPI(id)         { /* upgrade or create Full KYC wallet */ }
async function setWalletLimits(id, limits)    { /* set balance + monthly load limits */ }
async function enableCrossBorder(id)          { /* set cross-border eligible flag */ }
async function scheduleKYCExpiry(id, date)    { /* schedule re-KYC reminder 30 days before expiry */ }
async function rejectWallet(id)               { /* reject wallet creation */ }
async function queueForReview(id)             { /* ops queue */ }

app.listen(3000);
```

---

### Step 3 — Test it

```bash
# Small PPI onboarding
curl -X POST http://localhost:3000/api/ppi/start \
  -H "Content-Type: application/json" \
  -d '{"customerId":"cust_001","mobile":"9999999999","ppiType":"SMALL"}'

# Full KYC PPI onboarding
curl -X POST http://localhost:3000/api/ppi/start \
  -H "Content-Type: application/json" \
  -d '{"customerId":"cust_002","mobile":"9999999998","ppiType":"FULL_KYC"}'

# Upgrade check (balance ₹8,500 — above threshold)
curl -X POST http://localhost:3000/api/ppi/check-upgrade \
  -H "Content-Type: application/json" \
  -d '{"customerId":"cust_001","currentBalanceInr":8500,"mobile":"9999999999"}'
# Returns: { "upgradeRequired": true, "kycUrl": "https://..." }

# Simulate APPROVE_SMALL webhook
curl -X POST http://localhost:3000/api/ppi/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"cust_001","status":"APPROVE_SMALL","ppi_tier":"SMALL"}'

# Simulate APPROVE_FULL webhook (Full KYC)
curl -X POST http://localhost:3000/api/ppi/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"cust_002","status":"APPROVE_FULL","ppi_tier":"FULL_KYC","kyc_expiry_date":"2027-05-11"}'
```

---

## PPI limits quick reference

| | Small PPI | Full KYC PPI |
|---|---|---|
| Verification | OTP + self-declaration | OVD + PAN + face match |
| Outstanding balance | ₹10,000 | ₹2,00,000 |
| Monthly load limit | ₹10,000 | ₹10,00,000 |
| Cross-border (PA-CB) | ❌ Not allowed | ✅ Allowed |
| Interoperability | Limited | Full (UPI, IMPS, NEFT) |
| KYC expiry | N/A | 2 years from KYC date |
| Cost | ~₹8–12 | ~₹20–25 |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| DPDP consent (wallet-specific) | Wallet balance tracker for upgrade trigger | CKYCR upload (PPI-specific) |
| Small PPI — OTP + self-declaration | KYC expiry re-KYC flow (use relay-existing-customer) | AML/sanctions screening |
| Full KYC — PAN + DigiLocker + OCR fallback + face | | FIU-IND STR/CTR filing |
| Liveness check (3 attempts + guidance) | | |
| Face match vs Aadhaar photo | | |
| Auto-upgrade trigger (configurable threshold) | | |
| Cross-border eligibility gate (Small PPI excluded) | | |
| KYC expiry tracking (2-year mandate) | | |

**Regulation:** RBI PPI Master Circular RBI/2017-18/153 · KYC Master Direction 2023 · PMLA Section 11A · DPDP Act 2023

**Cost:** Small PPI ~₹8–12 · Full KYC PPI ~₹20–25 per onboarding

---

## MCP — coming soon

```
/relay-ppi-wallet

→ Claude: "Small PPI or Full KYC? Cross-border needed? Upgrade threshold?"
→ Calls Relay MCP → creates PPI wallet onboarding workflow
→ Returns RELAY_WORKFLOW_ID
```
