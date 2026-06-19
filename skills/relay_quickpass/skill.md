---
name: relay-quickpass
description: Cashfree KYC workflow for QuickPass — DL-first identity verification for gig workers, two-wheeler loans, delivery partner onboarding. Driving licence OCR → RTO verification → face match → PAN advanced → bank account. No DigiLocker or Aadhaar required. Generates working Node.js + React integration code, compact Relay workflow spec. ~₹25–35 per verification.
triggers:
  - /relay-quickpass
  - quickpass verification workflow
  - DL based KYC relay
  - driving license verification workflow
  - gig worker onboarding relay
  - two wheeler loan KYC
  - delivery partner onboarding
tools:
  - Read/Write
---

# QuickPass — DL-First Verification

> Driving Licence + Face + PAN + Bank · No Aadhaar required · Gig workers, two-wheeler loans, delivery partners · 3–4 min journey · ~₹25–35 per verification

---

## Regulatory mandate

| Obligation | Regulation | Threshold / Condition |
|---|---|---|
| DL-based identity verification | RBI KYC Master Directions 2023 — Section 16 (Officially Valid Documents) | DL is a valid OVD under KYC MD — Aadhaar not required |
| RTO verification | Motor Vehicles Act 1988 · MoRTH digital database | DL must be VALID and not suspended or expired |
| Face match | RBI KYC MD 2023 — Section 18A | Selfie vs DL photo — threshold 0.75 |
| PAN Advanced check | RBI KYC MD 2023 — Section 17 | PAN as income-linked identity document |
| Bank account verification | PMLA Section 11A | Settlement / disbursement account must be verified |
| Consent capture | DPDP Act 2023 — Section 6 | Standalone screen before any data collection |
| AML screening | PMLA Section 11A | All customers including gig workers |
| STR filing | PMLA Section 12 · FIU-IND | Within 7 working days of suspicion |
| Record retention | PMLA Section 12 | 5 years from account closure |

> **Note:** This workflow explicitly does NOT use Aadhaar. It satisfies KYC requirements using DL (OVD) + PAN + face match per RBI KYC MD 2023 Section 16 — a valid and RBI-compliant path.

---

## When to use QuickPass instead of Standard CDD

QuickPass is designed for customers who:
- Have a driving licence but may not have Aadhaar linked to mobile (common with gig workers)
- Are applying for two-wheeler loans or vehicle-linked financial products
- Need fast onboarding without DigiLocker friction

Standard CDD (Aadhaar path) is preferred for bank accounts and higher-value credit. Use QuickPass for gig/vehicle use cases.

---

## What your customer experiences

1. Uploads driving licence photo (front + back)
2. OCR extracts name, DOB, DL number automatically
3. RTO database confirms licence is valid and not suspended
4. Takes a selfie — face matched against DL photo
5. PAN advanced check confirms income-linked identity
6. Bank account verified instantly
7. Done — decision in seconds

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
  "name": "quickpass_dl_kyc",
  "description": "DL-first KYC — OCR + RTO verify + face match + PAN advanced + BAV",
  "trigger": "api",
  "inputs": ["customer_id", "mobile"],
  "nodes": [
    { "id": "consent",      "type": "ui",  "template": "dpdp_consent", "on_denied": "REJECT" },
    { "id": "mob-send",     "type": "api", "call": "POST /mobile360/otp/send" },
    { "id": "mob-verify",   "type": "api", "call": "POST /mobile360/otp/verify",
      "prefill_outputs": ["name"] },
    { "id": "dl-ocr",       "type": "api", "call": "POST /bharat-ocr", "doc": "DRIVING_LICENCE",
      "content_type": "multipart/form-data",
      "on_forgery": "REJECT", "on_low_quality": "dl-ocr-retry",
      "outputs": ["dl_number", "name", "dob", "dl_photo_url"] },
    { "id": "dl-ocr-retry", "type": "ui",
      "msg": "Image unclear. Please retake in good lighting.", "then": "dl-ocr",
      "max_retries": 2, "on_exhausted": "REJECT" },
    { "id": "dl-verify",    "type": "api", "call": "POST /driving-license",
      "in": { "id_number": "{{dl_number}}", "dob": "{{dob}}" },
      "on_invalid": "REJECT", "on_suspended": "REJECT",
      "on_expired": "REJECT", "outputs": ["rto_name", "rto_photo_url"] },
    { "id": "name-match",   "type": "api", "call": "POST /name-match",
      "in": { "name1": "{{mob_name}}", "name2": "{{rto_name}}" },
      "token_sort_retry_below": 0.70, "on_below_60": "REJECT" },
    { "id": "liveness",     "type": "api", "call": "POST /face-liveness",
      "content_type": "multipart/form-data",
      "retry_flow": [
        { "attempt": 1, "on_fail": "selfie-guide-2" },
        { "attempt": 2, "on_fail": "selfie-guide-3" },
        { "attempt": 3, "on_fail": "REJECT" }
      ]},
    { "id": "selfie-guide-2", "type": "ui", "msg": "Couldn't verify. Better lighting + plain background.", "then": "liveness" },
    { "id": "selfie-guide-3", "type": "ui", "msg": "Last attempt. Full face visible, remove glasses.", "then": "liveness" },
    { "id": "face-match",   "type": "api", "call": "POST /face-match",
      "content_type": "multipart/form-data",
      "compare": "selfie vs rto_photo_url",
      "threshold": 0.75, "on_fail": "REJECT", "flag_if_below_80": "+1 AMBER" },
    { "id": "pan",          "type": "api", "call": "POST /pan/advance",
      "version": "2024-12-01", "on_invalid": "REJECT", "on_deleted": "REJECT",
      "note": "PAN advanced — includes income proxy, filing status, company director flags" },
    { "id": "bav",          "type": "api", "call": "POST /bank-account/sync",
      "on_fraud_account": "REJECT_AND_FLAG", "on_invalid": "REJECT",
      "flags": { "name_below_60": "REJECT", "name_60_to_84": "+1 AMBER" } },
    { "id": "risk-gate",    "type": "gate", "rules": [
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
      // ✅ DL + face + PAN + bank all passed — activate credit or onboard partner
      activateCustomer(customer_id);
      break;

    case 'REJECTED':
      // ❌ Hard reject — DL invalid/suspended, forgery, face mismatch, fraud_account
      // flags[] tells you the exact cause
      markRejected(customer_id, flags);
      break;

    case 'MANUAL_REVIEW':
      // ⚠️ 1 amber flag — route to ops for human check
      queueForReview(customer_id, flags);
      break;
  }

  res.json({ received: true });
});

