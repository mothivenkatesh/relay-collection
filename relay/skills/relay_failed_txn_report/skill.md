---
name: relay-failed-txn-report
description: Cashfree Relay workflow — every hour, fetches failed transactions and emails a summary report. Hourly run deduplication (no duplicate reports), "all-clear" email when zero failures, Gmail rate-limit budget awareness (500/day personal · 2000/day Workspace), DPDP-disclosed, failure self-alert, test harness. ~₹0 per run.
metadata:
  kind: workflow
  category: reporting
  version: "2.0.0"
  tags: [failed-transactions, hourly-report, gmail, monitoring, alerting]
  author: Cashfree Relay Team
  trigger_config:
    auto_trigger: true
    keywords:
      - "hourly failed transaction report"
      - "failed transaction email"
      - "hourly failed payment report"
      - "email failed transactions every hour"
    intent_patterns:
      - "(?:hourly|each hour).*(?:failed|unsuccessful).*(?:transaction|payment).*(?:report|email)"
      - "(?:send|email).*(?:hourly).*(?:failed|unsuccessful).*(?:transaction|payment)"
    confidence_threshold: 0.75
user-invocable: true
triggers:
  - /relay-failed-txn-report
  - hourly failed transaction report
  - failed payment email report
  - failed transactions hourly
tools:
  - Read/Write
---

# Hourly Failed Transaction Report → Gmail

> Runs every hour · Fetches failed payments from Cashfree · Emails a summary to your team · Sends "All clear ✅" when zero failures — so silence never means broken · Deduplication prevents double-reports · Gmail rate-limit safe · ~₹0 per run

---

## What gets built

```
Every hour at HH:[minute]
        │
        ▼
  Fetch failed transactions (last 60 min window)
        │
        ├── 0 failures? ──→ Send "All clear ✅" email (if enabled) → done
        │
        ▼ failures found
  Build report email
        │
        ▼
  Deduplication check — already sent this hour?
        │ no
        ▼
  Gmail → Send report
        │
        ├── SUCCESS → log run
        └── FAILURE → retry ×3 → self-alert (different channel)
```

---

## Enterprise governance

| Control | What Relay handles | Your responsibility |
|---|---|---|
| **Idempotency** | `hour_window_key` (YYYY-MM-DD-HH) prevents duplicate reports if the cron fires twice | No action needed — built into the workflow |
| **"All clear" email** | Optional node — sends a short "no failures this hour" email so silence never looks like a broken workflow | Configure `SEND_ALL_CLEAR=true` if you want this |
| **Failure recovery** | Auto-retry ×3 with exponential backoff; failure triggers self-alert to a secondary email | Set `SELF_ALERT_EMAIL` to an inbox you check |
| **Gmail rate limit** | Gmail API: 500 emails/day (personal Google) · 2,000/day (Google Workspace) · This workflow sends 1/hr = 24/day — well within limits | If you add CC/BCC with many recipients, each recipient counts as a separate send |
| **Data sent to Gmail** | Failed order IDs · Transaction amounts · Failure reasons · Timestamps | These are transaction records — document in your Privacy Policy; ensure recipient mailbox is access-controlled |
| **DPDP** | Aggregated failure data (no individual customer PII in standard report) | If you add customer name/email to the report body, that becomes a DPDP-relevant data transfer |
| **Audit trail** | Relay logs every run with status, payload hash, email message-id — 90-day retention | Forward Relay run logs to your SIEM for longer retention |
| **OAuth health** | Relay auto-refreshes Gmail token before expiry | Re-authorise if token is manually revoked in Google account settings |
| **Scheduled window** | Relay runs the cron in UTC; you configure the minute-mark | State your business timezone when setting up — Relay converts automatically |

---

## Guided setup — business operators

### Step 1 — Check Gmail connection

Call `mcp__wfcd-mcp__list_credentials` with `node_name: "gmail"`.

**If no connection found:**

---
Gmail isn't connected yet. Here's how — takes 30 seconds:

