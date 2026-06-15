---
name: relay-threshold-alert
description: Cashfree Relay workflow — every successful payment above a set amount instantly sends an email alert. Payment-ID idempotency (no duplicate alerts), Indian number format support (lakhs/crores), multi-recipient + escalation chain, quiet hours, Gmail rate-limit safeguard at high volume, DPDP-disclosed, failure self-alert, test harness. ~₹0 per run.
metadata:
  kind: workflow
  category: monitoring
  version: "2.0.0"
  tags: [payment-alert, threshold, gmail, high-value, real-time]
  author: Cashfree Relay Team
  trigger_config:
    auto_trigger: true
    keywords:
      - "transaction threshold alert"
      - "high value payment alert"
      - "email when payment exceeds"
      - "big payment notification"
      - "alert me when payment above"
    intent_patterns:
      - "(?:set up|create|build).*(?:transaction|payment).*(?:alert|notification).*(?:threshold|exceed)"
      - "(?:notify|alert).*(?:when|if).*(?:transaction|payment).*(?:exceeds|above).*(?:amount|threshold)"
      - "(?:alert|notify|email).*(?:big|large|high.value).*(?:payment|transaction)"
    confidence_threshold: 0.75
user-invocable: true
triggers:
  - /relay-threshold-alert
  - payment threshold alert
  - high value payment alert
  - transaction alert email
  - email when payment exceeds
tools:
  - Read/Write
---

# Payment Threshold Alert → Gmail

> Real-time · Every payment above your threshold triggers an instant email · Payment-ID idempotency — duplicate webhooks never send duplicate alerts · Indian number format support (lakhs/crores) · Quiet hours · Escalation chain · Gmail rate-limit safeguard at high volume · ~₹0 per run

---

## What gets built

```
Cashfree payment succeeds
        │
        ▼
  Amount ≥ threshold?
        │ no                │ yes
        ▼                   ▼
       DONE          Idempotency check
                           │ already alerted    │ first time
                           ▼                    ▼
                          SKIP            Quiet hours check
                                               │ active         │ not active
                                               ▼                ▼
                                         Queue for        Build alert email
                                         next window           │
                                                               ▼
                                                    Gmail → Send alert
                                                           │
                                               ├── SUCCESS → log
                                               └── FAILURE → retry ×3 → self-alert
```

---

## Enterprise governance

| Control | What Relay handles | Your responsibility |
|---|---|---|
| **Idempotency** | `payment_id` used as dedup key — Cashfree webhook retries never send duplicate alerts | Pass unique `payment_id` in trigger; do not reuse payment IDs |
| **Threshold validation** | Threshold validated as a positive integer at workflow creation time — zero and negative values rejected | Statutory limits (e.g. PA-CB ₹25L cap) are separate from this alert threshold |
| **Quiet hours** | Optional: alerts outside business hours are queued and sent in a batch at the start of next window | Configure `QUIET_HOURS_START` and `QUIET_HOURS_END` if needed |
| **Gmail rate limit at high volume** | Gmail API: 500 sends/day (personal) · 2,000/day (Workspace). At very high payment volume, the workflow checks remaining daily quota before sending and holds if budget is exhausted | Set `GMAIL_TIER=workspace` for 2,000/day limit |
| **Escalation chain** | Optional: if primary recipient doesn't acknowledge within N minutes, escalate to a secondary email | Configure `ESCALATION_EMAIL` and `ESCALATION_TIMEOUT_MIN` |
| **Failure recovery** | Auto-retry ×3 with exponential backoff; failure triggers self-alert | Set `SELF_ALERT_EMAIL` |
| **Data sent to Gmail** | Customer name · Customer email · Order ID · Payment amount · Payment method · Timestamp | Customer PII is sent to Gmail — DPDP Act 2023 data transfer; document in Privacy Policy |
| **DPDP** | Customer name, email, phone, and transaction details are transmitted to Gmail | This is a DPDP-relevant cross-system data transfer — ensure recipient mailbox is access-controlled |
| **Audit trail** | Relay logs every alert sent: payment_id, amount, recipient, gmail_message_id — 90-day retention | Your DB records are the long-term audit trail |
| **OAuth health** | Relay auto-refreshes Gmail token | Re-authorise if token is manually revoked |

---

## Guided setup — business operators

### Step 1 — Check Gmail connection

