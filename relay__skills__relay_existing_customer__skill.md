---
name: relay-existing-customer
description: Cashfree Relay workflow for Existing Customer Re-KYC (Perpetual KYC) — CKYC lookup-first path for returning customers, change-in-circumstance re-verification, periodic re-verification by risk tier. CKYC Docker required for short path. Generates working Node.js integration code, compact Relay workflow spec. ~₹15–45 per re-verification depending on CKYC hit.
triggers:
  - /relay-existing-customer
  - existing customer KYC relay
  - re-KYC workflow
  - perpetual KYC relay
  - CKYC lookup relay
  - customer re-verification workflow
tools:
  - Read/Write
---

# Existing Customer Re-KYC (Perpetual KYC)

> CKYC lookup-first (short path for returning customers) · Change-in-circumstance triggers · Periodic re-verification by risk tier · CKYC Docker required for short path

---

## Regulatory mandate

| Obligation | Regulation | Frequency / Deadline |
|---|---|---|
| Periodic KYC updation | RBI KYC Master Directions 2023 — Section 38 | HIGH risk: 2yr · MEDIUM: 8yr · LOW: 10yr · PEP: 1yr |
| CKYC short path eligibility | PMLA Rule 9(1A) · CERSAI circular | CKYC Docker required; clean record mandatory |
| Targeted re-verification | RBI KYC MD 2023 — Section 38(iii) | Only changed attribute needs re-verification |
| CKYC upload post re-KYC | PMLA Rule 9(1A) · CERSAI upload mandate | Within 10 business days of re-KYC completion |
| Re-consent capture | DPDP Act 2023 — Section 6 | Fresh consent required for each re-KYC event |
| AML screening | PMLA Section 11A | Re-screen at each re-KYC event |
| STR filing | PMLA Section 12 · FIU-IND | Within 7 working days of suspicion |
| CTR filing | PMLA Section 12 · FIU-IND | By 15th of succeeding month for cash > ₹10L |
| PEP re-KYC — senior approval | RBI KYC MD 2023 — Section 32 | Annual re-KYC + senior management sign-off |

---

## The problem this solves

Banks and NBFCs must periodically re-verify customers under RBI's perpetual KYC framework. Without CKYC, every returning customer goes through full KYC again — the same 10-minute journey they did at onboarding. CKYC short path cuts this to under 2 minutes for eligible customers.

| Path | Trigger | Customer experience | Cost |
|---|---|---|---|
| CKYC short path | CKYC record found + clean | Mobile OTP → confirm details → done | ~₹15 |
| Targeted re-verify | Specific document changed | Re-verify only changed document | ~₹25–35 |
| Full re-KYC | No CKYC record / high risk | Full onboarding flow (PAN + Aadhaar + face + bank) | ~₹40–45 |

---

## 3 re-KYC trigger types

| Trigger | Example | Re-verify |
|---|---|---|
| Periodic scheduled | HIGH risk: 1yr, MEDIUM: 2yr, LOW: 10yr | Full or CKYC short |
| Change in circumstance | Name change, address change, new job | Changed attribute only |
| Risk upgrade | EDD escalation, new sanctions match | Full re-KYC |

---

## Prerequisite: CKYC Docker

The CKYC short path requires your CKYC on-premises Docker to be deployed and connected. Without it, all customers go through full re-KYC.

```bash
# Check if CKYC Docker is reachable
curl http://<your-ckyc-docker-host>/health
# Expected: { "status": "ok", "ckyc_sync": "connected" }
```

