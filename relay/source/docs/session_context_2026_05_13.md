# Relay Session Context — 2026-05-13

## What was discussed

### 1. What is Cashfree Relay?
Relay is the **umbrella brand** for all Cashfree AI + workflow surfaces:
- **Visual Workflow Builder** — no-code, most mature surface
- **MCP servers** — Cashfree payments lifecycle as MCP tool calls
- **ChatGPT / Claude Skills** — installable AI instruction packs
- **Plugins** — Dify, n8n integrations

**Stage:** Private beta (as of this session). Q1 FY27 KPIs: New MCP installs + New Skills installed.

### 2. Competitive positioning
| Competitor | What they do | Relay's counter |
|---|---|---|
| Razorpay Agent Studio | Agent-first, walled garden, Claude Agent SDK, outcome-based pricing | Workflow-first, open MCP, Cashfree-native triggers, maker-checker |
| n8n | Open-source canvas, Indian dev mindshare | Payments-native, pre-built India templates, PCI perimeter compliance |

**Don't call Relay:** "hosted n8n" or "agent platform" — that's Razorpay's lane.

### 3. Native event triggers (the wedge)
Payment Success/Failed/Dropped, Refund Success/Cancelled, Dispute Created/Updated/Closed, Schedule.

### 4. Connectors (current)
Google Sheets, Slack, Gmail, Zoho Invoice, Calendly, Google Calendar, WhatsApp Business, Gemini, OpenAI, Cashfree Payments, HTTP Request.

### 5. Three personas
- **Operator** — primary; ops lead, finance, founder's office; wants workflow, not code
- **Builder** — developer; uses MCP + Claude Code
- **Partner** — agency/freelancer; authors + resells verticalised Skills

### 6. Shipped use cases (Wave 1)
1. Calendar event on payment success
2. Big-ticket payment alert (WhatsApp/Slack/Gmail)
3. Auto-append transactions to Google Sheets
4. Hourly failed-payment digest

### 7. Roadmap use cases (Wave 2)
5. Dropped cart → auto payment link recovery
6. Sell from WhatsApp/Instagram DM
7. Monthly collection cycle on autopilot
8. COD confirmation to reduce RTO
9. Settlement reconciliation → Tally/Zoho Books

### 8. Org context
Mothi runs PM + PMM solo on Relay — flagged single point of failure.
Q1 ask: Product Intern. Q2 ask: dedicated Relay PM hire.

### 9. Outreach drafted
Short note to Sarvam AI DevRel to pitch Relay partnership (voice AI connector + co-marketing: webinar + in-person dev event).

## Files added this session
- `relay-product-note.md` — full Relay product note (positioning, personas, use cases, open questions)
- `relay-product-note-vinesh-qa.md` — Vinesh's Q&A on Relay capabilities (engineering answers)
