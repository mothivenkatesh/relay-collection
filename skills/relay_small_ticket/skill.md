---
name: relay-small-ticket
description: Cashfree KYC workflow for small-ticket lending — BNPL, PayLater, quick loans, gig worker credit (<₹60K). Generates working Node.js + React integration code, compact Relay workflow spec, and RBI compliance brief. No Video KYC. Customer completes in 3–5 minutes. ~₹30–40 per verification.
triggers:
  - /relay-small-ticket
  - small ticket lending
  - BNPL KYC workflow
  - quick loan onboarding
  - gig worker credit KYC
  - PayLater workflow
tools:
  - Read/Write
---

# Small-Ticket KYC — BNPL / Quick Loans

> PAN + Aadhaar + Face + Bank · For loans and credit limits <₹60K · 3–5 min customer journey · ~₹30–40 per verification · RBI DLG Guidelines + PMLA

---

## Regulatory mandate

| Obligation | Regulation | Threshold / Deadline |
|---|---|---|
| Customer identification | RBI KYC Master Directions 2023 — Section 16 (OVD) · Section 17 (PAN) | All borrowers |
| Digital lending KYC | RBI Digital Lending Guidelines 2022 (RBI/2022-23/111) — Para 5 | All LSP / DLG arrangements |
| Consent capture | DPDP Act 2023 — Section 6 · RBI DLG Guidelines — Para 6 | Standalone screen before any data collection |
| AML screening | PMLA Section 11A | All borrowers |
| STR filing | PMLA Section 12 · FIU-IND | Within 7 working days of suspicion |
| CTR filing | PMLA Section 12 · FIU-IND | By 15th of succeeding month for cash > ₹10L |
| Record retention | PMLA Section 12 | 5 years from loan closure |
| Credit bureau reporting | RBI Credit Information Companies Regulations 2006 | Monthly — all credit accounts |
| Loan limit scope | RBI DLG Guidelines 2022 | This workflow is calibrated for < ₹60K; use relay-standard-cdd above ₹60K |

---

## What your customer experiences

1. Taps "Get credit limit" — enters mobile number, receives OTP
2. Sees PAN pre-filled (~70% of the time, from mobile intelligence) — confirms with one tap
3. Verifies Aadhaar via DigiLocker (preferred) or uploads Aadhaar photo
4. Takes a quick selfie — face is matched against Aadhaar photo
5. Enters bank account number — verified instantly
6. Done. Decision in seconds.

---

## Quickstart — 15 minutes to live

### Environment variables

```env
CASHFREE_CLIENT_ID=           # sandbox.cashfree.com → Secure ID → Developers
CASHFREE_CLIENT_SECRET=
CASHFREE_BASE_URL=https://sandbox.cashfree.com/verification
CASHFREE_WEBHOOK_SECRET=      # Dashboard → Webhooks → copy secret
BASE_URL=http://localhost:3000
RELAY_WORKFLOW_ID=            # paste after importing workflow below
```

---

### Step 1 — Import workflow into Relay

Go to Relay → Workflows → New → Import JSON → paste:

```json
{
  "name": "small_ticket_kyc",
  "description": "BNPL / quick loans <60K — PAN + Aadhaar + Face + BAV",
  "trigger": "api",
  "inputs": ["customer_id", "mobile"],
  "nodes": [
    { "id": "consent",           "type": "ui",   "template": "dpdp_consent", "on_denied": "REJECT" },
    { "id": "mob-send",          "type": "api",  "call": "POST /mobile360/otp/send", "in": { "mobile_number": "{{mobile}}" } },
    { "id": "mob-verify",        "type": "api",  "call": "POST /mobile360/otp/verify", "prefill_outputs": ["pan", "name", "risk_level"] },
    { "id": "pan",               "type": "api",  "call": "POST /pan", "version": "2024-12-01", "on_invalid": "REJECT", "on_deleted": "REJECT" },
    { "id": "digilocker",        "type": "api",  "call": "POST /digilocker", "doc": "AADHAAR", "timeout_min": 10, "on_timeout": "digilocker-retry", "on_denied": "ocr" },
    { "id": "digilocker-retry",  "type": "api",  "call": "POST /digilocker", "doc": "AADHAAR", "on_timeout": "ocr" },
    { "id": "ocr",               "type": "api",  "call": "POST /bharat-ocr", "doc": "AADHAAR", "content_type": "multipart/form-data", "on_forgery": "REJECT", "flag_on_ocr_fallback": "+1 AMBER" },
    { "id": "liveness",          "type": "api",  "call": "POST /face-liveness", "content_type": "multipart/form-data", "max_retries": 3, "guidance_ui_between_retries": true, "on_exhausted": "REJECT" },
    { "id": "face-match",        "type": "api",  "call": "POST /face-match", "content_type": "multipart/form-data", "threshold": 0.75, "on_fail": "REJECT" },
    { "id": "name-match",        "type": "api",  "call": "POST /name-match", "token_sort_retry_if_below": 0.70 },
    { "id": "bav",               "type": "api",  "call": "POST /bank-account/sync", "on_fraud_account": "REJECT_AND_FLAG", "on_invalid": "REJECT", "rate_limit": "15/account/24h" },
    { "id": "risk-gate",         "type": "gate", "rules": [
        { "if": "amber_flags == 0",  "out": "APPROVE" },
        { "if": "amber_flags <= 2",  "out": "MANUAL_REVIEW" },
        { "if": "amber_flags >= 3",  "out": "REJECT" }
    ]}
  ]
}
```

