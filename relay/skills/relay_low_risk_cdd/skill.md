---
name: relay-low-risk-cdd
description: Cashfree KYC workflow for Low-Risk CDD — Video KYC bypass for existing customers or new customers with low transaction limits (<₹60K). 50% cost reduction vs Standard CDD. Generates working Node.js + React integration code, compact Relay workflow spec, RBI compliance brief. ~₹20–35 per verification.
triggers:
  - /relay-low-risk-cdd
  - low risk CDD
  - video KYC bypass
  - existing customer onboarding
  - second account KYC
  - payments bank KYC
tools:
  - Read/Write
---

# Low-Risk CDD — Video KYC Bypass

> PAN + Aadhaar + Face + Bank (no VKYC) · Existing customers or low-limit new customers · 3–4 min journey · ~₹20–35 per verification · 50% cheaper than Standard CDD · RBI risk-based CDD approach

---

## Regulatory mandate

| Obligation | Regulation | Threshold / Condition |
|---|---|---|
| Risk-based CDD approach | RBI KYC Master Directions 2023 — Section 9 (Risk categorisation) | Lenders may apply simplified measures for low-risk customers |
| Low-risk eligibility criteria | RBI KYC MD 2023 — Section 9(b) | Existing relationship + low transaction limit + low Mobile360 risk |
| Mandatory escalation to full CDD | RBI KYC MD 2023 — Section 9(c) | Any amber flag triggers Standard CDD (VKYC path) |
| Consent capture | DPDP Act 2023 — Section 6 | Standalone screen before any data collection |
| AML screening | PMLA Section 11A | All customers — low risk does not exempt AML |
| STR filing | PMLA Section 12 · FIU-IND | Within 7 working days of suspicion |
| PMLA retention | PMLA Section 12 | 5 years from account closure |

---

## When to use this instead of Standard CDD

Use Low-Risk CDD when **all** of these are true:
- Customer has an existing relationship with you (or transaction limit <₹60K), **and**
- PAN is VALID with Aadhaar seeding Y, **and**
- BAV name match is strong (≥85), **and**
- Mobile360 risk band is LOW

Any failure → escalate automatically to Standard CDD (VKYC path). Your code handles both via the same webhook.

**Discovery question for merchants:** "Do you run the same full KYC journey for a customer opening their second account? You're likely paying ₹50/VKYC unnecessarily."

---

## What your customer experiences

1. Consents (standalone DPDP screen)
2. Mobile OTP → PAN pre-filled if available
3. Aadhaar verified via DigiLocker or photo upload
4. Selfie taken for face match
5. Bank account confirmed
6. Result in seconds — no agent call

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
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "low_risk_cdd_bypass",
  "description": "Video KYC bypass — PAN + Aadhaar + Face + BAV, escalates to VKYC on flag",
  "trigger": "api",
  "inputs": ["customer_id", "mobile"],
  "nodes": [
    { "id": "consent",          "type": "ui",   "template": "dpdp_consent", "on_denied": "REJECT" },
    { "id": "mob-send",         "type": "api",  "call": "POST /mobile360/otp/send" },
    { "id": "mob-verify",       "type": "api",  "call": "POST /mobile360/otp/verify",
      "prefill_outputs": ["pan", "name"],
      "risk_check": { "HIGH": "ESCALATE_T2", "MEDIUM": "+1 AMBER" }
    },
    { "id": "pan",              "type": "api",  "call": "POST /pan", "version": "2024-12-01",
      "on_invalid": "REJECT",
      "flags": { "aadhaar_seeding_not_Y": "+1 AMBER", "name_match_below_80": "+1 AMBER" }
    },
    { "id": "digilocker",       "type": "api",  "call": "POST /digilocker", "doc": "AADHAAR",
      "timeout_min": 10, "on_timeout": "digilocker-retry", "on_denied": "ocr" },
    { "id": "digilocker-retry", "type": "api",  "call": "POST /digilocker", "doc": "AADHAAR", "on_timeout": "ocr" },
    { "id": "ocr",              "type": "api",  "call": "POST /bharat-ocr", "doc": "AADHAAR",
      "content_type": "multipart/form-data", "on_forgery": "REJECT", "flag_on_fallback": "+1 AMBER" },
    { "id": "liveness",         "type": "api",  "call": "POST /face-liveness",
      "content_type": "multipart/form-data", "max_retries": 3, "guidance_ui": true, "on_exhausted": "ESCALATE_T2" },
    { "id": "face-match",       "type": "api",  "call": "POST /face-match",
      "content_type": "multipart/form-data", "threshold": 0.75, "on_fail": "REJECT",
      "flag_if_below_80": "+1 AMBER" },
    { "id": "bav",              "type": "api",  "call": "POST /bank-account/sync",
      "on_fraud_account": "REJECT_AND_FLAG",
      "on_invalid": "REJECT",
      "name_match": { "below_60": "REJECT", "60_to_84": "ESCALATE_T2", "85_plus": "pass" }
    },
    { "id": "bypass-gate",      "type": "gate", "rules": [
        { "if": "amber_flags == 0", "out": "APPROVE" },
        { "if": "amber_flags <= 2", "out": "ESCALATE_T2" },
        { "if": "amber_flags >= 3", "out": "REJECT" }
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

app.post('/api/kyc/start', async (req, res) => {
  const { customerId, mobile } = req.body;
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
        redirect_url: `${BASE_URL}/kyc/done`,
        webhook_url:  `${BASE_URL}/api/kyc/webhook`,
      }),
    }
  );
  const { run_id, hosted_url } = await r.json();
  res.json({ kycUrl: hosted_url, runId: run_id });
});

