---
name: relay-payment-calendar
description: Cashfree Relay workflow — every successful payment automatically creates a Google Calendar event. Guided non-dev setup, idempotent event creation (no duplicates on webhook retries), OAuth health check, DPDP data-flow disclosure, failure self-alert, test harness with realistic payloads. ~₹0 per run (no Secure ID APIs consumed).
metadata:
  kind: workflow
  category: integration
  version: "2.0.0"
  tags: [payment, calendar, automation, google-calendar]
  author: Cashfree Relay Team
  trigger_config:
    auto_trigger: true
    keywords:
      - "payment success calendar"
      - "create calendar event on payment"
      - "add payment to calendar"
      - "calendar event when payment succeeds"
    intent_patterns:
      - "(?:create|set up|make|build).*(?:workflow|automation).*(?:payment|order).*(?:calendar|event)"
      - "(?:when|on).*(?:payment|order).*(?:success|complete).*(?:add|create).*(?:calendar|event)"
    confidence_threshold: 0.75
user-invocable: true
triggers:
  - /relay-payment-calendar
  - payment calendar workflow
  - calendar event on payment
  - google calendar payment automation
tools:
  - Read/Write
---

# Payment Success → Google Calendar Event

> Every successful payment on your Cashfree account creates a Google Calendar event automatically · Idempotent — duplicate webhooks never create duplicate events · OAuth health-checked · DPDP-disclosed · ~0 additional cost per run

---

## What gets built

```
Cashfree payment succeeds
        │
        ▼
  Relay payment_success trigger
        │
        ▼
  Idempotency check ──── already processed? ──→ SKIP (no duplicate)
        │ first time
        ▼
  Build event title (from payment data)
        │
        ▼
  Google Calendar → Create Event
        │
        ├── SUCCESS → log + done
        └── FAILURE → retry ×3 (exponential backoff) → self-alert email
```

---

## Enterprise governance

| Control | What Relay handles | Your responsibility |
|---|---|---|
| **Idempotency** | `payment_id` used as dedup key — retried webhooks skip silently | Pass unique `payment_id` in trigger payload |
| **Failure recovery** | Auto-retry ×3 with exponential backoff (2s → 4s → 8s); failure triggers self-alert | Monitor self-alert inbox; resolve within SLA |
| **OAuth health** | Relay auto-refreshes Google tokens before expiry | Re-authorise if token is manually revoked in Google account |
| **Data sent to Google** | Customer name · Payment amount · Order ID · Payment timestamp | Ensure your Google Workspace DPA covers this under DPDP Act 2023 |
| **DPDP — data flow** | Payment data leaves Cashfree infrastructure and enters Google Calendar | If customers are Indian residents, document this transfer in your Privacy Policy |
| **Audit trail** | Relay logs every run with status, timestamp, payload hash — 90-day retention | Export logs to your SIEM for longer retention |
| **Encryption** | TLS 1.3 in transit to Google APIs · Cashfree data at rest AES-256 | Google Calendar data governed by Google's security posture |
| **Token scope** | Minimal: `calendar.events` only — no read access to existing events | Do not grant broader Google OAuth scopes |
| **Run budget** | No Secure ID API calls — cost is Google API quota only | Google Calendar API: 1M requests/day; effectively unlimited for this use case |

---

## Guided setup — business operators

### Step 1 — Check Google Calendar connection

Call `mcp__wfcd-mcp__list_credentials` with `node_name: "google-calendar"`.

**If no connection found:**

---
Your Google Calendar isn't connected yet. Let's fix that — takes 30 seconds:

1. Go to **Relay → Settings → Connections**
2. Click **+ Add Connection**
3. Choose **Google Calendar**
4. Sign in and allow access — Relay only gets permission to *create* events, nothing else
5. Come back and type **"done"** — I'll pick up from here
---

**If one connection found** — confirm:
> Found **[account name]** connected. I'll use this — good?

**If multiple** — list and pick:
> Which Google Calendar account?
> 1. [Account 1]
> 2. [Account 2]
> (type the number)

---

### Step 2 — Configuration (one question at a time)

**Q1 — Which calendar?**
> Which calendar should payment events go into?
>
> · Type **"main"** for your primary calendar
> · Or type a calendar email address for a shared team calendar

*"main" → `primary`; email address → used as calendarId*

---

**Q2 — Event title?**
> What should each calendar event be called?
>
> 1. **Payment received — ₹[Amount]**
> 2. **Payment from [Customer Name]**
> 3. **Order [Order ID] paid — ₹[Amount]**
> 4. Write your own

*Internally maps to template variables — never shown to user.*

---