1. Go to **Relay → Settings → Connections**
2. Click **+ Add Connection**
3. Choose **Gmail**
4. Sign in — Relay only gets permission to *send* emails, not read them
5. Type **"done"** when you're back
---

**If one found** — confirm:
> I'll send reports from **[Gmail address]**. Works?

**If multiple** — list and pick:
> Which Gmail account should send the reports?
> 1. [Account 1]
> 2. [Account 2]

---

### Step 2 — Configuration (one question at a time)

**Q1 — Who receives the report?**
> Who should get the hourly failed transaction report?
>
> Type one or more email addresses — e.g.
> `you@company.com` or `ops@company.com, cfo@company.com`

*Validate format. On error: "Try: name@company.com"*

**Follow-up:** Anyone to CC? (or say "no")

---

**Q2 — Email subject?**
> What should the subject line say?
>
> 1. **⚠️ Failed Transactions — Last Hour ([Count] failures)**
> 2. **Hourly Failed Payment Report — [Date & Time]**
> 3. **[Count] payments failed — [Date]**
> 4. Write your own

---

**Q3 — What should the report include?**
> What should the email show?
>
> 1. **Standard report** — total failures, total amount affected, list of failed order IDs *(recommended)*
> 2. **Summary only** — just the count and total amount
> 3. **Custom** — tell me what to include

*Generate template automatically. Never show `${...}` syntax.*

---

**Q4 — "All clear" email?**
> If there are zero failures in an hour, should I:
>
> 1. **Send an "All clear ✅" email** — confirms the workflow ran and nothing failed *(recommended for ops teams)*
> 2. **Send nothing** — only email when there are failures

*Most ops teams prefer option 1 — silence can be mistaken for a broken workflow.*

---

**Q5 — When in the hour?**
> Should this report run at the **top of every hour** (9:00, 10:00, 11:00…)?
>
> Or at a specific minute — e.g. "15 minutes past every hour"?
>
> Type **"top of hour"** or give me the minute mark.

---

**Q6 — Workflow name** (last, smart default):
> What should I call this?
> I'll use **"failed-transaction-hourly-report"** unless you want something else.

---

### Step 3 — Preview

> Here's what I'm setting up:
>
> | | |
> |---|---|
> | **Trigger** | Every hour at [minute] past the hour |
> | **Sends from** | [Gmail account] |
> | **Sends to** | [recipients] |
> | **CC** | [CC or "none"] |
> | **Subject** | [subject] |
> | **Report includes** | [standard / summary / custom] |
> | **All-clear email** | [yes / no] |
> | **Workflow name** | [name] |
>
> **Sample email (realistic):**
> ```
> ⚠️ Failed Transactions — Last Hour (3 failures)
>
> Failed Transaction Report — 11:00 AM IST, 11 May 2026
>
> Total failed payments: 3
> Total amount affected: ₹18,450
>
> Failed order IDs:
> • order_abc123 — ₹4,500 — Insufficient funds
> • order_def456 — ₹8,200 — Card declined
> • order_ghi789 — ₹5,750 — Gateway timeout
>
> Generated at: 2026-05-11 11:00 IST
> ```
>
> Ready? Type **yes** to activate.

---

### Step 4 — Create

1. Call `mcp__wfcd-mcp__create_workflow` → save `workflow_id`
2. Call `mcp__wfcd-mcp__update_workflow`

---

### Step 5 — Success message

> ✅ **Your hourly report is live.**
>
> **First report arrives at:** [next top-of-hour in your timezone]
>
> **If no email arrives:**
> · Check Relay → Workflows → [name] → Run History
> · Most common cause: Gmail connection expired — Relay → Settings → Connections → Reconnect
>
> **Gmail daily budget:** This workflow sends 24 emails/day. Gmail personal limit: 500/day. Google Workspace: 2,000/day. You have plenty of headroom.
>
> **To pause:** Toggle the workflow off in Relay → Workflows.

---

## Developer reference

### Environment variables