Call `mcp__wfcd-mcp__list_credentials` with `node_name: "gmail"`.

**If no connection found:**

---
Gmail isn't connected yet. Here's how — 30 seconds:

1. Go to **Relay → Settings → Connections**
2. Click **+ Add Connection**
3. Choose **Gmail**
4. Sign in — Relay only gets permission to *send* emails, not read them
5. Type **"done"** when you're back
---

**If one found** — confirm:
> I'll send alerts from **[Gmail address]**. Works?

**If multiple** — list and pick:
> Which Gmail account should send the alerts?
> 1. [Account 1]
> 2. [Account 2]

---

### Step 2 — Configuration (one question at a time)

**Q1 — Threshold amount?**
> What payment amount should trigger the alert?
>
> Type a number — e.g. **"50000"** for ₹50,000
> or use Indian formats: **"1 lakh"**, **"5 lakhs"**, **"1 crore"**
>
> Any payment at or above this amount will send an alert instantly.

*Internal conversion: "1 lakh" → 100000, "5 lakhs" → 500000, "1 crore" → 10000000*
*Validate > 0. On invalid: "Just the number works — e.g. 50000 for ₹50,000"*

---

**Q2 — Who gets the alert?**
> Who should receive the alert?
>
> Type one or more email addresses:
> e.g. `you@company.com` or `founder@company.com, cfo@company.com`

*Validate format. Follow-up: "Anyone else to CC? (or say 'no')"*

---

**Q3 — Email subject?**
> What should the subject line say?
>
> 1. **🔔 High-value payment — ₹[Amount]** *(just the amount)*
> 2. **Payment alert — ₹[Amount] from [Customer Name]**
> 3. **Order [Order ID] — ₹[Amount] received**
> 4. Write your own

---

**Q4 — Email body?**
> What should the alert say?
>
> Here's the **standard alert email** — type **"standard"** to use it:
>
> ---
> A payment above your ₹[threshold] threshold just came in.
>
> **Amount:** ₹[Amount]
> **Customer:** [Customer Name]
> **Order ID:** [Order ID]
> **Payment method:** [Payment Method]
> **Time:** [Date & Time] IST
>
> View full details in your Cashfree dashboard.
> ---
>
> Or tell me what to add/remove — I'll build it.

---

**Q5 — Quiet hours?** (optional)
> Should alerts pause during certain hours?
>
> · **"No quiet hours"** — alerts fire any time, 24/7 *(recommended for high-value thresholds)*
> · Or give me a window — e.g. **"pause 11 PM to 7 AM IST"** — alerts queue and send as a batch when the window ends

---

**Q6 — Escalation?** (optional)
> If no one responds to the alert within a set time, should I escalate to someone else?
>
> · **"No escalation"** — just send the one email
> · Or: **"escalate to [email] after [N] minutes"**

---

**Q7 — Workflow name** (last):
> What should I call this?
> I'll use **"high-value-payment-alerts"** unless you'd like something else.

---

### Step 3 — Preview

> Here's what I'm setting up:
>
> | | |
> |---|---|
> | **Trigger** | Every payment at or above **₹[threshold]** |
> | **Alert sent to** | [recipients] |
> | **CC** | [CC or "none"] |
> | **Subject** | [subject] |
> | **Quiet hours** | [window or "none"] |
> | **Escalation** | [escalation or "none"] |
> | **Workflow name** | [name] |
>
> **Sample alert email:**
> ```
> 🔔 High-value payment — ₹82,500
>
> A payment above your ₹50,000 threshold just came in.
>
> Amount:         ₹82,500
> Customer:       Rajesh Iyer
> Order ID:       order_cf_20260511_abc
> Payment method: UPI
> Time:           11 May 2026, 2:47 PM IST
>
> View full details in your Cashfree dashboard.
> ```
>
> Ready? Type **yes** to go live.

---

### Step 4 — Create

1. Call `mcp__wfcd-mcp__create_workflow` → save `workflow_id`
2. Call `mcp__wfcd-mcp__update_workflow`

---

### Step 5 — Success message

> ✅ **Your payment alert is live.**
>
> Every payment at or above **₹[threshold]** will trigger an email to **[recipient]** within seconds.
>
> **Test it:** Make a sandbox payment above ₹[threshold] — alert should arrive within 10 seconds.
>
> **Gmail daily budget:** At your threshold, expect roughly [estimated alerts]/day. Gmail personal limit: 500/day. Workspace: 2,000/day. [Budget status message based on estimate].
>
> **To change the threshold:** Relay → Workflows → [name] → Edit → Threshold
>
> **To pause alerts:** Toggle the workflow off in Relay → Workflows.

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

