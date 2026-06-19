---
name: relay-gold-verify-pay
description: Cashfree KYC workflow for Gold Verify & Pay — inline KYC before checkout for high-value orders (>₹2L default threshold, configurable). Returning user vault skip, PAN 360 + Aadhaar + face match + BAV, payment link released on completion. RBI PAN mandate for jewellers, forex, gaming. Generates working Node.js integration code, compact Relay workflow spec. ~₹30–50 per verification.
triggers:
  - /relay-gold-verify-pay
  - gold verify and pay workflow
  - jeweller KYC before payment
  - verify and pay template
  - high value transaction verification relay
  - KYC before checkout
  - inline KYC payment
tools:
  - Read/Write
---

# Gold Verify & Pay — Inline KYC Before Checkout

> KYC at checkout for orders above your threshold · Returning user vault skip · PAN + Aadhaar + Face + Bank → payment link released · RBI PAN mandate compliant · ~₹30–50 per verification

---

## Regulatory mandate

| Obligation | Regulation | Threshold |
|---|---|---|
| PAN collection — jewellery | Income Tax Rule 114B(d) | Cash transactions > ₹2L at jewellers |
| PAN collection — forex | Income Tax Rule 114B(f) | Forex purchase > ₹50K |
| PAN collection — luxury / D2C | Income Tax Rule 114B | Cash transactions > ₹2L across specified categories |
| PAN collection — gaming | GST + Income Tax Rule 114B | Aggregate deposits / withdrawals > ₹10K per day |
| AML screening | PMLA Section 11A | All high-value transactions |
| STR filing | PMLA Section 12 · FIU-IND | Within 7 working days of suspicion |
| CTR filing | PMLA Section 12 · FIU-IND | By 15th of succeeding month for cash > ₹10L |
| PAN reporting — Form 60 | Income Tax Rule 114B | If customer declines PAN — collect Form 60 |
| Record retention | PMLA Section 12 | 5 years from transaction date |

---

## When to use Gold Verify & Pay

Use this when:
- Transaction amount exceeds a threshold (default ₹2L; configurable to any value)
- RBI requires PAN collection for high-value purchases (jewellery, forex, luxury, gaming)
- You want to release the payment link only after identity is verified — not before

This is an **inline** flow (embedded in your checkout), not a standalone account-opening KYC.

---

## What your customer experiences

1. Proceeds to checkout → sees "Verify identity to complete purchase"
2. **Returning user**: verified vault found → skip to payment link (0 seconds)
3. **New user**: mobile OTP → PAN confirm → Aadhaar via DigiLocker → selfie → bank account
4. All checks pass → payment link appears inline in the checkout
5. Customer pays — order confirmed

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
KYC_THRESHOLD_INR=200000   # trigger KYC above this amount
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "gold_verify_pay",
  "description": "Inline KYC at checkout → payment link on completion",
  "trigger": "api",
  "inputs": ["customer_id", "mobile", "order_id", "amount"],
  "nodes": [
    { "id": "amount-gate",    "type": "condition",
      "if": "amount >= KYC_THRESHOLD_INR", "then": "vault-check", "else": "pay-link" },

    { "id": "vault-check",    "type": "condition",
      "if": "customer_kyc_verified == true", "then": "pay-link", "else": "consent",
      "note": "Returning verified users skip re-KYC — vault stores verification_id" },

    { "id": "consent",        "type": "ui",  "template": "dpdp_consent", "on_denied": "REJECT" },
    { "id": "mob-send",       "type": "api", "call": "POST /mobile360/otp/send" },
    { "id": "mob-verify",     "type": "api", "call": "POST /mobile360/otp/verify",
      "prefill_outputs": ["pan", "name"] },
    { "id": "pan",            "type": "api", "call": "POST /pan", "version": "2024-12-01",
      "on_invalid": "REJECT", "flags": { "aadhaar_seeding_not_Y": "+1 AMBER" } },
    { "id": "digilocker",     "type": "api", "call": "POST /digilocker", "doc": "AADHAAR",
      "timeout_min": 10, "on_timeout": "digilocker-retry", "on_denied": "ocr" },
    { "id": "digilocker-retry","type": "api", "call": "POST /digilocker", "doc": "AADHAAR",
      "on_timeout": "ocr" },
    { "id": "ocr",            "type": "api", "call": "POST /bharat-ocr", "doc": "AADHAAR",
      "content_type": "multipart/form-data", "on_forgery": "REJECT", "flag_on_fallback": "+1 AMBER" },
    { "id": "liveness",       "type": "api", "call": "POST /face-liveness",
      "content_type": "multipart/form-data",
      "max_retries": 3, "guidance_ui": true, "on_exhausted": "REJECT" },
    { "id": "face-match",     "type": "api", "call": "POST /face-match",
      "content_type": "multipart/form-data",
      "threshold": 0.75, "on_fail": "REJECT", "flag_if_below_80": "+1 AMBER" },
    { "id": "bav",            "type": "api", "call": "POST /bank-account/sync",
      "on_fraud_account": "REJECT_AND_FLAG", "on_invalid": "REJECT",
      "flags": { "name_below_60": "REJECT", "name_60_to_84": "+1 AMBER" } },
    { "id": "vault-write",    "type": "api", "call": "POST /vault",
      "in": { "customer_id": "{{customer_id}}", "verification_id": "{{run_id}}" },
      "note": "Store verification result so returning users skip re-KYC" },
    { "id": "risk-gate",      "type": "gate", "rules": [
        { "if": "amber_flags == 0", "out": "pay-link" },
        { "if": "amber_flags <= 2", "out": "pay-link" },
        { "if": "amber_flags >= 3", "out": "REJECT" }
    ]},
    { "id": "pay-link",       "type": "api", "call": "POST /pg/links",
      "in": { "amount": "{{amount}}", "meta": { "order_id": "{{order_id}}", "kyc_verified": true } },
      "outputs": ["payment_url"] }
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
  KYC_THRESHOLD_INR = '200000',
} = process.env;

