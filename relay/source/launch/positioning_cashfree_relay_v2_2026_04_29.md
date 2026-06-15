# Cashfree Relay — Positioning & GTM (v2)

| Author | Mothi Venkatesh |
| :---- | :---- |
| Owners | Vinesh Kumar, Subramanian K |
| Stakeholders | Shritama Saha, Priyam Shankar Jha, Kumar Anubhav, Harshit Pai, Satyam Tripathi, Shanthalingaiah S M |
| Final Approver | Ramkumar Venkatesan |
| Version | v2 (supersedes v1 WIP dated April 2026) |
| Date | 2026-04-29 |
| Launch | Private beta open. Public beta + GA TBD. |

---

## Executive summary

Cashfree Relay is a **Growth Operator Agent** for Indian merchants — battle-tested workflow templates that reduce losses (RTO, fraud, drop-offs), improve sales (cart recovery, COD-to-prepaid, retry flows), and recover revenue (refund triage, dispute response, reconciliation), exposed through Cashfree MCP so any AI agent the merchant uses can run them. The visual workflow builder is the on-ramp for non-technical operators today; the MCP server is the destination that puts these growth playbooks inside every AI agent the merchant uses tomorrow.

The thesis: every payment processor is racing to put AI inside their dashboard. Relay does the opposite — it puts Cashfree inside the AI the merchant already uses. Razorpay built a walled garden of agents inside Razorpay. Stripe shipped Agent Toolkit for developers building their own agents. Relay is the Indian-payments-native MCP that the merchant owns: works in Claude today, any MCP-compatible agent tomorrow.

**Core promise:** the fastest path from "Cashfree merchant" to "Cashfree merchant with a Growth Operator Agent that recovers revenue, reduces fraud, and grows sales" — measured in minutes, not sprints.

---

## Sequencing decision (Option B — locked 2026-04-29)

The current private beta surface is a no-code workflow builder on the Cashfree Merchant Dashboard. The MCP server is on the roadmap. There is a real gap between what ships today and the public positioning.

**Decision: lead with vision, ship the wedge.** Three commitments make this honest, not vapor:

1. **MCP commitment with a hard timeline.** Eng confirms MCP server live within 6–8 weeks of private beta opening, before any public beta or PR. If MCP slips, the public-facing positioning is paused — not stretched.
2. **Templates that exist today are real. Templates on the 90-day roadmap are labeled as such.** No marketing copy claims a template that hasn't been built and run by at least one beta merchant.
3. **Eng's 7 use cases are recast in Growth Operator language** — same triggers, same actions, framed as outcomes (reduce RTO, recover failed payments, prevent fraud). See template library spec in companion doc.

What private beta proves: the workflows work, the merchants get value, the templates are real. What MCP at GA proves: those same workflows are accessible from any AI agent the merchant chooses.

---

## v1 → v2 — what changed and why

This v2 supersedes the WIP v1 framing of Relay as a "no-code AI workflow platform with AI nodes."

**Why the shift:** Razorpay launched Agent Studio at Sprint 2026 — agent-first, marketplace-driven, Claude Agent SDK-based. Stripe shipped Agent Toolkit for developers. The "AI workflow builder" frame puts Relay in n8n's category and Razorpay's slipstream. Neither is winnable.

The MCP-first frame creates a category where Cashfree is the only Indian-payments-native option:

| Old frame | New frame |
| :---- | :---- |
| AI workflow platform with AI nodes | Cashfree exposed as MCP, callable by any AI agent |
| Workflow-first, agent secondary | Agent-first, workflow-builder as on-ramp |
| Compete with Zapier/n8n | Compete with Razorpay's walled garden |
| Visual builder is the product | Visual builder is the on-ramp; MCP is the product |

**What stays unchanged:**
- 9 payment triggers, 1 schedule trigger, 10 connectors + HTTP — these are now MCP primitives surfaced through a builder
- Private beta cohort, white-glove onboarding model, beta success criteria
- Maker/Checker for sensitive actions
- Native Cashfree compliance perimeter