app.post('/api/kyc/webhook', (req, res) => {
  const sig = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody).digest('base64');
  if (sig !== expected) return res.status(401).send('Bad signature');

  const { customer_id, status, flags } = req.body;

  switch (status) {
    case 'APPROVED':
      // ✅ Bypass granted — no VKYC needed
      activateAccount(customer_id);
      break;

    case 'ESCALATE_T2':
      // 📋 Didn't qualify for bypass — redirect to Standard CDD (VKYC path)
      // Trigger your Standard CDD workflow for this customer
      startStandardCDD(customer_id);
      break;

    case 'REJECTED':
      // ❌ Hard reject — PAN invalid, forgery, fraud_account, or 3+ amber flags
      markRejected(customer_id, flags);
      break;
  }

  res.json({ received: true });
});

async function activateAccount(id)    { /* update DB */ }
async function startStandardCDD(id)   { /* trigger relay-standard-cdd workflow */ }
async function markRejected(id, flags){ /* update DB, notify customer */ }

app.listen(3000);
```

---

### Step 3 — Frontend (React)

```jsx
// KYCFlow.jsx — same pattern as relay-small-ticket
import { useState } from 'react';

export function KYCFlow({ customerId, mobile }) {
  const [phase, setPhase] = useState('idle');

  const start = async () => {
    setPhase('loading');
    const res = await fetch('/api/kyc/start', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ customerId, mobile }),
    });
    const { kycUrl } = await res.json();
    window.location.href = kycUrl;
  };

  if (phase === 'idle')    return <button onClick={start}>Verify identity</button>;
  if (phase === 'loading') return <p>Setting up verification…</p>;
}
```

---

### Step 4 — Test it

```bash
curl -X POST http://localhost:3000/api/kyc/start \
  -H "Content-Type: application/json" \
  -d '{"customerId":"test_001","mobile":"9999999999"}'

# Test APPROVED
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"test_001","status":"APPROVED","flags":[]}'

# Test bypass fail → ESCALATE_T2
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"test_001","status":"ESCALATE_T2","flags":["aadhaar_not_linked","bav_name_moderate"]}'
```

---

## Bypass eligibility (ALL must pass)

| Check | Pass condition | Fail action |
|---|---|---|
| PAN status | VALID | Hard reject |
| Aadhaar seeding | Y (linked) | +1 AMBER |
| Mobile360 risk | LOW | HIGH → T2; MEDIUM → +1 AMBER |
| BAV name match | ≥85 | 60–84 → T2; <60 → REJECT |
| Face match | ≥0.75 | <0.75 → REJECT |
| Amber total | 0 | 1–2 → T2; 3+ → REJECT |

---

## Enterprise governance

| Control | Cashfree platform | Your responsibility |
|---|---|---|
| **Data residency** | India-only · AWS ap-south-1 (Mumbai) · No cross-border transfer | Receiving systems must be India-hosted or covered by a DPA |
| **Encryption** | TLS 1.3 in transit · AES-256 at rest · Session hash chain | Maintain equivalent standards in your storage layer |
| **Audit trail** | Immutable session logs retained 7 years | PMLA: 5 years minimum from relationship end — your DB must also retain |
| **Escalation** | ESCALATE_T2 webhook status triggers Standard CDD automatically | Ensure relay-standard-cdd workflow is live before deploying Low-Risk CDD |
| **FIU-IND — STR** | `flags[]` in webhook surfaces suspicion triggers | File STR within 7 working days of suspicion on goAML portal |
| **FIU-IND — CTR** | Transaction metadata delivered via webhook | File CTR by 15th of succeeding month for cash transactions > ₹10L |
| **Re-KYC schedule** | Relay supports re-trigger — use relay-existing-customer | HIGH risk: 2 yr · MEDIUM: 8 yr · LOW: 10 yr · PEP: 1 yr |
| **DPDP rights** | Consent event stored per DPDP Act 2023 — Section 6 | Data Principal rights (access / correction / erasure) are your obligation |
| **Board policy** | Workflow enforces your configured KYC policy | Board-approved KYC/AML policy + Designated Director required before FIU-IND registration |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| DPDP standalone consent | CKYC Docker | AML/PEP |
| Mobile360 OTP + PAN pre-fill | Standard CDD workflow (for T2 escalations) | |
| PAN 360 with seeding check | | |
| DigiLocker → bharat-ocr fallback | | |
| Face liveness + match | | |
| BAV + fraud_account hard reject | | |
| Auto-escalation to Standard CDD (T2) | | |

**Regulation:** RBI KYC Master Directions 2023 — Section 9 (risk-based CDD) · PMLA Sections 11A, 12 · PML Rules 2005 · DPDP Act 2023 — Section 6

**Cost:** ~₹20–35 (bypass approved) · Escalated to T2 costs add Standard CDD pricing

---

## MCP — coming soon

```
/relay-low-risk-cdd

→ Creates both Low-Risk and Standard CDD workflows
→ Links them (T2 escalation wired automatically)
→ Returns both RELAY_WORKFLOW_IDs
```