async function activateCustomer(id)      { /* activate in your system */ }
async function markRejected(id, flags)   { /* update DB, notify customer */ }
async function queueForReview(id, flags) { /* add to ops queue */ }

app.listen(3000);
```

---

### Step 3 — Frontend (React)

```jsx
// QuickPassButton.jsx
import { useState } from 'react';

export function QuickPassButton({ customerId, mobile }) {
  const [phase, setPhase] = useState('idle');

  const start = async () => {
    setPhase('loading');
    const res = await fetch('/api/kyc/start', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify({ customerId, mobile }),
    });
    const { kycUrl } = await res.json();
    setPhase('redirecting');
    window.location.href = kycUrl;
  };

  if (phase === 'idle')        return <button onClick={start}>Verify with DL</button>;
  if (phase === 'loading')     return <p>Setting up verification…</p>;
  if (phase === 'redirecting') return <p>Redirecting to secure verification…</p>;
}
```

---

### Step 4 — Test it

```bash
# Start a TurboPass session
curl -X POST http://localhost:3000/api/kyc/start \
  -H "Content-Type: application/json" \
  -d '{"customerId":"gig_001","mobile":"9999999999"}'

# Simulate APPROVED webhook
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"gig_001","status":"APPROVED","flags":[]}'

# Simulate REJECTED (DL suspended)
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"gig_001","status":"REJECTED","flags":["dl_suspended"]}'
```

---

## DL verification states

| DL status | Action |
|---|---|
| VALID | Proceed to face match |
| INVALID | Hard reject |
| SUSPENDED | Hard reject (safety-critical for gig/vehicle use cases) |
| EXPIRED | Hard reject |
| NOT_FOUND | Hard reject |

---

## Enterprise governance

| Control | Cashfree platform | Your responsibility |
|---|---|---|
| **Data residency** | India-only · AWS ap-south-1 (Mumbai) · No cross-border transfer | Receiving systems must be India-hosted or covered by a DPA |
| **Encryption** | TLS 1.3 in transit · AES-256 at rest · Session hash chain | Maintain equivalent standards in your storage layer |
| **Audit trail** | Immutable session logs retained 7 years | PMLA: 5 years minimum from relationship end — your DB must also retain |
| **CKYCR upload** | Not included — DL path does not auto-trigger CKYCR | Upload to CKYCR manually post-approval if required by your RBI licence |
| **FIU-IND — STR** | `flags[]` in webhook surfaces suspicion triggers | File STR within 7 working days of suspicion on goAML portal |
| **FIU-IND — CTR** | Transaction metadata delivered via webhook | File CTR by 15th of succeeding month for cash transactions > ₹10L |
| **Re-KYC schedule** | Relay supports re-trigger — use relay-existing-customer | HIGH risk: 2 yr · MEDIUM: 8 yr · LOW: 10 yr · PEP: 1 yr |
| **DPDP rights** | Consent event stored per DPDP Act 2023 — Section 6 | Data Principal rights (access / correction / erasure) are your obligation |
| **Board policy** | Workflow enforces your configured KYC policy | Board-approved KYC/AML policy + Designated Director required before FIU-IND registration |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| DPDP consent (standalone) | Credit bureau pull (if needed) | Aadhaar verification |
| Mobile OTP + name pre-fill | | AML/PEP screening |
| DL SmartOCR (front + back) | | |
| RTO database verification | | |
| Name cross-validation | | |
| Face liveness (3 attempts + guidance) | | |
| Face match selfie vs RTO photo | | |
| PAN Advanced check | | |
| BAV sync + fraud flag | | |
| Amber flag gate | | |

**Regulation:** RBI KYC Master Directions 2023 — Section 16 (DL as OVD) · Motor Vehicles Act 1988 (RTO database) · PMLA Sections 11A, 12 · PML Rules 2005 · DPDP Act 2023 — Section 6

**Cost:** ~₹25–35 per verification (no VKYC path)

---

## MCP — coming soon

```
/relay-quickpass

→ Claude: "Gig worker or two-wheeler loan? Credit bureau needed?"
→ Calls Relay MCP → creates + publishes workflow
→ Returns RELAY_WORKFLOW_ID, already live
```