Copy the workflow ID → set as `RELAY_WORKFLOW_ID`.

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

// ─── Start KYC ──────────────────────────────────────────────────────────────
// Call this from your frontend when customer clicks "Get credit limit"
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
  // hosted_url — redirect your customer here. Cashfree hosts the KYC UI.
  res.json({ kycUrl: hosted_url, runId: run_id });
});

// ─── Webhook handler ─────────────────────────────────────────────────────────
// Cashfree calls this when KYC is complete. No polling needed.
app.post('/api/kyc/webhook', (req, res) => {
  // Always verify the signature first
  const sig = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody)
    .digest('base64');

  if (sig !== expected) return res.status(401).send('Bad signature');

  const { customer_id, run_id, status, flags } = req.body;

  switch (status) {
    case 'APPROVED':
      // ✅ Activate credit limit — all checks passed
      activateCreditLimit(customer_id);
      break;

    case 'REJECTED':
      // ❌ One or more hard-reject signals: PAN invalid, forgery, face mismatch, fraud_account
      // flags[] tells you which signal triggered the rejection
      markRejected(customer_id, flags);
      break;

    case 'MANUAL_REVIEW':
      // ⚠️ 1–2 amber flags — route to your ops queue for human review
      queueForReview(customer_id, flags);
      break;
  }

  res.json({ received: true }); // must respond 200 or Cashfree retries
});

// Your DB calls go here
async function activateCreditLimit(id) { /* update DB */ }
async function markRejected(id, flags) { /* update DB, notify customer */ }
async function queueForReview(id, flags) { /* add to ops queue */ }

app.listen(3000);
```

**Python alternative:**

```python
# app.py (Flask)
import hmac, hashlib, base64
from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)

@app.route('/api/kyc/start', methods=['POST'])
def start_kyc():
    data = request.json
    r = requests.post(
        f"https://api.cashfree.com/relay/v1/workflows/{os.environ['RELAY_WORKFLOW_ID']}/runs",
        headers={
            'x-client-id':     os.environ['CASHFREE_CLIENT_ID'],
            'x-client-secret': os.environ['CASHFREE_CLIENT_SECRET'],
        },
        json={
            'customer_id':  data['customerId'],
            'mobile':       data['mobile'],
            'redirect_url': f"{os.environ['BASE_URL']}/kyc/done",
            'webhook_url':  f"{os.environ['BASE_URL']}/api/kyc/webhook",
        }
    )
    result = r.json()
    return jsonify({'kycUrl': result['hosted_url'], 'runId': result['run_id']})

@app.route('/api/kyc/webhook', methods=['POST'])
def kyc_webhook():
    sig      = request.headers.get('x-cashfree-signature')
    expected = base64.b64encode(
        hmac.new(os.environ['CASHFREE_WEBHOOK_SECRET'].encode(),
                 request.data, hashlib.sha256).digest()
    ).decode()
    if sig != expected:
        return 'Bad signature', 401

    payload = request.json
    status, customer_id = payload['status'], payload['customer_id']

    if status == 'APPROVED':
        activate_credit_limit(customer_id)
    elif status == 'REJECTED':
        mark_rejected(customer_id, payload.get('flags', []))
    elif status == 'MANUAL_REVIEW':
        queue_for_review(customer_id, payload.get('flags', []))

    return jsonify({'received': True})
```

---

### Step 3 — Frontend (React)

```jsx
// KYCButton.jsx
import { useState } from 'react';

export function KYCButton({ customerId, mobile }) {
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
    // Customer completes KYC on Cashfree's hosted page (~3–5 min)
    // Cashfree fires your /api/kyc/webhook when done
    // Cashfree redirects customer back to BASE_URL/kyc/done
  };

  if (phase === 'idle')        return <button onClick={start}>Check eligibility</button>;
  if (phase === 'loading')     return <p>Setting up secure verification…</p>;
  if (phase === 'redirecting') return <p>Redirecting…</p>;
}

