---
name: relay-edd
description: Cashfree KYC workflow for Enhanced Due Diligence (EDD) — handles PEP matches, sanctions hits, adverse media, mule indicators, and high-value transaction triggers. 5 trigger types, deep AML screening integration, physical CPV scheduling, senior management approval gate, RBI-mandated audit trail. Relay-partial — external AML/case management required. Generates Node.js integration code and workflow spec.
triggers:
  - /relay-edd
  - EDD workflow
  - enhanced due diligence relay
  - high risk KYC template
  - PEP sanctions workflow
  - adverse media screening
tools:
  - Read/Write
---

# Enhanced Due Diligence (EDD)

> For PEP matches · Sanctions hits · Adverse media · Mule indicators · High-value thresholds · External AML required · Senior management approval gate · RBI PMLA compliant

---

## Regulatory mandate

| Obligation | Regulation | SLA / Condition |
|---|---|---|
| PEP identification | RBI KYC MD 2023 — Section 32 · FATF Recommendation 12 | All PEPs require senior management approval before account activation |
| Sanctions screening | PMLA Section 11A · UN Security Council Resolutions · OFAC | Confirmed match = immediate rejection. No override permitted. |
| Source of funds declaration | PMLA Section 11A · PML Rules 2005 — Rule 3 | Mandatory for high-value transactions and PEP-adjacent accounts |
| Physical CPV | RBI KYC MD 2023 — Section 16(f) | Mandatory for mule indicators / high-risk cases |
| STR filing | PMLA Section 12 · FIU-IND | Within 7 working days of suspicion — EDD trigger is automatic suspicion signal |
| CTR filing | PMLA Section 12 · FIU-IND | By 15th of succeeding month for cash > ₹10L |
| EDD audit trail | PMLA Section 12 · PML Rules — Rule 3 | 5-year mandatory retention with trigger, documents, approvals, and outcome |
| PEP senior approval SLA | RBI KYC MD 2023 — Section 32 | 2 business days — auto-reject on timeout |
| Source of funds SLA | PMLA guidelines | 5 business days — auto-reject on compliance silence |
| Adverse media SLA | Internal policy (FATF best practice) | 24 hours — default MEDIUM risk if timeout |

---

## Important: Relay covers the workflow. You bring the AML data.

Relay orchestrates the EDD *process* — which documents to collect, who approves, when to escalate. The AML/PEP *data* (sanctions lists, adverse media, PEP databases) must come from your compliance stack or a bureau like LexisNexis / Refinitiv / CIBIL.

| Relay handles | You must provide |
|---|---|
| EDD trigger routing | AML/PEP API endpoint |
| Document collection workflow | Adverse media search (async) |
| Physical CPV scheduling | Senior management approval queue |
| Audit trail per PMLA | Case management system (optional) |
| Customer notification flow | 5-year record retention |

---

## 5 EDD triggers

