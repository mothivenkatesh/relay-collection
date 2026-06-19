---
name: relay-daily-txn-sheets
description: Cashfree Relay workflow — every day at a chosen time, appends a transaction summary row to Google Sheets. Date-keyed idempotency (no duplicate rows), column header auto-creation, sample row preview with realistic numbers, spreadsheet-not-found guard, DPDP-disclosed, failure self-alert, test harness. ~₹0 per run.
metadata:
  kind: workflow
  category: reporting
  version: "2.0.0"
  tags: [transactions, google-sheets, daily-report, summary, automation]
  author: Cashfree Relay Team
  trigger_config:
    auto_trigger: true
    keywords:
      - "daily transaction summary google sheets"
      - "daily transaction report sheets"
      - "log transactions to google sheets daily"
      - "daily sheets transaction summary"
    intent_patterns:
      - "(?:daily|each day).*(?:transaction|payment).*(?:summary|report).*(?:to|in).*(?:google sheets|spreadsheet)"
      - "(?:create|set up|build).*(?:daily|recurring).*(?:transaction|payment).*(?:google sheets|spreadsheet)"
    confidence_threshold: 0.75
user-invocable: true
triggers:
  - /relay-daily-txn-sheets
  - daily transaction sheets
  - transaction summary google sheets
  - daily payment report spreadsheet
tools:
  - Read/Write
---

# Daily Transaction Summary → Google Sheets

> Runs once a day at your chosen time · Appends one summary row to your Google Sheet · Date-keyed idempotency — reruns never add duplicate rows · Column headers auto-created on first run · Realistic sample row in the preview · ~₹0 per run

---

## What gets built

```
Every day at HH:MM IST
        │
        ▼
  Fetch today's transaction summary from Cashfree
        │
        ▼
  Idempotency check — row for today already exists?
        │ no            │ yes
        ▼               ▼
  Build summary row   SKIP (no duplicate)
        │
        ▼
  Check column headers exist in sheet
        │ missing       │ present
        ▼               ▼
  Create header row  Continue
        │
        ▼
  Google Sheets → Append row
        │
        ├── SUCCESS → log run
        └── FAILURE → retry ×3 → self-alert
```

---

## Enterprise governance

| Control | What Relay handles | Your responsibility |
|---|---|---|
| **Idempotency** | Row keyed on `YYYY-MM-DD` — if the cron misfires and runs twice, the second run detects the existing row and skips | No action needed — built into the workflow |
| **Column header bootstrap** | On the very first run, Relay checks if headers exist. If missing, it inserts them automatically before appending data | Ensure the sheet tab is empty or already has matching headers |
| **Spreadsheet-not-found guard** | If the spreadsheet name is not found in the connected Google Drive, Relay fails gracefully and sends a self-alert with instructions | Verify spreadsheet name matches exactly, including case |
| **Failure recovery** | Auto-retry ×3 with exponential backoff; failure triggers self-alert email | Set `SELF_ALERT_EMAIL` |
| **Google Sheets rate limit** | Sheets API: 300 requests/min — this workflow makes 2–4 requests/day, zero risk | Not a concern at this usage level |
| **Data sent to Google Sheets** | Aggregated daily totals — date, counts, amounts · No individual customer records in standard config | If you add per-customer rows, that becomes a DPDP-relevant transfer |
| **DPDP** | Aggregated data (not PII) in standard config | If customised to include customer names/emails, document in Privacy Policy |
| **Audit trail** | Relay logs every run with status, row data hash — 90-day retention | The Google Sheet itself is your primary audit record; back it up |
| **OAuth health** | Relay auto-refreshes Sheets token | Re-authorise if token is manually revoked |
| **Timezone** | Relay runs cron in UTC; configured in IST by default | Explicitly state timezone if different — Relay converts |

---

## Guided setup — business operators

### Step 1 — Check Google Sheets connection

Call `mcp__wfcd-mcp__list_credentials` with `node_name: "google-sheets"`.

**If no connection found:**

---
Google Sheets isn't connected yet. Here's how — 30 seconds:

1. Go to **Relay → Settings → Connections**
2. Click **+ Add Connection**
3. Choose **Google Sheets**
4. Sign in — Relay only gets permission to *edit* sheets you specify, nothing else
5. Type **"done"** when you're back
---

**If one found** — confirm:
> Found **[account name]**. I'll use this — good?

**If multiple** — list and pick:
> Which Google account has the spreadsheet?
> 1. [Account 1]
> 2. [Account 2]

---

### Step 2 — Configuration (one question at a time)

