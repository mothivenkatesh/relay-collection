---
name: relay-nri-wealthtech
description: Cashfree KYC workflow for NRI Investor Account Onboarding — SEBI/FEMA-compliant. NRE/NRO/FCNR/Demat account type routing, passport + overseas address proof, FATCA/CRS self-declaration, PIS permission check, VKYC mandatory (no bypass), Aadhaar eSign. Face match threshold 0.80. Generates working Node.js integration code, compact Relay workflow spec. ~₹80–120 per onboarding.
triggers:
  - /relay-nri-wealthtech
  - NRI investor onboarding
  - NRI demat account relay
  - NRI KYC workflow
  - non-resident investor onboarding
  - FEMA KYC relay
  - NRE NRO account KYC
tools:
  - Read/Write
---

# NRI Investor Onboarding — SEBI/FEMA Compliant

> Passport + Overseas Address + FATCA/CRS + PIS + VKYC (mandatory) + eSign · NRE / NRO / FCNR / Demat routing · No Aadhaar bypass available for NRIs · ~₹80–120 per onboarding

---

## Regulatory mandate

| Obligation | Regulation | Threshold / Deadline |
|---|---|---|
| NRI KYC for securities | SEBI KYC Master Circular 2023 · FEMA 1999 — Section 6 | All NRI demat and trading accounts |
| VKYC — mandatory for NRIs | SEBI Circular SEBI/HO/MIRSD/FATF/P/CIR/2022/158 | No bypass available — mandatory for all NRI accounts |
| PIS permission | RBI circular on Portfolio Investment Scheme — FEMA 20(R) | Required for NRE accounts participating in equity market |
| FATCA / CRS declaration | India-US IGA (signed 2015) · CRS enacted via Income Tax Act Section 285BA | Mandatory for all NRI account openings |
| Overseas address proof | SEBI KYC MC 2023 — NRI-specific clause | Document must be < 3 months old (utility bill / bank statement) |
| Face match threshold | SEBI V-CIP Circular 2022 — NRI provisions | 0.80 minimum (stricter than resident 0.75) |
| PMLA — NRI customer risk | PMLA 2002 · FIU-IND NRI risk classification | NRIs from FATF grey-list countries require enhanced monitoring |
| STR filing | PMLA Section 12 · FIU-IND | Within 7 working days of suspicion |
| CTR filing | PMLA Section 12 · FIU-IND | By 15th of succeeding month for > ₹10L |
| Signed document retention | SEBI regulations | 5 years |

---

## Key differences from resident investor (relay-wealthtech-broker)

| | Resident Investor | NRI Investor |
|---|---|---|
| Primary ID | Aadhaar (DigiLocker preferred) | Passport (mandatory) |
| VKYC | Risk-gated (medium risk only) | Mandatory — no bypass |
| Face threshold | 0.75 | 0.80 (stricter for remote intl.) |
| Address proof | Aadhaar address sufficient | Overseas address proof required |
| FATCA/CRS | Not required | Mandatory self-declaration |
| PIS permission | Not applicable | Required for NRE equity trading |
| Account types | Demat + trading | NRE / NRO / FCNR / Demat |
| VKYC scheduling | Standard hours | Timezone-aware (IST + customer TZ) |

---

## What your customer experiences

