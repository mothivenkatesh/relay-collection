---
name: relay-pa-cb-export
description: Cashfree KYC workflow for PA-CB Export Direction — Indian exporter onboarding under FEMA, RBI PA-CB guidelines, and EDPMS mandate. PAN + GSTIN verification, entity name cross-check, ECA account check (goods exporters), EDPMS registration for outward remittance, 10% UBO with nationality, AD Bank intimation. Generates Node.js integration code and Relay workflow spec. ~₹25–40 per exporter onboarding.
triggers:
  - /relay-pa-cb-export
  - cross-border export KYC
  - Indian exporter verification
  - PA-CB export direction
  - EDPMS flagging workflow
  - outward remittance KYC
tools:
  - Read/Write
---

# PA-CB Export Direction — Indian Exporter KYC

> Indian exporter onboarding · PAN + GSTIN + ECA check · EDPMS flagging for outward remittance · AD Bank intimation · 10% UBO with nationality · FEMA + PA-CB compliant · ~₹25–40 per onboarding

---

## Regulatory context

This workflow covers Cashfree's **PA-CB licence — Export direction**: onboarding Indian merchants who receive foreign currency payments (export of goods or services).

| Requirement | Rule |
|---|---|
| GSTIN mandatory | Indian exporters must have valid GSTIN for foreign currency billing |
| PAN–GSTIN name match | Entity name on PAN must match GSTIN legal name — required for EDPMS routing |
| EDPMS flagging | Mandatory for all foreign currency export settlements per FEMA 1999 |
| AD Bank intimation | Authorised Dealer bank must be notified for each export settlement |
| ECA (Export Credit Account) | Required for goods exporters receiving >$25,000 per shipment |
| Export proceeds realisation | Goods: 9 months · Software on-site: 12 months · Software off-site: 6 months |
| ₹25L per-transaction cap | Hard cap per PA-CB guidelines — no exceptions |
| 10% UBO threshold | Nationality and country of residence required (FATF obligation) |

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
EDPMS_API_URL=          # Cashfree internal or your EDPMS integration endpoint
ECA_CHECK_API_URL=      # ECA account verification endpoint
CKYC_DOCKER_DEPLOYED=false
CKYC_ONPREM_URL=
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "pa_cb_export_kyc",
  "description": "PA-CB Export — Indian exporter KYC, EDPMS flagging, ECA check, BAV",
  "trigger": "api",
  "inputs": ["merchant_id", "pan", "gstin", "mobile", "ad_bank_name", "export_type"],
  "nodes": [
    { "id": "consent", "type": "ui", "template": "dpdp_consent",
      "msg": "We need to verify your business for cross-border payment services under FEMA guidelines.",
      "on_denied": "REJECT" },

    { "id": "mob-send", "type": "api", "call": "POST /mobile360/otp/send" },
    { "id": "mob-verify", "type": "api", "call": "POST /mobile360/otp/verify",
      "prefill_outputs": ["name"] },

    { "id": "pan-verify", "type": "api", "call": "POST /pan", "version": "2024-12-01",
      "on_invalid": "REJECT", "on_deleted": "REJECT",
      "outputs": ["pan_name", "entity_type", "director_flag", "filing_status"] },

    { "id": "gstin-verify", "type": "api", "call": "POST /gstin",
      "in": { "gstin": "{{gstin}}", "pan": "{{pan}}" },
      "on_invalid": "REJECT", "on_suspended": "REJECT", "on_cancelled": "REJECT",
      "on_pan_mismatch": "REJECT",
      "outputs": ["legal_name", "registration_date", "business_type", "state_code"] },

    { "id": "name-match", "type": "api", "call": "POST /name-match",
      "in": { "name1": "{{pan_name}}", "name2": "{{legal_name}}" },
      "on_below_60": "REJECT",
      "note": "PAN entity name must match GSTIN legal name — required for EDPMS routing" },

    { "id": "eca-gate", "type": "condition",
      "if": "export_type == 'GOODS'", "then": "eca-check", "else": "ubo-check",
      "note": "ECA check for goods exporters only — services exporters skip to UBO" },

    { "id": "eca-check", "type": "api", "call": "{{ECA_CHECK_API_URL}}/verify",
      "in": { "gstin": "{{gstin}}", "pan": "{{pan}}" },
      "on_not_found": "+1 AMBER",
      "note": "ECA required for goods export >$25,000 per shipment — flag if missing for high-volume accounts" },

    { "id": "ubo-check", "type": "ui", "template": "ubo_declaration",
      "threshold_pct": 10,
      "required_fields": ["shareholder_name", "shareholding_pct", "nationality", "country_of_residence"],
      "note": "10% UBO threshold — nationality and country of residence required for FATF risk scoring" },

    { "id": "bav", "type": "api", "call": "POST /bank-account/sync",
      "on_fraud_account": "REJECT_AND_FLAG", "on_invalid": "REJECT",
      "flags": {
        "name_below_60": "REJECT",
        "name_60_to_84": "+1 AMBER"
      },
      "note": "Settlement account must match GSTIN entity name — critical for EDPMS routing" },

    { "id": "edpms-flag", "type": "api", "call": "{{EDPMS_API_URL}}/register",
      "in": {
        "merchant_id": "{{merchant_id}}",
        "pan": "{{pan}}",
        "gstin": "{{gstin}}",
        "ad_bank_name": "{{ad_bank_name}}",
        "export_type": "{{export_type}}",
        "settlement_account": "{{bav_account_number}}"
      },
      "outputs": ["edpms_ref_number"],
      "note": "EDPMS registration — all outward remittances must be flagged per FEMA 1999" },

    { "id": "ckyc-upload-gate", "type": "condition",
      "if": "CKYC_DOCKER_DEPLOYED == true", "then": "ckyc-push", "else": "risk-gate" },
    { "id": "ckyc-push", "type": "api", "call": "{{CKYC_ONPREM_URL}}/upload",
      "async": true, "mandate_days": 10 },

    { "id": "risk-gate", "type": "gate", "rules": [
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

app.post('/api/cb-export/start', async (req, res) => {
  const {
    merchantId,
    pan,
    gstin,
    mobile,
    adBankName,
    exportType,   // 'GOODS' | 'SERVICES' | 'SOFTWARE'
  } = req.body;

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
        merchant_id:  merchantId,
        pan,
        gstin,
        mobile,
        ad_bank_name: adBankName,
        export_type:  exportType,
        redirect_url: `${BASE_URL}/cb-export/done`,
        webhook_url:  `${BASE_URL}/api/cb-export/webhook`,
      }),
    }
  );

  const { run_id, hosted_url } = await r.json();
  res.json({ kycUrl: hosted_url, runId: run_id });
});

