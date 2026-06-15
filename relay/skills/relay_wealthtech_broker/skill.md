---
name: relay-wealthtech-broker
description: Cashfree KYC workflow for WealthTech Broker/Demat account onboarding — SEBI-compliant. KRA lookup-first path (cuts 10min→2min for existing investors), selfie drop-off recovery orchestrator (addresses 29.2% abandonment), nomination step, reverse penny-drop BAV, Aadhaar eSign for 5 SEBI-mandatory documents, SEBI VKYC with geolocation. Generates working Node.js + React integration code. ~₹15–110 per onboarding depending on KRA hit and VKYC.
triggers:
  - /relay-wealthtech-broker
  - wealthtech broker onboarding
  - demat account KYC
  - trading account relay
  - SEBI KYC workflow
  - stockbroker onboarding
  - mutual fund KYC
tools:
  - Read/Write
---

# WealthTech Broker / Demat Account Onboarding

> SEBI-compliant demat + trading account KYC · KRA lookup-first (10 min → 2 min for existing investors) · Selfie recovery for 29.2% abandonment · Nomination + eSign (5 docs) + SEBI VKYC · ~₹15–110 per onboarding · SEBI KYC Master 2023

---

## Regulatory mandate

| Obligation | Regulation | Threshold / Deadline |
|---|---|---|
| KYC for securities accounts | SEBI KYC Master Circular 2023 (SEBI/HO/MIRSD/2023) | All demat and trading account openings |
| KRA registration check | SEBI KYC (Know Your Client) Regulations 2011 | First port of call for all new SEBI-regulated account openings |
| Video KYC (SEBI V-CIP) | SEBI Circular SEBI/HO/MIRSD/FATF/P/CIR/2022/158 | Mandatory for medium-risk new investors; geolocation required |
| Nomination | SEBI circular dated April 2024 | Mandatory electronic nomination — standalone screen, electronically written |
| eSign — 5 mandatory documents | SEBI Stockbrokers Regulations 1992 — Schedule II | AOF, Risk Disclosure, Rights & Obligations, Running Account Auth, Nomination Ack |
| Zero pre-checked consent | SEBI Circular on consent — Zerodha model | No pre-ticked boxes at any stage |
| AML / PEP screening | PMLA Section 11A · SEBI PMLA guidelines | All new investors |
| STR filing | PMLA Section 12 · FIU-IND | Within 7 working days of suspicion |
| CTR filing | PMLA Section 12 · FIU-IND | By 15th of succeeding month for cash > ₹10L |
| Record retention (signed docs) | SEBI IA Regulations 2013 | 5 years |

---

## What your customer experiences

**Existing investor (KRA found):** OTP → PAN confirm → bank account → eSign 5 docs → done in ~2 minutes.

**New investor:** OTP → PAN confirm → Aadhaar via DigiLocker → selfie (up to 3 guided attempts) → nomination → bank account → eSign 5 docs → optional SEBI VKYC → demat activated.

---

## Key differences from Standard CDD