---

## 1. Product Overview

### What is Cashfree Relay

Cashfree Relay turns the Cashfree platform into a **Growth Operator Agent** — battle-tested workflow templates that reduce losses, improve sales, reduce fraud, and recover revenue, exposed through MCP so any AI agent can run them. Three surfaces, one underlying engine:

1. **Cashfree MCP (the spine).** An MCP server that exposes Cashfree primitives — orders, payments, refunds, payouts, settlements, subscriptions, payment links, customer data, dispute lifecycle — as scoped, audited, compliant tools. Any MCP-compatible AI agent (Claude Desktop, Cursor, internal copilots) can call them.

2. **Indian payment use case templates.** Working agent templates for the highest-leverage Indian payment workflows: RTO/COD recovery, refund triage, fake-order detection, abandoned-cart recovery, daily reconciliation, dispute response, payout orchestration. Drop in, point at your data, run.

3. **No-code workflow builder.** A visual canvas that surfaces the same MCP primitives for non-technical operators. Build a workflow visually, share the link, watch runs, configure thresholds. Same engine as the MCP — just a different surface.

The same primitives. The same compliance perimeter. The same audit trail. Three ways in.

### Why we built it

Three forces converged in late 2025:

**The MCP standard arrived.** Anthropic's Model Context Protocol turned "AI agent integration" from a custom build per-agent into a shared specification. Stripe shipped Agent Toolkit. Sentry, Linear, Slack, GitHub all shipped MCP servers. The infrastructure for "any AI agent calling any business system" became real, fast.

**Razorpay drew the line first.** At Sprint 2026, Razorpay announced Agent Studio — pre-built agents inside Razorpay. Closed surface. Their agents, their dashboard, their orchestration. A merchant who wants an AI ops teammate using Razorpay must use Razorpay's agents. Cashfree merchants told us they want the opposite: their AI, calling our APIs.

**Indian operators want chat, not dashboards.** D2C ops, SaaS finance, EdTech founders — every one we spoke to in beta intake had already pasted payment data into Claude or ChatGPT to ask a question. They are operating with AI. Cashfree had no way to be inside that loop.

We built Relay because the dashboard era of payments is ending. The merchant's primary surface is becoming the AI assistant. We need to be there.

### The Shift — why now

Every company is racing to put AI into their dashboard. Relay does the opposite: it puts Cashfree inside the AI the merchant already uses.

Indian merchants don't want one more dashboard. They want to ask:

> *"identify all RTO-prone COD orders from the last 7 days and send a UPI prepayment link on WhatsApp"*

— and have it done. The merchant types this into Claude. Claude calls Cashfree MCP. Orders are queried, classified, links generated, WhatsApp dispatched, audit logged. The merchant never opened the Cashfree dashboard.

n8n owns the Indian operator's workflow mindshare. Razorpay Agent Studio is another dashboard. Cashfree Relay is the only path that puts Cashfree where the merchant is already thinking — inside Claude.

---

## 2. Target Audience & Use Cases

### Personas (3 personas, one product)

| Persona | Tool | Day-1 job |
| :---- | :---- | :---- |
| **Merchant operator / PM** (D2C ops, EdTech, SaaS finance, RevOps) | Claude Desktop, visual builder | Run a template — RTO recovery, refund triage, daily recon |
| **Developer** (CTO, senior engineer at SMB merchant) | Claude Code, MCP directly | Wire MCP into existing systems, extend templates, build custom agents |
| **Partner** (web dev agency, freelancer, indie builder) | Both | Package and resell verticalized Relay templates to their merchant clients |

### Use cases by persona

**Merchant operator — Day 1**
- Morning: "summarize last night's failed payments and group by failure reason" → Claude returns a categorized brief
- Mid-day: "for every dispute filed today, draft an evidence response based on order history" → drafts ready in Gmail for review
- End-of-day: "send a WhatsApp retry link to every customer who dropped checkout above ₹2000" → 47 messages dispatched, log in Sheet

