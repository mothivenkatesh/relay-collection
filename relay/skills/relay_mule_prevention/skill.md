---
name: relay-mule-prevention
description: Cashfree KYC workflow for Mule Account Prevention — detect money mule accounts at onboarding using device velocity, geographic mismatch, Mobile360 risk signals, BAV name match, and mule score. Account freeze with dispute path. Generates working Node.js integration code, compact Relay workflow spec. External systems needed for cross-bank pattern detection. ~₹30–45 per check.
triggers:
  - /relay-mule-prevention
  - mule account detection relay
  - mule prevention workflow
  - fraud detection onboarding
  - money mule KYC checks
  - account fraud relay
tools:
  - Read/Write
---

# Mule Account Prevention

> Device velocity + geographic mismatch + Mobile360 risk + BAV + mule score gate · Catches synthetic identities at onboarding · Account freeze with dispute path · ~₹30–45 per check

---

## Regulatory mandate

| Obligation | Regulation | Threshold / Condition |
|---|---|---|
| Mule account detection | RBI Cyber Security Framework 2016 — Section 7 · RBI circular on mule accounts (2024) | All new account openings — mandatory fraud screening |
| Device velocity check | RBI Cyber Security Framework 2016 | Flag if > 5 accounts opened from same device in 30 days |
| Geographic mismatch | RBI Cyber Security Framework 2016 | Flag if device location vs declared address > 500 km |
| Bank account fraud flag | PMLA Section 11A · RBI circular on fraud accounts | Hard reject — no override on fraud_account flag |
| Account freeze | RBI Cyber Security Framework 2016 — Incident Response | Immediate freeze on mule score > 70 |
| VKYC dispute path | RBI KYC MD 2023 — Section 18A | Frozen account holder can challenge via VKYC |
| STR filing | PMLA Section 12 · FIU-IND | Within 7 working days — mule suspected accounts are automatic suspicion events |
| CTR filing | PMLA Section 12 · FIU-IND | By 15th of succeeding month for cash > ₹10L |
| Cyber incident reporting | RBI Cyber Security Framework — Section 11 | Report detected fraud accounts as cyber events to CERT-In |
| Record retention | PMLA Section 12 | 5 years — include all fraud signals and freeze/unfreeze actions |

---

## What Relay can check vs what needs external systems

| Signal | Relay (built-in) | Needs external system |
|---|---|---|
| Device velocity (>5 accounts/device/30d) | ✅ Mobile360 device signals | |
| Geographic mismatch (>500km device/address) | ✅ Mobile360 geo signals | |
| Mobile risk band (LOW / MEDIUM / HIGH) | ✅ Mobile360 | |
| BAV name match score | ✅ BAV sync | |
| Aadhaar linkage status | ✅ PAN 360 seeding check | |
| Cross-bank mule pattern | ❌ | Your risk/network graph system |
| Mule score model | ❌ | Your fraud ML or partner (e.g. CIBIL FI) |
| Cross-merchant device rings | ❌ | Industry fraud consortium |

Use Relay for the signals it has. Pass those signals to your external mule score model for the final decision.

---

## What your risk team experiences