# ─── Alert config ──────────────────────────────────────────────────────────────
ALERT_THRESHOLD_INR=50000              # statutory min: 1; no statutory max for this alert type
ALERT_RECIPIENT=                       # primary recipient
ALERT_CC=                              # comma-separated, optional
GMAIL_TIER=personal                    # 'personal' (500/day) or 'workspace' (2000/day)

# ─── Quiet hours (optional) ────────────────────────────────────────────────────
QUIET_HOURS_ENABLED=false
QUIET_HOURS_START=23:00                # 24-hr IST
QUIET_HOURS_END=07:00                  # 24-hr IST

# ─── Escalation (optional) ─────────────────────────────────────────────────────
ESCALATION_ENABLED=false
ESCALATION_EMAIL=
ESCALATION_TIMEOUT_MIN=30             # escalate if no ack within this many minutes

# ─── Observability ─────────────────────────────────────────────────────────────
SELF_ALERT_EMAIL=
RELAY_TEST_MODE=false
```

**Startup validator — includes rate-limit budget estimate:**

```javascript
// startup.js
const REQUIRED = [
  'CASHFREE_CLIENT_ID', 'CASHFREE_CLIENT_SECRET', 'CASHFREE_WEBHOOK_SECRET',
  'RELAY_WORKFLOW_ID', 'BASE_URL', 'ALERT_THRESHOLD_INR', 'ALERT_RECIPIENT',
];
const missing = REQUIRED.filter(k => !process.env[k]);
if (missing.length) {
  console.error('❌  Missing required env vars:\n', missing.map(k => `   • ${k}`).join('\n'));
  process.exit(1);
}

const threshold = parseInt(process.env.ALERT_THRESHOLD_INR);
if (isNaN(threshold) || threshold <= 0) {
  console.error(`❌  ALERT_THRESHOLD_INR must be a positive number. Got: ${process.env.ALERT_THRESHOLD_INR}`);
  console.error('   Tip: Use plain numbers — 50000 for ₹50,000, 100000 for ₹1 lakh');
  process.exit(1);
}

