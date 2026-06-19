---
name: relay-gift-city
description: Cashfree KYC workflow for GIFT City (IFSCA) onboarding — 3-layer VKYC mandatory, GPS geo-tagging during VKYC, IFSCA jurisdiction validation, debit freeze state machine (auto-freeze until VKYC + POA complete), FATF-compliant foreign national path. Face match threshold 0.80. Generates working Node.js integration code, compact Relay workflow spec. ~₹100–140 per onboarding.
triggers:
  - /relay-gift-city
  - GIFT City KYC relay
  - IFSCA onboarding workflow
  - IFSC jurisdiction KYC
  - Gujarat IFSC account opening
  - foreign national IFSC KYC
tools:
  - Read/Write
---

# GIFT City (IFSCA) Onboarding

> 3-layer mandatory VKYC · GPS geo-tagging · IFSCA jurisdiction validation · Debit freeze until completion · FATF foreign national path · ~₹100–140 per onboarding

---

## Regulatory mandate

| Obligation | Regulation | Threshold / Condition |
|---|---|---|
| IFSCA KYC baseline | IFSCA (Banking) Regulations 2020 — Regulation 9 | All GIFT City account openings |
| 3-layer mandatory VKYC | IFSCA V-CIP guidelines | No bypass — all accounts regardless of risk |
| GPS geo-tagging | IFSCA V-CIP guidelines — Clause 7 | Customer device location captured during VKYC session |
| Debit freeze until VKYC | IFSCA (Banking) Regulations 2020 — Regulation 9(4) | Account opened but debit-frozen until VKYC + POA confirmed |
| FATF country check | FATF Recommendations 10–12 · IFSCA AML guidelines | Mandatory for all foreign nationals |
| Senior management approval | IFSCA AML guidelines — FATF-high-risk nationals | Board-level signatory for accounts from FATF grey/black-list countries |
| AML / sanctions screening | PMLA 2002 · UN Security Council Resolutions | All customers |
| STR filing | PMLA Section 12 · FIU-IND | Within 7 working days of suspicion |
| CTR filing | PMLA Section 12 · FIU-IND | By 15th of succeeding month for > ₹10L |
| Record retention | IFSCA regulations + PMLA Section 12 | 5 years from account closure |

---

## GIFT City requires more than standard SEBI KYC

IFSCA operates under its own regulatory framework. Key requirements beyond standard SEBI onboarding:

| Requirement | SEBI (standard) | IFSCA (GIFT City) |
|---|---|---|
| VKYC | Risk-gated | Mandatory for all accounts |
| VKYC layers | 1 | 3 (liveness + agent + document review) |
| GPS geo-tagging | Not required | Required during VKYC |
| Debit freeze | Not applicable | Auto-imposed until VKYC + POA complete |
| Foreign nationals | Rare edge case | Explicit FATF path required |
| Face threshold | 0.75 | 0.80 |
| Jurisdiction proof | Not required | GIFT City address / entity proof required |

---

## What your customer experiences

**Indian resident:**
1. Consent + mobile OTP → PAN confirm → Aadhaar (DigiLocker / OCR)
2. Selfie liveness check
3. 3-layer VKYC with GPS geo-tagging (agent verifies location is permissible)
4. POA (Proof of Address for GIFT City entity) uploaded
5. Account opened — debit freeze lifted after VKYC + POA confirmed