1. New account application arrives
2. Relay checks device velocity, geo mismatch, mobile risk, BAV name match
3. Signals forwarded to your mule score model (webhook POST to your ML endpoint)
4. Mule score returned → APPROVE / FLAG / FREEZE
5. Frozen accounts enter dispute path — customer can challenge via VKYC

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
MULE_SCORE_API_URL=    # your fraud ML endpoint or CIBIL FI / Bureau endpoint
DEVICE_VELOCITY_LIMIT=5   # max accounts per device per 30 days
GEO_MISMATCH_KM=500       # flag if device location vs address > this distance
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "mule_prevention_kyc",
  "description": "Mule detection at onboarding — device velocity + geo + BAV + external mule score",
  "trigger": "api",
  "inputs": ["customer_id", "mobile"],
  "nodes": [
    { "id": "consent",        "type": "ui",  "template": "dpdp_consent", "on_denied": "REJECT" },
    { "id": "mob-send",       "type": "api", "call": "POST /mobile360/otp/send" },
    { "id": "mob-verify",     "type": "api", "call": "POST /mobile360/otp/verify",
      "prefill_outputs": ["pan", "name"],
      "risk_signals": {
        "device_velocity_above": "{{DEVICE_VELOCITY_LIMIT}}",
        "geo_mismatch_above_km": "{{GEO_MISMATCH_KM}}",
        "risk_band_HIGH": "+2 AMBER",
        "risk_band_MEDIUM": "+1 AMBER",
        "device_velocity_flag": "+1 AMBER",
        "geo_mismatch_flag": "+1 AMBER"
      }
    },
    { "id": "pan",            "type": "api", "call": "POST /pan", "version": "2024-12-01",
      "on_invalid": "REJECT",
      "flags": { "aadhaar_seeding_not_Y": "+1 AMBER", "recently_issued": "+1 AMBER" } },
    { "id": "digilocker",     "type": "api", "call": "POST /digilocker", "doc": "AADHAAR",
      "timeout_min": 10, "on_timeout": "digilocker-retry", "on_denied": "ocr" },
    { "id": "digilocker-retry","type": "api","call": "POST /digilocker", "doc": "AADHAAR",
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
      "on_fraud_account": "REJECT_AND_FLAG",
      "on_invalid": "REJECT",
      "flags": {
        "name_below_60": "REJECT",
        "name_60_to_84": "+1 AMBER",
        "account_age_under_30_days": "+1 AMBER"
      }
    },
    { "id": "mule-score-gate","type": "gate", "rules": [
        { "if": "amber_flags == 0", "out": "APPROVE" },
        { "if": "amber_flags <= 2", "out": "mule-score-check" },
        { "if": "amber_flags >= 3", "out": "FREEZE" }
    ]},
    { "id": "mule-score-check","type": "api", "call": "{{MULE_SCORE_API_URL}}/score",
      "in": {
        "customer_id": "{{customer_id}}",
        "amber_flags": "{{amber_flags}}",
        "device_id": "{{mob_device_id}}",
        "mobile_risk_band": "{{mob_risk_band}}",
        "geo_delta_km": "{{mob_geo_delta_km}}",
        "pan": "{{pan}}",
        "bank_account": "{{bav_account_number}}"
      },
      "on_score_below_30": "APPROVE",
      "on_score_30_to_70": "MANUAL_REVIEW",
      "on_score_above_70": "FREEZE"
    },
    { "id": "FREEZE",         "type": "api", "call": "POST /account/freeze",
      "in": { "customer_id": "{{customer_id}}", "freeze_type": "FULL" },
      "then": "freeze-dispute-path" },
    { "id": "freeze-dispute-path", "type": "ui",
      "msg": "Account temporarily frozen for security review. Request a review to proceed.",
      "options": ["Request VKYC review"],
      "on_vkyc_requested": "vkyc-dispute" },
    { "id": "vkyc-dispute",   "type": "api", "call": "POST /vkyc",
      "meta": { "reason": "mule_dispute", "preferred_language": "{{input.lang | default: 'hi'}}" },
      "states": {
        "APPROVE": "unfreeze-approve",
        "REJECT": "REJECT",
        "UNABLE_TO_VALIDATE": "vkyc-reschedule",
        "FAILED": "MANUAL_ESCALATION"
      }
    },
    { "id": "unfreeze-approve","type": "api", "call": "POST /account/unfreeze",
      "in": { "customer_id": "{{customer_id}}", "freeze_type": "FULL" },
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

  const { customer_id, status, flags, risk_signals } = req.body;

  switch (status) {
    case 'APPROVED':
      // ✅ Clean profile — mule score below threshold
      activateAccount(customer_id);
      break;

    case 'REJECTED':
      // ❌ Hard signals: forgery, fraud_account, face mismatch, or VKYC rejected dispute
      markRejected(customer_id, flags);
      break;

    case 'MANUAL_REVIEW':
      // ⚠️ Mule score 30–70 — your fraud team reviews
      // risk_signals contains device_id, geo_delta, mobile_risk_band
      queueFraudReview(customer_id, flags, risk_signals);
      break;

    case 'ACCOUNT_FROZEN':
      // 🔒 Score > 70 — account frozen, customer in dispute path
      updateStatus(customer_id, 'FROZEN_MULE_SUSPECTED');
      break;

    case 'MANUAL_ESCALATION':
      // VKYC dispute recording failed
      queueOpsReview(customer_id, 'vkyc_dispute_failed');
      break;
  }

  res.json({ received: true });
});