**Q1 — Which spreadsheet?**
> What's the name of the Google Sheet you want to update?
>
> Type the exact name — e.g. **"Daily Revenue 2026"** or **"Cashfree Reports"**
>
> *(The sheet must already exist in your Google Drive. I'll connect by name.)*

*On not-found: "Couldn't find '[name]'. Double-check the name or share the direct link."*

---

**Q2 — Which tab?**
> Which tab inside that sheet should I add rows to?
>
> Type the tab name — or say **"first tab"** if you're not sure.

*"first tab" → `Sheet1`; otherwise use as-is*

---

**Q3 — What time?**
> What time each day should this run?
>
> Type a time like **"9 AM"**, **"11 PM"**, **"midnight"** — and your timezone if it's not IST.
>
> Tip: most teams run it overnight (e.g. **11:30 PM IST**) so the full day's data is in before anyone checks in the morning.

---

**Q4 — What columns?**
> What should each row include?
>
> Here's the **standard daily summary** — type **"standard"** to use it:
>
> | Column | What it shows |
> |---|---|
> | Date | The date covered by this row |
> | Total Transactions | All payments processed (success + failed) |
> | Successful Payments | Count of successful transactions |
> | Failed Payments | Count of failed transactions |
> | Success Rate | % of payments that succeeded |
> | Total Amount (₹) | Total value of all transactions |
> | Success Amount (₹) | Value of successful payments only |
>
> Or tell me which columns to add, remove, or rename.

---

**Q6 — Workflow name** (last):
> What should I call this workflow?
> I'll use **"daily-transaction-summary-sheets"** unless you'd like something else.

---

### Step 3 — Preview

> Here's what I'm setting up:
>
> | | |
> |---|---|
> | **Trigger** | Every day at [time] IST |
> | **Spreadsheet** | [name] |
> | **Tab** | [tab] |
> | **Columns** | [list] |
> | **Workflow name** | [name] |
>
> **Here's what each row will look like** (example numbers):
>
> | Date | Total Txns | Successful | Failed | Success Rate | Total (₹) | Success (₹) |
> |---|---|---|---|---|---|---|
> | 2026-05-11 | 284 | 271 | 13 | 95.4% | ₹9,42,800 | ₹9,08,350 |
>
> *(Actual numbers come from your Cashfree account)*
>
> **First run:** Relay will check if your sheet has headers. If not, it adds them automatically before the first data row.
>
> Ready? Type **yes** to activate.

---

### Step 4 — Create

1. Call `mcp__wfcd-mcp__create_workflow` → save `workflow_id`
2. Call `mcp__wfcd-mcp__update_workflow`

---

### Step 5 — Success message

> ✅ **Your daily summary is live.**
>
> **First row appears at:** [next scheduled run time in user's timezone]
>
> **What to expect on first run:**
> · Relay checks for column headers — adds them if missing
> · First data row appended immediately after
>
> **If a row doesn't appear:**
> · Relay → Workflows → [name] → Run History for the error
> · Most common causes: spreadsheet name changed, or Google Sheets connection expired
>
> **To change the schedule or columns:** Relay → Workflows → [name] → Edit
>
> **To pause:** Toggle the workflow off.

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

# ─── Sheet config ──────────────────────────────────────────────────────────────
SPREADSHEET_NAME=                      # exact Google Sheets name
SHEET_TAB_NAME=Sheet1                  # tab name within the spreadsheet
REPORT_SCHEDULE_TIME=23:30             # 24-hr format, IST
REPORT_TIMEZONE=Asia/Kolkata

# ─── Observability ─────────────────────────────────────────────────────────────
SELF_ALERT_EMAIL=
RELAY_TEST_MODE=false
```

**Startup validator:**

```javascript
// startup.js
const REQUIRED = [
  'CASHFREE_CLIENT_ID', 'CASHFREE_CLIENT_SECRET', 'CASHFREE_WEBHOOK_SECRET',
  'RELAY_WORKFLOW_ID', 'BASE_URL', 'SPREADSHEET_NAME',
];
const missing = REQUIRED.filter(k => !process.env[k]);
if (missing.length) {
  console.error('❌  Missing required env vars:\n', missing.map(k => `   • ${k}`).join('\n'));
  process.exit(1);
}
// Validate schedule time format
const timeRegex = /^([01]\d|2[0-3]):([0-5]\d)$/;
if (!timeRegex.test(process.env.REPORT_SCHEDULE_TIME || '23:30')) {
  console.error('❌  REPORT_SCHEDULE_TIME must be in HH:MM format (e.g. 23:30)');
  process.exit(1);
}
console.log(`✅  Config OK. Daily report scheduled at ${process.env.REPORT_SCHEDULE_TIME} IST.`);
```

---

### Relay workflow spec

```json
{
  "name": "daily_txn_summary_sheets",
  "description": "Daily — appends transaction summary row to Google Sheets",
  "trigger": "schedule",
  "schedule": {
    "type":       "cron",
    "expression": "{{CRON_MINUTE}} {{CRON_HOUR}} * * *",
    "timezone":   "{{REPORT_TIMEZONE}}"
  },
  "nodes": [
    {
      "id": "fetch-summary",
      "type": "api",
      "call": "GET /transactions/summary",
      "params": {
        "date":     "{{today}}",
        "timezone": "{{REPORT_TIMEZONE}}"
      },
      "outputs": [
        "totalCount", "successCount", "failedCount",
        "successRate", "totalAmount", "successAmount"
      ]
    },
    {
      "id": "idempotency-check",
      "type": "integration",
      "connector": "google-sheets",
      "action": "find_row",
      "params": {
        "spreadsheet_name": "{{SPREADSHEET_NAME}}",
        "sheet_tab":        "{{SHEET_TAB_NAME}}",
        "search_column":    "Date",
        "search_value":     "{{today_formatted}}"
      },
      "on_found":     "SKIP",
      "on_not_found": "header-check",
      "note": "If today's row already exists, skip. Prevents duplicate rows on cron misfire."
    },
    {
      "id": "header-check",
      "type": "integration",
      "connector": "google-sheets",
      "action": "check_headers",
      "params": {
        "spreadsheet_name": "{{SPREADSHEET_NAME}}",
        "sheet_tab":        "{{SHEET_TAB_NAME}}",
        "expected_headers": "{{COLUMN_HEADERS}}"
      },
      "on_missing": "create-headers",
      "on_present": "append-row"
    },
    {
      "id": "create-headers",
      "type": "integration",
      "connector": "google-sheets",
      "action": "append_row",
      "params": {
        "spreadsheet_name": "{{SPREADSHEET_NAME}}",
        "sheet_tab":        "{{SHEET_TAB_NAME}}",
        "values":           "{{COLUMN_HEADERS}}"
      },
      "then": "append-row",
      "note": "Inserts header row on first-ever run. Subsequent runs skip this node."
    },
    {
      "id": "append-row",
      "type": "integration",
      "connector": "google-sheets",
      "action": "append_row",
      "params": {
        "spreadsheet_name": "{{SPREADSHEET_NAME}}",
        "sheet_tab":        "{{SHEET_TAB_NAME}}",
        "values": [
          "{{today_formatted}}",
          "{{totalCount}}",
          "{{successCount}}",
          "{{failedCount}}",
          "{{successRate}}%",
          "{{totalAmount}}",
          "{{successAmount}}"
        ]
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
        "subject": "⚠️ Relay workflow failed — daily-txn-summary-sheets",
        "body":    "Daily transaction summary row for {{today_formatted}} could not be written to Google Sheets after 3 attempts.\n\nSpreadsheet: {{SPREADSHEET_NAME}}\nTab: {{SHEET_TAB_NAME}}\nError: {{error.message}}\nRun ID: {{run_id}}\n\nCommon causes:\n• Spreadsheet was renamed or moved\n• Google Sheets connection expired\n\nFix: Relay → Settings → Connections → Reconnect Google Sheets"
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
const processed = new Map(); // swap for Redis in prod

/**
 * @typedef {Object} RelaySheetsWebhook
 * @property {string}  run_id
 * @property {'SUCCESS'|'FAILURE'|'SKIPPED'} status
 * @property {string}  date               - YYYY-MM-DD
 * @property {number}  total_count
 * @property {number}  success_count
 * @property {number}  failed_count
 * @property {string}  success_rate       - e.g. "95.4%"
 * @property {number}  total_amount
 * @property {number}  success_amount
 * @property {string}  spreadsheet_row    - A1 notation of the appended row (on SUCCESS)
 * @property {string}  [error_message]
 * @property {string}  timestamp
 */

app.post('/api/relay/sheets/webhook', (req, res) => {
  const sig      = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody).digest('base64');
  if (sig !== expected) return res.status(401).json({ error: 'Invalid signature' });

  /** @type {RelaySheetsWebhook} */
  const payload = req.body;
  if (processed.has(payload.run_id)) return res.json({ received: true, duplicate: true });
  processed.set(payload.run_id, Date.now());

  if (RELAY_TEST_MODE === 'true') {
    console.log('🧪 TEST MODE:', JSON.stringify(payload, null, 2));
    return res.json({ received: true, test_mode: true });
  }

  switch (payload.status) {
    case 'SUCCESS':
      console.log(`📊  Row appended — ${payload.date} · ${payload.total_count} txns · ₹${payload.total_amount} · row: ${payload.spreadsheet_row}`);
      recordDailySummary(payload);
      break;
    case 'SKIPPED':
      console.log(`⏭️  Duplicate skipped — row for ${payload.date} already exists`);
      break;
    case 'FAILURE':
      console.error(`❌  Sheets write failed — ${payload.date}: ${payload.error_message}`);
      logFailure(payload);
      break;
  }

  res.json({ received: true });
});

// ─── Health check ─────────────────────────────────────────────────────────────
app.get('/health', async (req, res) => {
  const checks = { server: 'ok', google_sheets: 'unknown' };
  try {
    const r = await fetch(
      'https://api.cashfree.com/relay/v1/credentials/google-sheets/health',
      { headers: { 'x-client-id': process.env.CASHFREE_CLIENT_ID,
                   'x-client-secret': process.env.CASHFREE_CLIENT_SECRET } }
    );
    checks.google_sheets = r.ok ? 'ok' : 'token_expired';
  } catch { checks.google_sheets = 'unreachable'; }

  const healthy = Object.values(checks).every(v => v === 'ok');
  res.status(healthy ? 200 : 503).json({
    status: healthy ? 'healthy' : 'degraded',
    checks,
    next_scheduled_run: getNextRunTime(process.env.REPORT_SCHEDULE_TIME, process.env.REPORT_TIMEZONE),
    tip: checks.google_sheets !== 'ok'
      ? '→ Reconnect Sheets: Relay → Settings → Connections'
      : undefined,
  });
});

function getNextRunTime(scheduledTime, timezone) {
  // Returns ISO timestamp of next scheduled run — useful for monitoring
  const [h, m] = (scheduledTime || '23:30').split(':').map(Number);
  const now = new Date();
  const next = new Date(now);
  next.setHours(h, m, 0, 0);
  if (next <= now) next.setDate(next.getDate() + 1);
  return next.toISOString();
}

async function recordDailySummary(payload) { /* store in your DB */ }
async function logFailure(payload)          { /* store in your DB */ }

app.listen(3000, () => console.log('🚀  Relay sheets receiver on :3000'));
```

---

### Test harness

```bash
# ── 1. Health check (shows next scheduled run time) ───────────────────────────
curl http://localhost:3000/health

# ── 2. Simulate SUCCESS ───────────────────────────────────────────────────────
curl -X POST http://localhost:3000/api/relay/sheets/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{
    "run_id":          "run_20260511",
    "status":          "SUCCESS",
    "date":            "2026-05-11",
    "total_count":     284,
    "success_count":   271,
    "failed_count":    13,
    "success_rate":    "95.4%",
    "total_amount":    942800,
    "success_amount":  908350,
    "spreadsheet_row": "A15:G15",
    "timestamp":       "2026-05-11T18:00:03Z"
  }'

# ── 3. Simulate SKIPPED (duplicate — cron fired twice) ────────────────────────
curl -X POST http://localhost:3000/api/relay/sheets/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{
    "run_id":    "run_20260511_duplicate",
    "status":    "SKIPPED",
    "date":      "2026-05-11",
    "timestamp": "2026-05-11T18:00:31Z"
  }'

# ── 4. Simulate FAILURE (spreadsheet renamed) ─────────────────────────────────
curl -X POST http://localhost:3000/api/relay/sheets/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{
    "run_id":        "run_20260512",
    "status":        "FAILURE",
    "date":          "2026-05-12",
    "error_message": "Spreadsheet '\''Daily Revenue 2026'\'' not found in Google Drive",
    "timestamp":     "2026-05-12T18:00:45Z"
  }'

# ── 5. Test mode ───────────────────────────────────────────────────────────────
RELAY_TEST_MODE=true node server.js
```

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| Guided Google Sheets connection setup | `SELF_ALERT_EMAIL` for failure notifications | Per-merchant breakdown rows |
| Date-keyed idempotency — duplicate rows never appended | Health check cron (run `/health` every 15 min) | Chart / graph auto-update |
| Column header auto-creation on first run | Your DB schema for `recordDailySummary()` | Multi-sheet fan-out |
| Spreadsheet-not-found guard with helpful error | | Historical backfill for past dates |
| Auto-retry ×3 with exponential backoff | | |
| Self-alert with diagnosis hints on failure | | |
| `getNextRunTime()` in health check | | |
| DPDP data-flow disclosure | | |
| Startup env validator with schedule time format check | | |
| Test mode (`RELAY_TEST_MODE=true`) | | |

**DPDP note:** Standard columns (date, counts, amounts) are aggregate data — no individual customer PII. Adding customer-level data changes the DPDP classification of this workflow.

**Google Sheets rate limit:** 300 API requests/minute. This workflow makes 2–4 requests/day. Zero risk.

**Cost:** No Secure ID API calls. Cashfree Transactions Summary API calls consume standard quota only.

**SLA:** Row appended within 30 seconds of the scheduled time. On Google Sheets API degradation, Relay retries for up to 14 seconds before alerting.

---

## MCP — coming soon

```
/relay-daily-txn-sheets

→ Claude: "Spreadsheet name? Tab? Time? Standard columns or custom?"
→ Calls Relay MCP → create_workflow(template: 'daily_txn_sheets', config)
→ Returns RELAY_WORKFLOW_ID, already live
```