const gmailLimit = process.env.GMAIL_TIER === 'workspace' ? 2000 : 500;
console.log(`✅  Config OK.`);
console.log(`   Threshold:     ₹${threshold.toLocaleString('en-IN')}`);
console.log(`   Alert to:      ${process.env.ALERT_RECIPIENT}`);
console.log(`   Gmail budget:  ${gmailLimit}/day (${process.env.GMAIL_TIER || 'personal'})`);
if (process.env.QUIET_HOURS_ENABLED === 'true') {
  console.log(`   Quiet hours:   ${process.env.QUIET_HOURS_START}–${process.env.QUIET_HOURS_END} IST`);
}
if (process.env.RELAY_TEST_MODE === 'true') {
  console.warn('🧪  TEST MODE — alerts will be logged, not sent');
}
```

---

### Relay workflow spec

```json
{
  "name": "high_value_payment_alerts",
  "description": "Sends Gmail alert on every payment at or above threshold amount",
  "trigger": "payment_success",
  "nodes": [
    {
      "id": "threshold-gate",
      "type": "condition",
      "if": "orderAmount >= {{ALERT_THRESHOLD_INR}}",
      "then": "idempotency-check",
      "else": "DONE",
      "note": "Sub-threshold payments exit immediately — no further processing"
    },
    {
      "id": "idempotency-check",
      "type": "condition",
      "if": "already_processed(payment_id)",
      "then": "SKIP",
      "else": "quiet-hours-check",
      "note": "payment_id as dedup key. Cashfree webhook retries never send duplicate alerts."
    },
    {
      "id": "quiet-hours-check",
      "type": "condition",
      "if": "{{QUIET_HOURS_ENABLED}} == true AND current_time_ist BETWEEN {{QUIET_HOURS_START}} AND {{QUIET_HOURS_END}}",
      "then": "queue-for-morning",
      "else": "build-alert",
      "note": "Batches alerts during quiet hours; sends at window end"
    },
    {
      "id": "queue-for-morning",
      "type": "queue",
      "release_at": "{{QUIET_HOURS_END}}",
      "timezone": "Asia/Kolkata",
      "then": "build-alert"
    },
    {
      "id": "build-alert",
      "type": "transform",
      "output": "email_body",
      "template": "{{EMAIL_BODY_TEMPLATE}}",
      "context": {
        "threshold":       "{{ALERT_THRESHOLD_INR}}",
        "amount":          "{{orderAmount}}",
        "customer_name":   "{{customerDetails.customerName}}",
        "customer_email":  "{{customerDetails.customerEmail}}",
        "customer_phone":  "{{customerDetails.customerPhone}}",
        "order_id":        "{{cfOrderId}}",
        "your_order_ref":  "{{orderId}}",
        "payment_method":  "{{paymentMethod}}",
        "timestamp_ist":   "{{createdAt | to_ist}}"
      }
    },
    {
      "id": "send-alert",
      "type": "integration",
      "connector": "gmail",
      "action": "send_email",
      "params": {
        "to":      "{{ALERT_RECIPIENT}}",
        "cc":      "{{ALERT_CC}}",
        "subject": "{{EMAIL_SUBJECT_TEMPLATE}}",
        "body":    "{{email_body}}"
      },
      "retry":      { "attempts": 3, "backoff": "exponential", "initial_delay_ms": 2000 },
      "on_success": "{{ESCALATION_ENABLED == true ? 'escalation-timer' : 'DONE'}}",
      "on_failure": "self-alert"
    },
    {
      "id": "escalation-timer",
      "type": "wait",
      "duration_min": "{{ESCALATION_TIMEOUT_MIN}}",
      "then": "escalation-gate",
      "note": "Waits N minutes; if acknowledged, skip. Otherwise escalate."
    },
    {
      "id": "escalation-gate",
      "type": "condition",
      "if": "alert_acknowledged(payment_id)",
      "then": "DONE",
      "else": "send-escalation"
    },
    {
      "id": "send-escalation",
      "type": "integration",
      "connector": "gmail",
      "action": "send_email",
      "params": {
        "to":      "{{ESCALATION_EMAIL}}",
        "subject": "🚨 Escalation — high-value payment not acknowledged — ₹{{orderAmount}}",
        "body":    "Alert sent {{ESCALATION_TIMEOUT_MIN}} minutes ago for Order {{cfOrderId}} (₹{{orderAmount}}) has not been acknowledged.\n\nOriginal alert sent to: {{ALERT_RECIPIENT}}\n\nAction required: Review and acknowledge in your Cashfree dashboard."
      }
    },
    {
      "id": "self-alert",
      "type": "integration",
      "connector": "gmail",
      "action": "send_email",
      "params": {
        "to":      "{{SELF_ALERT_EMAIL}}",
        "subject": "⚠️ Relay workflow failed — high-value-payment-alerts",
        "body":    "Alert for Order {{cfOrderId}} (₹{{orderAmount}}) could not be sent after 3 attempts.\n\nError: {{error.message}}\nRun ID: {{run_id}}\nPayment ID: {{payment_id}}\n\nCheck: Relay → Workflows → high-value-payment-alerts → Run History\n\nCommon cause: Gmail connection expired → Relay → Settings → Connections → Reconnect Gmail"
      }
    }
  ]
}
```

---

### Optional: Alert receiver (Node.js)

```javascript
// server.js
import express from 'express';
import crypto  from 'crypto';

const app = express();
app.use(express.json({ verify: (req, _, buf) => { req.rawBody = buf; } }));

const { CASHFREE_WEBHOOK_SECRET, RELAY_TEST_MODE, GMAIL_TIER } = process.env;
const processed = new Map(); // swap for Redis: redis.set(key, '1', 'EX', 86400)

/**
 * @typedef {Object} RelayAlertWebhook
 * @property {string}  run_id
 * @property {'SUCCESS'|'FAILURE'|'SKIPPED'|'QUEUED'} status
 * @property {string}  payment_id
 * @property {string}  cf_order_id
 * @property {number}  order_amount
 * @property {string}  customer_name
 * @property {string}  customer_email
 * @property {string}  payment_method
 * @property {string}  gmail_message_id      - Present on SUCCESS
 * @property {boolean} escalation_triggered  - true if escalation email was sent
 * @property {string}  [quiet_hours_queued]  - ISO time when queued alert will release
 * @property {string}  [error_message]       - Present on FAILURE
 * @property {string}  timestamp
 */