1. Selects account type (NRE / NRO / FCNR / Demat only)
2. Mobile OTP → passport uploaded (front + visa page)
3. Overseas address proof uploaded (utility bill / bank statement)
4. FATCA/CRS self-declaration form (country of residence, TIN)
5. PIS permission verified (NRE trading accounts only — external bank API)
6. Selfie for face match against passport photo
7. Mandatory VKYC — scheduled in customer's timezone
8. Aadhaar eSign on account opening documents
9. Account activated post-VKYC

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
PIS_API_URL=              # your bank's PIS permission check endpoint
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "nri_wealthtech_kyc",
  "description": "NRI investor onboarding — passport + overseas address + FATCA/CRS + PIS + mandatory VKYC",
  "trigger": "api",
  "inputs": ["customer_id", "mobile", "account_type", "country_of_residence", "timezone"],
  "nodes": [
    { "id": "consent",        "type": "ui",  "template": "dpdp_consent", "on_denied": "REJECT" },
    { "id": "account-route",  "type": "condition",
      "if": "account_type in ['NRE','NRO','FCNR','DEMAT']", "then": "mob-send", "else": "REJECT",
      "note": "Only valid NRI account types proceed" },
    { "id": "mob-send",       "type": "api", "call": "POST /mobile360/otp/send" },
    { "id": "mob-verify",     "type": "api", "call": "POST /mobile360/otp/verify",
      "prefill_outputs": ["name"] },

    { "id": "passport-ocr",   "type": "api", "call": "POST /bharat-ocr", "doc": "PASSPORT",
      "content_type": "multipart/form-data",
      "on_forgery": "REJECT", "on_expired_doc": "REJECT",
      "outputs": ["passport_number", "name", "dob", "nationality", "expiry_date", "passport_photo_url"] },
    { "id": "passport-verify","type": "api", "call": "POST /passport",
      "in": { "id_number": "{{passport_number}}", "dob": "{{dob}}", "name": "{{name}}" },
      "on_invalid": "REJECT", "on_not_found": "+1 AMBER" },

    { "id": "address-proof",  "type": "api", "call": "POST /bharat-ocr", "doc": "OVERSEAS_ADDRESS",
      "content_type": "multipart/form-data",
      "accepted_docs": ["utility_bill", "bank_statement", "govt_id_with_address"],
      "on_forgery": "REJECT", "on_expired": "REJECT",
      "note": "Document must be < 3 months old for utility bill / bank statement" },

    { "id": "fatca-crs",      "type": "ui",  "template": "fatca_crs_declaration",
      "in": { "country_of_residence": "{{country_of_residence}}" },
      "on_declined": "REJECT",
      "note": "Captures TIN, country of tax residency — SEBI mandate for NRIs" },

    { "id": "pis-check",      "type": "condition",
      "if": "account_type == 'NRE'", "then": "pis-verify", "else": "liveness" },
    { "id": "pis-verify",     "type": "api", "call": "{{PIS_API_URL}}/check",
      "in": { "pan": "{{pan}}", "account_type": "NRE" },
      "on_not_approved": "+1 AMBER", "on_rejected": "REJECT",
      "note": "PIS = Portfolio Investment Scheme — required for NRE equity trading" },

    { "id": "liveness",       "type": "api", "call": "POST /face-liveness",
      "content_type": "multipart/form-data",
      "retry_flow": [
        { "attempt": 1, "on_fail": "selfie-guide-2" },
        { "attempt": 2, "on_fail": "selfie-guide-3" },
        { "attempt": 3, "on_fail": "vkyc-nri" }
      ]},
    { "id": "selfie-guide-2", "type": "ui", "msg": "Couldn't verify. Better lighting + plain background.", "then": "liveness" },
    { "id": "selfie-guide-3", "type": "ui", "msg": "Last attempt before video KYC.", "then": "liveness" },
    { "id": "face-match",     "type": "api", "call": "POST /face-match",
      "content_type": "multipart/form-data",
      "compare": "selfie vs passport_photo_url",
      "threshold": 0.80,
      "on_fail": "vkyc-nri", "flag_if_below_85": "+1 AMBER" },
    { "id": "name-match",     "type": "api", "call": "POST /name-match",
      "in": { "name1": "{{mob_name}}", "name2": "{{passport_name}}" },
      "token_sort_retry_below": 0.70 },

    { "id": "esign-docs",     "type": "api", "call": "POST /esignature",
      "documents": ["Account Opening Form (AOF)", "FATCA/CRS Declaration", "Risk Disclosure"],
      "on_declined": "REJECT", "on_expired": "resend-esign-once" },

    { "id": "vkyc-nri",       "type": "api", "call": "POST /vkyc",
      "meta": {
        "regulator": "SEBI",
        "geolocation_required": true,
        "preferred_language": "{{input.lang | default: 'en'}}",
        "timezone": "{{timezone}}",
        "note": "VKYC is mandatory for NRIs — no bypass path exists"
      },
      "nudge_at": "-4h",
      "states": {
        "APPROVE": "APPROVE",
        "REJECT": "REJECT",
        "UNABLE_TO_VALIDATE": "vkyc-reschedule",
        "FAILED": "MANUAL_ESCALATION"
      }
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
  const { customerId, mobile, accountType, countryOfResidence, timezone, preferredLanguage = 'en' } = req.body;

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
        metadata: {
          account_type:         accountType,
          country_of_residence: countryOfResidence,
          timezone,
          preferred_language:   preferredLanguage,
        },
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
      // ✅ VKYC passed — activate NRI account
      activateNRIAccount(customer_id);
      if (signed_document_url) storeDocuments(customer_id, signed_document_url);
      break;

    case 'VKYC_REQUIRED':
      // 📹 Relay sending VKYC link (scheduled in customer timezone)
      updateStatus(customer_id, 'VKYC_PENDING');
      break;

    case 'VKYC_APPROVED':
      activateNRIAccount(customer_id);
      if (signed_document_url) storeDocuments(customer_id, signed_document_url);
      break;

    case 'REJECTED':
      markRejected(customer_id, flags);
      break;

    case 'MANUAL_ESCALATION':
      // VKYC recording failed — do NOT auto-reject NRI customers
      queueOpsReview(customer_id, 'vkyc_recording_failed');
      break;
  }

  res.json({ received: true });
});

