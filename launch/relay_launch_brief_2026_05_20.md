# Cashfree Relay — Strategic Launch Brief
**Date:** 2026-05-20
**Format:** PMM Launch Brief (mirrors MCP brief structure)
**Launch size:** XL
**Tentative launch date:** 1 June 2026

---

## 1. Target Audience

**Primary:** Developers and technical operators (PMs, growth engineers, automation leads) at D2C brands, ecommerce companies, and fintech startups who are already building on Cashfree Payments — and currently own the glue layer between payment events and everything else the business needs to act on.

**Secondary:** Business/growth/revenue heads at ecommerce and D2C companies who consume the outcomes — recovered revenue, fewer RTOs, live settlement visibility, automated recon — but never touch the tooling themselves.

**The dynamic:** Developer or technical PM sets the workflow up once → business head receives the outcome continuously. Relay makes the developer the hero to the business without making them the bottleneck forever.

---

## 2. Context / Trigger: Why Is This Relevant NOW?

Three things converging:

**MCP is now the standard for agentic workflows.** The same MCP infrastructure that lets Claude answer "what's my settlement status?" is now the backbone for *generating and running automated workflows*. Relay uses MCP not just for Q&A, but to describe, build, and execute payment-triggered workflows in plain language — no YAML, no webhook config, no cron expressions. The infrastructure is stable. The timing is right.

**Payment operations have a developer tax that shouldn't exist.** Every time a business wants a new payment-triggered action — a WhatsApp on failure, a Sheets row on success, a Slack alert on a ₹1L+ transaction — it lands as a developer ticket. That ticket gets scoped, estimated, built, deployed, and eventually breaks in production and gets re-opened. The business waits. The developer resents it. Both lose. Relay closes this loop.

**Razorpay launched Agent Studio at Sprint 2026.** Agent-first, Claude Agent SDK-based, marketplace model. The category is being defined now. Cashfree's differentiation is workflow-first + payment-native triggers + MCP-native generation — not agent framing. The 18-month window before competitors copy is open. Relay needs to plant the flag.

---

## 3. When Was This Released?

**Tentative launch date: 1 June 2026**
Currently in beta. First merchant onboarded before official launch — using Relay to trigger custom CRM workflows from Cashfree Payment Form parameters.

---

## 4. What Is the Merchant Pain Point This Solves?

**The core problem:** Every payment event in Cashfree is supposed to trigger something in the business. A failure needs a recovery sequence. A COD needs a confirmation. A ₹1L+ transaction needs a finance alert. A daily settlement needs a recon update.

Today, that "something" is either:
- A developer ticket that takes 2 weeks and breaks in 6
- A manual ops process (a Slack message that says "please check")
- A ₹6–12K/month Zapier subscription that requires webhook wiring to even start

Three concrete pain points:

**1. Payment-triggered actions require engineering time.** "Add WhatsApp on payment failure" is not a complex feature — but it lands in a sprint, gets estimated at 3 days, deprioritised twice, and ships late. By then, the business has lost the recovery window on 3 weeks of failed payments.

**2. Automation tools don't understand payments.** Zapier and n8n treat Cashfree as a generic API. Merchants must write webhook handlers, parse JSON payloads, handle idempotency, and manage auth — before they've even gotten to the business logic. A developer's weekend project just to get an invoice email.

**3. The maintenance burden compounds.** Every payment automation built outside Cashfree is a liability. Webhook signatures rotate. API versions change. The freelancer who built the integration is unavailable. The workflow silently breaks and no one knows until settlements don't match.

**Downstream effect:** Developers spend disproportionate time on plumbing instead of product. Businesses run manual recovery processes that leak revenue. Growth heads don't know their recovery rate because it was never automated.

---

## 5. Key Highlights

**Payment events as first-class workflow triggers.**
Cashfree Relay ships 9 typed payment triggers — Payment Success, Payment Failed, Payment Dropped, Refund Success, Refund Cancelled, Dispute Created, Dispute Updated, Dispute Closed, and Schedule — as native objects. Zero webhook setup. Zero payload mapping. The event is the primitive.

**Describe the workflow. MCP builds it.**
Relay uses the same MCP infrastructure as Cashfree's agent layer. Developers can describe a workflow in plain English via Claude Desktop or any MCP-compatible client — "when payment fails, send WhatsApp recovery, Gmail backup at 2 hours, Slack ops alert at end of day" — and Relay generates, configures, and activates it. No drag-and-drop required (though the visual builder exists for those who want it).

**Set it up once. The business outcome runs forever.**
Unlike the MCP query layer (ask → answer), Relay is always-on automation. Once a workflow is live, it fires on every matching event — 24/7, without a developer watching it, without a cron job to maintain. The developer ships it once. The business gets the outcome continuously.