**Developer — Day 1**
- Wire Cashfree MCP into the merchant's internal Slack copilot
- Extend the abandoned-cart template with custom segmentation logic
- Build a reconciliation agent that runs nightly, writes to internal data warehouse

**Partner — Day 1**
- Bundle "Refund Triage Agent for D2C" as a paid add-on for their Shopify store clients
- White-label a "Daily Settlement Brief" agent for a portfolio of EdTech merchants
- Ship verticalized templates faster than the merchant could build alone

---

## 3. Challenges we solve

| # | Challenge | What it costs the merchant today |
| :---- | :---- | :---- |
| 1 | **AI agents have no native way to act on Cashfree data.** Merchants paste payment data into ChatGPT manually. No audit. No access control. Compliance exposure on every paste. | Hours per week on copy-paste. Sensitive data leaving the compliance perimeter on every query. |
| 2 | **Generic workflow tools (n8n, Zapier, Make) require dev time and leak data.** Webhook setup, payload mapping, OAuth juggling, third-party data residency, ongoing maintenance. | 2–6 weeks of engineering per workflow. Compliance review per third-party tool. |
| 3 | **Razorpay's Agent Studio is a closed surface.** Their agents, their dashboard, no portability. Merchants who want their own AI to use payments data are blocked. | Lock-in. No path to extend or own the agent layer. |
| 4 | **Indian payment use cases have no off-the-shelf agents.** RTO recovery, COD prepayment nudges, fake-order detection, UPI deep-linking — no global tool ships these. | Every Indian D2C builds the same 5 workflows from scratch. |
| 5 | **Sensitive payment actions have no agent-safe pattern.** Autonomous agents touching refunds, payouts, or customer comms = either reckless or blocked. | Either fraud risk, or AI never reaches the workflows that matter. |

---

## 4. Research & Insights

> *Note: this section borrows the Signzy mind-map structure (regulatory signals, competitive landscape, customer discovery) and applies it to Relay.*

### Regulatory signals
- **DPDP Act enforcement (2026)** put data minimization and processor accountability in scope. Sending payment data to third-party AI tools (without merchant configuration) = exposure.
- **RBI guidance on AI in fintech (draft, late 2025)** signals that agentic actions on payments will need explicit consent flows, audit trails, and reversibility — features that walled-garden agents struggle to expose to merchants.
- Implication: a compliant MCP layer (audit-by-default, scoped tool calls, no data leakage) becomes a regulatory asset, not just a product feature.

### Competitive landscape
- **Razorpay Agent Studio (Sprint 2026):** agent-first, Claude Agent SDK, marketplace of pre-built agents (Cart Conversion with Nugget/SuperU, Dispute Responder, Subscription Recovery via ElevenLabs, Cashflow Forecaster). Closed, walled, deploy-from-marketplace. No external MCP.
- **Stripe Agent Toolkit:** SDK that wraps Stripe APIs as agent tools. Developer-targeted, not merchant-targeted. India-shaped use cases (RTO, COD, UPI) absent.
- **n8n:** wins Indian dev mindshare on workflow depth. Self-hosted option = data residency story. No payment-native primitives.
- **Zapier / Make:** breadth of connectors, weak on AI-native and payments.
- **Vertical SaaS automation (Shopify Flow, HubSpot Workflows):** proves the pattern that platform-embedded automation beats third-party glue, but neither addresses Indian payments.
- **Gap:** no Indian-payments-native MCP exists. Razorpay has not announced one. Cashfree has the window.

### Customer discovery
From beta-intake conversations with ~30 candidate merchants:
- **9 of 10** had already pasted payment data into ChatGPT/Claude in the last quarter to answer an ops question
- **6 of 10** had a janky Zapier or n8n workflow they were maintaining manually
- **Top unprompted ask:** "can the AI understand which orders are likely RTO?" — Indian-context use case, no global tool ships it
- **Compliance heads (when present):** flagged "data leaving Cashfree perimeter into third-party AI" as their #1 concern — which means a compliant MCP becomes a *sales unblock*, not just a feature
- **No merchant** asked for "another dashboard." Every merchant asked for "AI that already knows our data"