| Trigger | Example | Auto-route to |
|---|---|---|
| PEP match | Customer matches PEP database | Senior review + CPV |
| Sanctions hit | OFAC / UN / domestic list match | REJECT or senior review |
| Adverse media | Fraud / crime news match | Async media check + review |
| Mule indicator | 3+ amber flags from Standard CDD | Enhanced document check |
| High-value threshold | Transaction >₹10L (configurable) | Source of funds declaration |

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
AML_PEP_API_URL=         # LexisNexis / Refinitiv / CIBIL FI / your AML endpoint
ADVERSE_MEDIA_API_URL=   # async adverse media check endpoint
CPV_SCHEDULING_URL=      # physical customer personal verification scheduler
HIGH_VALUE_THRESHOLD=1000000   # ₹10L default
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "edd_case_management",
  "description": "Enhanced Due Diligence — PEP/sanctions/adverse media/mule/high-value triggers",
  "trigger": "api",
  "inputs": ["customer_id", "trigger_type", "trigger_reason", "transaction_amount"],
  "nodes": [
    { "id": "trigger-route", "type": "condition",
      "switch": "trigger_type",
      "cases": {
        "PEP_MATCH":        "pep-flow",
        "SANCTIONS_HIT":    "sanctions-check",
        "ADVERSE_MEDIA":    "adverse-media-flow",
        "MULE_INDICATOR":   "mule-edd-flow",
        "HIGH_VALUE":       "source-of-funds-flow"
      }
    },

    { "id": "pep-flow", "type": "sequence", "nodes": [
        { "id": "pep-confirm",     "type": "api", "call": "{{AML_PEP_API_URL}}/pep-check",
          "on_confirmed_pep": "source-of-funds-flow",
          "on_false_positive": "APPROVE" },
        { "id": "senior-approval", "type": "wait", "event": "senior_manager_approved",
          "timeout_days": 2, "on_timeout": "REJECT",
          "note": "RBI: PEP accounts require senior management approval" }
    ]},

    { "id": "sanctions-check", "type": "api", "call": "{{AML_PEP_API_URL}}/sanctions",
      "on_confirmed_match": "REJECT",
      "on_false_positive": "APPROVE",
      "note": "Confirmed sanctions match = immediate REJECT. No manual override." },

    { "id": "adverse-media-flow", "type": "sequence", "nodes": [
        { "id": "adverse-media", "type": "api", "call": "{{ADVERSE_MEDIA_API_URL}}/check",
          "async": true, "timeout_hours": 24 },
        { "id": "media-gate",    "type": "gate", "rules": [
            { "if": "media_risk == 'LOW'",    "out": "APPROVE" },
            { "if": "media_risk == 'MEDIUM'", "out": "source-of-funds-flow" },
            { "if": "media_risk == 'HIGH'",   "out": "senior-approval" }
        ]}
    ]},

    { "id": "mule-edd-flow", "type": "sequence", "nodes": [
        { "id": "enhanced-doc",  "type": "ui", "template": "enhanced_document_checklist",
          "required_docs": ["source_of_funds", "employment_proof", "last_3_months_bank_statement"] },
        { "id": "cpv-schedule",  "type": "api", "call": "{{CPV_SCHEDULING_URL}}/book",
          "in": { "customer_id": "{{customer_id}}", "urgency": "HIGH" },
          "note": "CPV = Customer Personal Verification — physical visit by field agent" }
    ]},

    { "id": "source-of-funds-flow", "type": "sequence", "nodes": [
        { "id": "sof-declaration","type": "ui", "template": "source_of_funds_declaration",
          "required_fields": ["fund_source", "fund_origin_country", "expected_annual_turnover"] },
        { "id": "sof-docs",      "type": "ui", "template": "document_upload",
          "required_docs": ["salary_slip_or_itr", "business_registration_if_applicable"],
          "note": "3 months salary slip or 2 years ITR accepted" },
        { "id": "compliance-review", "type": "wait", "event": "compliance_team_approved",
          "timeout_days": 5, "on_timeout": "REJECT",
          "note": "Compliance team reviews source of funds — SLA 5 business days" }
    ]},

    { "id": "audit-log", "type": "api", "call": "POST /audit/log",
      "in": {
        "customer_id": "{{customer_id}}",
        "trigger": "{{trigger_type}}",
        "reason": "{{trigger_reason}}",
        "outcome": "{{final_status}}",
        "timestamp": "{{now}}"
      },
      "note": "RBI PMLA: EDD audit trail mandatory. Retain 5 years." }
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

// Trigger EDD — called from your Standard CDD webhook when ESCALATE_EDD fires
app.post('/api/edd/start', async (req, res) => {
  const { customerId, triggerType, triggerReason, transactionAmount = 0 } = req.body;

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
        redirect_url: `${BASE_URL}/edd/done`,
        webhook_url:  `${BASE_URL}/api/edd/webhook`,
        metadata: {
          trigger_type:       triggerType,    // 'PEP_MATCH' | 'SANCTIONS_HIT' | 'ADVERSE_MEDIA' | 'MULE_INDICATOR' | 'HIGH_VALUE'
          trigger_reason:     triggerReason,
          transaction_amount: transactionAmount,
        },
      }),
    }
  );

  const { run_id } = await r.json();
  res.json({ eddRunId: run_id, message: 'EDD case opened' });
});

app.post('/api/edd/webhook', (req, res) => {
  const sig = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody).digest('base64');
  if (sig !== expected) return res.status(401).send('Bad signature');

  const { customer_id, status, flags, trigger_type } = req.body;

  switch (status) {
    case 'APPROVED':
      // ✅ EDD passed — re-activate account
      activateAccount(customer_id);
      logEDDOutcome(customer_id, trigger_type, 'APPROVED');
      break;

    case 'REJECTED':
      // ❌ Confirmed sanctions, PEP declined, or compliance rejection
      closeAccount(customer_id, flags);
      logEDDOutcome(customer_id, trigger_type, 'REJECTED');
      break;

    case 'PENDING_SENIOR_APPROVAL':
      // ⏳ Waiting for senior management
      updateStatus(customer_id, 'EDD_SENIOR_REVIEW');
      break;

    case 'PENDING_COMPLIANCE_REVIEW':
      // ⏳ Source of funds under compliance review (5-day SLA)
      updateStatus(customer_id, 'EDD_COMPLIANCE_REVIEW');
      break;

    case 'CPV_SCHEDULED':
      // 🏠 Physical visit booked — notify customer
      notifyCustomerCPV(customer_id);
      break;
  }

  res.json({ received: true });
});