async function activateAccount(id)              { /* activate */ }
async function markRejected(id, flags)          { /* update DB, notify */ }
async function queueFraudReview(id, flags, sigs){ /* add to fraud team queue with signals */ }
async function updateStatus(id, status)         { /* update DB */ }
async function queueOpsReview(id, note)         { /* ops queue */ }

app.listen(3000);
```

---

### Step 3 — Test it

```bash
# Clean profile (no flags)
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"test_001","status":"APPROVED","flags":[]}'

# Medium risk — mule score check triggered
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"test_002","status":"MANUAL_REVIEW","flags":["device_velocity","bav_name_moderate"],"risk_signals":{"device_id":"dev_xyz","geo_delta_km":520,"mobile_risk_band":"MEDIUM"}}'

# High risk — account frozen
curl -X POST http://localhost:3000/api/kyc/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"customer_id":"test_003","status":"ACCOUNT_FROZEN","flags":["device_velocity","geo_mismatch","mobile_risk_HIGH","bav_name_moderate"]}'
```

---

## Mule signal quick reference

| Signal | Relay source | Hard reject | Flag |
|---|---|---|---|
| Mobile risk HIGH | Mobile360 | No | +2 AMBER |
| Device velocity >5/30d | Mobile360 | No | +1 AMBER |
| Geo mismatch >500km | Mobile360 | No | +1 AMBER |
| PAN Aadhaar seeding N | PAN 360 | No | +1 AMBER |
| PAN recently issued | PAN 360 | No | +1 AMBER |
| BAV name match <60 | BAV | Yes | — |
| Bank account age <30d | BAV | No | +1 AMBER |
| Aadhaar OCR fallback | OCR | No | +1 AMBER |
| Face match <0.75 | Face match | Yes | — |
| Fraud account flag | BAV | Yes | — |

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
| **Cyber incident reporting** | Fraud account flags delivered in webhook | Report to CERT-In as cyber event within 6 hours of confirmed mule account |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| DPDP consent | Mule score API (your ML or bureau) | Cross-bank network graph |
| Mobile360 device + geo signals | Account freeze/unfreeze API | Industry consortium data |
| PAN 360 seeding + recency | | |
| Aadhaar (DigiLocker → OCR fallback) | | |
| Face liveness + match | | |
| BAV sync + account age flag | | |
| Amber flag aggregator → mule score gate | | |
| Account freeze with VKYC dispute path | | |

**Regulation:** RBI Cyber Security Framework 2016 — Sections 7, 11 · RBI Mule Account Circular 2024 · PMLA Sections 11A, 12 · PML Rules 2005 · DPDP Act 2023 — Section 6 · CERT-In cyber incident reporting guidelines

**Cost:** ~₹30–45 per check (excludes external mule score API cost)

---

## MCP — coming soon

```
/relay-mule-prevention

→ Claude: "Device velocity limit? Geo threshold? Mule score API endpoint?"
→ Calls Relay MCP → creates + publishes workflow
→ Returns RELAY_WORKFLOW_ID
```