---

## 5. Solution Overview

### Architecture

```
                    Merchant's AI agent
            (Claude Desktop, Cursor, internal copilot)
                            │
                            ▼
                ┌───────────────────────┐
                │   Cashfree MCP        │ ← scoped, audited, compliant tool calls
                │   (the spine)         │
                └───────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
   ┌─────────┐        ┌─────────┐         ┌─────────┐
   │ Visual  │        │ Templates│        │ Direct  │
   │ Builder │        │ Library  │        │ MCP call│
   │(no-code)│        │ (Indian) │        │ (devs)  │
   └─────────┘        └─────────┘         └─────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            ▼
              Cashfree compliance perimeter
              (PCI, RBI, DPDP — all data stays inside)
```

### Key features

**Cashfree MCP — the primitives**
- **Read tools:** orders, payments, refunds, payouts, settlements, subscriptions, payment links, customer data, dispute lifecycle, webhook event stream
- **Action tools:** create payment link, initiate refund, generate cashgram, register webhook, update subscription state — gated by Maker/Checker for sensitive actions
- **Auth model:** scoped tokens per agent, OAuth-style consent, full audit trail in Cashfree dashboard
- **Compliance posture:** zero raw payment data leaves Cashfree's perimeter — the agent gets answers, not databases

**Indian payment use case templates** (private beta seeds, GA library)
- RTO/COD recovery — flag prone orders, send prepayment link via WhatsApp
- Refund triage — classify reason, draft customer comm, route to ops
- Fake-order detection — composite signal (address mismatch, repeat phone, velocity), flag for review
- Abandoned-cart recovery — auto-WhatsApp with discount code on drop
- Daily reconciliation — pull settlements, diff against orders, surface mismatches
- Dispute response — gather evidence from order history, draft response narrative
- Payout orchestration — schedule, trigger, log

**No-code workflow builder** (current private beta surface)
- 9 payment-event triggers, 1 schedule trigger
- 10 connectors + HTTP escape hatch
- Visual canvas, drag-and-drop, real-time test mode
- Same primitives as MCP, surfaced for non-technical operators
- AI nodes (Gemini, OpenAI) as composable steps inside workflows

**Native install paths**
- Claude Desktop — paste config, MCP server live, ask anything
- Cursor / Claude Code — for developers wiring into existing stacks
- Cashfree dashboard — visual builder for ops/finance who never touch terminal

---

## 6. Positioning Statement

**Formal positioning (For X who Y, Cashfree Relay is Z that does W. Unlike A, we B.):**

> For Indian payment merchants whose ops, finance, and growth teams want to recover lost revenue, reduce fraud, and grow sales — without building workflows from scratch — Cashfree Relay is a Growth Operator Agent: battle-tested templates (RTO recovery, fake-order detection, cart recovery, refund triage) exposed as MCP tools, callable from Claude, Cursor, and any MCP-compatible agent. Unlike generic workflow tools that need 6 weeks of dev time per template, or closed agent platforms that lock merchants into one vendor's surface, Relay ships proven growth playbooks the merchant runs from inside the AI they already use.

**Category line:**
> *Agent-native infrastructure for India's payment stack.*

**One-liner (merchant-facing):**
> *Cashfree, but inside the AI your team already uses. Ask Claude. Get it done.*

**Sharpest claim (internal — for sales pitch and PR):**
> *The fastest path from "Cashfree merchant" to "Cashfree merchant with a Growth Operator Agent that recovers revenue, reduces fraud, and improves sales — without writing a workflow from scratch." Minutes, not sprints.*

---

## 7. Key Messages & Benefits

### 4 Messaging Pillars

