# Cashfree Relay — Launch Package

PMM launch artifacts for Relay private beta → GA.

**Plugs into Cashfree's existing GTM operating model** — the [gtm-ops](https://github.com/mothivenkatesh/gtm-ops) 3-loop architecture, DIN approval gate, 13 reliability rules, 3-surface BI rule. See [03-gtm-strategy.md §0](03-gtm-strategy.md) for integration.

## Files

| File | Purpose | Audience |
|---|---|---|
| [01-prfaq.md](01-prfaq.md) | Press release + customer FAQ + internal FAQ | Internal alignment, leadership review |
| [02-positioning.md](02-positioning.md) | Positioning canvas, message house, taglines, objection handling | Sales, marketing, content team |
| [03-gtm-strategy.md](03-gtm-strategy.md) | North star metric, beta selection, phased launch plan, risks | Cross-functional execution team |
| [04-launch-blog.md](04-launch-blog.md) | Public-facing launch post (~900 words) | Cashfree merchants — drives beta applications |
| [05-launch-emails.md](05-launch-emails.md) | 4-email sequence (founder, CSM, applicant, welcome) | Beta cohort recruitment + onboarding |
| [06-pr-questionnaire-completed.md](06-pr-questionnaire-completed.md) | **Completed PR questionnaire** with all gaps filled (1.1, 1.3, 3.1–3.3, 4.2 vs Razorpay, 6.2, 6.3) | Comms team, leadership |
| [07-launch-readiness-questions.md](07-launch-readiness-questions.md) | **Engineering readiness questions** + drafted PMM answers (targeting, AI use cases, PPI levers) + 37 high-signal Eng questions | Engineering, PMM |
| [positioning-cashfree-relay-v2-2026-04-29.md](positioning-cashfree-relay-v2-2026-04-29.md) | **v2 positioning doc** — Growth Operator Agent + MCP-first anchor (Option B locked). Supersedes v1 WIP. | Leadership, cross-functional |
| [08-template-library-spec.md](08-template-library-spec.md) | **Template library SoT** — 7 templates live today (✅), 4 Growth Operator templates roadmap (🟡), 4 post-GA (🔴). Publication rules. | PMM, Eng, Sales, Comms |
| [09-mcp-commitment-memo.md](09-mcp-commitment-memo.md) | **Decision memo to Eng** — formal ask for MCP within 6–8 weeks, with three downside paths if not. | Eng leadership, Vinesh, Subramanian |
| [10-dev-release-note.md](10-dev-release-note.md) | **Developer release note** — beta announcement copy in founder/community voice; covers origin story, automations, native nodes, MCP building path, honest beta caveats. | Developer community (Discord, forums, dev newsletters) |
| [razorpay-agent-studio-strategy-explained-2026-04-29.md](razorpay-agent-studio-strategy-explained-2026-04-29.md) | **Razorpay strategy decoded** — five-layer analysis showing it's an MDR-replacement business model, not an AI product. Worked take-rate math. Three lessons for Cashfree. | Leadership, PMM, Product |

## Key product facts (as of 2026-04-27)

- **Stage:** Private beta
- **Category:** No-code AI workflow platform (workflow-first, with AI as a node — not agent-first)
- **Build modes:** Visual builder + AI Agent (describe in plain English) — both produce the same editable workflow
- **Triggers:** 9 event-based (payment/refund/dispute lifecycles) + 1 schedule (Simple Schedule, no cron)
- **Connectors:** 10 (Sheets, Slack, Gmail, Zoho Invoice, Calendly, Google Calendar, WhatsApp Business, Gemini, OpenAI, Cashfree Payments) + HTTP Request node
- **Templates:** None ready-to-use yet — beta merchants build from scratch with white-glove onboarding
- **Roadmap:** MCP server (post-GA) — connect external AI agents (Claude Desktop, Cursor, etc.) to Relay primitives

## Competitive context

**Razorpay Agent Studio** (Sprint 2026) is the direct competitor — agent-first, Claude Agent SDK-based, marketplace of pre-built agents (Cart Conversion, Dispute Responder, Subscription Recovery, Cashflow Forecaster). Cashfree Relay is a fast-follower — must differentiate on approach, not mimic.

**Relay's defensible wedge vs Razorpay:**
1. Composable visual workflow > autonomous black-box agent (transparency)
2. Maker/Checker security nodes (compliance teams' preference)
3. AI is opt-in per node, not orchestrator (control)
4. Native Cashfree infra, full payment data access (zero compliance review for merchant)

## Metrics framing (the punchline)

**North star at GA:** Successful Workflow Runs per Active Merchant per Month. (Not "workflows created" — that's vanity.)
**Stickiness cut:** % of active merchants with ≥1 workflow firing daily.

**Private beta does NOT use the north star.** It's a learning sprint:
> 15+ merchants build and run their own workflow end-to-end, unprompted, within 14 days.

Three sub-goals: ≥75% activation, 15–20 unique use cases, ≥30% with workflow firing 5×/week 2.

## Top decisions still open

1. **Beta cohort selection** — apply 4 filters (technical capability, ₹10L+ volume + ops pain, engagement willingness, trustworthy operator). Portfolio mix across D2C / SaaS / marketplace / EdTech / fintech / services. See 03-gtm-strategy.md §4–8.
2. **Pricing model at GA** — leaning ₹999–1,999/month Pro tier + free tier. Validate via late-beta WTP conversations.
3. **Public beta gate** — block until ≥10 ready-to-use templates exist + ≥40% self-serve activation.
4. **Press timing** — press-light at private beta, press-heavy at GA. Reeju LinkedIn at GA Day 0.
5. **Connector roadmap priority** — Tally → HubSpot → Shopify based on inbound merchant requests during beta.

## Critical risk to flag in next leadership review

**Two risks, ranked:**

1. **Wrong merchants in beta = false negatives.** If we pick non-technical low-volume merchants, they'll churn and we'll wrongly conclude the product is "too hard." Hard-gate the 4 filters; don't dilute for politics.
2. **No-template gap kills self-serve activation at public beta.** Private beta survives on white-glove. Public beta + GA cannot launch without ≥10 templates. Dedicate one PMM + one designer to building templates from Week 2 of private beta, sourced from what merchants build live.