app.post('/api/cb-export/webhook', (req, res) => {
  const sig = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody).digest('base64');
  if (sig !== expected) return res.status(401).send('Bad signature');

  const { merchant_id, status, flags, edpms_ref_number, export_type } = req.body;

  switch (status) {
    case 'APPROVED':
      // ✅ Indian exporter verified — enable foreign currency settlement
      activateExporter(merchant_id, edpms_ref_number);
      scheduleRealisationCheck(merchant_id, export_type); // FEMA proceeds compliance
      break;

    case 'REJECTED':
      // ❌ PAN/GSTIN invalid, name mismatch, or fraud account
      // flags[]: 'pan_invalid', 'gstin_suspended', 'name_mismatch', 'fraud_account'
      rejectMerchant(merchant_id, flags);
      break;

    case 'MANUAL_REVIEW':
      // ⚠️ ECA not found or moderate name match — ops review
      queueForOps(merchant_id, flags);
      break;
  }

  res.json({ received: true });
});

// FEMA: schedule export proceeds realisation check
function realisationDeadlineMonths(exportType) {
  if (exportType === 'GOODS')            return 9;
  if (exportType === 'SOFTWARE_ON_SITE') return 12;
  return 6; // SOFTWARE_OFF_SITE, SERVICES
}

async function activateExporter(id, edpmsRef)        { /* activate CB collection, store EDPMS ref */ }
async function scheduleRealisationCheck(id, type)    { /* schedule FEMA compliance reminder */ }
async function rejectMerchant(id, flags)             { /* update DB */ }
async function queueForOps(id, flags)                { /* ops queue */ }

app.listen(3000);
```

---

### Step 3 — Test it

```bash
# Software exporter onboarding
curl -X POST http://localhost:3000/api/cb-export/start \
  -H "Content-Type: application/json" \
  -d '{"merchantId":"exp_001","pan":"AABCE1234F","gstin":"29AABCE1234F1Z5","mobile":"9999999999","adBankName":"HDFC Bank","exportType":"SOFTWARE"}'

# Goods exporter onboarding (ECA check triggered)
curl -X POST http://localhost:3000/api/cb-export/start \
  -H "Content-Type: application/json" \
  -d '{"merchantId":"exp_002","pan":"AABCF5678G","gstin":"27AABCF5678G1Z3","mobile":"9999999998","adBankName":"ICICI Bank","exportType":"GOODS"}'

# Simulate APPROVED webhook
curl -X POST http://localhost:3000/api/cb-export/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"merchant_id":"exp_001","status":"APPROVED","flags":[],"edpms_ref_number":"EDPMS20251234","export_type":"SOFTWARE"}'

# Simulate REJECTED (GSTIN suspended)
curl -X POST http://localhost:3000/api/cb-export/webhook \
  -H "x-cashfree-signature: <sign>" \
  -d '{"merchant_id":"exp_003","status":"REJECTED","flags":["gstin_suspended"]}'
```

---

## Export proceeds realisation schedule (FEMA)

| Export type | Realisation deadline | Action on breach |
|---|---|---|
| Goods | 9 months from shipment date | AD Bank reporting + RBI intimation |
| Software — on-site | 12 months from invoice date | AD Bank reporting |
| Software — off-site | 6 months from invoice date | AD Bank reporting |
| Services (other) | 6 months | AD Bank reporting |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| DPDP consent | EDPMS API integration | AD Bank portal filing |
| Mobile OTP | ECA check API | Export proceeds realisation monitoring |
| PAN Advanced (director flag, filing status) | CKYCR Docker (optional) | FIU-IND STR/CTR filing |
| GSTIN verification + PAN cross-check | | FEMA penalty tracking |
| Entity name match | | |
| ECA account check (goods exporters) | | |
| 10% UBO declaration (with nationality) | | |
| BAV — settlement account | | |
| EDPMS registration flag | | |
| CKYCR async upload | | |

**Regulation:** FEMA 1999 · RBI AP (DIR Series) Circular · RBI PA-CB Guidelines · PMLA Section 11A · DPDP Act 2023

**Cost:** ~₹25–40 per exporter onboarding

---

## MCP — coming soon

```
/relay-pa-cb-export

→ Claude: "Export type (goods / services / software)? ECA account present? AD Bank?"
→ Calls Relay MCP → creates PA-CB export workflow with EDPMS flagging
→ Returns RELAY_WORKFLOW_ID
```