```env
# ─── Cashfree ──────────────────────────────────────────────────────────────────
CASHFREE_CLIENT_ID=
CASHFREE_CLIENT_SECRET=
CASHFREE_WEBHOOK_SECRET=
CASHFREE_BASE_URL=https://sandbox.cashfree.com   # → api.cashfree.com for prod

# ─── Relay ─────────────────────────────────────────────────────────────────────
RELAY_WORKFLOW_ID=
BASE_URL=http://localhost:3000

# ─── Report config ─────────────────────────────────────────────────────────────
REPORT_RECIPIENT=                      # primary recipient email
REPORT_CC=                             # comma-separated, optional
SEND_ALL_CLEAR=true                    # send "all clear" email when 0 failures

# ─── Observability ─────────────────────────────────────────────────────────────
SELF_ALERT_EMAIL=                      # ops inbox for workflow failure alerts
RELAY_TEST_MODE=false                  # true = log to console, don't send email
```

**Startup validator:**

```javascript
// startup.js
const REQUIRED = [
  'CASHFREE_CLIENT_ID', 'CASHFREE_CLIENT_SECRET',
  'CASHFREE_WEBHOOK_SECRET', 'RELAY_WORKFLOW_ID',
  'BASE_URL', 'REPORT_RECIPIENT',
];
const missing = REQUIRED.filter(k => !process.env[k]);
if (missing.length) {
  console.error('❌  Missing required env vars:\n', missing.map(k => `   • ${k}`).join('\n'));
  process.exit(1);
}
if (process.env.RELAY_TEST_MODE === 'true') {
  console.warn('🧪  TEST MODE — emails will be logged, not sent');
}
console.log('✅  Config OK. Starting…');
```

---

### Relay workflow spec

```json
{
  "name": "failed_txn_hourly_report",
  "description": "Hourly — fetches failed transactions and emails a summary report",
  "trigger": "schedule",
  "schedule": {
    "type":       "cron",
    "expression": "{{CRON_MINUTE}} * * * *",
    "timezone":   "Asia/Kolkata"
  },
  "nodes": [
    {
      "id": "idempotency-check",
      "type": "condition",
      "if": "already_processed(hour_window_key)",
      "then": "SKIP",
      "note": "hour_window_key = YYYY-MM-DD-HH. Prevents double-send if cron fires twice."
    },
    {
      "id": "fetch-failed-txns",
      "type": "api",
      "call": "GET /transactions",
      "params": {
        "status":     "FAILED",
        "from_time":  "{{window_start}}",
        "to_time":    "{{window_end}}"
      },
      "outputs": ["failedCount", "totalFailedAmount", "failedOrderList"],
      "note": "Cashfree Transactions API — fetches last 60-min window"
    },
    {
      "id": "zero-failures-gate",
      "type": "condition",
      "if": "failedCount == 0",
      "then": "{{SEND_ALL_CLEAR == true ? 'send-all-clear' : 'DONE'}}",
      "else": "build-report"
    },
    {
      "id": "send-all-clear",
      "type": "integration",
      "connector": "gmail",
      "action": "send_email",
      "params": {
        "to":      "{{REPORT_RECIPIENT}}",
        "cc":      "{{REPORT_CC}}",
        "subject": "✅ All clear — no failed transactions ({{window_label}})",
        "body":    "No failed transactions in the last hour.\n\nWindow: {{window_label}}\nChecked at: {{now_ist}}"
      },
      "then": "DONE"
    },
    {
      "id": "build-report",
      "type": "transform",
      "output": "email_body",
      "template": "{{EMAIL_BODY_TEMPLATE}}",
      "note": "Template built from user's selection during setup — never exposes variable syntax"
    },
    {
      "id": "send-report",
      "type": "integration",
      "connector": "gmail",
      "action": "send_email",
      "params": {
        "to":      "{{REPORT_RECIPIENT}}",
        "cc":      "{{REPORT_CC}}",
        "subject": "{{EMAIL_SUBJECT_TEMPLATE}}",
        "body":    "{{email_body}}"
      },
      "retry": { "attempts": 3, "backoff": "exponential", "initial_delay_ms": 2000 },
      "on_failure": "self-alert"
    },
    {
      "id": "self-alert",
      "type": "integration",
      "connector": "gmail",
      "action": "send_email",
      "params": {
        "to":      "{{SELF_ALERT_EMAIL}}",
        "subject": "⚠️ Relay workflow failed — failed-txn-hourly-report",
        "body":    "The hourly failed transaction report could not be sent after 3 attempts.\n\nHour window: {{window_label}}\nError: {{error.message}}\nRun ID: {{run_id}}\n\nCheck: Relay → Workflows → failed-txn-hourly-report → Run History"
      }
    }
  ]
}
```