| # | Pillar | Promise |
| :---- | :---- | :---- |
| 1 | **Agent-native, not dashboard-bolted-on** | Cashfree shows up where your team already thinks |
| 2 | **India-first templates** | RTO, COD, fake orders, refund triage — solved Day 1, not Q4 |
| 3 | **No-code for ops. Full-code for engineering.** | Same MCP. One install. Everyone gets the surface they need. |
| 4 | **Secure by construction** | Your data never leaves Cashfree's compliant perimeter |

### Persona × Pain × Message × Proof Point

| Persona | Pain Point | Message | Proof Point |
| :---- | :---- | :---- | :---- |
| **D2C founder / ops lead** | RTO eats 18% of COD GMV; nobody's automated the prevention | "Stop losing 18% of COD revenue to RTO. Your AI can identify and prevent it." | RTO recovery template; beta merchant case study (target: ≥30% RTO reduction) |
| **SaaS finance manager** | Failed renewals churn silently; no automated triage | "Every failed renewal gets categorized, customer-messaged, and CRM-updated within 30 seconds." | Subscription recovery template; subscription-event MCP tools |
| **EdTech founder** | Founder is the bottleneck on every payment ops thing | "Your AI handles enrollment-to-payment-to-Calendly without you in the loop." | Payment link → Calendly → Zoho Invoice template |
| **Compliance / risk lead** | Generic AI tools leak payment data outside the compliance perimeter | "Audited, scoped, agent-safe. Data stays inside Cashfree's RBI/PCI/DPDP perimeter." | Maker/Checker on sensitive actions, full audit trail, zero raw data egress |
| **Developer / CTO** | Building AI agents on top of payments means writing wrappers, handling auth, parsing webhooks | "Native MCP. Cashfree primitives are tools. Write the agent, not the integration." | MCP spec, Claude Code install path, sample agents in repo |
| **Web dev agency / partner** | No way to package payment-AI value for SMB clients | "Resell verticalized Relay templates as a paid add-on to your merchant clients." | Partner template kit (post-GA) |

### Core Benefits
- **Time-to-first-automation:** under 10 minutes for any starter template
- **Workflows shipped per active merchant:** 3+ in the first month
- **RTO/COD recovery uplift:** ≥30% reduction in RTO-prone order failures (beta target)
- **Refund-handling time:** from hours-per-batch to seconds-per-event
- **Compliance:** zero new third-party data residency to clear
- **Portability:** merchant owns the agent layer; works in any MCP-compatible client

### Secondary Benefits
- **Cost:** lower than maintaining a Zapier + freelancer + custom-script stack
- **Audit:** every agent call logged in Cashfree dashboard — regulator-friendly by default
- **Future-proofing:** as MCP-compatible agents proliferate (Cursor, OpenCode, internal copilots), Relay just works — no migration

---

## 8. Competitive Landscape & USPs

### Primary competitors and their wins

**Razorpay Agent Studio** — Won Indian fintech mindshare on agent-first positioning. Strong: pre-built agents for cart, dispute, subscription. Branded launch via Sprint 2026. Voice integrations (ElevenLabs partnership). Marketplace pattern.

**Stripe Agent Toolkit** — Won developer mindshare for agentic payments globally. Strong: developer SDK breadth, MCP server, Anthropic + OpenAI integrations. Established Stripe brand among AI-native builders.

**n8n** — Won Indian operator workflow mindshare. Strong: self-hosting (data residency), 6,400+ community workflows, depth of integrations, transparent pricing.

**Zapier / Make** — Won SMB workflow mindshare globally. Strong: 8,000+ connectors, mature pricing, AI agents add-on.

**Razorpay (core dashboard)** — Won Indian payments dashboard share. Strong: brand, MDR, market depth.

### What sets Cashfree Relay apart (USPs)

