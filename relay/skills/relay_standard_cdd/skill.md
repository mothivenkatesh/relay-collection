---
name: relay-standard-cdd
description: Cashfree KYC workflow for full CDD with Video KYC — bank accounts, NBFC onboarding, savings/current accounts. Parallel document + financial verification tracks, risk-gated VKYC, CKYC async upload. Generates working Node.js + React integration code, compact Relay workflow spec, RBI compliance brief. 5–10 min customer journey. ~₹35–100 per verification depending on VKYC.
triggers:
  - /relay-standard-cdd
  - standard KYC
  - bank account onboarding
  - NBFC KYC workflow
  - video KYC relay
  - savings account KYC
tools:
  - Read/Write
---

# Standard CDD with Video KYC — Bank / NBFC Onboarding

> Full RBI-compliant CDD · PAN + Aadhaar + Face + Bank + conditional VKYC · 5–10 min journey · ~₹35–50 without VKYC, ~₹85–100 with VKYC · RBI KYC Master 2023

---

## Regulatory mandate

| Obligation | Regulation | Threshold / Deadline |
|---|---|---|
| Customer identification (OVD + PAN) | RBI KYC Master Directions 2023 — Section 16 (OVD) · Section 17 (PAN/Aadhaar) | All new customer accounts |
| Video KYC (V-CIP) | RBI KYC Master Directions 2023 — Section 18A | Mandatory when DigiLocker fails or amber flags ≥ 1 |
| CKYC upload | RBI KYC MD 2023 — Section 56 · PMLA Rule 9(1A) | Within 10 business days of onboarding |
| AML / PEP screening | PMLA Section 11A · PML (Maintenance of Records) Rules 2005 | All new customers |
| STR filing | PMLA Section 12 · FIU-IND guidelines | Within 7 working days of suspicion |
| CTR filing | PMLA Section 12 · FIU-IND guidelines | By 15th of succeeding month for cash > ₹10L |
| Record retention | PMLA Section 12 | 5 years from account closure |
| Beneficial ownership disclosure | KYC MD 2023 — October 2023 Amendment | All shareholders ≥ 10% shareholding |
| Data consent | DPDP Act 2023 — Section 6 | Standalone consent screen before any data collection |

---

## What your customer experiences

1. Consents to data collection (standalone screen, DPDP-compliant)
2. Enters mobile OTP — sees PAN pre-filled if Mobile360 has the data (~70%)
3. Document track: verifies Aadhaar via DigiLocker, or uploads photo + takes selfie
4. Financial track (runs in parallel): bank account verified instantly
5. Clean profiles: approved straight-through, no human needed
6. Medium-risk profiles: invited to a 5-minute video KYC call with a Cashfree agent
7. VKYC completed → account activated, CKYC uploaded in background within 10 days

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
CKYC_DOCKER_DEPLOYED=false     # set true when on-prem CKYC Docker is running
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "standard_cdd_vkyc",
  "description": "Full CDD — PAN + Aadhaar + Face + BAV + conditional VKYC",
  "trigger": "api",
  "inputs": ["customer_id", "mobile"],
  "parallel_tracks": true,
  "nodes": [
    { "id": "consent",          "type": "ui",   "template": "dpdp_consent", "on_denied": "REJECT" },
    { "id": "mob-send",         "type": "api",  "call": "POST /mobile360/otp/send" },
    { "id": "mob-verify",       "type": "api",  "call": "POST /mobile360/otp/verify", "prefill_outputs": ["pan", "name", "risk_level"] },

    { "track": "A",
      "nodes": [
        { "id": "pan",          "type": "api",  "call": "POST /pan", "version": "2024-12-01", "on_invalid": "REJECT" },
        { "id": "digilocker",   "type": "api",  "call": "POST /digilocker", "doc": "AADHAAR", "timeout_min": 10, "on_timeout": "digilocker-retry", "on_denied": "ocr" },
        { "id": "digilocker-retry", "type": "api", "call": "POST /digilocker", "doc": "AADHAAR", "on_timeout": "ocr" },
        { "id": "ocr",          "type": "api",  "call": "POST /bharat-ocr", "doc": "AADHAAR", "content_type": "multipart/form-data", "on_forgery": "REJECT", "flag_on_fallback": "+1 AMBER" }
      ]
    },

    { "track": "B",
      "nodes": [
        { "id": "bav",          "type": "api",  "call": "POST /bank-account/sync", "on_fraud_account": "REJECT_AND_FLAG", "on_invalid": "REJECT", "on_name_moderate": "+1 AMBER" },
        { "id": "ckyc-check",   "type": "condition", "if": "CKYC_DOCKER_DEPLOYED == true", "then": "ckyc-lookup", "else": "flag_ckyc_skip" },
        { "id": "aml-pep",      "type": "api",  "call": "{{INTERNAL_AML_URL}}/screen", "on_sanctions": "REJECT", "on_pep": "ESCALATE_EDD" }
      ]
    },

    { "id": "merge",   "type": "join", "waits_for": ["A", "B"] },

    { "id": "liveness",         "type": "api",  "call": "POST /face-liveness", "content_type": "multipart/form-data", "max_retries": 3, "guidance_ui": true, "on_exhausted": "vkyc" },
    { "id": "face-match",       "type": "api",  "call": "POST /face-match", "content_type": "multipart/form-data", "threshold": 0.75, "on_fail": "REJECT" },
    { "id": "name-match",       "type": "api",  "call": "POST /name-match", "token_sort_retry_below": 0.70 },

    { "id": "risk-gate",        "type": "gate", "rules": [
        { "if": "amber_flags == 0",  "out": "APPROVE" },
        { "if": "amber_flags <= 2",  "out": "vkyc" },
        { "if": "amber_flags >= 3",  "out": "ESCALATE_EDD" }
    ]},

    { "id": "vkyc",             "type": "api",  "call": "POST /vkyc",
      "meta": { "preferred_language": "{{input.lang | default: 'hi'}}", "assisted_preferred": "{{age >= 65}}" },
      "nudge_at": "-4h",
      "states": {
        "APPROVE": "ckyc-upload",
        "REJECT": "REJECT",
        "UNABLE_TO_VALIDATE": "vkyc-reschedule",
        "LINK_EXPIRED": "vkyc-regen-once",
        "FAILED": "MANUAL_ESCALATION"
      }
    },
    { "id": "ckyc-upload",      "type": "api",  "call": "{{CKYC_ONPREM_URL}}/upload", "async": true, "mandate_days": 10 }
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

// ─── Start KYC ───────────────────────────────────────────────────────────────
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
        customer_id:       customerId,
        mobile,
        redirect_url:      `${BASE_URL}/kyc/done`,
        webhook_url:       `${BASE_URL}/api/kyc/webhook`,
        metadata: { preferred_language: preferredLanguage },
      }),
    }
  );

  const { run_id, hosted_url } = await r.json();
  res.json({ kycUrl: hosted_url, runId: run_id });
});