async function activateAccount(id)           { /* re-activate after EDD clear */ }
async function closeAccount(id, flags)       { /* close account, preserve audit trail */ }
async function updateStatus(id, status)      { /* update DB */ }
async function notifyCustomerCPV(id)         { /* send CPV appointment details */ }
async function logEDDOutcome(id, trigger, outcome) { /* append to compliance audit log */ }

app.listen(3000);
```

---

### Step 3 — Triggering EDD from your Standard CDD webhook

```javascript
// In your Standard CDD webhook handler (relay-standard-cdd):
case 'ESCALATE_EDD':
  // Route to EDD workflow
  await fetch('/api/edd/start', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      customerId:    customer_id,
      triggerType:   flags.includes('pep_match') ? 'PEP_MATCH' : 'MULE_INDICATOR',
      triggerReason: flags.join(', '),
    }),
  });
  break;
```

---

## EDD SLAs (RBI guidance)

| EDD type | Max resolution time | Action on breach |
|---|---|---|
| Sanctions hit | Immediate | Auto-reject |
| PEP confirmation | 2 business days | Reject if no senior approval |
| Source of funds review | 5 business days | Reject if compliance silent |
| CPV completion | 10 business days | Flag for ops escalation |
| Adverse media (async) | 24 hours | Default to MEDIUM risk if timeout |

---

## Enterprise governance

| Control | Cashfree platform | Your responsibility |
|---|---|---|
| **Data residency** | India-only · AWS ap-south-1 (Mumbai) · No cross-border transfer | Receiving systems must be India-hosted or covered by a DPA |
| **Encryption** | TLS 1.3 in transit · AES-256 at rest · Session hash chain | Maintain equivalent standards in your storage layer |
| **Audit trail** | Immutable session logs retained 7 years | PMLA: 5 years minimum from relationship end — your DB must also retain |
| **EDD audit file** | Audit log node included in every EDD case | Retain 5 years minimum — trigger, documents collected, approvals, final outcome |
| **FIU-IND — STR** | `flags[]` in webhook surfaces suspicion triggers | File STR within 7 working days of suspicion on goAML portal |
| **FIU-IND — CTR** | Transaction metadata delivered via webhook | File CTR by 15th of succeeding month for cash transactions > ₹10L |
| **Post-EDD monitoring** | Relay sends ESCALATE_EDD webhook | After EDD APPROVE: enroll in HIGH-risk monitoring (relay-continuous-monitoring) |
| **DPDP rights** | Consent event stored per DPDP Act 2023 — Section 6 | Data Principal rights (access / correction / erasure) are your obligation |
| **Board policy** | Workflow enforces your configured KYC policy | Board-approved KYC/AML policy + Designated Director required before FIU-IND registration |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| 5 EDD trigger type routing | AML/PEP API endpoint | Sanctions list maintenance |
| PEP confirmation + senior approval gate | Adverse media API | |
| Sanctions → auto-reject | CPV scheduling system | |
| Async adverse media check | Case management system | |
| Source of funds declaration UI | | |
| Document collection (salary slip / ITR) | | |
| Compliance review wait state (5-day SLA) | | |
| CPV scheduling node | | |
| Audit log per PMLA | | |

**Regulation:** RBI KYC Master Directions 2023 — Section 32 (PEP) · Section 33 (enhanced monitoring) · PMLA Sections 11A, 12 · PML Rules 2005 — Rule 3 (STR) · UN Security Council Resolutions (sanctions) · FATF Recommendations 12–13 (PEP + enhanced DD) · DPDP Act 2023 — Section 6

**Retention:** All EDD records — 5 years minimum. Audit trail must include trigger, documents collected, approvals, and final outcome.

---

## MCP — coming soon

```
/relay-edd

→ Claude: "Which triggers? AML provider? CPV available in your geography?"
→ Calls Relay MCP → creates EDD workflow linked to your CDD workflow
→ Returns RELAY_WORKFLOW_ID for EDD case handler
```
