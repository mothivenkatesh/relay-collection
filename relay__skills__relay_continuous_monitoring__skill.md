---
name: relay-continuous-monitoring
description: Cashfree Relay workflow for Post-Onboarding Continuous Monitoring — cron-triggered periodic re-checks, anomaly detection rules (transaction spikes, geographic anomalies, dormancy breaks), trust score decay, daily deduplication guard, alert routing by severity. Relay-partial — anomaly ML and trust score model require external systems. Generates Node.js integration code and webhook handler.
triggers:
  - /relay-continuous-monitoring
  - continuous monitoring relay
  - post-onboarding KYC monitoring
  - transaction monitoring workflow
  - perpetual KYC monitoring
  - anomaly detection relay
tools:
  - Read/Write
---

# Post-Onboarding Continuous Monitoring

> Periodic re-checks · Anomaly signals (spikes, geo, dormancy) · Trust score decay · Daily dedup guard · Alert routing by severity · External ML required for scoring

---

## Regulatory mandate

| Obligation | Regulation | Frequency |
|---|---|---|
| Continuous transaction monitoring | PMLA Section 11A · PML Rules 2005 — Rule 3 | Ongoing — real-time anomaly detection |
| Periodic re-verification by risk tier | RBI KYC MD 2023 — Section 38 | HIGH: daily check · MEDIUM: weekly · LOW: monthly |
| PAN re-verification | RBI KYC MD 2023 — Section 17 | HIGH: quarterly · MEDIUM: 6-monthly · LOW: yearly |
| Adverse media re-screening | PMLA Section 11A · FATF Recommendation 10 | As detected; minimum annually for HIGH risk |
| STR filing | PMLA Section 12 · FIU-IND | Within 7 working days of suspicion — each monitoring alert must be assessed |
| CTR filing | PMLA Section 12 · FIU-IND | By 15th of succeeding month for cash > ₹10L |
| Record retention | PMLA Section 12 | 5 years from account closure |
| Trust score model | Not regulated specifically — but must be explainable | Model documentation required for RBI exam / internal audit |

---

## What Relay handles vs what needs your systems

| Relay handles | Your systems must provide |
|---|---|
| Cron-triggered workflow runs (daily/weekly) | Transaction anomaly detection ML |
| Webhook triggers from your transaction system | Trust score model |
| Document expiry re-verification | Anomaly alert ingestion |
| Adverse media re-screening (via your API) | CKYC update (CKYC Docker) |
| Alert routing by severity | Alert management / SIEM |
| Daily deduplication (one check per customer/day) | |

---

## 4 monitoring trigger types