// ─── Webhook ──────────────────────────────────────────────────────────────────
app.post('/api/kyc/webhook', (req, res) => {
  const sig = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody)
    .digest('base64');
  if (sig !== expected) return res.status(401).send('Bad signature');

  const { customer_id, status, flags, vkyc_link } = req.body;

  switch (status) {
    case 'APPROVED':
      // ✅ Straight-through — no VKYC needed
      activateAccount(customer_id);
      break;

    case 'VKYC_REQUIRED':
      // 📹 Customer invited to video KYC — Cashfree sends link via SMS/WhatsApp
      // No action needed from you; Cashfree manages the VKYC session
      updateStatus(customer_id, 'VKYC_PENDING');
      break;

    case 'VKYC_APPROVED':
      // ✅ VKYC passed — activate and CKYC uploads in background
      activateAccount(customer_id);
      break;

    case 'VKYC_UNABLE_TO_VALIDATE':
      // 🔄 Agent couldn't validate — Cashfree reschedules automatically
      updateStatus(customer_id, 'VKYC_RESCHEDULED');
      break;

    case 'REJECTED':
      // ❌ Hard reject — flags[] contains reason
      markRejected(customer_id, flags);
      break;

    case 'ESCALATE_EDD':
      // 🔍 3+ amber flags or PEP match — route to compliance team
      escalateToEDD(customer_id, flags);
      break;

    case 'MANUAL_ESCALATION':
      // ⚠️ VKYC recording failed — do NOT auto-reject, ops needs to review
      queueOpsReview(customer_id, 'vkyc_recording_failed');
      break;
  }

  res.json({ received: true });
});

async function activateAccount(id)       { /* update DB */ }
async function updateStatus(id, status)  { /* update DB */ }
async function markRejected(id, flags)   { /* update DB, notify customer */ }
async function escalateToEDD(id, flags)  { /* add to compliance queue */ }
async function queueOpsReview(id, note)  { /* add to ops queue */ }

app.listen(3000);
```

---

### Step 3 — Frontend (React)

```jsx
// KYCFlow.jsx
import { useState, useEffect } from 'react';