**Q3 — Event time?**
> When should the event be placed on the calendar?
>
> · **"When it happens"** — event created at the exact time of payment *(recommended)*
> · A fixed time like "10 AM IST" — all events placed at that time regardless of when payment comes in

---

**Q4 — Reminders?**
> Should Google Calendar send a reminder for this event?
>
> 1. **Yes — notify everyone** (email + popup)
> 2. **No reminders** — just silently add it
> 3. Only notify people outside my organisation

---

**Q5 — Workflow name** (last, smart default):
> What should I call this workflow?
> I'll use **"payment-success-calendar"** unless you want something else.

---

### Step 3 — Preview before creating

> Here's what I'm setting up:
>
> | | |
> |---|---|
> | **Trigger** | Every successful payment on your Cashfree account |
> | **Calendar** | [selected] |
> | **Event title** | [plain-English description] |
> | **Event time** | [at payment time / fixed time] |
> | **Reminders** | [selection] |
> | **Workflow name** | [name] |
>
> Ready? Type **yes** to go live, or tell me what to change.

*Never proceed without explicit yes.*

---

### Step 4 — Create

1. Call `mcp__wfcd-mcp__create_workflow` → save `workflow_id`
2. Call `mcp__wfcd-mcp__update_workflow` with `workflow_id`

---

### Step 5 — Success message

> ✅ **Live. Your payment calendar is running.**
>
> Every successful payment will now appear in your Google Calendar automatically.
>
> **Test it:** Make a sandbox payment → check your calendar within 10 seconds.
>
> **If an event doesn't appear:**
> · Check Relay → Workflows → [name] → Run History for errors
> · Most common cause: Google Calendar connection was revoked — go to Settings → Connections to reconnect
>
> **To pause:** Toggle the workflow off in Relay → Workflows.

---

## Developer reference

### Environment variables

```env
# ─── Cashfree ──────────────────────────────────────────────────────────────────
CASHFREE_CLIENT_ID=                    # from sandbox.cashfree.com → Developers
CASHFREE_CLIENT_SECRET=
CASHFREE_WEBHOOK_SECRET=               # Dashboard → Webhooks → Signing Secret
CASHFREE_BASE_URL=https://sandbox.cashfree.com  # swap to api.cashfree.com for prod

# ─── Relay ─────────────────────────────────────────────────────────────────────
RELAY_WORKFLOW_ID=                     # returned after create_workflow
BASE_URL=http://localhost:3000         # your server's public URL

# ─── Observability ─────────────────────────────────────────────────────────────
SELF_ALERT_EMAIL=                      # where to send failure alerts (ops inbox)
RELAY_TEST_MODE=false                  # set true to log instead of creating events
```

**Startup validator** — paste this at the top of your server before any routes:

```javascript
// startup.js — run this before app.listen()
const REQUIRED = [
  'CASHFREE_CLIENT_ID', 'CASHFREE_CLIENT_SECRET',
  'CASHFREE_WEBHOOK_SECRET', 'RELAY_WORKFLOW_ID', 'BASE_URL',
];
const missing = REQUIRED.filter(k => !process.env[k]);
if (missing.length) {
  console.error('❌  Missing required env vars:\n', missing.map(k => `   • ${k}`).join('\n'));
  console.error('\n   Copy .env.example → .env and fill in the blanks.\n');
  process.exit(1);
}
console.log('✅  All env vars present. Starting server…');
```

---

### Relay workflow spec

```json
{
  "name": "payment_success_calendar",
  "description": "Creates a Google Calendar event on every successful Cashfree payment",
  "trigger": "payment_success",
  "nodes": [
    {
      "id": "idempotency-check",
      "type": "condition",
      "if": "already_processed(payment_id)",
      "then": "SKIP",
      "note": "Cashfree webhooks can fire 2–3× per payment. This gate ensures exactly-once event creation."
    },
    {
      "id": "build-title",
      "type": "transform",
      "output": "event_title",
      "template": "{{EVENT_TITLE_TEMPLATE}}",
      "note": "Template set at workflow creation — e.g. 'Payment received — ₹${orderAmount}'"
    },
    {
      "id": "create-calendar-event",
      "type": "integration",
      "connector": "google-calendar",
      "action": "create_event",
      "params": {
        "calendar_id":  "{{CALENDAR_ID}}",
        "title":        "{{event_title}}",
        "start":        "{{payment_timestamp}}",
        "end":          "{{payment_timestamp | add: '1h'}}",
        "description":  "Order ID: {{cfOrderId}}\nAmount: ₹{{orderAmount}}\nCustomer: {{customerName}}\nMethod: {{paymentMethod}}",
        "send_updates": "{{NOTIFICATION_SETTING}}"
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
        "subject": "⚠️ Relay workflow failed — payment-success-calendar",
        "body":    "Payment {{cfOrderId}} (₹{{orderAmount}}) could not be added to Google Calendar after 3 attempts.\n\nError: {{error.message}}\n\nRun ID: {{run_id}}\nTimestamp: {{timestamp}}\n\nCheck: Relay → Workflows → payment-success-calendar → Run History"
      },
      "note": "Self-alert fires only after all retries exhausted. Requires Gmail connector."
    }
  ]
}
```