**1. Open MCP, not a closed agent.**
Razorpay Agent Studio is a walled garden — their agents, their dashboard, no extension surface. Relay is an open MCP that the merchant owns. Works in Claude today, any MCP-compatible agent tomorrow. The merchant keeps the keys, the audit trail, and the freedom to switch AI assistants without rebuilding.

**2. Indian payments, natively.**
Stripe Agent Toolkit doesn't ship RTO recovery. n8n doesn't know what COD is. Razorpay's agents address Indian use cases but only inside Razorpay's surface. Relay is the only MCP that ships Indian payment primitives (RTO, COD, UPI deep-linking, BBPS, NACH) as first-class tools.

**3. Same engine, three surfaces.**
Most competitors force a choice: developer SDK (Stripe), no-code builder (Zapier), or closed agent (Razorpay). Relay surfaces the same MCP through (a) direct MCP for developers, (b) templates for ops, and (c) visual builder for non-technical operators. One install, three doors in.

**4. Secure by construction, not by configuration.**
n8n + OpenAI + Sheets means data is in three third-party systems by Wednesday. Relay runs inside Cashfree's existing PCI/SOC/DPDP perimeter. The agent never sees raw payment data — only the answers it's allowed to. No glue code. No key management. No compliance review.

**5. The single sharpest claim:**
> *Relay is the fastest path from "Cashfree merchant" to "Cashfree merchant with an AI ops teammate that understands Indian payments" — measured in minutes, not sprints.*

---

## 9. Outcomes & KPIs

### Product north star (post-GA)
**Successful agent calls per active merchant per month** — measures actual value delivered, not workflows built. Includes both MCP-direct calls and visual-builder workflow runs.

### Stickiness cut
**% of active merchants with ≥1 agent call firing daily** — separates "tried it" from "operating with it."

### Private beta launch goal
**15+ merchants build and run their own workflow end-to-end, unprompted, within 14 days of access** (not the north star — beta is a learning sprint, not a growth sprint).

### Phase milestones

| Phase | Active merchants | What ships | What we learn |
| :---- | :---- | :---- | :---- |
| **Private beta** (now) | 15–20 hand-picked | Visual builder, 9 triggers, 10 connectors, HTTP, AI nodes | Which workflows merchants actually build → template library |
| **Closed public beta** | ~500 | + 10 published templates, in-app guided tour | Self-serve activation rate; pricing intent |
| **GA** | 2,000+ | + Cashfree MCP server (Claude Desktop), pricing live | North star metric live; partner program seed |
| **GA + 6 months** | 5,000+ | + MCP for Cursor, Claude Code; partner template kit | PPI lift on existing Cashfree base |

### Adoption targets
- Internal: ~100 active merchants in v1 + soft unveil
- External: a few thousand by Phase 2 close
- PPI target: 25% of active Cashfree merchants with ≥1 active Relay workflow weekly by end of Year 1; 50% by end of Year 2

---

## 10. Pricing

**Private beta:** free. No card, no usage caps for now.

**Closed public beta:** free. Visible "Pro tier coming soon" pricing card to capture intent.

**GA pricing (working hypothesis — to validate in late beta):**

| Tier | Target merchant | Includes | Approx. price |
| :---- | :---- | :---- | :---- |
| **Free** | All Cashfree merchants | 5 workflows, 500 runs/month, 1 MCP-connected agent, basic templates | ₹0 |
| **Pro** | Growing SMB | Unlimited workflows, 10K runs/month, premium connectors (WhatsApp, Tally), AI node credits, all templates | ₹999–1,999/month |
| **Business** | High-volume merchants | Usage-based above Pro caps, custom MCP scopes, priority support, partner template access | Usage-based |

**Pricing principles:**
- Free tier generous enough to drive PPI on existing Cashfree base
- Pro tier priced under "n8n + freelancer + Zapier" alternative spend
- AI node calls metered separately (token-based pass-through)
- Partner templates may carry revenue-share (post-GA, TBD)

---

## 11. GTM Plan (high-level — see [03-gtm-strategy.md](03-gtm-strategy.md) for full detail)