export function KYCFlow({ customerId, mobile, preferredLanguage = 'hi' }) {
  const [phase, setPhase] = useState('idle');
  const [status, setStatus] = useState(null);

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

  // Poll for result after customer returns from Cashfree's page
  useEffect(() => {
    if (phase !== 'returned') return;
    const interval = setInterval(async () => {
      const res = await fetch(`/api/kyc/status/${customerId}`);
      const data = await res.json();
      if (data.status !== 'IN_PROGRESS') {
        setStatus(data.status);
        setPhase('done');
        clearInterval(interval);
      }
    }, 3000);
    return () => clearInterval(interval);
  }, [phase]);

  if (phase === 'idle')      return <button onClick={start}>Open account</button>;
  if (phase === 'loading')   return <p>Setting up verification…</p>;
  if (phase === 'returned')  return <p>Processing… this takes a few seconds.</p>;
  if (phase === 'done') {
    if (status === 'APPROVED')      return <p>✅ Account opened! Redirecting…</p>;
    if (status === 'VKYC_PENDING')  return <p>📹 Video KYC link sent to your phone.</p>;
    if (status === 'REJECTED')      return <p>❌ Verification unsuccessful. Contact support.</p>;
    return <p>Under review — we'll reach out within 24 hours.</p>;
  }
}
```

---

### Step 4 — Test it

```bash
# Start KYC
curl -X POST http://localhost:3000/api/kyc/start \
  -H "Content-Type: application/json" \
  -d '{"customerId":"test_001","mobile":"9999999999","preferredLanguage":"hi"}'

# Simulate APPROVED webhook
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign with CASHFREE_WEBHOOK_SECRET>" \
  -d '{"customer_id":"test_001","status":"APPROVED","flags":[]}'

# Simulate VKYC_REQUIRED webhook
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"test_001","status":"VKYC_REQUIRED","flags":["aadhaar_not_linked"]}'
```

---

## VKYC cost and state reference

| VKYC outcome | Cost | Your action |
|---|---|---|
| APPROVE | ₹50 | `activateAccount()` |
| REJECT | ₹50 | `markRejected()` — do NOT retry VKYC |
| UNABLE_TO_VALIDATE | ₹30 | Cashfree reschedules — update status to `VKYC_RESCHEDULED` |
| LINK_EXPIRED | ₹0 | Cashfree regens once — no action |
| FAILED (recording) | ₹50 | `queueOpsReview()` — do NOT auto-reject |

---

## Enterprise governance

| Control | Cashfree platform | Your responsibility |
|---|---|---|
| **Data residency** | India-only · AWS ap-south-1 (Mumbai) · No cross-border transfer | Receiving systems must be India-hosted or covered by a DPA |
| **Encryption** | TLS 1.3 in transit · AES-256 at rest · Session hash chain | Maintain equivalent standards in your storage layer |
| **Audit trail** | Immutable session logs retained 7 years | PMLA: 5 years minimum from relationship end — your DB must also retain |
| **CKYCR upload** | Async upload node with 10-business-day countdown timer | Deploy CKYCR Docker (CERSAI) or connect via CERSAI API credentials |
| **FIU-IND — STR** | `flags[]` in webhook surfaces suspicion triggers | File STR within 7 working days of suspicion on goAML portal |
| **FIU-IND — CTR** | Transaction metadata delivered via webhook | File CTR by 15th of succeeding month for cash transactions > ₹10L |
| **Re-KYC schedule** | Relay supports re-trigger — use relay-existing-customer | HIGH risk: 2 yr · MEDIUM: 8 yr · LOW: 10 yr · PEP: 1 yr |
| **DPDP rights** | Consent event stored per DPDP Act 2023 — Section 6 | Data Principal rights (access / correction / erasure) are your obligation |
| **Board policy** | Workflow enforces your configured KYC policy | Board-approved KYC/AML policy + Designated Director required before FIU-IND registration |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| DPDP standalone consent | CKYC on-prem Docker | AML/PEP (external API) |
| Mobile360 OTP + PAN pre-fill | AML/PEP endpoint URL | Cross-bank mule detection |
| PAN 360 with Aadhaar seeding check | VKYC multilingual agent pool | |
| Parallel Doc + Financial tracks | | |
| DigiLocker → bharat-ocr fallback | | |
| Face liveness (3 attempts + guidance) | | |
| Face match (threshold 0.75) | | |
| Name cross-validation + token-sort retry | | |
| BAV sync + fraud_account hard reject | | |
| Amber flag aggregator | | |
| VKYC: all 5 states handled correctly | | |
| CKYC async upload (10-day mandate timer) | | |
| Pre-expiry VKYC nudge (4h before expiry) | | |
| Multilingual + age-65 assisted routing | | |

**Regulation:** RBI KYC Master Directions 2023 (Sections 16, 17, 18A, 56) · PMLA Sections 11A, 12 · PML Rules 2005 · KYC MD Oct 2023 Amendment (10% UBO) · DPDP Act 2023 — Section 6

**Cost:** ~₹35–50 without VKYC · ~₹85–100 with VKYC approved · ~₹110–120 for UNABLE_TO_VALIDATE ×2

---

## MCP — coming soon

```
/relay-standard-cdd

→ Claude: "VKYC required? CKYC Docker deployed? Preferred languages?"
→ Calls Relay MCP → creates workflow with your config
→ Returns RELAY_WORKFLOW_ID, already live
→ Outputs code above, pre-filled
```