---

### Optional: Relay notification receiver (Node.js)

Add this if you want your own system to record every calendar event created:

```javascript
// server.js
import express from 'express';
import crypto  from 'crypto';

const app = express();
app.use(express.json({ verify: (req, _, buf) => { req.rawBody = buf; } }));

const { CASHFREE_WEBHOOK_SECRET, RELAY_TEST_MODE } = process.env;

// ─── Idempotency store — swap Map for Redis in production ─────────────────────
// Redis: await redis.set(`relay:processed:${key}`, '1', 'EX', 86400)
const processed = new Map();

// ─── Types (JSDoc) ────────────────────────────────────────────────────────────
/**
 * @typedef {Object} RelayCalendarWebhook
 * @property {string} run_id           - Unique Relay run ID — use as idempotency key
 * @property {string} workflow_id
 * @property {'SUCCESS'|'FAILURE'|'SKIPPED'} status
 * @property {string} payment_id       - Cashfree payment ID
 * @property {string} cf_order_id      - Cashfree order ID
 * @property {number} order_amount     - Payment amount in INR
 * @property {string} customer_name
 * @property {string} calendar_event_id - Google Calendar event ID (on SUCCESS)
 * @property {string} [error_message]  - Present on FAILURE
 * @property {string} timestamp        - ISO 8601
 */

app.post('/api/relay/calendar/webhook', (req, res) => {
  // ── 1. Verify signature ────────────────────────────────────────────────────
  const sig      = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody)
    .digest('base64');
  if (sig !== expected) {
    console.warn('⚠️  Bad webhook signature — possible replay attack');
    return res.status(401).json({ error: 'Invalid signature' });
  }

  // ── 2. Idempotency ─────────────────────────────────────────────────────────
  /** @type {RelayCalendarWebhook} */
  const payload = req.body;
  const key     = payload.run_id;

  if (processed.has(key)) {
    console.log(`⏭️  Duplicate webhook ignored — run_id: ${key}`);
    return res.json({ received: true, duplicate: true });
  }
  processed.set(key, Date.now());

  // ── 3. Handle status ───────────────────────────────────────────────────────
  if (RELAY_TEST_MODE === 'true') {
    console.log('🧪 TEST MODE — would process:', JSON.stringify(payload, null, 2));
    return res.json({ received: true, test_mode: true });
  }

  switch (payload.status) {
    case 'SUCCESS':
      // ✅ Calendar event created — record in your system
      console.log(`📅  Event created — order ${payload.cf_order_id} · ₹${payload.order_amount} · event_id: ${payload.calendar_event_id}`);
      recordCalendarEvent(payload);
      break;

    case 'SKIPPED':
      // ⏭️  Duplicate payment webhook — Relay already deduplicated this
      console.log(`⏭️  Skipped duplicate — payment_id: ${payload.payment_id}`);
      break;

    case 'FAILURE':
      // ❌ All retries exhausted — self-alert already sent by Relay
      // Log here for your own records; do NOT retry from here (Relay handles retries)
      console.error(`❌  Calendar event failed — order ${payload.cf_order_id}: ${payload.error_message}`);
      logFailure(payload);
      break;
  }

  res.json({ received: true });
});

// ─── Health check — test Google Calendar connection is still live ─────────────
app.get('/health', async (req, res) => {
  const checks = {
    server:          'ok',
    env_vars:        'ok',
    google_calendar: 'unknown',
  };

  try {
    // Ping the Relay credentials endpoint to verify Google Calendar token is valid
    const r = await fetch(
      'https://api.cashfree.com/relay/v1/credentials/google-calendar/health',
      { headers: { 'x-client-id': process.env.CASHFREE_CLIENT_ID,
                   'x-client-secret': process.env.CASHFREE_CLIENT_SECRET } }
    );
    checks.google_calendar = r.ok ? 'ok' : 'token_expired';
  } catch {
    checks.google_calendar = 'unreachable';
  }

  const healthy = Object.values(checks).every(v => v === 'ok');
  res.status(healthy ? 200 : 503).json({
    status: healthy ? 'healthy' : 'degraded',
    checks,
    tip: checks.google_calendar !== 'ok'
      ? '→ Reconnect Google Calendar: Relay → Settings → Connections'
      : undefined,
  });
});

async function recordCalendarEvent(payload) { /* store in your DB */ }
async function logFailure(payload)           { /* store failure in your DB */ }

app.listen(3000, () => console.log('🚀  Relay calendar receiver on :3000'));
```