**Phased launch:** internal alignment → private beta (15–20) → closed public beta (~500) → GA (2,000+).

**Beta sourcing priority:**
1. CSM/AM intro list (top 200 SMB)
2. Recent support tickets where merchants asked "can you do X automatically?"
3. Top n8n/Zapier-using Cashfree merchants (via webhook traffic correlation)
4. Reeju + Mohit founder-to-founder asks (3–5 slots reserved)
5. Cashfree Discord (post-public-beta)

**Channel plan at GA:**
- Cashfree dashboard CTA (push to existing 100K+ merchants)
- Founder LinkedIn — Reeju leads with the MCP thesis
- Tech press — TechCrunch India, YourStory, Inc42, Moneycontrol, The Paypers
- Partner co-marketing — WhatsApp BSPs, Zoho, Anthropic (MCP ecosystem)
- Cashfree Discord — community of practice
- Webinar — "Your AI as a payments ops teammate"

**Plugs into Cashfree's gtm-ops infrastructure** — DIN approval gate, 13 reliability rules, 3 lifecycle loops (Acquisition / Nurture / Re-engagement agents), 3-surface BI rule. No Relay-specific dashboard. See `03-gtm-strategy.md §0`.

---

## 12. Risks

| Risk | Likelihood | Impact | Mitigation |
| :---- | :---- | :---- | :---- |
| **MCP server slips post-GA** — positioning depends on it but Eng timeline unconfirmed | Medium | High | Position v1 (private beta) honestly as "visual builder + templates, MCP roadmap public." Don't promise MCP at private beta. Lock MCP date with Eng before public-beta gate. |
| **Razorpay copies the MCP wedge** | Medium | High | First-mover window estimated at 3–9 months. Lock partnerships (Anthropic, Cursor, BSPs) early. File DIN, ship fast. |
| **No-template gap kills self-serve at public beta** | High | High | Block public beta until ≥10 templates exist. Templates sourced from private beta merchant workflows. Dedicated PMM + designer from beta Week 2. |
| **Wrong merchants in beta = false negatives** | High | Critical | Hard-gate the 4-filter selection (technical capability, ₹10L+ volume + ops pain, engagement, good standing). Don't dilute for politics. |
| **Agent does something irreversible** (auto-refunds ₹10L) | Low | Critical | Maker/Checker on sensitive actions by default. Per-run caps. Circuit breaker on anomaly. **The Cashfree Payments *action* node is the hot zone — not the triggers.** |
| **AI nodes leak PII to OpenAI/Gemini** | Medium | High | Default redaction policy. PII-safe mode opt-in. Legal/DPDP signoff before private beta opens. BYOK option for compliance-sensitive customers post-GA. |
| **Pricing model misjudged at GA** | Medium | Medium | Late-beta WTP conversations. Anchor ₹999–1,999 Pro. |
| **Connector reliability (third-party breakage)** | Medium | High | Per-connector health dashboard. Auto-retry with backoff. Status page. OAuth refresh notifications to merchants. |
| **MCP authentication confusion** | Medium | Medium | One-click consent flow in Cashfree dashboard. Scoped tokens visible to merchant. Revoke-anytime UX. |

---

## 13. What to Avoid Saying

These are explicit guardrails for sales, comms, and content.

1. **Don't call it a "workflow tool" or "Zapier for payments."** It's an MCP-first agent layer with a workflow builder as one surface. The other framing buries the strategic differentiation.

2. **Don't lead with "AI."** Lead with the merchant outcome — RTO recovered, refund cleared, payout shipped. Operator language wins over feature language.

3. **Don't pitch it as a "Claude plugin" or "AI feature."** It's infrastructure with templates. Claude is one of many agents that can call it.

4. **Don't promise full autonomy on irreversible actions** (refunds, payouts). Relay supports Maker/Checker. We lean into supervised autonomy.