| | Standard CDD | WealthTech Broker |
|---|---|---|
| Regulation | RBI KYC Master 2023 | SEBI KYC Master 2023 |
| VKYC | Optional (risk-gated) | Mandatory for medium-risk; geolocation required |
| eSign | Optional | 5 mandatory SEBI documents |
| Nomination | No | Yes (SEBI 2024: electronically written) |
| KRA lookup | No | Yes (avoids re-onboarding existing investors) |
| Consent | No pre-ticked boxes | SEBI mandates zero pre-checked boxes (Zerodha model) |

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
KRA_INTEGRATION_DEPLOYED=false   # set true when NSDL/CDSL/CAMS is connected
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "wealthtech_broker_kyc",
  "description": "SEBI demat/trading account — KRA-first, selfie recovery, nomination, eSign, SEBI VKYC",
  "trigger": "api",
  "inputs": ["customer_id", "mobile"],
  "nodes": [
    { "id": "consent",         "type": "ui",  "template": "dpdp_consent",
      "sebi_note": "zero pre-checked boxes — SEBI mandate", "on_denied": "REJECT" },
    { "id": "kra-check",       "type": "condition",
      "if": "KRA_INTEGRATION_DEPLOYED == true", "then": "kra-lookup", "else": "full-onboarding" },
    { "id": "kra-lookup",      "type": "api", "call": "{{KRA_URL}}/search", "in": { "pan": "{{pan}}" },
      "on_verified": "kra-short-path", "on_pending": "full-onboarding", "on_not_found": "full-onboarding" },
    { "id": "kra-short-path",  "type": "sequence",
      "nodes": ["bav", "esign-docs", "APPROVE"],
      "note": "Existing investor — skip PAN/Aadhaar/face. BAV + eSign only." },

    { "id": "mob-send",        "type": "api", "call": "POST /mobile360/otp/send" },
    { "id": "mob-verify",      "type": "api", "call": "POST /mobile360/otp/verify",
      "prefill_outputs": ["pan", "name"] },
    { "id": "pan",             "type": "api", "call": "POST /pan", "version": "2024-12-01",
      "on_invalid": "REJECT", "flags": { "aadhaar_seeding_not_Y": "+1 AMBER" } },
    { "id": "digilocker",      "type": "api", "call": "POST /digilocker", "doc": "AADHAAR",
      "timeout_min": 10, "on_timeout": "digilocker-retry", "on_denied": "ocr" },
    { "id": "digilocker-retry","type": "api", "call": "POST /digilocker", "doc": "AADHAAR", "on_timeout": "ocr" },
    { "id": "ocr",             "type": "api", "call": "POST /bharat-ocr", "doc": "AADHAAR",
      "content_type": "multipart/form-data", "on_forgery": "REJECT", "flag_on_fallback": "+1 AMBER" },

    { "id": "selfie-guide",    "type": "ui",
      "tips": ["Good lighting", "Remove glasses", "Plain background", "Look at camera"],
      "then": "liveness" },
    { "id": "liveness",        "type": "api", "call": "POST /face-liveness",
      "content_type": "multipart/form-data",
      "retry_flow": [
        { "attempt": 1, "on_fail": "selfie-guide-2" },
        { "attempt": 2, "on_fail": "selfie-guide-3" },
        { "attempt": 3, "on_fail": "vkyc-sebi" }
      ]
    },
    { "id": "selfie-guide-2",  "type": "ui", "msg": "Couldn't verify. Try better lighting.", "then": "liveness" },
    { "id": "selfie-guide-3",  "type": "ui", "msg": "One more try. Full face visible, plain background.", "then": "liveness" },
    { "id": "face-match",      "type": "api", "call": "POST /face-match",
      "content_type": "multipart/form-data", "threshold": 0.75,
      "on_fail": "REJECT", "flag_if_below_80": "+1 AMBER" },
    { "id": "name-match",      "type": "api", "call": "POST /name-match", "token_sort_retry_below": 0.70 },

    { "id": "nomination",      "type": "ui", "template": "nomination_form",
      "note": "SEBI 2024: standalone screen, electronically written acknowledgement" },

    { "id": "bav",             "type": "api", "call": "POST /bank-account/sync",
      "note": "Reverse penny-drop preferred in wealthtech — no ₹1 debit from customer",
      "on_fraud_account": "REJECT_AND_FLAG", "on_invalid": "REJECT",
      "flags": { "name_60_to_85": "+1 AMBER", "name_below_60": "REJECT" } },

    { "id": "esign-docs",      "type": "api", "call": "POST /esignature",
      "documents": [
        "Account Opening Form (AOF)",
        "Risk Disclosure Document",
        "Rights & Obligations",
        "Running Account Authorization",
        "Nomination Acknowledgement"
      ],
      "on_declined": "REJECT", "on_expired": "resend-esign-once" },

    { "id": "risk-gate",       "type": "gate", "rules": [
        { "if": "amber_flags == 0", "out": "APPROVE" },
        { "if": "amber_flags <= 2", "out": "vkyc-sebi" },
        { "if": "amber_flags >= 3", "out": "MANUAL_REVIEW" }
    ]},

    { "id": "vkyc-sebi",       "type": "api", "call": "POST /vkyc",
      "meta": { "regulator": "SEBI", "geolocation_required": true,
                "preferred_language": "{{input.lang | default: 'hi'}}" },
      "nudge_at": "-4h",
      "states": { "APPROVE": "APPROVE", "REJECT": "REJECT",
                  "UNABLE_TO_VALIDATE": "vkyc-reschedule", "FAILED": "MANUAL_ESCALATION" }
    }
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
  const { customerId, mobile, preferredLanguage = 'hi' } = req.body;

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
        metadata:     { preferred_language: preferredLanguage },
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

  const { customer_id, status, flags, signed_document_url } = req.body;

  switch (status) {
    case 'APPROVED':
      // ✅ Demat account can be activated
      // For KRA path: signed_document_url may be absent (no eSign in short path)
      activateDematAccount(customer_id);
      break;

    case 'VKYC_REQUIRED':
      // 📹 SEBI VKYC — Cashfree sends link. Geolocation captured by agent.
      updateStatus(customer_id, 'VKYC_PENDING');
      break;

    case 'VKYC_APPROVED':
      activateDematAccount(customer_id);
      if (signed_document_url) storeDocuments(customer_id, signed_document_url);
      break;

    case 'REJECTED':
      markRejected(customer_id, flags);
      break;

    case 'MANUAL_REVIEW':
      // 3+ amber flags — compliance team reviews
      queueComplianceReview(customer_id, flags);
      break;

    case 'MANUAL_ESCALATION':
      // VKYC recording failed — preserve all partial data
      queueOpsReview(customer_id, 'vkyc_recording_failed');
      break;
  }

  res.json({ received: true });
});

async function activateDematAccount(id) { /* activate in your system */ }
async function storeDocuments(id, url)  { /* store signed docs — 5yr retention */ }
async function updateStatus(id, s)      { /* update DB */ }
async function markRejected(id, flags)  { /* update DB, notify customer */ }
async function queueComplianceReview(id, flags) { /* compliance queue */ }
async function queueOpsReview(id, note) { /* ops queue */ }