| Trigger | Relay trigger method | Frequency |
|---|---|---|
| Periodic re-check (scheduled) | Cron (`daily` / `weekly` / `monthly`) | Per risk tier config |
| Transaction anomaly | Webhook from your transaction system | Real-time |
| Document expiry | Internal timer in Relay | 30 days before expiry |
| Adverse media match | Webhook from your media screening system | As detected |

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
ANOMALY_API_URL=          # your transaction anomaly detection endpoint
TRUST_SCORE_API_URL=      # your trust score model endpoint
ADVERSE_MEDIA_API_URL=    # your adverse media re-screening endpoint
CKYC_DOCKER_DEPLOYED=false
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "continuous_monitoring",
  "description": "Post-onboarding monitoring — cron + webhook triggers, anomaly + trust score gate",
  "trigger": ["cron", "webhook"],
  "inputs": ["customer_id", "trigger_type", "risk_tier"],
  "nodes": [
    { "id": "dedup-guard",    "type": "condition",
      "if": "customer_checked_today == true", "then": "SKIP",
      "note": "One check per customer per day max — prevents runaway billing" },

    { "id": "trigger-route",  "type": "condition",
      "switch": "trigger_type",
      "cases": {
        "SCHEDULED":           "trust-score-check",
        "TRANSACTION_ANOMALY": "anomaly-check",
        "DOCUMENT_EXPIRY":     "doc-refresh",
        "ADVERSE_MEDIA":       "media-rescreen"
      }
    },

    { "id": "trust-score-check","type": "api", "call": "{{TRUST_SCORE_API_URL}}/score",
      "in": { "customer_id": "{{customer_id}}", "risk_tier": "{{risk_tier}}" },
      "outputs": ["trust_score", "decay_reason"],
      "on_score_above_70": "NO_ACTION",
      "on_score_30_to_70": "soft-review",
      "on_score_below_30": "trigger-re-kyc" },

    { "id": "anomaly-check",  "type": "api", "call": "{{ANOMALY_API_URL}}/check",
      "in": { "customer_id": "{{customer_id}}" },
      "outputs": ["anomaly_type", "anomaly_severity"],
      "on_LOW": "NO_ACTION",
      "on_MEDIUM": "soft-review",
      "on_HIGH": "trigger-re-kyc" },

    { "id": "doc-refresh",    "type": "sequence", "nodes": [
        { "id": "doc-recheck","type": "api", "call": "POST /pan", "version": "2024-12-01",
          "on_invalid": "escalate-compliance" },
        { "id": "ckyc-update","type": "condition",
          "if": "CKYC_DOCKER_DEPLOYED == true", "then": "ckyc-refresh", "else": "flag_ckyc_skip" }
    ]},

    { "id": "media-rescreen", "type": "api", "call": "{{ADVERSE_MEDIA_API_URL}}/rescreen",
      "in": { "customer_id": "{{customer_id}}" },
      "on_HIGH_RISK": "escalate-compliance",
      "on_MEDIUM_RISK": "soft-review",
      "on_LOW_RISK": "NO_ACTION" },

    { "id": "soft-review",    "type": "api", "call": "POST /alert",
      "in": {
        "customer_id": "{{customer_id}}",
        "severity": "MEDIUM",
        "message": "Monitoring flag — review within 5 days"
      }},

    { "id": "trigger-re-kyc", "type": "api", "call": "POST /alert",
      "in": {
        "customer_id": "{{customer_id}}",
        "severity": "HIGH",
        "action": "INITIATE_RE_KYC",
        "message": "Trust score critical — initiate re-verification"
      }},

    { "id": "escalate-compliance","type": "api", "call": "POST /alert",
      "in": {
        "customer_id": "{{customer_id}}",
        "severity": "CRITICAL",
        "action": "ESCALATE_EDD",
        "message": "Escalate to compliance for EDD"
      }}
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

// Trigger a monitoring run for a specific customer
// Call this from your cron job or transaction system
app.post('/api/monitor/run', async (req, res) => {
  const { customerId, triggerType = 'SCHEDULED', riskTier = 'LOW' } = req.body;

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
        webhook_url:  `${BASE_URL}/api/monitor/webhook`,
        metadata: { trigger_type: triggerType, risk_tier: riskTier },
      }),
    }
  );

  const { run_id } = await r.json();
  res.json({ monitorRunId: run_id });
});

// Call this from your transaction system when an anomaly is detected
app.post('/api/monitor/anomaly', async (req, res) => {
  const { customerId, anomalyType, severity } = req.body;
  await triggerMonitoringRun(customerId, 'TRANSACTION_ANOMALY');
  res.json({ triggered: true });
});

app.post('/api/monitor/webhook', (req, res) => {
  const sig = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody).digest('base64');
  if (sig !== expected) return res.status(401).send('Bad signature');

  const { customer_id, status, action, severity } = req.body;

  switch (status) {
    case 'NO_ACTION':
      // ✅ Clean — no action needed. Log and move on.
      logMonitoringResult(customer_id, 'CLEAN');
      break;

    case 'SOFT_REVIEW':
      // ⚠️ Medium alert — route to ops queue (5-day SLA)
      queueForReview(customer_id, severity);
      break;

    case 'RE_KYC_REQUIRED':
      // 🔴 Trust score critical — initiate re-KYC workflow
      // Use relay-existing-customer skill
      initiateReKYC(customer_id);
      break;

    case 'ESCALATE_EDD':
      // 🚨 Critical — document expired or adverse media HIGH — route to EDD
      // Use relay-edd skill
      initiateEDD(customer_id, 'ADVERSE_MEDIA');
      break;

    case 'SKIPPED':
      // Already checked today — dedup guard triggered
      break;
  }

  res.json({ received: true });
});