5. **Don't claim "world's first" or "India's first."** Razorpay claimed "world's first AI Agent Studio for payments" at Sprint 2026. Cashfree is a fast-follower in market timing. Lead on substance, not firsts.

6. **Don't position as "Razorpay killer" or compare directly.** Stay above the fight. Differentiate by approach (open MCP vs walled garden), not attack.

7. **Don't position against developers.** Claude Code support means engineers extend Relay. They aren't the threat — they're the second persona.

8. **Don't say "hosted n8n for Cashfree merchants."** Accurate internally, but undersells the MCP + native-data + compliance wedge externally.

9. **Don't promise pre-built templates at private beta.** They don't exist yet. Set expectations: "We're co-building your first workflow with you."

10. **Don't share specific roadmap dates** for MCP, Cursor support, partner kit until product-locked.

11. **Don't reference specific beta merchant names** without explicit, written permission. Quote anonymously by category until case studies are formally signed off.

12. **Don't lead with the visual builder in PR.** Leading with the visual builder = sounds like Zapier. Lead with MCP + templates + builder as three surfaces.

---

## 14. Collaterals & Launch Dependencies

**Mandatory before private beta opens:**
- [ ] DIN brief filed and approved (PMM, with Reeju/Mohit/Sales/Comms signoff)
- [ ] 9 mandatory artifacts uploaded to DIN
- [ ] Internal 1-pager for Sales/CS/Support/SE
- [ ] Beta application form (5 fields)
- [ ] White-glove onboarding playbook
- [ ] Beta cohort Slack channel set up
- [ ] Kill-switch criteria defined
- [ ] HITL approval gate for first 100 outreach emails
- [ ] UTM scheme locked per channel
- [ ] Legal/DPDP signoff on AI node data flow

**Mandatory before public beta:**
- [ ] ≥10 published templates in-product
- [ ] In-app guided tour
- [ ] Loom library of top use cases
- [ ] Per-connector health dashboard
- [ ] FeatureBase or in-product feedback path live

**Mandatory before GA:**
- [ ] Cashfree MCP server live (Claude Desktop minimum)
- [ ] Pricing model validated against ≥10 WTP conversations
- [ ] ≥3 case studies with quantified outcomes
- [ ] Founder LinkedIn post drafted
- [ ] Tech press list locked
- [ ] Partner co-marketing agreements (WhatsApp BSPs, Zoho)

**Stretch for GA + 6 months:**
- [ ] MCP for Cursor, Claude Code
- [ ] Partner template kit
- [ ] BYOK for AI nodes (compliance-sensitive merchants)
- [ ] Public roadmap

---

## Appendix: how to read this doc against v1

| v1 section | v2 status |
| :---- | :---- |
| Author / stakeholders | Kept |
| Product Category line | Reframed: "Agent-native infrastructure for India's payment stack" |
| Product Name | Kept: Cashfree Relay |
| One-liner | Reframed: "Cashfree, but inside the AI your team already uses" |
| The Shift | Kept and expanded |
| What Cashfree Relay is (4 components) | Kept and reordered — MCP is now the spine, builder is the on-ramp |
| 2 Personas | Expanded to 3 (Operator + Developer + Partner) |
| What makes Relay different | Kept and sharpened — competitive landscape now formal |
| Messaging Pillars (4) | Kept |
| Outcomes | Kept and expanded with phase milestones |
| What to avoid saying | Kept and expanded (12 items vs 5) |

**New sections in v2:**
- v1 → v2 reconciliation
- Challenges we solve (5 enumerated)
- Research & Insights (regulatory + competitive + customer discovery)
- Solution Overview with architecture diagram
- Formal positioning statement
- Persona × Pain × Message × Proof Point table
- Competitor wins + our USPs (formal)
- Pricing
- GTM plan
- Risks
- Collaterals & launch dependencies
- This appendix

---

*v2 written 2026-04-29 by Mothi Venkatesh. Awaiting review from Vinesh, Subramanian, and final approval from Ramkumar.*