async function activateNRIAccount(id)    { /* activate NRE/NRO/FCNR/Demat */ }
async function storeDocuments(id, url)   { /* store signed docs — 5yr retention (SEBI) */ }
async function updateStatus(id, status)  { /* update DB */ }
async function markRejected(id, flags)   { /* update DB, notify customer */ }
async function queueOpsReview(id, note)  { /* ops queue */ }

app.listen(3000);
```

---

### Step 3 — Frontend (React)

```jsx
// NRIKYCForm.jsx
import { useState } from 'react';

export function NRIKYCForm({ customerId, mobile }) {
  const [accountType, setAccountType]   = useState('NRE');
  const [country, setCountry]           = useState('');
  const [timezone, setTimezone]         = useState(
    Intl.DateTimeFormat().resolvedOptions().timeZone
  );
  const [phase, setPhase]               = useState('form');

  const start = async () => {
    setPhase('loading');
    const res = await fetch('/api/kyc/start', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify({ customerId, mobile, accountType, countryOfResidence: country, timezone }),
    });
    const { kycUrl } = await res.json();
    setPhase('redirecting');
    window.location.href = kycUrl;
  };

  if (phase === 'form') return (
    <div>
      <select value={accountType} onChange={e => setAccountType(e.target.value)}>
        <option value="NRE">NRE (repatriable)</option>
        <option value="NRO">NRO (non-repatriable)</option>
        <option value="FCNR">FCNR (foreign currency)</option>
        <option value="DEMAT">Demat only</option>
      </select>
      <input placeholder="Country of residence" value={country} onChange={e => setCountry(e.target.value)} />
      <button onClick={start}>Open NRI account</button>
    </div>
  );
  if (phase === 'loading')     return <p>Setting up your KYC…</p>;
  if (phase === 'redirecting') return <p>Redirecting to secure verification…</p>;
}
```

---

### Step 4 — Test it

```bash
# Start NRI onboarding (NRE account, Singapore)
curl -X POST http://localhost:3000/api/kyc/start \
  -H "Content-Type: application/json" \
  -d '{"customerId":"nri_001","mobile":"9999999999","accountType":"NRE","countryOfResidence":"SG","timezone":"Asia/Singapore"}'

# Simulate VKYC_APPROVED (mandatory path for all NRIs)
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"nri_001","status":"VKYC_APPROVED","flags":[],"signed_document_url":"https://secure.cashfree.com/docs/signed_xyz.pdf"}'
```

---

## VKYC timezone scheduling

| Region | Scheduling note |
|---|---|
| Gulf (UAE, Kuwait, Oman) | UTC+4 — IST evenings work; prefer 7–10 PM IST |
| US/Canada | UTC-5 to UTC-8 — IST early mornings; prefer 7–9 AM IST |
| Singapore/Malaysia | UTC+8 — IST afternoons work; prefer 2–5 PM IST |
| UK/Europe | UTC+0 to UTC+2 — IST evenings; prefer 6–9 PM IST |

Relay schedules VKYC slots in customer timezone automatically when `timezone` metadata is passed.

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
| **Re-KYC — NRI** | Relay supports re-trigger | FATF high-risk country NRIs: annual review · Others: 2yr (HIGH) / 8yr (MEDIUM) |
| **DPDP rights** | Consent event stored per DPDP Act 2023 — Section 6 | Data Principal rights (access / correction / erasure) are your obligation |
| **Board policy** | Workflow enforces your configured KYC policy | Board-approved KYC/AML policy + Designated Director required before FIU-IND registration |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| DPDP consent | PIS permission API (your bank) | CKYC upload (NRI CKYC mandate varies) |
| Mobile OTP | Overseas address template verification | AML/PEP screening |
| Passport OCR + verification | | |
| Overseas address proof OCR | | |
| FATCA/CRS UI + declaration | | |
| PIS permission check gate | | |
| Face liveness + match (0.80 threshold) | | |
| Mandatory SEBI VKYC + timezone scheduling | | |
| Aadhaar eSign (AOF + FATCA/CRS + Risk Disclosure) | | |
| VKYC MANUAL_ESCALATION — do NOT auto-reject | | |

**Regulation:** SEBI KYC Master Circular 2023 (SEBI/HO/MIRSD/2023) · FEMA 1999 — Section 6 · FEMA 20(R) (PIS) · SEBI V-CIP Circular 2022 · FATCA/CRS — India-US IGA 2015 · Income Tax Act Section 285BA (CRS) · PMLA Sections 11A, 12 · PML Rules 2005 · DPDP Act 2023 — Section 6

**Cost:** Passport + address OCR + VKYC mandatory: ~₹80–120 per onboarding

---

## MCP — coming soon

```
/relay-nri-wealthtech

→ Claude: "Account type? Country? PIS API available?"
→ Calls Relay MCP → creates + publishes workflow with timezone config
→ Returns RELAY_WORKFLOW_ID
```