async function triggerMonitoringRun(id, type) {
  await fetch('/api/monitor/run', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ customerId: id, triggerType: type }),
  });
}
async function logMonitoringResult(id, result) { /* log to audit trail */ }
async function queueForReview(id, severity)    { /* add to ops queue */ }
async function initiateReKYC(id)               { /* trigger relay-existing-customer workflow */ }
async function initiateEDD(id, trigger)        { /* trigger relay-edd workflow */ }

app.listen(3000);
```

---

### Step 3 — Setting up your cron

```bash
# Example: daily cron to run monitoring for all active customers
# This hits your own endpoint which fans out to Relay per customer

# crontab entry (runs at 2 AM IST = 8:30 PM UTC)
30 20 * * * curl -X POST https://yourapp.com/api/monitor/batch-run

# Or using node-cron in your app:
import cron from 'node-cron';
cron.schedule('30 20 * * *', async () => {
  const customers = await getActiveCustomers();
  for (const c of customers) {
    await fetch('/api/monitor/run', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        customerId: c.id,
        triggerType: 'SCHEDULED',
        riskTier: c.riskTier,
      }),
    });
    await new Promise(r => setTimeout(r, 100)); // rate limit: 10/sec
  }
});
```

---

## Re-check frequency by risk tier

| Risk tier | Scheduled re-check | PAN re-check | CKYC update |
|---|---|---|---|
| LOW | Monthly | Yearly | On change |
| MEDIUM | Weekly | Every 6 months | Every 6 months |
| HIGH | Daily | Every 3 months | Every 3 months |
| EDD | Per case SLA | Per EDD outcome | Per EDD outcome |

---

## Enterprise governance

| Control | Cashfree platform | Your responsibility |
|---|---|---|
| **Data residency** | India-only · AWS ap-south-1 (Mumbai) · No cross-border transfer | Receiving systems must be India-hosted or covered by a DPA |
| **Encryption** | TLS 1.3 in transit · AES-256 at rest · Session hash chain | Maintain equivalent standards in your storage layer |
| **Audit trail** | Immutable session logs retained 7 years | PMLA: 5 years minimum from relationship end — your DB must also retain |
| **CKYC update trigger** | Sends RE_KYC_REQUIRED webhook when trust score critical | Use relay-existing-customer to trigger re-KYC; upload updated CKYCR within 10 days |
| **FIU-IND — STR** | `flags[]` in webhook surfaces suspicion triggers | File STR within 7 working days of suspicion on goAML portal |
| **FIU-IND — CTR** | Transaction metadata delivered via webhook | File CTR by 15th of succeeding month for cash transactions > ₹10L |
| **Re-KYC schedule** | Relay supports re-trigger — use relay-existing-customer | HIGH risk: 2 yr · MEDIUM: 8 yr · LOW: 10 yr · PEP: 1 yr |
| **DPDP rights** | Consent event stored per DPDP Act 2023 — Section 6 | Data Principal rights (access / correction / erasure) are your obligation |
| **Board policy** | Workflow enforces your configured KYC policy | Board-approved KYC/AML policy + Designated Director required before FIU-IND registration |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| Cron + webhook dual trigger | Trust score model (your ML) | Real-time transaction monitoring |
| Daily deduplication guard | Anomaly detection API | Cross-institution data |
| Trust score → alert routing | Adverse media API | |
| Transaction anomaly webhook handler | CKYC Docker (for CKYC update) | |
| Document expiry re-verification | Alert management / SIEM | |
| Adverse media re-screening | | |
| Severity-based alert routing | | |
| Re-KYC and EDD escalation triggers | | |

**Regulation:** RBI KYC Master Directions 2023 — Section 38 (periodic updation by risk tier) · PMLA Sections 11A, 12 · PML Rules 2005 — Rule 3 (transaction monitoring) · FATF Recommendation 10 (ongoing due diligence) · DPDP Act 2023 — Section 6

---

## MCP — coming soon

```
/relay-continuous-monitoring

→ Claude: "Risk tiers? Anomaly API endpoint? Trust score model?"
→ Calls Relay MCP → creates monitoring workflow
→ Returns RELAY_WORKFLOW_ID (cron + webhook)
```