// pages/kyc/done.jsx — landing page after customer returns from Cashfree
export default function KYCDone() {
  // Decision comes via webhook (async), not URL params.
  // Show a waiting state; update via your own API polling or WebSocket.
  return (
    <div>
      <h2>Verification submitted</h2>
      <p>We're processing your details. This usually takes under 30 seconds.</p>
    </div>
  );
}
```

---

### Step 4 — Test it

```bash
# 1. Start a KYC session
curl -X POST http://localhost:3000/api/kyc/start \
  -H "Content-Type: application/json" \
  -d '{"customerId": "test_001", "mobile": "9999999999"}'

# Returns: { "kycUrl": "https://verify.cashfree.com/...", "runId": "run_abc" }

# 2. Open kycUrl in your browser and complete the flow with sandbox test credentials:
#    PAN:  ABCDE1234F  |  Aadhaar: 1234 5678 9012  |  OTP: any 6 digits

# 3. Cashfree fires your webhook. Simulate it:
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <generate with your CASHFREE_WEBHOOK_SECRET>" \
  -d '{"customer_id":"test_001","run_id":"run_abc","status":"APPROVED","flags":[]}'
```

---

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Missing `x-api-version: 2024-12-01` on PAN call | `aadhaar_seeding_status` silently absent | Relay workflow spec sets this automatically |
| Sending base64 for face APIs | 400 error | Relay sends raw binary (multipart) — handled by workflow |
| Not verifying webhook signature | Security gap | Always verify before processing — see webhook handler above |
| Same `verification_id` for multiple calls | 409 conflict | Relay generates unique IDs per node automatically |
| Re-verifying same bank account >15 times in 24h | Account auto-flagged as fraud | Relay deduplicates; don't call BAV manually in parallel |

---

## Enterprise governance

| Control | Cashfree platform | Your responsibility |
|---|---|---|
| **Data residency** | India-only · AWS ap-south-1 (Mumbai) · No cross-border transfer | Receiving systems must be India-hosted or covered by a DPA |
| **Encryption** | TLS 1.3 in transit · AES-256 at rest · Session hash chain | Maintain equivalent standards in your storage layer |
| **Audit trail** | Immutable session logs retained 7 years | PMLA: 5 years minimum from relationship end — your DB must also retain |
| **Credit bureau** | Not included in Relay | Report to all 4 credit bureaus (CIBIL, Experian, Equifax, CRIF) monthly — mandatory |
| **FIU-IND — STR** | `flags[]` in webhook surfaces suspicion triggers | File STR within 7 working days of suspicion on goAML portal |
| **FIU-IND — CTR** | Transaction metadata delivered via webhook | File CTR by 15th of succeeding month for cash transactions > ₹10L |
| **Re-KYC schedule** | Relay supports re-trigger — use relay-existing-customer | HIGH risk: 2 yr · MEDIUM: 8 yr · LOW: 10 yr · PEP: 1 yr |
| **DPDP rights** | Consent event stored per DPDP Act 2023 — Section 6 | Data Principal rights (access / correction / erasure) are your obligation |
| **Board policy** | Workflow enforces your configured KYC policy | Board-approved KYC/AML policy + Designated Director required before FIU-IND registration |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| DPDP consent (standalone, not bundled T&C) | CKYC Docker (for CKYC upload post-approval) | AML / PEP screening |
| Mobile OTP + PAN pre-fill (~70% fill rate) | | Cross-bank mule detection |
| PAN 360 with `aadhaar_seeding_status` check | | |
| Aadhaar via DigiLocker → bharat-ocr fallback | | |
| Face liveness (3 attempts + guidance UI) | | |
| Face match selfie vs Aadhaar photo (0.75 threshold) | | |
| Name cross-validation with token-sort retry | | |
| Bank account verification (sync + fraud flag) | | |
| Amber flag aggregator (0=APPROVE, 1–2=REVIEW, 3+=REJECT) | | |
| Hard reject: PAN invalid, forgery, face mismatch, fraud_account | | |

**Regulation:** RBI Digital Lending Guidelines 2022 (RBI/2022-23/111) — Para 5, 6 · PMLA Sections 11A, 12 · PML Rules 2005 · RBI Credit Information Companies Regulations 2006 · DPDP Act 2023 — Section 6

**Cost per verification:** ~₹30–40 (no VKYC path)

---

## MCP — coming soon

```
/relay-small-ticket

→ Claude: "VKYC needed? CKYC Docker deployed?"
→ Calls Relay MCP → creates + publishes workflow
→ Returns RELAY_WORKFLOW_ID (already live)
→ Outputs code above, pre-filled

Time to live: under 60 seconds.
```