**Foreign national (FATF path):**
1. Passport OCR + country of origin validation
2. FATF-category check (high-risk countries → MANUAL_REVIEW)
3. Overseas address proof
4. Mandatory 3-layer VKYC with GPS
5. Senior management approval gate for high-risk nationalities

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
IFSCA_JURISDICTION_API_URL=   # IFSCA/GIFT City address validation endpoint
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "gift_city_ifsca_kyc",
  "description": "IFSCA GIFT City onboarding — 3-layer VKYC mandatory, GPS geo-tagging, debit freeze state machine",
  "trigger": "api",
  "inputs": ["customer_id", "mobile", "nationality", "account_entity_type"],
  "nodes": [
    { "id": "consent",         "type": "ui",  "template": "dpdp_consent", "on_denied": "REJECT" },
    { "id": "nationality-gate","type": "condition",
      "if": "nationality == 'IN'", "then": "mob-send", "else": "foreign-national-path" },

    { "id": "mob-send",        "type": "api", "call": "POST /mobile360/otp/send" },
    { "id": "mob-verify",      "type": "api", "call": "POST /mobile360/otp/verify",
      "prefill_outputs": ["pan", "name"] },
    { "id": "pan",             "type": "api", "call": "POST /pan", "version": "2024-12-01",
      "on_invalid": "REJECT" },
    { "id": "digilocker",      "type": "api", "call": "POST /digilocker", "doc": "AADHAAR",
      "timeout_min": 10, "on_timeout": "digilocker-retry", "on_denied": "ocr" },
    { "id": "digilocker-retry","type": "api", "call": "POST /digilocker", "doc": "AADHAAR",
      "on_timeout": "ocr" },
    { "id": "ocr",             "type": "api", "call": "POST /bharat-ocr", "doc": "AADHAAR",
      "content_type": "multipart/form-data", "on_forgery": "REJECT", "flag_on_fallback": "+1 AMBER" },
    { "id": "liveness",        "type": "api", "call": "POST /face-liveness",
      "content_type": "multipart/form-data",
      "max_retries": 3, "guidance_ui": true, "on_exhausted": "vkyc-ifsca" },
    { "id": "face-match",      "type": "api", "call": "POST /face-match",
      "content_type": "multipart/form-data",
      "threshold": 0.80, "on_fail": "vkyc-ifsca", "flag_if_below_85": "+1 AMBER" },

    { "id": "foreign-national-path", "type": "sequence", "nodes": [
        { "id": "fatf-check",  "type": "api", "call": "{{INTERNAL_AML_URL}}/fatf-category",
          "in": { "nationality": "{{nationality}}" },
          "on_high_risk": "MANUAL_REVIEW", "on_sanctions": "REJECT" },
        { "id": "passport-ocr","type": "api", "call": "POST /bharat-ocr", "doc": "PASSPORT",
          "content_type": "multipart/form-data", "on_forgery": "REJECT" },
        { "id": "passport-verify","type": "api", "call": "POST /passport",
          "on_invalid": "REJECT" }
    ]},

    { "id": "gift-city-address","type": "api", "call": "POST /bharat-ocr", "doc": "GIFT_CITY_POA",
      "content_type": "multipart/form-data",
      "note": "GIFT City entity address proof — office / registered address in IFSC zone",
      "on_forgery": "REJECT" },

    { "id": "jurisdiction-validate","type": "api", "call": "{{IFSCA_JURISDICTION_API_URL}}/validate",
      "in": { "address": "{{gift_city_address}}", "entity_type": "{{account_entity_type}}" },
      "on_invalid_jurisdiction": "REJECT" },

    { "id": "debit-freeze",    "type": "api", "call": "POST /account/freeze",
      "in": { "customer_id": "{{customer_id}}", "freeze_type": "DEBIT" },
      "note": "Debit freeze imposed immediately — lifted only after VKYC + POA confirmed" },

    { "id": "vkyc-ifsca",      "type": "api", "call": "POST /vkyc",
      "meta": {
        "regulator": "IFSCA",
        "geolocation_required": true,
        "vkyc_layers": 3,
        "preferred_language": "{{input.lang | default: 'en'}}",
        "note": "3-layer VKYC: liveness check + live agent + document review by IFSCA-trained agent"
      },
      "nudge_at": "-4h",
      "states": {
        "APPROVE": "lift-freeze",
        "REJECT": "REJECT",
        "UNABLE_TO_VALIDATE": "vkyc-reschedule",
        "FAILED": "MANUAL_ESCALATION"
      }
    },
    { "id": "lift-freeze",     "type": "api", "call": "POST /account/unfreeze",
      "in": { "customer_id": "{{customer_id}}", "freeze_type": "DEBIT" },
      "then": "APPROVE" }
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
  const { customerId, mobile, nationality = 'IN', accountEntityType, preferredLanguage = 'en' } = req.body;

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
        metadata: { nationality, account_entity_type: accountEntityType, preferred_language: preferredLanguage },
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

  const { customer_id, status, flags, geolocation } = req.body;

  switch (status) {
    case 'APPROVED':
      // ✅ 3-layer VKYC passed + debit freeze lifted by Relay
      // geolocation is provided by Cashfree VKYC agent
      activateGIFTCityAccount(customer_id, geolocation);
      break;

    case 'VKYC_REQUIRED':
      // 📹 Relay sending VKYC link with GPS capture
      updateStatus(customer_id, 'VKYC_PENDING_GPS');
      break;

    case 'REJECTED':
      // ❌ Jurisdiction invalid, FATF high-risk, forgery, or VKYC reject
      markRejected(customer_id, flags);
      break;

    case 'MANUAL_REVIEW':
      // Foreign national with high-risk nationality — senior management approval required
      queueSeniorApproval(customer_id, flags);
      break;

    case 'MANUAL_ESCALATION':
      // VKYC recording failed — do NOT auto-reject
      queueOpsReview(customer_id, 'vkyc_recording_failed');
      break;
  }

  res.json({ received: true });
});

