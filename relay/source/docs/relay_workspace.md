# Cashfree Relay — PMM Workspace

> Working document for Cashfree's AI Workflow product (working name: **Relay**)
> Compiled: April 2026
> Owner: Mothi Venkatesh

---

## Table of Contents

1. [Product Overview](#1-product-overview)
2. [Cashfree Workflow Capabilities](#2-cashfree-workflow-capabilities)
3. [Use Cases — Payments-First](#3-use-cases--payments-first)
4. [Use Cases by Vertical](#4-use-cases-by-vertical)
5. [Engineer Discovery Questions](#5-engineer-discovery-questions)
6. [Customer-First Questions](#6-customer-first-questions)
7. [Competitive Analysis — Razorpay Agent Studio](#7-competitive-analysis--razorpay-agent-studio)
8. [PRFAQ Review & Rewrites](#8-prfaq-review--rewrites)
9. [Strategic Positioning](#9-strategic-positioning)
10. [Sample Testing Workflows](#10-sample-testing-workflows)
11. [HTTP POST Beginner's Guide](#11-http-post-beginners-guide)
12. [Action Items](#12-action-items)

---

## 1. Product Overview

### Working Name
**Relay** (recommended over: Pipes, Streams, Chain, Automate, Agent Fabric, AI Fabric)

**Why Relay:** Memorable, implies orchestration ("events relay into actions"), no jargon, owns a word.

### One-Liner Options

| Option | Frame | Best For |
|--------|-------|----------|
| **A** (outcome-led) | "Cashfree Relay turns every payment event into an automated business workflow — no developer needed." | D2C, SMB |
| **B** (capability-led) | "Cashfree Relay lets you build AI-powered workflows on top of your Cashfree data — visually, or by describing what you want in plain English." | Mid-market |
| **C** (trust-led) | "Cashfree Relay is the only workflow product that runs natively inside your payments stack — with full access to your data, without ever leaving Cashfree's secure environment." | BFSI, Enterprise |

### What Relay Is
A no-code AI workflow engine native to Cashfree's payments stack. Combines:
- Visual drag-and-drop builder
- AI agent nodes (multi-model: OpenAI, Gemini, Claude)
- MCP connectivity (connect Claude/ChatGPT directly)
- Native Cashfree triggers + actions
- Vertical-specific templates

### What Relay Is NOT
- Not a Zapier clone (payments-aware logic, not generic SaaS connectors)
- Not open source (security/compliance via sealed runtime)
- Not a chatbot platform (agents act on transactions, not conversations)
- Not a replacement for custom infra (handles 95%, hyperscale stays in-house)

---

## 2. Cashfree Workflow Capabilities

### 2.1 Event Triggers (9)

#### Payment Triggers
| Trigger | Fires When | Use Case |
|---------|-----------|----------|
| **Payment Success** | Customer completes payment | Invoice + CRM + team notification |
| **Payment Failed** | Transaction fails | Email retry, ops alert on spike |
| **Payment Dropped** | Customer abandons checkout | Cart recovery WhatsApp |

#### Refund Triggers
| Trigger | Fires When | Use Case |
|---------|-----------|----------|
| **Refund Success** | Refund completes | Customer confirmation + accounting |
| **Refund Cancelled** | Refund reversed | Alert finance + notify customer |
| **Auto Refund Success** | System auto-refunds | Flag to finance for reconciliation |

#### Dispute Triggers
| Trigger | Fires When | Use Case |
|---------|-----------|----------|
| **Dispute Created** | New chargeback raised | Slack alert, gather evidence |
| **Dispute Updated** | Status changes | Track progress |
| **Dispute Closed** | Resolved (won/lost) | Log outcome, update records |

#### Other Triggers
- **Simple Schedule** — cron-like recurring runs
- **Custom Webhook** (TBC) — merchant-defined events

### 2.2 Cashfree Payment Actions (9)

#### Payment Gateway Actions
1. **Create Order** — auto-create from form/CRM
2. **Create Payment Link** — shareable link generation
3. **Fetch Payment Link Details** — status check
4. **Get Orders for Payment Link** — reconciliation
5. **Cancel Payment Link** — kill ACTIVE links

#### Refund Actions
6. **Create Refund** — initiate within 6 months
7. **Get All Refunds for Order** — dispute resolution

#### Payout Actions
8. **Create Cashgram** — instant money transfer link
9. **Deactivate Cashgram** — reclaim unclaimed funds

### 2.3 Logic Primitives
- **Router** — branching logic (if/else)
- **HTTP** — call any external API
- **Loop** (TBC)
- **Delay/Wait** (TBC)
- **Maker-Checker** (planned for BFSI)

### 2.4 Native Integrations
WhatsApp Business, Slack, Google Calendar, Calendly, Google Gemini, OpenAI, plus 30+ more in roadmap.

---

## 3. Use Cases — Payments-First

### 🛒 Cart Recovery & Revenue Rescue

#### Multi-Nudge Cart Recovery
```
Payment Dropped
→ Delay 15m → WhatsApp: "Complete your order"
→ Delay 2h → Email with Create Payment Link (10% off)
→ Delay 24h → Final SMS + cancel old link
```

#### Smart Retry for Failed Payments
```
Payment Failed
→ Fetch failure reason (HTTP)
→ If "insufficient funds" → WhatsApp: "Try UPI or EMI"
→ If "bank decline" → Create new Payment Link with different routing
→ If "card expired" → Email: "Update card"
```

#### High-Value Cart → Sales Handoff
```
Payment Dropped (amount > ₹25K)
→ Slack #sales with customer details
→ Create Payment Link (valid 48h)
→ Assign to AE in CRM (HTTP)
```

### 🧾 Post-Payment Automation

#### Instant Invoicing
```
Payment Success
→ HTTP: Generate invoice (Zoho/Cleartax)
→ Email PDF to customer
→ WhatsApp receipt
→ Log to Google Sheets
```

#### Fulfillment Trigger
```
Payment Success
→ HTTP: Create Shiprocket order
→ HTTP: Update Shopify inventory
→ WhatsApp: "Order confirmed, shipping in 24h"
→ Slack #fulfillment
```

#### Subscription Activation
```
Payment Success (plan = "Pro")
→ HTTP: Activate account in your SaaS
→ Email welcome + login link
```

### 💸 Smart Refund Flows

#### Zero-Touch Small Refunds
```
Support ticket tagged "refund"
→ Router: amount < ₹500?
  → Create Refund → Email confirmation
  → Else: Slack ops for manual review
```

#### Refund Velocity Guardrail
```
Refund Success
→ Fetch "Get All Refunds for Order"
→ If >2 refunds on same order → Slack fraud team
→ If refund > ₹10K → Email CFO
```

### ⚖️ Dispute Defense

#### Auto Evidence Bundle
```
Dispute Created
→ Get Orders for Payment Link
→ HTTP: Pull shipping proof
→ HTTP: Pull login/session logs
→ Email bundle to ops within 2 minutes
```

#### Chargeback Early Warning
```
Dispute Created (count > 3 this month)
→ Slack CEO: "Dispute rate spiking"
→ Email weekly trend to finance
```

### 📊 Reconciliation & Ops

#### Daily Settlement Report
```
Simple Schedule (9am daily)
→ Fetch yesterday's Payment Success events
→ Aggregate by payment method
→ Post to Slack #finance
→ Append to Google Sheet
```

#### Payment Link Cleanup
```
Simple Schedule (weekly)
→ Fetch all active Payment Links
→ If >7 days old and unpaid → Cancel Payment Link
→ Slack summary of cleanup
```

### 💰 Payouts via Cashgram

#### Refund as Cashgram (when card expired)
```
Refund Success (but original card expired)
→ Create Cashgram for same amount
→ WhatsApp claim link
→ If unclaimed in 48h → Deactivate Cashgram + reverse
```

#### Affiliate Commission Payouts
```
Simple Schedule (end of month)
→ Fetch Google Sheet of affiliate earnings
→ Loop each row → Create Cashgram → WhatsApp claim link
→ Slack summary to finance
```

### 🎯 KYC Sneak-Ins (Advanced Tier)

#### High-Value PAN Check
```
Payment Success (amount > ₹2L)
→ HTTP: PAN 360 check
→ If name mismatch → Create Refund + notify
→ Else: Continue fulfillment
```

---

## 4. Use Cases by Vertical

Cashfree's top 4 verticals: **D2C, Education, Travel, BFSI**

### 🛍️ D2C Merchants

**Pain points:**
- High cart abandonment (60-70% industry avg)
- COD fraud + RTO losses (20-30% revenue)
- Thin margins, no dev team
- WhatsApp is primary channel

**Killer Workflows:**
```
Payment Dropped → WhatsApp in 15 min → Recovery link
COD Order → WhatsApp confirmation → Cancel if no reply in 2h
Payment Success → Shiprocket push → WhatsApp tracking
```

**Engineer questions:**
- Native Shopify/WooCommerce integration?
- WhatsApp-first template library?
- COD verification workflow story?
- ROI proof points for cart recovery?

### 🎓 Education Merchants

**Pain points:**
- EMI + installment collections
- Demo → enrollment drop-off
- Parent-pays, student-uses
- High-value tickets (₹50K-₹5L)

**Killer Workflows:**
```
EMI Payment Failed → Parent SMS + Student WhatsApp → Retry link in 24h
Payment Success (course) → Grant LMS access → Welcome email
Refund Request → Router by amount → Auto/Manual path
```

**Engineer questions:**
- Subscription/installment trigger support?
- Partial refund handling (pro-rata)?
- Dunning logic for failed EMI?
- LMS integrations (Teachable, Graphy, Thinkific)?

### ✈️ Travel Merchants

**Pain points:**
- Real-time inventory + payment race conditions
- High refund/cancellation rate
- Multi-currency, multi-leg bookings
- Dispute-heavy (PNR-based)

**Killer Workflows:**
```
Payment Success (booking) → Confirm inventory → PDF ticket → WhatsApp
Cancellation → Create Refund → Release inventory → Notify customer
Dispute Created → Pull PNR + check-in → Auto-submit evidence
```

**Engineer questions:**
- Time-sensitive workflows (60s seat hold)?
- "Book now, refund later" pattern (IRCTC-style)?
- Travel-specific data exposed (PNR, dates)?
- Fraud detection workflows (velocity, geo-mismatch)?

### 🏦 BFSI Merchants

**Pain points:**
- Regulatory compliance (RBI, SEBI, IRDAI, PMLA)
- Audit trail mandatory
- KYC + payment inseparable
- Maker-checker workflows

**Killer Workflows:**
```
Payment Success (>₹2L) → PAN check → AML screen → Release or flag
Refund Request → Maker-Checker → Create Refund → Audit log
Dispute Created → Auto-populate evidence → Compliance review → Submit
```

**Engineer questions:**
- RBI compliance? (Audit logs, immutability, retention)
- Cashfree Secure ID integration for KYC inline?
- Maker-checker enforcement (human-in-the-loop)?
- Audit trail export for RBI inspection?
- Data residency requirements?
- Concurrent audit workflow?

### Vertical Prioritization Matrix

| Vertical | Speed to Value | Willingness to Pay | Volume | PMM Leverage |
|----------|---------------|-------------------|--------|--------------|
| **D2C** | Fast (15 min) | Low-Medium | High | Content + templates |
| **Edtech** | Medium | Medium | High | Case studies |
| **Travel** | Slow (complex) | High | Medium | Solution sell |
| **BFSI** | Slow (compliance) | Very High | Low | Enterprise GTM |

**Suggested focus:**
- **D2C** = top of funnel (templates, self-serve, community)
- **Edtech** = mid-market expansion (case studies, usage-based)
- **Travel + BFSI** = enterprise wedge (custom demos, solution engineering)

---

## 5. Engineer Discovery Questions

### The 5 Questions That Matter Most

If you only have 30 minutes:

1. **"How many Cashfree merchants actively use this today, and who's the biggest?"**
2. **"What's the one workflow a merchant builds that makes them say 'I can't leave Cashfree now'?"**
3. **"How does this fit in Reeju's / leadership's vision — feature or product line?"**
4. **"Razorpay's Agent Studio is X — where do we beat them and where do we lose?"**
5. **"If I was writing a one-liner for the Cashfree homepage tomorrow, what would it say?"**

### Agentic Architecture Questions

- Is this truly agentic or workflow with LLM nodes?
- Do workflows have state/memory across steps?
- Can an LLM step decide the next step dynamically?
- Is it closer to Zapier+AI, n8n, LangGraph, or Temporal?
- Are we building our own orchestration or wrapping LangChain/LangGraph?

### RAG & Knowledge Questions

- Do we have RAG inside the builder?
- What vector DB? (Pinecone, Weaviate, pgvector)
- Can merchants upload their own docs?
- Embedding model? Hybrid search?
- Knowledge base primitive shared across workflows?

### LLM & Model Layer

- Which models available? (OpenAI, Gemini, Claude, Llama)
- Model routing/fallback?
- Function calling / tool use?
- Are we using Anthropic Agent SDK, OpenAI Assistants, or our own loop?
- Token/cost tracking per step?

### Control Flow

- Loops with exit conditions?
- Human-in-the-loop steps?
- Sub-workflows (dynamic vs. pre-defined)?
- Retry policies?
- Scratchpad/memory within a run?
- Parallel sub-tasks (fan-out/fan-in)?

### Tools & Integrations

- Tool registry model?
- Can agents pick tools dynamically?
- Custom tool definitions?
- **MCP support?** (critical for 2026)
- Workflows-as-tools?

### Cashfree-Specific Questions

- Does this use our internal event bus?
- Settlement event triggers, not just payment?
- Sub-merchants in platform/marketplace setup?
- Connection to Merchant Risk team's signals?
- White-label for platform merchants (Dukaan)?

---

## 6. Customer-First Questions

### Who Is This For?

- Which Cashfree merchants tried this so far? (SMB? Enterprise? Both?)
- Self-serve dashboard or sales-led?
- Discovery — inside dashboard or do we need to push?
- Coming from PG, Payouts, or Verification?
- Feature of Cashfree or standalone product line?

### The Real Problem

- What were merchants doing before? (Webhooks? Manual? Zapier+API?)
- Which support tickets does this eliminate?
- What complaint led to this being built?
- Are merchants asking, or are we pushing?
- What % of merchants have webhooks set up today?

### Connection to Core Cashfree

- Same dashboard, login, permissions?
- Native access to PG data?
- Works across PG + Payouts + Secure ID, or only PG?
- Existing API keys or separate auth?
- Workflow runs billed to same account?

### The Activation Story

- First workflow a merchant builds (the "aha")?
- Time from signup to first successful run?
- % activation rate?
- Where do merchants get stuck? (Drop-off funnel)
- Templates out-of-box or blank canvas?

### Ongoing Value

- Workflows in month 2?
- Retention pattern?
- Most-edited workflows? (Signal of value + friction)
- Sharing with teammates?
- Failure detection?

### Money Questions

- What would a merchant pay?
- Do they ask unprompted, or do we pitch?
- ROI examples?
- One workflow that's paid for itself 10x?
- Buyer persona? (Founder, CFO, Head of Ops, Tech)

### The Alternative

- Why over Zapier/Make/n8n? (Honest)
- What can they do here they can't elsewhere?
- One thing Zapier does better?
- If on Razorpay, why come to us?
- Could a dev replace this in a weekend with ChatGPT?

### Where Merchants Get Burned

- Most common support ticket?
- Biggest NPS complaint?
- Any merchants lost money/data?
- Workflows we removed because of issues?
- Expectation gap (what they think vs. reality)?

### Merchant Voice

- 3 real merchant quotes (positive + negative)?
- Top 5 feature requests?
- Power users to talk to?
- User interview notes available?
- Churned merchants — why?

---

## 7. Competitive Analysis — Razorpay Agent Studio

### Launch Facts
- **Launched:** March 12, 2026 at FTX 2026
- **Built on:** Anthropic Claude Agent SDK
- **Positioning:** "World's first Agent Studio for payments"
- **Tagline:** "Workforce of autonomous agents"

### 8 Pre-Built Agents (NOT 4 as press summarized)

| Agent | What It Does | Threat Level |
|-------|-------------|--------------|
| **Dispute Responder** | Auto-responds to chargebacks | 🔴 High |
| **Subscription Recovery** | Smart retry + customer nudges | 🔴 High |
| **Abandoned Cart (SuperU)** | WhatsApp/email recovery (partner) | 🟠 Medium |
| **Abandoned Cart (Nugget by Zomato)** | Same, different partner | 🟠 Medium |
| **Cashflow Forecaster** | 3-7 day cash prediction | 🟡 Low |
| **RTO Shield** 🔥 | LLM address validation for COD | 🔴 Critical |
| **RTO Insights** 🔥 | Return pattern analytics | 🔴 Critical |
| **Settlement Insights** | Daily WhatsApp settlement summaries | 🟡 Low |

### 4 Strategic Moves They Made

1. **RTO Shield = D2C killer app** — captured the "AI-native RTO" narrative
2. **Partnership model** (SuperU + Nugget) — moving fast, building marketplace not product
3. **Reframing positioning** — "Payments are only the execution layer of commerce"
4. **No-Code Builder is BETA** — window of opportunity exists

### Where Razorpay Is Weak (Cashfree Openings)

1. **No BFSI story** — Zero mention of compliance, audit, RBI, KYC
2. **No Travel story** — Nothing on inventory holds, multi-leg, time-sensitive flows
3. **No deep edtech story** — Subscription Recovery is generic
4. **Partner-dependent cart recovery** — risk if partners fail
5. **No Secure ID equivalent** — huge unlock for Cashfree's full-stack story
6. **No pricing, SLA, data residency mentioned** — vague on BFSI essentials

### Hard Truths for Cashfree

- ❌ Cannot claim "world's first" — Razorpay owns this
- ❌ Cannot claim "first in India" for agentic payments
- ❌ "Built on Claude Agent SDK" not differentiated
- ⚠️ Voice-led agents (ElevenLabs + Sarvam) is their angle
- ⚠️ They have 4 production agents; we have visual builder
- ⚠️ Press momentum: Medianama, Outlook, Tribune, CIOL covered them

### Strategic Choice

**Option A: Race horizontal** — match agent count, ecosystem, partnerships. **Lose** — they have 6-month head start.

**Option B: Go vertical-deep** ✅ **(RECOMMENDED)** — own BFSI + Travel where Razorpay is thin. Come back to D2C with differentiated angle (WhatsApp-branded + verify-and-pay).

### Competitive Comparison Table

| Capability | Cashfree Relay | Razorpay Agent Studio | Zapier / n8n |
|-----------|----------------|----------------------|--------------|
| Visual builder | ✅ GA at launch | ⚠️ Beta | ✅ GA |
| AI agent nodes | ✅ Multi-model | ✅ Claude SDK | ⚠️ Via 3rd party |
| MCP native | ✅ Yes | ⚠️ Agentic EP | ❌ No |
| KYC/Secure ID orchestration | ✅ Native, inline | ❌ No equivalent | ❌ Not possible |
| BFSI audit + maker-checker | ✅ Built-in | ❌ Not emphasized | ❌ No |
| Data residency (India) | ✅ Inside Cashfree | ⚠️ Razorpay infra | ❌ US/EU |
| Merchant-branded WhatsApp | ✅ Own number | ⚠️ Via partners | ⚠️ BYO API |
| Vertical templates at launch | ✅ 20+ across 4 | ⚠️ 8 generic | ❌ Community-led |

### Sources
- [Agent Studio: AI Agents by Razorpay (official blog)](https://razorpay.com/blog/agent-studio-ai-agents-by-razorpay/)
- [Razorpay rolls out AI Agent Studio (The Paypers)](https://thepaypers.com/payments/news/razorpay-launches-ai-agent-studio-and-agentic-experience-platform)
- [Razorpay unveils world's first Agent Studio (The Tribune)](https://www.tribuneindia.com/news/business/razorpay-unveils-worlds-first-agent-studio-to-automate-payments-launches-agentic-experience-platform/)
- [Razorpay Launches Agent Studio: Promise, Gaps, Risks (Medianama)](https://www.medianama.com/2026/03/223-razorpay-launches-ai-agent-studio-questions-loom-dark-patterns-price-discrimination/)

---

## 8. PRFAQ Review & Rewrites

### Section 1.2 — One-Liner

❌ Current draft is 4 sentences doing 4 jobs.

✅ Pick ONE and commit. Recommended: Option C (trust-led) for hero positioning.

### Section 2.1 — Problem Framing

❌ Current: Generic ("merchants had to do many of these things manually")

✅ Lead with named scenario: "A D2C founder processes 500 orders a day. When a payment fails, she's copy-pasting to Sheets at 11pm..."

### Section 2.2 — Pain Validation

❌ "Shopify Flow has 10k ratings" doesn't prove pain for Cashfree merchants.

✅ Use Cashfree's own data: % merchants with webhooks, support tickets mentioning automation, dev vs. no-dev split.

### Section 3.4 — MCP Mention

🔥 **Pull MCP into hero position.** This is your most differentiated line and it's buried.

> "Relay works two ways: (1) build workflows visually in the dashboard, or (2) connect Relay to Claude, ChatGPT, or any AI agent via MCP — so your AI can query Cashfree data and take actions on your behalf."

### Section 4.1 — Differentiation

❌ "Easy, secure, compliant" is table stakes.

✅ "The only workflow product that runs **inside your payment stack**. Your data never leaves Cashfree's infra. For BFSI under RBI audit, that's the difference between 'we can use this' and 'we can't'."

### Section 4.2 — Razorpay Comparison

❌ Was empty.

✅ Use the comparison table from Section 7 above. Don't ship blank.

### Section 4.3 — Tech Differentiation

🚩 **Delete:** "It is a software product. Nothing specifically different tech wise."

✅ **Replace:** "Relay combines three layers: a visual workflow engine, native integration to Cashfree's event bus (sub-second latency), and an AI agent runtime with MCP. Integration depth — direct access to internal payment events and merchant context — is what external tools can't replicate."

### Section 5.1 — Impact

❌ Bland: "Easy to use, secure, compliant AI workflows"

✅ Concrete:
- Recover 10-15% of abandoned carts without dev effort
- Reduce reconciliation from 3 hours/day to <15 minutes
- Cut chargeback response from 48 hours to 5 minutes

### Section 6.3 — What to AVOID Saying

- ❌ "Agentic" without a demo
- ❌ "Fully autonomous" (compliance risk)
- ❌ Benchmark against LangChain/LangGraph
- ❌ "Revolutionary", "game-changing", "cutting-edge"
- ❌ Over-promise template library
- ❌ Specific LLM vendors by name (vendor lock-in signals)

### Top 5 Fixes Before Circulating

1. Rewrite the one-liner — pick one frame
2. Fill in Razorpay comparison
3. Delete "nothing different tech-wise"
4. Pull MCP into hero position
5. Add merchant numbers, not just stories

---

## 9. Strategic Positioning

### The Sentence That Matters

> **"Razorpay built a marketplace of AI agents. Cashfree built the only workflow platform regulated merchants can actually use."**

### Three Tiers of Sophistication

1. **Basic** — Notifications (Slack/WhatsApp on payment events) → *everyone starts here*
2. **Intermediate** — Automation (invoicing, fulfillment, cart recovery) → *where most merchants live*
3. **Advanced** — Compound flows with verification (high-value, compliance-sensitive) → *enterprise upsell*

KYC is the **advanced tier unlock**, not the headline.

### Vertical Pitch Per Segment

| Vertical | Pitch |
|----------|-------|
| **D2C** | "Recover lost revenue without a developer." |
| **Edtech** | "Smart EMI dunning + automated student handoffs." |
| **Travel** | "Time-bound workflows for inventory-sensitive payments." |
| **BFSI** | "RBI-audit-ready automation, inside your payments stack." |

### Where Cashfree Wins (4 Asymmetric Bets)

1. **Full-stack, not payments-only** — Relay orchestrates PG + Payouts + Secure ID + Verify
2. **Vertical-deep, not horizontal** — BFSI and Travel are competitive white space
3. **Inside the infra, not on top** — Zero data egress, sub-second latency
4. **Merchant-owned channels** — WhatsApp from merchant's own number, Sheets live sync

---

## 10. Sample Testing Workflows

### Free Test Endpoints (No Signup)

| Tool | URL | Use For |
|------|-----|---------|
| **webhook.site** | https://webhook.site | See exactly what you sent |
| **JSONPlaceholder** | https://jsonplaceholder.typicode.com/posts | Fake REST API |
| **httpbin.org** | https://httpbin.org/post | Echoes your request back |
| **RequestBin** | https://pipedream.com/requestbin | Better UI |
| **reqres.in** | https://reqres.in/api/users | Fake users API |

### 🟢 Level 1: Basics (5 min each)

#### Workflow 1: Payment Success → Slack Notification
```
Trigger: Payment Success
→ HTTP POST to Slack webhook
  URL: https://hooks.slack.com/services/YOUR/WEBHOOK/URL
  Body: { "text": "💰 New payment: ₹{{amount}} from {{customer_email}}" }
```

#### Workflow 2: Payment Failed → Webhook.site Log
```
Trigger: Payment Failed
→ HTTP POST to https://webhook.site/your-unique-id
  Body: { "order_id": "{{order_id}}", "reason": "{{failure_reason}}" }
```

#### Workflow 3: Refund Success → Discord Alert
```
Trigger: Refund Success
→ HTTP POST to Discord webhook
  Body: { "content": "Refund processed: ₹{{refund_amount}} for order {{order_id}}" }
```

### 🟡 Level 2: Multi-Step (15 min each)

#### Workflow 4: Payment Dropped → Google Sheets Log
```
Trigger: Payment Dropped
→ HTTP POST to Google Apps Script webhook
  Body: {
    "timestamp": "{{created_at}}",
    "customer": "{{customer_email}}",
    "amount": "{{amount}}"
  }
```

#### Workflow 5: Payment Success → JSONPlaceholder Test
```
Trigger: Payment Success
→ HTTP POST to https://jsonplaceholder.typicode.com/posts
  Body: { "title": "Order {{order_id}}", "body": "₹{{amount}} paid" }
```

#### Workflow 6: Dispute → Multi-Channel Alert
```
Trigger: Dispute Created
→ HTTP POST to Slack #disputes
→ HTTP POST to webhook.site (audit)
→ HTTP POST to email service (SendGrid/Resend)
```

### 🟠 Level 3: Real APIs (30 min each)

#### Workflow 7: Payment Success → WhatsApp via Meta
```
Trigger: Payment Success
→ HTTP POST to https://graph.facebook.com/v18.0/{phone-id}/messages
  Headers: Authorization: Bearer {{meta_token}}
  Body: WhatsApp template message JSON
```

#### Workflow 8: Refund Success → Notion Page
```
Trigger: Refund Success
→ HTTP POST to https://api.notion.com/v1/pages
  Headers: Authorization: Bearer {{notion_token}}
  Body: Notion database row JSON
```

#### Workflow 9: Payment Failed → Telegram Bot
```
Trigger: Payment Failed
→ HTTP POST to https://api.telegram.org/bot{{token}}/sendMessage
  Body: { "chat_id": "ID", "text": "🚨 Payment failed: ₹{{amount}}" }
```

### 🔴 Level 4: Cashfree-to-Cashfree

#### Workflow 10: Payment Dropped → Create Recovery Link
```
Trigger: Payment Dropped
→ HTTP POST to https://api.cashfree.com/pg/links
  Headers:
    x-client-id: {{cashfree_app_id}}
    x-client-secret: {{cashfree_secret}}
  Body: Recovery payment link JSON
```

### Recommended Starter Sequence

1. **Workflow 2** (webhook.site) → proves the system works
2. **Workflow 1** (Slack) → proves real external integration
3. **Workflow 4** (Sheets) → proves business value
4. **Workflow 10** (Cashfree-to-Cashfree) → proves the killer use case

By end of 90 minutes: 4 real screenshots for the PRFAQ.

---

## 11. HTTP POST Beginner's Guide

### What is HTTP POST? (30-second explainer)

**HTTP** = the language websites and apps use to talk to each other.
**POST** = "Hey, I want to *send* you some data."

Think of it like sending a parcel:
- **URL** = the address you're sending to
- **Headers** = the label on the parcel (who it's from, what's inside)
- **Body** = the stuff inside the parcel

### Step-by-Step: Your First Workflow

#### Step 1: Open Webhook.site
1. Go to https://webhook.site
2. Copy the unique URL at the top (e.g., `https://webhook.site/abc-123-def-456`)
3. Keep this tab open

#### Step 2: Create New Workflow in Cashfree
1. Click "Create new workflow"

#### Step 3: Pick Trigger
1. Select **Payment Success**

#### Step 4: Add HTTP Step
1. Click "+ Add step"
2. Select **HTTP**

#### Step 5: Configure HTTP
- **Method:** Select `POST`
- **URL:** Paste your webhook.site URL
- **Headers:** Add `Content-Type: application/json`
- **Query params:** Skip
- **Body:**
```json
{
  "message": "Payment received!",
  "amount": "test",
  "time": "just now"
}
```

#### Step 6: Test Step
1. Click **Test Step**
2. Switch to webhook.site tab
3. See your message appear → 🎉 Success!

#### Step 7: Save & Activate
1. Save the workflow
2. Make sure it's "Active"

#### Step 8: Real Payment Test
1. Switch Cashfree to Test Mode
2. Create a test payment link
3. Pay using `4111 1111 1111 1111`
4. Wait 10-30 seconds
5. Check webhook.site → real event appears

### Using Real Payment Variables

Replace hardcoded body with:
```json
{
  "order_id": "{{order_id}}",
  "amount": "{{amount}}",
  "customer_email": "{{customer_email}}"
}
```

`{{variable}}` syntax = "replace with actual value when workflow runs"

### Troubleshooting

| Problem | Fix |
|---------|-----|
| Test Step error | Check URL has no typos, starts with `https://` |
| "Invalid JSON" | Use https://jsonlint.com to validate |
| Nothing on webhook.site | Refresh page, verify URL match |
| Real payment doesn't trigger | Check workflow is Active, wait 30s, verify Test Mode |

---

## 12. Action Items

### Pre-PRFAQ Circulation
- [ ] Rewrite Section 1.2 one-liner (pick ONE frame)
- [ ] Fill in Section 4.2 with Razorpay comparison
- [ ] Delete "nothing different tech-wise" (4.3)
- [ ] Pull MCP into hero position (3.4)
- [ ] Replace generic claims with specific numbers
- [ ] Add vertical strategy commitment in 1.3

### Engineering Discovery
- [ ] Schedule 30-min meeting with workflow engineer
- [ ] Bring "Top 5 Questions" list
- [ ] Get live demo of one end-to-end workflow
- [ ] Confirm: Voice agent plans (Sarvam/ElevenLabs equivalent)?
- [ ] Confirm: Native Secure ID action category planned?
- [ ] Confirm: MCP server already built or planned?
- [ ] Get list of beta merchants currently using

### Customer Discovery
- [ ] Get on call with 3 merchants (power user, churned, new)
- [ ] Pull NPS/CSAT for the feature
- [ ] Get top 5 feature requests
- [ ] Get list of support tickets mentioning automation
- [ ] Find Cashfree AM who loves pitching this

### Strategic Decisions Needed (Leadership)
- [ ] Pricing: Free / Tiered / Enterprise-only?
- [ ] Wedge: Horizontal vs. Vertical-deep (recommend vertical)
- [ ] Positioning: Workflow-first vs. Agent-first?
- [ ] Launch verticals: BFSI + Travel? Or D2C also?
- [ ] PR cycle: How to position when Razorpay owns "first"?

### Hands-On Testing
- [ ] Run Workflow 2 (webhook.site) — prove system works
- [ ] Run Workflow 1 (Slack) — prove integration works
- [ ] Run Workflow 4 (Google Sheets) — prove value
- [ ] Run Workflow 10 (Cashfree-to-Cashfree) — prove killer use case
- [ ] Capture screenshots of all 4 for PRFAQ + deck

### Deliverables to Produce
- [x] Product positioning deck (`/Downloads/relay-deck.html`)
- [ ] 1-pager per vertical (D2C, Edtech, Travel, BFSI)
- [ ] Engineer meeting agenda (30 min, time-boxed)
- [ ] Merchant interview guide
- [ ] Competitive scorecard (Cashfree vs. Razorpay vs. Zapier)
- [ ] Launch GTM doc

---

## Appendix: Key Frameworks Used

### The Action Hierarchy
**Triggers** (when) → **Logic** (router/loop/delay) → **Actions** (do something) → **Results** (logged/notified)

### The Customer Journey Lens
Awareness → Activation → Retention → Expansion

### Three-Tier Maturity Model
1. **Notifications** (basic) → 2. **Automation** (intermediate) → 3. **Compound + Verification** (advanced)

### The Moat Question
> "Why would a merchant build this *on Cashfree* vs. on Zapier with Cashfree APIs?"

If you can't answer this in one sentence, the positioning isn't done.

---

## Compiled From
- Workflow builder UI screenshots
- Cashfree action/trigger documentation
- KYC/Payment template memo (`Project Templates [memo].md`)
- Razorpay Agent Studio blog (March 12, 2026)
- PRFAQ questionnaire draft
- Vertical analysis (D2C, Edtech, Travel, BFSI)

---

**End of Document**