app.post('/api/checkout/verify', async (req, res) => {
  const { customerId, mobile, orderId, amount } = req.body;

  // Below threshold — skip KYC, return payment link directly
  if (amount < parseInt(KYC_THRESHOLD_INR)) {
    const paymentUrl = await createPaymentLink(orderId, amount);
    return res.json({ requiresKyc: false, paymentUrl });
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
        customer_id:  customerId,
        mobile,
        redirect_url: `${BASE_URL}/checkout/done?order=${orderId}`,
        webhook_url:  `${BASE_URL}/api/checkout/webhook`,
        metadata:     { order_id: orderId, amount },
      }),
    }
  );

  const { run_id, hosted_url } = await r.json();
  res.json({ requiresKyc: true, kycUrl: hosted_url, runId: run_id });
});

app.post('/api/checkout/webhook', (req, res) => {
  const sig = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody).digest('base64');
  if (sig !== expected) return res.status(401).send('Bad signature');

  const { customer_id, status, flags, payment_url } = req.body;

  switch (status) {
    case 'APPROVED':
      // ✅ KYC passed — payment link has been created by Relay
      // payment_url is in the webhook; send it to customer or surface inline
      sendPaymentLink(customer_id, payment_url);
      break;

    case 'REJECTED':
      // ❌ Hard reject — cancel order, notify customer
      cancelOrder(customer_id, flags);
      break;
  }

  res.json({ received: true });
});

async function createPaymentLink(orderId, amount) {
  // Your existing payment link creation logic
}
async function sendPaymentLink(customerId, url) { /* send via SMS/WhatsApp */ }
async function cancelOrder(customerId, flags)   { /* cancel order, notify */ }

app.listen(3000);
```

---

### Step 3 — Frontend (React)

```jsx
// CheckoutVerify.jsx
import { useState } from 'react';

