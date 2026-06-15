# Cashfree Relay — Where We Are and Where We Should Go

*By Mothi · May 13, 2026 · For Aditi, Priyam, Yashasvi · Friday read*

---

## Before You Read This

I'm writing this in plain language because in Tuesday's call we went in circles and I think the main reason was that we never got on the same page about what Relay actually is today.

So this doc does three things:
1. Tells you what Relay is right now — honestly, no marketing
2. Answers every question that came up in the call
3. Recommends what we do on Friday

I'm also attaching real Reddit threads from D2C operators in India. I scraped 271 posts from the last 6 months across r/IndiaStartups, r/IndiaBusiness, r/n8n, and r/developersIndia. The quotes in this doc are from real merchants and real developers. Not my words.

---

## Part 1 — What Relay Is Today

Let me be straight about this because I think we've been a little fuzzy.

**Relay today = a no-code workflow builder + an MCP server.**

That's it. Two things.

The workflow builder is what merchants log into. It has a templates page (I'm pushing for carousel), pre-built workflows for things like "when payment succeeds, create a Calendly event," and connectors for Slack, Gmail, Google Sheets, WhatsApp, Calendar.

The MCP is what we shipped a week ago. It lets a developer connect Cashfree to Claude or ChatGPT and create workflows by prompting. Not running them, not making decisions — just creating and managing them by typing.

**What Relay is NOT today:**
- It is not an agent. There's no memory. No goal-setting. No self-correction. The workflow runs the same steps every time, like a chron job.
- It is not what Razorpay launched at Sprint 2026. They built actual agents using Claude Agent SDK. We built rules.

I know we sometimes call Relay "agentic" on slides. I think we should stop. Not because it sounds smaller, but because if we say agentic and ship rules, we lose trust with developers fast. Razorpay already got called out by Medianama for dark pattern risk in their agent demos. We don't need to walk into that. We earn the agentic label when we have memory and goal-setting, which engineering said is the next cycle.

---

## Part 2 — Answering The Questions From Tuesday's Call

### Q1 (Aditi): "Is this different from what Lavika is building?"

Yes, very different. Lavika is building **packaged voice AI products** — one product, one outcome (recover the payment, recover the cart). She charges per call or per outcome.

Relay is a **workflow builder** — many products, many outcomes, the merchant builds what they need.

One analogy: Lavika is selling pizza. Relay is selling an oven plus recipes. Both have a place. They should not be one positioning.

My recommendation: keep them separate in GTM. Different decks, different ICPs, different landing pages. Together they live under one Cashfree AI umbrella narrative, but each has its own room.

### Q2 (Priyam): "Why build a workflow builder when n8n exists? Why not just connect our MCP to n8n?"

This is the biggest question in the call and the one I've been thinking about most. Let me answer it with real evidence.

A guy in Jaipur posted on r/n8n in March 2026. His family runs a clothing store. He wanted to build a WhatsApp AI agent so customers don't wait 30 minutes for a reply. He knew n8n. He had time.

**It took him 2 months. The final workflow has 44 nodes and 2 AI agents.**

His own words:
> *"Version 1 was embarrassing. Version 3 had no memory, no routing, no sense of where a customer is in their journey. I started over properly. The final system: 44 nodes."*
> — r/n8n, March 2026, 356 upvotes, 117 comments

The top reply, 25 upvotes:
> *"This is the part people miss: the model is rarely the hard part, the state machine is."*

Here's what this proves:

**n8n is not the alternative to Relay. n8n is the proof the problem exists.**

If a developer needs 2 months to build it for his own family, the D2C ops lead in Jaipur who is not a developer — who is losing ₹1L a month to RTO — never builds it. She is not the customer who switches from n8n to Relay. She is the customer n8n was never going to reach.

So Relay is not competing with n8n. Relay is competing with what she is doing today:
- Interakt for WhatsApp — ₹8,000–18,000/month
- Pabbly or Zapier — ₹4,000–12,000/month
- An ops person doing it manually — ₹20,000–35,000/month
- Total: ₹40,000–80,000 per month

That is the budget we are after. Not n8n's audience.

### Q3 (Priyam): "What's the real-world problem statement?"

Three real Reddit threads from the last 6 months, all from Indian D2C operators in their own words:

**r/IndiaStartups, Nov 28 2025 — 78 upvotes, 68 comments:**
> *"A friend of mine is running a small apparel DTC brand and COD fraud is becoming a serious problem these days. Last month alone, 23% of COD orders were fake/undelivered, average loss per fake order is around ₹350. We've tried OTP verification, restricting certain postal codes, charging extra for COD. Nothing is really helping :("*

**r/IndiaStartups, Dec 5 2025 — 188 upvotes, 51 comments — "20+ D2C brands brutal reality":**
> *"If you are doing less than 500 orders a month, logistics companies generally do not care about your grievances regarding RTO."*
> *"If there is no repeating customer, there is no sale."*

**r/IndiaBusiness, Feb 2026 — "10cr revenue business down to 2cr debt":**
> A founder describing how operational chaos (payment ops, RTO, manual everything) ate his business.

So the problem statement, simply:

**A payment event happens. Something should happen next — a WhatsApp confirm, a refund check, a calendar invite, a settlement entry. Today nothing happens unless a human makes it happen. The data is in Cashfree but it goes nowhere.**

That's the problem. Relay's job is to make the next thing happen automatically.

### Q4 (Priyam): "Is Relay just a rule engine then?"

Today, yes. Honest answer.

The MCP is the AI layer for **creating** workflows. The workflows themselves are deterministic — trigger fires, steps run in order, outcome happens. Conditional branching, but no memory, no self-correction.

I think that's actually fine for launch. Operators don't need an agent. They need reliable automation that they can audit when it goes wrong. Every step logged. Every action reversible. Maker-checker on big actions like refunds.

The agent layer comes next cycle. Engineering has confirmed they'll add memory + goal-setting on top of the workflow engine. When that lands, we can claim "agentic" honestly.

### Q5 (Aditi): "Who is the TG? Don't just say developer."

We've been sloppy here. Let me name three specific personas. No "developer" — actual people you could picture.

**Persona 1 — Neha, D2C Ops Lead**
- 26 years old, ops co-founder at a D2C apparel brand in Jaipur
- 6,000 orders/month, 40% COD, RTO rate 29%
- Uses Shopify, Cashfree, Shiprocket, Interakt
- Pays ₹36,700/month for stitched tools
- Cannot write code. Tried Zapier — half her zaps are broken
- **Relay value:** She switches on a template, drops her RTO by 10 points in 30 days, saves ₹50K–80K/month

**Persona 2 — Suresh, Web Dev Agency in Coimbatore**
- 2-person agency, 9 active D2C clients
- Builds Shopify stores, sets up Cashfree, runs n8n for clients on a DigitalOcean droplet
- Charges ₹6,000–20,000/month per client for "maintenance"
- His pain: rebuilding the same Cashfree → WhatsApp flow from scratch for every new client
- **Relay value:** Deploys a template in 20 minutes, charges ₹7,000/month as a managed service, scales to 20 clients without scaling the team

**Persona 3 — Arjun, Indie Builder**
- Solo founder building a fintech micro-SaaS (lending, reconciliation, or COD risk API)
- Read the Cashfree agent-skills GitHub
- Tried Cashfree MCP in Claude Code
- Frustrated by generic webhooks — no payment context, no event primitives
- **Relay value:** Uses MCP layer to skip writing webhook handlers. Publishes his workflow as a Relay template, gets distribution to Cashfree's merchant base

These three personas all want different things. But the product underneath serves all of them — if we ship templates for Neha, agency-mode for Suresh, MCP+SDK for Arjun.

### Q6 (Priyam): "Can we have 3 use cases per persona — at least 9 in total?"

Yes. Here they are:

**For Neha (Ops Lead) — what she will activate Day 1:**

1. **COD Confirm via WhatsApp** — When a COD order is placed for ₹500+, send a WhatsApp confirmation within 5 minutes from her own Business number. Customer taps "Confirm" or "Cancel." If no reply in 30 mins, follow up. If no reply in 2 hrs, hold for review. Expected outcome: RTO drops from 28–32% to 16–20% in 30 days. (Data: CampaignHQ India 2026.)

2. **Failed Payment Recovery** — When payment fails, look at the error code. Send the right WhatsApp message: UPI timeout → "tap to retry," card declined → "try a different method." Expected outcome: 10–15% of failures recovered within 5 minutes.

3. **Settlement to Google Sheets, Daily** — Every morning at 6 AM, pull yesterday's settlement data, write to her sheet, flag mismatches. Expected outcome: 2–3 hours of daily manual work eliminated.

**For Suresh (Agency) — what he resells to his clients:**

4. **Post-Payment Calendar Booking** — When a service business (tutor, salon, clinic) gets paid, auto-create a Google Calendar event + send a confirmation to both sides. Suresh charges ₹5,000/month for this to his service-business clients.

5. **Big-Ticket Alert + CRM Update** — Payment above ₹50,000 → Slack to founder + Google Sheets deal tracker + optional Zoho CRM update. He sells this to his B2B clients.

6. **Multi-Client COD-to-Prepaid Promise** — Suresh deploys the COD template across 10 clients from one dashboard. He pitches new clients: "I'll cut your RTO by 30% in 60 days or one month free." Possible because the template is pre-validated.

**For Arjun (Indie Builder) — what makes him build on Relay:**

7. **Programmable Payment Event Hooks via MCP** — He asks Claude: "Show me payment failures in last 24 hrs, grouped by error code, with top 20 by amount." MCP returns a structured response he can act on. Today this is 3 API calls + custom parsing.

8. **Template Distribution** — He builds a Tally reconciliation workflow, publishes it as a Relay template. Every Cashfree merchant who activates it is his customer. His CAC: zero.

9. **Multi-Product Orchestration** — His lending app needs PG + Secure ID + Payouts in one flow. Relay orchestrates all three. Razorpay's Agent Studio is PG-only — this is our differentiator.

### Q7 (Aditi): "How does Relay fit in the three tracks you laid out?"

You named three:

| Track | What it is | Where Relay fits |
|---|---|---|
| **1. End-user AI** | Consumer discovers + pays inside LLMs | This is Cashfree Here. Not Relay. |
| **2. Payment ops VAS** | Out-of-box AI products (cart recovery, voice agent) | Lavika's products. Some overlap with Relay but sold differently — outcome-first, packaged. |
| **3. Developer workflow builder** | Build any payment workflow, payments at center | **This is Relay.** |

Relay belongs only in track 3. We should not try to position all three under one banner. There can be one umbrella AI landing page that says "Cashfree is AI-native," but Relay needs its own page, its own onboarding, its own ICP.

### Q8 (Aditi): "What is the future for Agent Studio — is that a direction we want to go?"

I think yes, but in two stages.

**Stage 1 (now → 2 quarters):** Ship Relay as a payments-native workflow builder + MCP. Win the operator persona who is paying ₹40–80K/month for stitched tools. Win the agency persona who is rebuilding the same n8n flow 15 times.

**Stage 2 (3+ quarters out):** Add memory + goal-setting. Become a true agent platform. By then we have real merchant data, real workflow patterns, and we can pick the 3 outcomes worth committing to (RTO recovery, failed payment recovery, reconciliation).

If we try to build Stage 2 first, we lose. Razorpay is 6 months ahead on agents and has Claude Agent SDK. But Razorpay does not have what we have: PG + Payouts + Secure ID under one stack, with KYC compliance built in, in the merchant's own dashboard.

Our wedge is **regulated, full-stack, operator-friendly.** Not agent-first.

### Q9 (Priyam): "Is Relay competing with Razorpay Agent Studio?"

Yes, but in a specific way. Different lanes.

| | Razorpay Agent Studio | Cashfree Relay |
|---|---|---|
| Built on | Claude Agent SDK | Workflow engine + Cashfree MCP |
| Pricing | Per-outcome, opaque | Workflow-based, transparent |
| Persona | Merchants who trust agent autonomy | Operators who want audit trails |
| Compliance | Generic | KYC, Secure ID, RBI built-in |
| Scope | PG only | PG + Payouts + Secure ID + Verify |
| Open MCP | No | Yes |
| n8n node | Yes (Dec 2025) | Coming |

The wedge is: **Razorpay is for the merchant who wants AI to do it for them. Relay is for the operator who wants to see every step and decide what's automated.**

---

## Part 3 — Honest Open Questions

Things I need answers on before Friday or I will keep flip-flopping:

1. **What is the product called?** "Cashfree Relay" today covers both the workflow builder and the MCP. The Slack thread didn't resolve this. Are these one brand or two? My vote: one brand, two surfaces — call them "Relay Workflows" (no-code) and "Relay MCP" (developer).

2. **Who is the launch ICP — operator or developer?** If operator, the landing page leads with templates and the COD example. If developer, it leads with MCP, API docs, GitHub. Cannot lead with both.

3. **What's the pricing model?** Free with Cashfree account? Per workflow? Per execution? This changes the activation story dramatically.

4. **Is there a white-label path for agencies?** If Suresh (Persona 2) is real, we need multi-client management and some attribution. If not, we drop the agency persona.

5. **When does engineering commit to memory + goal-setting?** This is the bridge to true agentic. Need a date or we permanently position as workflow + MCP and rebuild expectations.

---

## Part 4 — What I Recommend We Decide On Friday

Five decisions. Each one is decidable in 10 minutes.

1. **Launch ICP = D2C Ops Lead.** Developer is secondary. Landing page leads with templates.
2. **Drop "agentic" from the headline.** Use "payment-native workflow automation." Earn agentic when we have memory.
3. **Keep VAS (Lavika) separate from Relay.** Different decks. One umbrella narrative.
4. **Lead with three templates at launch:** COD confirm, failed payment recovery, settlement reconciliation. The three that Reddit threads explicitly asked for.
5. **Pin a date for memory layer commitment** with Ram and engineering. Without this, our roadmap story has no spine.

---

## Part 5 — The Single Positioning Statement

Here's where I land after all this:

> **Cashfree Relay turns Indian payment events into business actions in 30 minutes — without code, without webhooks, without a developer.**
>
> **It is the only payment-native workflow product built for the operator who will never open n8n.**

If we can agree on this sentence on Friday, the next 6 months of GTM unblocks.

---

## Part 6 — The Evidence (For Anyone Who Wants To Verify)

I scraped 271 Reddit posts from Feb–May 2026 across 12 India-relevant subreddits. Full report in `reddit_d2c_india_report.md`. Top sources for this doc:

| Subreddit | Posts | Why it matters |
|---|---|---|
| r/IndiaStartups | 47 | D2C founder pain in own words |
| r/IndiaBusiness | 38 | SMB ops reality |
| r/developersIndia | 36 | Indian dev integration pain with Razorpay/Cashfree |
| r/n8n | 28 | What technical builders are doing today (and how long it takes) |
| r/smallbusiness | 14 | Long-tail SMB voice |
| Others | 108 | Broader context |

And industry data from G2, Capterra, Trustpilot, Shipway, WareIQ, CampaignHQ, BePragma, IBSIntelligence (full source list in the positioning doc v1).

---

## Closing Note

I think we are closer to a sharp positioning than the Tuesday call suggested. We just need to commit to two things:

1. **Be honest about what Relay is today.** Workflow builder + MCP. Not an agent. The Jaipur story shows what happens when builders pretend they have memory and they don't.

2. **Pick the operator persona, not the developer.** Developer is the secondary unlock for distribution via MCP and templates. But the budget — the ₹40–80K/month being spent today — belongs to the operator. That's our market.

If we agree on these two things on Friday, I can ship the full positioning doc, the landing page brief, and the launch blog by next week. If we don't, I'll keep flip-flopping and so will engineering.

That's it. See you Friday.

---

*Mothi · mothi.venkatesh@cashfree.com*
*Attached: full positioning doc v1 · Jaipur memo · Reddit raw data · 271 posts*