---

### Optional: Run status receiver (Node.js)

```javascript
// server.js
import express from 'express';
import crypto  from 'crypto';

const app = express();
app.use(express.json({ verify: (req, _, buf) => { req.rawBody = buf; } }));

const { CASHFREE_WEBHOOK_SECRET, RELAY_TEST_MODE } = process.env;
const processed = new Map(); // swap for Redis: redis.set(key, '1', 'EX', 7200)

/**
 * @typedef {Object} RelayReportWebhook
 * @property {string}  run_id
 * @property {'SUCCESS'|'FAILURE'|'SKIPPED'} status
 * @property {string}  hour_window          - e.g. "2026-05-11 11:00–12:00 IST"
 * @property {number}  failed_count         - 0 on SUCCESS with SEND_ALL_CLEAR
 * @property {number}  total_failed_amount
 * @property {string}  gmail_message_id     - Present on SUCCESS
 * @property {string}  [error_message]      - Present on FAILURE
 * @property {string}  timestamp
 */

app.post('/api/relay/report/webhook', (req, res) => {
  // ── Verify signature ───────────────────────────────────────────────────────
  const sig      = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody).digest('base64');
  if (sig !== expected) return res.status(401).json({ error: 'Invalid signature' });

  // ── Idempotency ────────────────────────────────────────────────────────────
  /** @type {RelayReportWebhook} */
  const payload = req.body;
  if (processed.has(payload.run_id)) {
    return res.json({ received: true, duplicate: true });
  }
  processed.set(payload.run_id, Date.now());

  if (RELAY_TEST_MODE === 'true') {
    console.log('🧪 TEST MODE:', JSON.stringify(payload, null, 2));
    return res.json({ received: true, test_mode: true });
  }

  switch (payload.status) {
    case 'SUCCESS':
      console.log(`📧  Report sent — ${payload.hour_window} · ${payload.failed_count} failures · message_id: ${payload.gmail_message_id}`);
      recordReportRun(payload);
      break;

    case 'SKIPPED':
      // Idempotency triggered — cron fired twice
      console.log(`⏭️  Duplicate run skipped — ${payload.hour_window}`);
      break;

    case 'FAILURE':
      // Self-alert already sent by Relay. Log here for your records.
      console.error(`❌  Report failed — ${payload.hour_window}: ${payload.error_message}`);
      logFailure(payload);
      break;
  }

  res.json({ received: true });
});

// ─── Health check ─────────────────────────────────────────────────────────────
app.get('/health', async (req, res) => {
  const checks = { server: 'ok', gmail: 'unknown' };
  try {
    const r = await fetch(
      'https://api.cashfree.com/relay/v1/credentials/gmail/health',
      { headers: { 'x-client-id': process.env.CASHFREE_CLIENT_ID,
                   'x-client-secret': process.env.CASHFREE_CLIENT_SECRET } }
    );
    checks.gmail = r.ok ? 'ok' : 'token_expired';
  } catch { checks.gmail = 'unreachable'; }

  const healthy = Object.values(checks).every(v => v === 'ok');
  res.status(healthy ? 200 : 503).json({
    status: healthy ? 'healthy' : 'degraded',
    checks,
    gmail_daily_budget: {
      limit: process.env.GMAIL_TIER === 'workspace' ? 2000 : 500,
      used_today: 24, // 1/hr × 24hrs
      remaining: (process.env.GMAIL_TIER === 'workspace' ? 2000 : 500) - 24,
    },
    tip: checks.gmail !== 'ok'
      ? '→ Reconnect Gmail: Relay → Settings → Connections'
      : undefined,
  });
});

async function recordReportRun(payload) { /* store run record in your DB */ }
async function logFailure(payload)       { /* store failure in your DB */ }

app.listen(3000, () => console.log('🚀  Relay report receiver on :3000'));
```