async function activateGIFTCityAccount(id, geo) { /* activate, log geo for IFSCA audit */ }
async function updateStatus(id, status)          { /* update DB */ }
async function markRejected(id, flags)           { /* update DB, notify */ }
async function queueSeniorApproval(id, flags)    { /* senior management queue */ }
async function queueOpsReview(id, note)          { /* ops queue */ }

app.listen(3000);
```

---

### Step 3 — Test it

```bash
# Indian resident onboarding
curl -X POST http://localhost:3000/api/kyc/start \
  -H "Content-Type: application/json" \
  -d '{"customerId":"gc_001","mobile":"9999999999","nationality":"IN","accountEntityType":"IFSC_BRANCH"}'

# Foreign national (Singapore) — FATF compliant
curl -X POST http://localhost:3000/api/kyc/start \
  -H "Content-Type: application/json" \
  -d '{"customerId":"gc_002","mobile":"9999999999","nationality":"SG","accountEntityType":"FOREIGN_ENTITY"}'

# Simulate APPROVED with geo
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"gc_001","status":"APPROVED","flags":[],"geolocation":{"lat":23.15,"lon":72.68}}'
```

---

## Debit freeze state machine

| State | Trigger | Next state |
|---|---|---|
| FREEZE_IMPOSED | Workflow started | — |
| VKYC_PENDING | After KYC docs verified | — |
| FREEZE_REVIEW | 3-layer VKYC completed | — |
| FREEZE_LIFTED | IFSCA VKYC APPROVE + POA confirmed | ACCOUNT_ACTIVE |
| FREEZE_PERMANENT | VKYC REJECT | ACCOUNT_CLOSED |

---

## Enterprise governance

| Control | Cashfree platform | Your responsibility |
|---|---|---|
| **Data residency** | India-only · AWS ap-south-1 (Mumbai) · No cross-border transfer | Receiving systems must be India-hosted or covered by a DPA |
| **Encryption** | TLS 1.3 in transit · AES-256 at rest · Session hash chain | Maintain equivalent standards in your storage layer |
| **Audit trail** | Immutable session logs retained 7 years | PMLA: 5 years minimum from relationship end — your DB must also retain |
| **IFSCA audit trail** | GPS + VKYC session data retained 7 years | Submit IFSCA periodic compliance reports — your compliance team's obligation |
| **FIU-IND — STR** | `flags[]` in webhook surfaces suspicion triggers | File STR within 7 working days of suspicion on goAML portal |
| **FIU-IND — CTR** | Transaction metadata delivered via webhook | File CTR by 15th of succeeding month for cash transactions > ₹10L |
| **Re-KYC schedule** | Relay supports re-trigger — use relay-existing-customer | HIGH risk: 2 yr · MEDIUM: 8 yr · LOW: 10 yr · PEP: 1 yr |
| **DPDP rights** | Consent event stored per DPDP Act 2023 — Section 6 | Data Principal rights (access / correction / erasure) are your obligation |
| **Board policy** | Workflow enforces your configured KYC policy | Board-approved KYC/AML policy + Designated Director required before FIU-IND registration |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| DPDP consent | IFSCA jurisdiction validation API | Ongoing IFSCA reporting |
| Mobile OTP | AML/PEP endpoint (for FATF check) | |
| PAN + Aadhaar (Indian residents) | Account freeze/unfreeze API | |
| Passport + FATF check (foreign nationals) | | |
| GIFT City POA address proof | | |
| Face liveness + match (0.80 threshold) | | |
| 3-layer IFSCA VKYC with GPS geo-tagging | | |
| Debit freeze → auto-lift on APPROVE | | |
| Senior management approval gate (FATF high-risk) | | |

**Regulation:** IFSCA (Banking) Regulations 2020 — Regulation 9 · IFSCA V-CIP Guidelines (Clause 7 — GPS) · FATF Recommendations 10–12 · PMLA Sections 11A, 12 · PML Rules 2005 · UN Security Council Resolutions (sanctions) · DPDP Act 2023 — Section 6

**Note:** GPS geo-tagging and 3-layer VKYC support via Cashfree VKYC — confirm availability with Cashfree account team before deploying.

**Cost:** ~₹100–140 per onboarding (3-layer VKYC + document verification)

---

## MCP — coming soon

```
/relay-gift-city

→ Claude: "Indian resident or foreign national? Entity type?"
→ Calls Relay MCP → creates workflow with IFSCA config
→ Returns RELAY_WORKFLOW_ID
```