Set `CKYC_DOCKER_DEPLOYED=true` in your env once deployed.

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
CKYC_DOCKER_DEPLOYED=false   # set true when CKYC Docker is running
CKYC_ONPREM_URL=             # http://your-ckyc-docker-host
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "existing_customer_rekyc",
  "description": "Re-KYC — CKYC short path for existing customers, full re-KYC fallback",
  "trigger": "api",
  "inputs": ["customer_id", "mobile", "trigger_type", "changed_attribute"],
  "nodes": [
    { "id": "consent",       "type": "ui",  "template": "dpdp_consent",
      "msg": "We need to update your verification details.", "on_denied": "REJECT" },

    { "id": "ckyc-gate",     "type": "condition",
      "if": "CKYC_DOCKER_DEPLOYED == true", "then": "ckyc-lookup", "else": "full-rekyc",
      "note": "CKYC short path only available with on-prem Docker deployed" },

    { "id": "ckyc-lookup",   "type": "api", "call": "{{CKYC_ONPREM_URL}}/lookup",
      "in": { "pan": "{{pan}}", "mobile": "{{mobile}}" },
      "on_found_clean": "ckyc-short-path",
      "on_found_stale": "targeted-verify",
      "on_not_found": "full-rekyc",
      "on_found_flagged": "full-rekyc" },

    { "id": "ckyc-short-path","type": "sequence",
      "note": "Customer in CKYC — just re-confirm mobile OTP + display existing details for confirmation",
      "nodes": [
        { "id": "mob-send",    "type": "api", "call": "POST /mobile360/otp/send" },
        { "id": "mob-verify",  "type": "api", "call": "POST /mobile360/otp/verify" },
        { "id": "details-confirm","type": "ui", "template": "ckyc_details_confirmation",
          "note": "Show existing CKYC data — name, DOB, address — ask customer to confirm",
          "on_confirmed": "APPROVE", "on_changed": "targeted-verify" }
      ]},

    { "id": "targeted-verify","type": "condition",
      "switch": "changed_attribute",
      "cases": {
        "ADDRESS": "address-reverify",
        "NAME":    "name-reverify",
        "BANK":    "bav-reverify",
        "NONE":    "full-rekyc"
      }},

    { "id": "address-reverify","type": "api", "call": "POST /digilocker", "doc": "AADHAAR",
      "timeout_min": 10, "on_timeout": "address-ocr", "on_denied": "address-ocr" },
    { "id": "address-ocr",   "type": "api", "call": "POST /bharat-ocr", "doc": "AADHAAR",
      "content_type": "multipart/form-data", "on_forgery": "REJECT" },

    { "id": "name-reverify", "type": "api", "call": "POST /pan", "version": "2024-12-01",
      "note": "Name change — re-verify PAN matches new legal name",
      "on_invalid": "REJECT" },

    { "id": "bav-reverify",  "type": "api", "call": "POST /bank-account/sync",
      "on_fraud_account": "REJECT_AND_FLAG", "on_invalid": "REJECT",
      "flags": { "name_below_60": "REJECT", "name_60_to_84": "+1 AMBER" } },

    { "id": "full-rekyc",    "type": "sequence",
      "note": "Full re-KYC — same as initial onboarding. Customer completes in 5–8 min.",
      "nodes": [
        { "id": "mob-send-full",   "type": "api", "call": "POST /mobile360/otp/send" },
        { "id": "mob-verify-full", "type": "api", "call": "POST /mobile360/otp/verify",
          "prefill_outputs": ["pan", "name"] },
        { "id": "pan-full",        "type": "api", "call": "POST /pan", "version": "2024-12-01",
          "on_invalid": "REJECT" },
        { "id": "digilocker-full", "type": "api", "call": "POST /digilocker", "doc": "AADHAAR",
          "timeout_min": 10, "on_timeout": "ocr-full", "on_denied": "ocr-full" },
        { "id": "ocr-full",        "type": "api", "call": "POST /bharat-ocr", "doc": "AADHAAR",
          "content_type": "multipart/form-data", "on_forgery": "REJECT" },
        { "id": "liveness-full",   "type": "api", "call": "POST /face-liveness",
          "content_type": "multipart/form-data", "max_retries": 3, "on_exhausted": "REJECT" },
        { "id": "face-match-full", "type": "api", "call": "POST /face-match",
          "content_type": "multipart/form-data", "threshold": 0.75, "on_fail": "REJECT" },
        { "id": "bav-full",        "type": "api", "call": "POST /bank-account/sync",
          "on_fraud_account": "REJECT_AND_FLAG", "on_invalid": "REJECT" }
      ]},

    { "id": "ckyc-update",   "type": "condition",
      "if": "CKYC_DOCKER_DEPLOYED == true", "then": "ckyc-upload", "else": "APPROVE" },
    { "id": "ckyc-upload",   "type": "api", "call": "{{CKYC_ONPREM_URL}}/upload",
      "async": true, "mandate_days": 10, "then": "APPROVE" }
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

// Trigger re-KYC for an existing customer
app.post('/api/rekyc/start', async (req, res) => {
  const { customerId, mobile, triggerType = 'PERIODIC', changedAttribute = 'NONE' } = req.body;

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
        redirect_url: `${BASE_URL}/rekyc/done`,
        webhook_url:  `${BASE_URL}/api/rekyc/webhook`,
        metadata: { trigger_type: triggerType, changed_attribute: changedAttribute },
      }),
    }
  );

  const { run_id, hosted_url } = await r.json();
  res.json({ rekycUrl: hosted_url, runId: run_id });
});