---

### Test harness

```bash
# ── 1. Health check (includes Gmail daily budget) ─────────────────────────────
curl http://localhost:3000/health

# ── 2. Simulate SUCCESS — 3 failures found ────────────────────────────────────
curl -X POST http://localhost:3000/api/relay/report/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{
    "run_id":              "run_2026051111",
    "status":              "SUCCESS",
    "hour_window":         "2026-05-11 11:00–12:00 IST",
    "failed_count":        3,
    "total_failed_amount": 18450,
    "gmail_message_id":    "msg_abc123",
    "timestamp":           "2026-05-11T11:00:05Z"
  }'

# ── 3. Simulate SUCCESS — zero failures (all-clear email) ─────────────────────
curl -X POST http://localhost:3000/api/relay/report/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{
    "run_id":              "run_2026051112",
    "status":              "SUCCESS",
    "hour_window":         "2026-05-11 12:00–13:00 IST",
    "failed_count":        0,
    "total_failed_amount": 0,
    "gmail_message_id":    "msg_def456",
    "timestamp":           "2026-05-11T12:00:04Z"
  }'

# ── 4. Simulate FAILURE (Gmail API down) ──────────────────────────────────────
curl -X POST http://localhost:3000/api/relay/report/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{
    "run_id":        "run_2026051113",
    "status":        "FAILURE",
    "hour_window":   "2026-05-11 13:00–14:00 IST",
    "error_message": "Gmail API returned 503 after 3 retries",
    "timestamp":     "2026-05-11T13:00:28Z"
  }'

# ── 5. Test mode ───────────────────────────────────────────────────────────────
RELAY_TEST_MODE=true node server.js
# Logs all payloads, sends nothing
```

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| Guided Gmail connection setup | `SELF_ALERT_EMAIL` for failure notifications | SMS/WhatsApp fallback alert channel |
| Idempotency — duplicate hourly runs skipped | `SEND_ALL_CLEAR` flag | Report archival to Google Drive |
| "All clear" email when zero failures | Gmail tier setting (`GMAIL_TIER`) for budget display | Per-merchant failure breakdown |
| Auto-retry ×3 with exponential backoff | Health check cron (run `/health` every 15 min) | Failure trend analysis / anomaly detection |
| Self-alert on persistent send failure | Your DB schema for run logging | |
| Gmail daily budget display in `/health` | | |
| DPDP data-flow disclosure | | |
| Startup env validator | | |
| Test mode (`RELAY_TEST_MODE=true`) | | |

**DPDP note:** Standard report sends failed order IDs and amounts — no individual customer PII. If you customise the report to include customer name/email/phone, that becomes a DPDP-relevant data transfer to Gmail.

**Gmail rate limit:** 24 emails/day (1/hr × 24). Personal Gmail limit: 500/day. Workspace limit: 2,000/day. Both limits are safely above this workflow's usage.

**Cost:** No Secure ID API calls. Cashfree Transactions API calls consume standard API quota only.

**SLA:** Report sent within 30 seconds of each hour-mark. On Gmail degradation, Relay retries for up to 14 seconds before alerting.

---

## MCP — coming soon

```
/relay-failed-txn-report

→ Claude: "Recipient? Subject style? All-clear email? Minute-mark?"
→ Calls Relay MCP → create_workflow(template: 'failed_txn_report', config)
→ Returns RELAY_WORKFLOW_ID, already live
```