**Use cases prioritised by real merchant revenue impact:**
- Failed payment recovery → WhatsApp + Gmail sequence → revenue recovered automatically
- COD confirmation + RTO nudge → fewer returns, lower ops cost
- High-value transaction alert → finance sees it in 40 seconds, not the morning report
- Settlement recon → Sheets/Zoho updated on every settlement, zero manual entries
- Abandoned cart recovery → WhatsApp trigger on payment drop, re-engagement without marketing ops involvement

**Built into Cashfree. Same auth, same data.**
Relay and the Cashfree dashboard call the same internal APIs. The workflow runs on the same RBI/PCI-DSS-compliant infrastructure. No data drift, no external token management, no separate login.

**AI-ready connectors out of the box.**
Gemini and OpenAI are native connectors — usable inside workflows for generating personalised recovery messages, summarising disputes, or classifying failure codes intelligently.

**Goal: ≥50% of top merchant payment operation tasks automated end-to-end by Relay.**

---

## 6. Feature Availability

| Surface | Status |
|---|---|
| Visual no-code workflow builder | Live (beta) |
| MCP-based workflow generation via Claude | Live (beta) |
| Payment event triggers (9 types) | Live |
| Schedule trigger | Live |
| Connectors: Sheets, Slack, Gmail, WhatsApp, Calendly, GCal, Zoho Invoice, Gemini, OpenAI, HTTP | Live |
| HITL (Gmail + Slack approval flows) | QA |
| Bolna voice connector | QA |
| Shopify connector | Roadmap (Q1 FY27) |
| Tally Prime connector | Roadmap (Q2 FY27) |
| Conditional branching | Roadmap |
| Webhook-based workflow entry | Roadmap |

---

## 7. Is This Industry-First? Launch Size?

**Industry-first:** Yes — as of launch date, no Indian payment processor offers native, no-code workflow automation with payment events as typed, structured triggers. Razorpay Agent Studio (Agent SDK-based) is the closest competitor, but it is agent-first and does not offer persistent, payment-native workflow automation. Comparable international reference: Stripe Workflows (in development), Shopify Flow (e-commerce-native, not payments-native).

**Launch size: XL**

Rationale: This creates a new product category (payments-native workflow automation) inside an existing product surface, with direct competitive pressure from Razorpay, a public MCP/AI narrative to ride, and measurable merchant outcomes from day one.

---

## 8. Engineering Blog / Launch Blog

Yes — in progress.

- **Launch blog:** Merchant-facing. Narrative: "Every payment event is a workflow waiting to run." Opens with the failed payment recovery use case. Closes with beta access CTA.
- **Engineering blog:** Developer-facing. Narrative: "How we built MCP-native workflow generation on top of a payments infrastructure." Covers the MCP server architecture, typed trigger schema, and the decision to use AI for workflow generation vs. a drag-only builder.

---

## 9. Impact Numbers (Expected)

| Metric | Target |
|---|---|
| Developer time saved per payment automation | ~2–3 days → ~30 minutes |
| Failed payment recovery rate (beta merchants) | 3–8% of dropped checkouts recovered automatically |
| Manual ops tasks eliminated per merchant/week | 3–5 hours of repetitive payment ops |
| Support ticket reduction (settlement/refund queries) | 20–30% reduction in payment status tickets |
| Retention signal | Merchants with ≥1 active workflow churn at significantly lower rate |

**Beta success bar (before GA):**
- 15+ merchants build and run a workflow end-to-end unprompted within 14 days of access
- ≥30% have a workflow firing ≥5× in week 2 (separates "tried it" from "using it")

---

## 10. What Do We Want People to Take Away?

**For developers:**
> "Payment events are now the starting point for automations, not a webhook integration project."

**For business/growth heads:**
> "Your team doesn't need to file a ticket to recover a failed payment. Relay already did it."

**The single message:**
> Cashfree Relay turns payment events into business actions — automatically, permanently, without engineering overhead.

---

## Key Distinction from the Cashfree MCP Layer

Both Relay and the Cashfree MCP agent use the same underlying MCP infrastructure. They solve different jobs:

| | Cashfree MCP (Agent layer) | Cashfree Relay |
|---|---|---|
| **Mode** | Query → Answer (ask once) | Trigger → Action (runs forever) |
| **Use case** | "What's my settlement status?" | "When settlement runs → sync to Sheets automatically" |
| **Interaction** | Conversational, on-demand | Set-and-forget, persistent |
| **Who triggers it** | Merchant, manually | Payment event, automatically |
| **Output** | Information | Business outcome |

Relay is the "always-on" layer. MCP is the "ask anything" layer. Together they cover the full surface of what merchants need from their payment data.

---

## References

- Positioning doc: `source/docs/relay_positioning_doc.md`
- PRFAQ: `source/launch/01_prfaq.md`
- GTM strategy: `source/launch/03_gtm_strategy.md`
- Video script (launch narrative): `source/docs/relay_launch_video_script_2026_05_20.md`
- Relay positioning locked May 13: `source/docs/relay_friday_doc_mothi_2026_05_13.md`
- AM GTM session notes (May 20): memory/reference_relay_am_gtm_may20.md