export function CheckoutVerify({ customerId, mobile, orderId, amount }) {
  const [phase, setPhase] = useState('idle');
  const [paymentUrl, setPaymentUrl] = useState(null);

  const startVerify = async () => {
    setPhase('loading');
    const res = await fetch('/api/checkout/verify', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify({ customerId, mobile, orderId, amount }),
    });
    const data = await res.json();

    if (!data.requiresKyc) {
      // Below threshold — payment link ready immediately
      setPaymentUrl(data.paymentUrl);
      setPhase('pay');
    } else {
      // Redirect to Cashfree-hosted KYC
      setPhase('redirecting');
      window.location.href = data.kycUrl;
    }
  };

  if (phase === 'idle')        return <button onClick={startVerify}>Proceed to pay</button>;
  if (phase === 'loading')     return <p>Preparing your order…</p>;
  if (phase === 'redirecting') return <p>Verifying identity…</p>;
  if (phase === 'pay')         return <a href={paymentUrl}>Pay ₹{amount.toLocaleString('en-IN')}</a>;
}
```

---

### Step 4 — Test it

```bash
# Order below threshold — KYC skipped
curl -X POST http://localhost:3000/api/checkout/verify \
  -H "Content-Type: application/json" \
  -d '{"customerId":"cust_001","mobile":"9999999999","orderId":"ord_001","amount":150000}'
# Returns: { requiresKyc: false, paymentUrl: "..." }

# Order above threshold — KYC triggered
curl -X POST http://localhost:3000/api/checkout/verify \
  -H "Content-Type: application/json" \
  -d '{"customerId":"cust_002","mobile":"9999999999","orderId":"ord_002","amount":250000}'
# Returns: { requiresKyc: true, kycUrl: "https://verify.cashfree.com/...", runId: "run_xyz" }

# Simulate APPROVED webhook
curl -X POST http://localhost:3000/api/checkout/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"cust_002","status":"APPROVED","flags":[],"payment_url":"https://pay.cashfree.com/..."}'
```

---

## Vault logic (returning user skip)

| Returning user state | Action |
|---|---|
| Verified within 12 months | Skip KYC — release payment link directly |
| Verified but >12 months | Re-verify (configurable window) |
| Never verified | Full KYC flow |
| Previously rejected | Block purchase |

---

## Enterprise governance

| Control | Cashfree platform | Your responsibility |
|---|---|---|
| **Data residency** | India-only · AWS ap-south-1 (Mumbai) · No cross-border transfer | Receiving systems must be India-hosted or covered by a DPA |
| **Encryption** | TLS 1.3 in transit · AES-256 at rest · Session hash chain | Maintain equivalent standards in your storage layer |
| **Audit trail** | Immutable session logs retained 7 years | PMLA: 5 years minimum from relationship end — your DB must also retain |
| **PAN transaction log** | Verification ID in webhook + vault record | Report Form 61 (Form 60 register) to Income Tax quarterly |
| **FIU-IND — STR** | `flags[]` in webhook surfaces suspicion triggers | File STR within 7 working days of suspicion on goAML portal |
| **FIU-IND — CTR** | Transaction metadata delivered via webhook | File CTR by 15th of succeeding month for cash transactions > ₹10L |
| **Re-KYC schedule** | Relay supports re-trigger — use relay-existing-customer | HIGH risk: 2 yr · MEDIUM: 8 yr · LOW: 10 yr · PEP: 1 yr |
| **DPDP rights** | Consent event stored per DPDP Act 2023 — Section 6 | Data Principal rights (access / correction / erasure) are your obligation |
| **Board policy** | Workflow enforces your configured KYC policy | Board-approved KYC/AML policy + Designated Director required before FIU-IND registration |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| Amount gate (configurable threshold) | Vault storage (your DB) | AML/PEP screening |
| Returning user vault check | Payment link template | |
| DPDP consent | | |
| Mobile OTP + PAN pre-fill | | |
| PAN 360 + Aadhaar (DigiLocker → OCR fallback) | | |
| Face liveness + match | | |
| BAV sync + fraud flag | | |
| Payment link released on approval | | |

**Regulation:** Income Tax Rule 114B (PAN collection at high-value transactions) · PMLA Sections 11A, 12 · PML Rules 2005 · GST Act 2017 (gaming / luxury) · DPDP Act 2023 — Section 6

**Cost:** ~₹30–50 per verified transaction (returns users: ₹0 re-verification)

---

## MCP — coming soon

```
/relay-gold-verify-pay

→ Claude: "Threshold amount? Sectors (jewellery/forex/gaming)? Return window?"
→ Calls Relay MCP → creates + publishes workflow
→ Returns RELAY_WORKFLOW_ID + vault schema
```