app.post('/api/rekyc/webhook', (req, res) => {
  const sig = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody).digest('base64');
  if (sig !== expected) return res.status(401).send('Bad signature');

  const { customer_id, status, flags, path_taken } = req.body;
  // path_taken: 'CKYC_SHORT' | 'TARGETED' | 'FULL_REKYC'

  switch (status) {
    case 'APPROVED':
      // ✅ Re-KYC complete — update verification timestamp
      updateVerificationTimestamp(customer_id, path_taken);
      break;

    case 'REJECTED':
      // ❌ Hard reject — suspend account, notify compliance
      suspendAccount(customer_id, flags);
      break;
  }

  res.json({ received: true });
});

async function updateVerificationTimestamp(id, path) { /* update DB, schedule next re-KYC */ }
async function suspendAccount(id, flags)             { /* suspend, log to compliance */ }

app.listen(3000);
```

---

### Step 3 — Test it

```bash
# Trigger re-KYC (CKYC short path — periodic)
curl -X POST http://localhost:3000/api/rekyc/start \
  -H "Content-Type: application/json" \
  -d '{"customerId":"cust_001","mobile":"9999999999","triggerType":"PERIODIC","changedAttribute":"NONE"}'

# Trigger re-KYC (address changed)
curl -X POST http://localhost:3000/api/rekyc/start \
  -H "Content-Type: application/json" \
  -d '{"customerId":"cust_002","mobile":"9999999999","triggerType":"CHANGE_IN_CIRCUMSTANCE","changedAttribute":"ADDRESS"}'

# Simulate APPROVED via CKYC short path
curl -X POST http://localhost:3000/api/rekyc/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"cust_001","status":"APPROVED","flags":[],"path_taken":"CKYC_SHORT"}'
```

---

## RBI perpetual KYC schedule

| Risk tier | Max time since last KYC | Action on breach |
|---|---|---|
| LOW | 10 years | Soft nudge → re-verify on next login |
| MEDIUM | 8 years | Soft nudge → scheduled re-KYC |
| HIGH | 2 years | Hard gate → must complete re-KYC to transact |
| PEP | 1 year | Hard gate → senior approval required |

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
| DPDP re-consent | CKYC on-prem Docker | AML/PEP re-screening |
| CKYC lookup → short path | | |
| Targeted re-verify (address / name / bank) | | |
| Full re-KYC fallback (PAN + Aadhaar + face + BAV) | | |
| CKYC async upload (10-day mandate) | | |

**Regulation:** RBI KYC Master Directions 2023 — Section 38 (periodic updation) · Section 32 (PEP annual review) · PMLA Sections 11A, 12 · PMLA Rule 9(1A) (CKYCR upload) · PML Rules 2005 · DPDP Act 2023 — Section 6

**Cost:** CKYC short path ~₹15 · Targeted re-verify ~₹25–35 · Full re-KYC ~₹40–45

---

## MCP — coming soon

```
/relay-existing-customer

→ Claude: "CKYC Docker deployed? Trigger type? Risk tier schedule?"
→ Calls Relay MCP → creates re-KYC workflow with CKYC lookup
→ Returns RELAY_WORKFLOW_ID
```