app.listen(3000);
```

---

### Step 3 — Frontend (React)

```jsx
// KYCFlow.jsx
import { useState } from 'react';

export function DematKYC({ customerId, mobile, preferredLanguage = 'hi' }) {
  const [phase, setPhase] = useState('idle');

  const start = async () => {
    setPhase('loading');
    const res = await fetch('/api/kyc/start', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify({ customerId, mobile, preferredLanguage }),
    });
    const { kycUrl } = await res.json();
    setPhase('redirecting');
    window.location.href = kycUrl;
  };

  return (
    <>
      {phase === 'idle'        && <button onClick={start}>Open demat account</button>}
      {phase === 'loading'     && <p>Setting up your KYC…</p>}
      {phase === 'redirecting' && <p>Redirecting to secure verification…</p>}
    </>
  );
}
```

---

### Step 4 — Test it

```bash
curl -X POST http://localhost:3000/api/kyc/start \
  -H "Content-Type: application/json" \
  -d '{"customerId":"inv_001","mobile":"9999999999","preferredLanguage":"hi"}'

# Simulate KRA short path (existing investor, approved)
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"inv_001","status":"APPROVED","flags":[]}'

# Simulate VKYC required (medium-risk new investor)
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"inv_001","status":"VKYC_REQUIRED","flags":["digilocker_fallback","face_match_borderline"]}'
```

---

## Conversion benchmarks (HyperVerge WealthTech Report)

| Optimization in this workflow | Conversion impact |
|---|---|
| KRA lookup-first | Existing investors: 10 min → 2 min |
| Mobile360 PAN pre-fill | ~17% fewer PAN drop-offs |
| 3-attempt selfie orchestrator with guidance | Addresses 29.2% selfie abandonment |
| DigiLocker → bharat-ocr fallback | Prevents 5.6% DigiLocker drop-offs |
| eSign nudge 4h before expiry | Recovers ~30% of pending sessions |

Industry baseline: 34% conversion. Best-in-class (Zerodha, Kotak): 60%+ with zero human touch.

---

## Enterprise governance

| Control | Cashfree platform | Your responsibility |
|---|---|---|
| **Data residency** | India-only · AWS ap-south-1 (Mumbai) · No cross-border transfer | Receiving systems must be India-hosted or covered by a DPA |
| **Encryption** | TLS 1.3 in transit · AES-256 at rest · Session hash chain | Maintain equivalent standards in your storage layer |
| **Audit trail** | Immutable session logs retained 7 years | PMLA: 5 years minimum from relationship end — your DB must also retain |
| **KRA upload** | Not included in Relay | Upload to KRA (NSDL/CDSL/CAMS) within 10 working days — SEBI mandate |
| **FIU-IND — STR** | `flags[]` in webhook surfaces suspicion triggers | File STR within 7 working days of suspicion on goAML portal |
| **FIU-IND — CTR** | Transaction metadata delivered via webhook | File CTR by 15th of succeeding month for cash transactions > ₹10L |
| **Re-KYC schedule** | Relay supports re-trigger — use relay-existing-customer | HIGH risk: 2 yr · MEDIUM: 8 yr · LOW: 10 yr · PEP: 1 yr |
| **DPDP rights** | Consent event stored per DPDP Act 2023 — Section 6 | Data Principal rights (access / correction / erasure) are your obligation |
| **Board policy** | Workflow enforces your configured KYC policy | Board-approved KYC/AML policy + Designated Director required before FIU-IND registration |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| DPDP consent (zero pre-checked — SEBI) | KRA integration (NSDL/CDSL/CAMS) | AML/PEP screening |
| Mobile360 OTP + PAN pre-fill | 5-year signed doc storage | |
| PAN 360 (SEBI: must be VALID) | | |
| DigiLocker → bharat-ocr fallback | | |
| 3-attempt selfie recovery orchestrator | | |
| Face match (0.75 threshold) | | |
| Name cross-validation + token-sort retry | | |
| Nomination (SEBI 2024 electronically written) | | |
| BAV reverse penny-drop | | |
| eSign — 5 SEBI-mandatory documents | | |
| SEBI VKYC with geolocation | | |
| VKYC pre-expiry nudge | | |
| Multilingual + age-65 assisted routing | | |

**Regulation:** SEBI KYC Master Circular 2023 (SEBI/HO/MIRSD/2023) · SEBI KYC Regulations 2011 · SEBI Stockbrokers Regulations 1992 — Schedule II · SEBI V-CIP Circular 2022 · PMLA Sections 11A, 12 · PML Rules 2005 · DPDP Act 2023 — Section 6

**Cost:** KRA hit ~₹15–20 · Full, no VKYC ~₹40–55 · Full + SEBI VKYC ~₹90–110

---

## MCP — coming soon

```
/relay-wealthtech-broker

→ Claude: "KRA integrated? VKYC mandatory? Languages needed?"
→ Creates + publishes workflow
→ Returns RELAY_WORKFLOW_ID, already live
```