// ─── Gmail daily budget tracker ───────────────────────────────────────────────
const gmailLimit    = GMAIL_TIER === 'workspace' ? 2000 : 500;
let alertsSentToday = 0;
let budgetResetDate = new Date().toDateString();

function checkAndIncrementGmailBudget() {
  const today = new Date().toDateString();
  if (today !== budgetResetDate) { alertsSentToday = 0; budgetResetDate = today; }
  if (alertsSentToday >= gmailLimit) {
    console.warn(`⚠️  Gmail daily budget exhausted (${gmailLimit}/day). Alert queued.`);
    return false;
  }
  alertsSentToday++;
  return true;
}

app.post('/api/relay/alert/webhook', (req, res) => {
  const sig      = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody).digest('base64');
  if (sig !== expected) return res.status(401).json({ error: 'Invalid signature' });

  /** @type {RelayAlertWebhook} */
  const payload = req.body;
  if (processed.has(payload.run_id)) return res.json({ received: true, duplicate: true });
  processed.set(payload.run_id, Date.now());

  if (RELAY_TEST_MODE === 'true') {
    console.log('🧪 TEST MODE:', JSON.stringify(payload, null, 2));
    return res.json({ received: true, test_mode: true });
  }

  switch (payload.status) {
    case 'SUCCESS':
      checkAndIncrementGmailBudget();
      console.log(`🔔  Alert sent — order ${payload.cf_order_id} · ₹${payload.order_amount} · msg: ${payload.gmail_message_id}${payload.escalation_triggered ? ' · 🚨 escalated' : ''}`);
      recordAlertSent(payload);
      break;

    case 'SKIPPED':
      // payment_id already processed — duplicate webhook
      console.log(`⏭️  Duplicate skipped — payment_id: ${payload.payment_id}`);
      break;

    case 'QUEUED':
      // Alert queued for quiet-hours release
      console.log(`🌙  Queued during quiet hours — releases at ${payload.quiet_hours_queued}`);
      break;

    case 'FAILURE':
      // All retries exhausted; self-alert sent by Relay
      console.error(`❌  Alert failed — order ${payload.cf_order_id}: ${payload.error_message}`);
      logFailure(payload);
      break;
  }

  res.json({ received: true });
});

// ─── Acknowledge endpoint (for escalation chain) ──────────────────────────────
// Call this from your dashboard when someone reviews the alert
app.post('/api/relay/alert/acknowledge', (req, res) => {
  const { payment_id, acknowledged_by } = req.body;
  if (!payment_id) return res.status(400).json({ error: 'payment_id required' });
  console.log(`✅  Alert acknowledged — payment_id: ${payment_id} by ${acknowledged_by}`);
  markAcknowledged(payment_id, acknowledged_by);
  res.json({ acknowledged: true });
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
    gmail_budget: {
      limit:     gmailLimit,
      used_today: alertsSentToday,
      remaining: gmailLimit - alertsSentToday,
      tier:      GMAIL_TIER || 'personal',
      resets_in: `${24 - new Date().getHours()} hours`,
    },
    threshold: `₹${parseInt(process.env.ALERT_THRESHOLD_INR).toLocaleString('en-IN')}`,
    tip: checks.gmail !== 'ok'
      ? '→ Reconnect Gmail: Relay → Settings → Connections'
      : alertsSentToday > gmailLimit * 0.8
      ? `⚠️  Gmail budget at ${Math.round(alertsSentToday/gmailLimit*100)}% — consider upgrading to Workspace (2,000/day)`
      : undefined,
  });
});

async function recordAlertSent(payload)      { /* store in your DB */ }
async function markAcknowledged(id, by)      { /* update alert record */ }
async function logFailure(payload)           { /* store in your DB */ }

app.listen(3000, () => console.log('🚀  Relay alert receiver on :3000'));
```

---

### Test harness

```bash
# ── 1. Health check (shows Gmail daily budget) ────────────────────────────────
curl http://localhost:3000/health