---

### Test harness

```bash
# ── 1. Health check ────────────────────────────────────────────────────────────
curl http://localhost:3000/health
# Expected: { "status": "healthy", "checks": { "server": "ok", "google_calendar": "ok" } }

# ── 2. Simulate SUCCESS ────────────────────────────────────────────────────────
curl -X POST http://localhost:3000/api/relay/calendar/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: $(echo -n '{"run_id":"run_001","status":"SUCCESS","payment_id":"pay_abc123","cf_order_id":"order_xyz","order_amount":4850,"customer_name":"Anjali Menon","calendar_event_id":"gcal_evnt_001","timestamp":"2026-05-11T09:32:00Z"}' | openssl dgst -sha256 -hmac "$CASHFREE_WEBHOOK_SECRET" -binary | base64)" \
  -d '{"run_id":"run_001","status":"SUCCESS","payment_id":"pay_abc123","cf_order_id":"order_xyz","order_amount":4850,"customer_name":"Anjali Menon","calendar_event_id":"gcal_evnt_001","timestamp":"2026-05-11T09:32:00Z"}'

# ── 3. Simulate duplicate (same run_id) — should return duplicate:true ─────────
curl -X POST http://localhost:3000/api/relay/calendar/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: $(echo -n '{"run_id":"run_001","status":"SUCCESS","payment_id":"pay_abc123","cf_order_id":"order_xyz","order_amount":4850,"customer_name":"Anjali Menon","calendar_event_id":"gcal_evnt_001","timestamp":"2026-05-11T09:32:00Z"}' | openssl dgst -sha256 -hmac "$CASHFREE_WEBHOOK_SECRET" -binary | base64)" \
  -d '{"run_id":"run_001","status":"SUCCESS","payment_id":"pay_abc123","cf_order_id":"order_xyz","order_amount":4850,"customer_name":"Anjali Menon","calendar_event_id":"gcal_evnt_001","timestamp":"2026-05-11T09:32:00Z"}'
# Expected: { "received": true, "duplicate": true }

# ── 4. Simulate FAILURE (all retries exhausted) ───────────────────────────────
curl -X POST http://localhost:3000/api/relay/calendar/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{"run_id":"run_002","status":"FAILURE","payment_id":"pay_def456","cf_order_id":"order_uvw","order_amount":12500,"error_message":"Google Calendar API returned 503","timestamp":"2026-05-11T09:45:00Z"}'

# ── 5. Test mode (no real processing) ─────────────────────────────────────────
RELAY_TEST_MODE=true node server.js
# All webhooks log to console, nothing written to DB
```

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| Guided Google Calendar connection setup | `SELF_ALERT_EMAIL` for failure notifications | Multi-calendar fan-out (one calendar per run) |
| Idempotency — duplicate webhooks silently skipped | Self-alert Gmail connector (for failure alerts) | Calendar event updates on refund/chargeback |
| Auto-retry ×3 with exponential backoff | Your DB schema for `recordCalendarEvent()` | Recurring event series |
| Self-alert email on persistent failure | Health check cron (run `/health` every 5 min) | Google Meet link generation |
| OAuth token auto-refresh (Relay-managed) | | |
| DPDP data-flow disclosure | | |
| Startup env validator | | |
| Test mode (`RELAY_TEST_MODE=true`) | | |
| Health check endpoint (`GET /health`) | | |

**DPDP note:** Customer name, order amount, and order ID leave Cashfree infrastructure and are written into Google Calendar. If your customers are Indian residents, document this third-party data transfer in your Privacy Policy under DPDP Act 2023.

**Cost:** No Secure ID API calls consumed. Google Calendar API quota: 1,000,000 requests/day — sufficient for all but the highest-volume merchants.

**SLA:** Calendar event created within 10 seconds of payment success in normal conditions. On Google API degradation, Relay retries for up to 14 seconds (2s + 4s + 8s) before alerting.

---

## MCP — coming soon

```
/relay-payment-calendar

→ Claude: "Which calendar? Event title format? Reminders?"
→ Calls Relay MCP → create_workflow(template: 'payment_calendar', config)
→ Returns RELAY_WORKFLOW_ID, already live
→ Outputs integration code above, pre-filled
```