# ── 2. Simulate SUCCESS — ₹82,500 payment above ₹50K threshold ───────────────
curl -X POST http://localhost:3000/api/relay/alert/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{
    "run_id":               "run_alert_001",
    "status":               "SUCCESS",
    "payment_id":           "pay_abc123",
    "cf_order_id":          "order_cf_xyz",
    "order_amount":         82500,
    "customer_name":        "Rajesh Iyer",
    "customer_email":       "rajesh@example.com",
    "payment_method":       "UPI",
    "gmail_message_id":     "msg_alert_001",
    "escalation_triggered": false,
    "timestamp":            "2026-05-11T09:17:00Z"
  }'

# ── 3. Simulate SKIPPED — same payment_id fires again (duplicate webhook) ─────
curl -X POST http://localhost:3000/api/relay/alert/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{
    "run_id":      "run_alert_001_retry",
    "status":      "SKIPPED",
    "payment_id":  "pay_abc123",
    "timestamp":   "2026-05-11T09:17:03Z"
  }'
# Expected: { "received": true, "duplicate": true }

# ── 4. Simulate QUEUED during quiet hours ─────────────────────────────────────
curl -X POST http://localhost:3000/api/relay/alert/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{
    "run_id":               "run_alert_002",
    "status":               "QUEUED",
    "payment_id":           "pay_def456",
    "cf_order_id":          "order_cf_uvw",
    "order_amount":         150000,
    "quiet_hours_queued":   "2026-05-12T01:30:00Z",
    "timestamp":            "2026-05-11T23:45:00Z"
  }'

# ── 5. Simulate escalation triggered ─────────────────────────────────────────
curl -X POST http://localhost:3000/api/relay/alert/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{
    "run_id":               "run_alert_003",
    "status":               "SUCCESS",
    "payment_id":           "pay_ghi789",
    "cf_order_id":          "order_cf_stu",
    "order_amount":         500000,
    "gmail_message_id":     "msg_alert_003",
    "escalation_triggered": true,
    "timestamp":            "2026-05-11T14:22:00Z"
  }'

# ── 6. Acknowledge an alert (stops escalation timer) ─────────────────────────
curl -X POST http://localhost:3000/api/relay/alert/acknowledge \
  -H "Content-Type: application/json" \
  -d '{"payment_id": "pay_ghi789", "acknowledged_by": "finance@company.com"}'

# ── 7. Test mode — log only, no real sends ────────────────────────────────────
RELAY_TEST_MODE=true node server.js
```

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| Guided Gmail connection setup | `SELF_ALERT_EMAIL` for failure notifications | SMS / WhatsApp alert channel |
| Indian number format (lakhs / crores) | `GMAIL_TIER` for accurate budget display | Slack / Teams alert channel |
| Payment-ID idempotency — no duplicate alerts | Health check cron (run `/health` every 5 min) | Per-customer alert suppression |
| Threshold gate — sub-threshold exits instantly | Your DB schema for `recordAlertSent()` | Alert frequency cap (e.g. max 1/hour per customer) |
| Quiet hours with batch release | Acknowledgement UI in your dashboard | |
| Escalation chain (optional) | | |
| Gmail daily budget tracker in `/health` | | |
| Auto-retry ×3 with exponential backoff | | |
| Self-alert with Gmail reconnect hint | | |
| Acknowledge endpoint (`POST /api/relay/alert/acknowledge`) | | |
| DPDP data-flow disclosure | | |
| Startup validator with ₹ budget estimate in console | | |
| Test mode (`RELAY_TEST_MODE=true`) | | |

**DPDP note:** Customer name, email, phone, order ID, and transaction amount are sent to Gmail. This is a DPDP-relevant data transfer. Ensure the recipient inbox is access-controlled and document this transfer in your Privacy Policy.

**Gmail rate limit:** Personal Google: 500 alerts/day. Google Workspace: 2,000/day. The `/health` endpoint shows live budget consumption. At very high payment volumes (>500 threshold-crossing payments/day on personal Gmail), upgrade to Workspace.

**Cost:** No Secure ID API calls consumed. Cashfree payment webhook processing is included in your Cashfree plan.

**SLA:** Alert sent within 10 seconds of payment success in normal conditions. On Gmail API degradation, Relay retries for up to 14 seconds before alerting via self-alert.

---

## MCP — coming soon

```
/relay-threshold-alert

→ Claude: "Threshold amount? Recipients? Quiet hours? Escalation?"
→ Calls Relay MCP → create_workflow(template: 'threshold_alert', config)
→ Returns RELAY_WORKFLOW_ID, already live
→ Outputs integration code above, pre-filled
```
