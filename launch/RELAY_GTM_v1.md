# Cashfree Relay — Go-To-Market Plan v2 (phased to GFF 2026)

**Generated:** 2026-04-29 · **v2 update:** 2026-04-29
**Methodology:** SuperPMM (Mothi Venkatesh, `mothivenkatesh/pmm-ops`)
**v2 changes:** 5-phase rollout to GFF 2026 1st week (Sep 1-7, Mumbai); Phase 0 explicit goal of **2-3 enterprise design partners** under NDA; Phase 3 category claim upgraded to *"Agent Workflows for India's payments infrastructure."*
**Evidence:** ~50,000 demand signals across 8 sources (dtc-research 28,253 + Agent A 2,316 + Agent B 5,143 + Agent C 13,976 + Agent D 1,127 + competitive scan + India landscape + MCP playbook + Swiggy launch deep-dive)

> **Operating principle (per Mothi's `dtc-research/CLAUDE.md`):** Stay on pain / persona / TAM / WTP / evidence. Use operator language verbatim. Lead with what corpus most strongly supports. Don't manufacture confidence from thin evidence.

---

## Executive Summary

1. **Position.** Cashfree Relay is the **open, payments-native workflow platform** for Indian merchants. Razorpay shipped Agent Studio + MCP March 2026 (Codex, Replit India, SuperU partnerships saturated dev/founder narrative); Cashfree is the right-mover, not first-mover. Four wedges: (i) **open OAuth without 6-week Tech Partner audit**, (ii) **Payouts + Reconciliation depth in MCP** (Razorpay's MCP is payment-link only), (iii) **self-hostable Indian-priced runtime** (Razorpay is enterprise SaaS only), (iv) **Indian back-office stack** (Tally + GST + WhatsApp + UPI + multi-PG recon).

2. **ICP (beachhead → secondary → tertiary).** Indian D2C brands at 1K–50K orders/month → EdTech (fee chasing) → B2B agencies (invoice dunning). 600K+ Cashfree merchant base provides internal funnel; brand voice in builder communities is **3.6x weaker than Razorpay** (5 vs 18 mentions in 13,976-signal builder corpus) — distribution challenge bigger than initially weighted.

3. **TAM.** ₹240 Cr/yr addressable bottom-up (~$28M); $30M top-down on iPaaS slice; SOM ₹4–25 Cr ARR achievable Year 1.

4. **Use case priority (evidence-ranked).** P0: **RTO/COD prevention** (837 signals — biggest), Refund Management HITL (1,500+), Reconciliation Anomaly Alerts (218+), Payouts Orchestration (Cashfree-only differentiator), Payment-failed → WhatsApp Recovery (357). P1: EdTech Fee Reminders (222), Bolna Voice Agent. **Cut: Cohorts → Google Ads** (<10 signals).

5. **Launch (5-phase, ~18 weeks runway to GFF).** Headline public moment is **Global Fintech Fest 2026 — Mumbai, Sep 1-7** under category claim *"Agent Workflows for India's payments infrastructure."* **Phase 0 Private Beta** (now → end May): close **2-3 enterprise design partners** + 3-5 mid-market under NDA; resolve `Map<String,Object>` blocker. **Phase 1 Developer Soft Unveil** (Jun → mid-Jul): `npx @cashfreepayments/relay-mcp` works locally; OAuth opens; 6 templates ship; "early access" framing only. **Phase 2 Template Gallery + Cohort Apps** (mid-Jul → end Aug): 15-20 templates; GitHub PRs into n8n/ActivePieces/Composio land; Relay Builders applications open. **Phase 3 GFF Headline** (Sep 1-7): Akash/Reeju/Mothi keynote; booth with 12-15 "Made on Relay" demos; press embargo lifts; Mothi launch tweet. **Phase 4 Post-GFF Compound** (Sep → Dec): vertical hackathon, podcast circuit, festive Q4, ecosystem report. Three-server MCP architecture (Payments / Payouts / Reconciliation). 6 framework adapters Phase 1. Google Form application gate.

6. **Top three risks.** (a) Razorpay narrative dominance — mitigate with sharp open-vs-gated counter-frame. (b) Payload-shape `Map<String,Object>` quality issue (Satyam-flagged Apr 28) — **delay launch 2 weeks rather than ship broken**. (c) Cashfree brand voice gap (3.6x weaker than Razorpay) — aggressive Day-0 amplification across Mothi-Twitter, dev.to/Hashnode, GitHub PRs, integration platforms (Composio/Pipedream/Replit/Cursor — Razorpay-zero whitespace).

7. **Mothi-personal angle (your $500K leg-1).** 8-month brand-building arc compounded by phased rollout. **Phase 0** (silent externally — but closing 2-3 enterprise design partners as PMM is visible internal promo signal). **Phase 1** (technical articles on Hashnode/dev.to + reply-camp on dev Twitter → establish authority externally). **Phase 2** (Builders cohort program ownership + GFF keynote rehearsal). **Phase 3** (GFF stage = PMM voice of Indian payments-AI on national fintech stage). **Phase 4** (podcast circuit — Latent Space, Pragmatic Engineer, Lenny's, TWIML, Inc42 AI Summit). Compounds Cashfree promo case AND indie-leg reach.

---

# Section 1: ICP & Market Research

## 1.1 Ideal Customer Profile

### Beachhead ICP — Indian D2C brands at scale-up

**Company type:** Indian D2C brands operating Shopify/WooCommerce; 1,000–50,000 orders/month; multi-channel (own website + marketplace + ad-driven); already on a payment gateway (Razorpay default; Cashfree minority); typical ARR ₹1–50 Cr.

**Must-have:** ≥1,000 orders/month volume threshold; multi-channel revenue; Indian PG history (Razorpay/Cashfree/PayU); ops team of 1–5 doing manual reconciliation, refund follow-ups, customer comms.

**Buyer persona — Founder-CEO or Head of Operations**
- Pain (verbatim): *"I'm hiring my third ops associate just to keep up with refunds and recon."*
- Decision criteria: ROI in <30 days; doesn't want another SaaS subscription with cost-creep
- Budget authority: ₹5K–50K/month direct sign-off

**End user — Ops Associate / CX Agent / Finance Ops**
- Daily workflow: Tabs between Razorpay/Cashfree dashboard, Google Sheets, Slack, WhatsApp Web, courier portal (Shiprocket/Delhivery), Tally
- Success metric: time-on-task; cases closed faster; zero missed reconciliations

**Current way (what they do TODAY):**
- Manual reconciliation: download CSVs from PG → paste into Sheets → manually match against bank statements ("3 hours every week," r/ecommerce/1r679zv)
- Refund approvals: WhatsApp DM founder for approval → log in PG → refund manually
- COD verification: WhatsApp manual confirmation before dispatch (fake-COD risk; "Sunny scammer" thread, r/StartUpIndia/1od3x24)
- Cart recovery: Klaviyo email ("spam-foldered") OR WhatsApp manual nudges
- Payment failure recovery: Razorpay's 3-retry system + branded-from-Razorpay-not-merchant email (r/indianstartups/1s32w1g)
- B2B fee chasing: Manual WhatsApp + email reminders via founder's personal accounts

**Buying triggers:**
1. RTO benchmark check — operator analyzes RTO%, sees 30–50%, looks for solutions
2. Razorpay account block (multiple verbatim cases) — *"they suddenly blocked our service"*
3. Magic Checkout COD failure (multiple operator reports — r/shopify/1riizfg)
4. Ops team headcount pressure
5. Q4/festive prep — volume spike anticipation
6. Cashfree Sales pitching during PG renewal cycle (warm internal funnel)

### Secondary ICP — EdTech operators

**Company type:** Indian EdTech institutes/platforms at 500–50,000 students; ₹50L–50Cr ARR; recurring fee collection model.

**Buyer:** Founder-CEO / Head of Operations / CFO. Pain: *"Fee follow-ups eat 2 days/month and we still miss collections; NACH mandate failures pile up."*

**End user:** Fees Coordinator / Admissions Ops. Workflow = Excel student list + NACH dashboard + WhatsApp reminders + manual payment-link generation. Industry benchmark: 55–60% on-time collection baseline; WhatsApp-automated reportedly hits 85% (CampaignHQ).

**Trigger:** Quarter-end collection pressure or institute scaling past 1,000 students.

### Tertiary ICP — B2B SaaS agencies

**Company type:** Indian agencies (digital marketing, dev shops, consulting); 5–50 person teams; billing ₹2L–50L/month; often building flows for D2C clients.

**Buyer pain (verbatim):** *"I have 6 invoices pending, total ₹3.4L outstanding, oldest 67 days. I'm refreshing my bank account waiting for client payment that's 3 months late so I can make payroll."* (r/indianstartups, score 34)

**Buying motion:** Agencies build flows for clients AND use them internally for invoicing — distribution channel multiplier.

## 1.2 ICP Scorecard (FletchPMM)

| Dimension | Score | Evidence |
|---|---|---|
| **Retention** | 8/10 | Workflows are sticky once configured; Cashfree PG attach increases switching cost. Counter: 689 PRICE-SENSITIVE signals → if pricing slips beyond Pabbly territory, churn risk |
| **Access** | 7/10 | 600K+ Cashfree merchant base → strong internal funnel. Brand voice in builder communities **3.6x weaker than Razorpay** → organic discovery weak |
| **Sales Velocity** | 6/10 | Visual builder = self-serve PLG (fast); MCP = developer adoption (medium); Enterprise = sales-led (slow) |
| **Activation** | 5/10 | First-workflow building has UX friction; Satyam's `Map<String,Object>` payload risk; templates + skills mitigate |

**Net ICP fit: 6.5/10** — solid beachhead with **brand-voice gap** as the weakest lever. Product-led discovery (npx, GitHub, dev.to) must compensate for low organic awareness.

## 1.3 SPICED ICP Diagnostic (Winning by Design)

| Element | Beachhead D2C | EdTech | Agency |
|---|---|---|---|
| **Situation** | 1K–50K orders/mo, multi-channel, Razorpay default | 500–50K students, recurring fees, NACH-dependent | 5–50 person agency, building for clients + invoicing |
| **Pain** | RTO 30–50%, refund follow-ups 2 hrs/day, recon 6–7 hrs/wk, "Razorpay blocked us" | Fee chasing 2 days/mo, NACH failures, ops headcount cost | Invoice dunning manually; clients 67–90d late; payroll-floating |
| **Impact** | RTO ₹180–240/failed COD; ops headcount ₹40K–80K/mo | Missing 30–40% on-time collections | Personal cash flow, founder dignity |
| **Critical Event** | Q4 prep / Razorpay block / Magic Checkout COD fail | Quarter-end collection / 1K-student crossing | Late-payment cascading to payroll |
| **Decision** | Founder/COO direct, ₹5K–50K/mo | Founder/CFO, ₹5K–20K/mo | Founder direct, ₹999–5K/mo |

## 1.4 TAM Sizing (Triangulated)

### Bottom-up
- Cashfree existing merchant base: ~300K total, **~30K (10%)** fit beachhead D2C ICP at 1K+ orders/month
- Blended ARPU: ₹3,000/mo Relay (mix of Free, ₹999 Starter, ₹4,999 Growth, ₹19,999+ Enterprise)
- 30K × ₹36K/yr × 100% addressable = **₹108 Cr/yr addressable** (~$13M)
- Indian D2C universe outside Cashfree: ~80K brands → **₹240 Cr/yr** if Cashfree captures 30%

### Top-down
- Indian iPaaS/automation market 2026 ≈ $300M (30% CAGR on prior base)
- Cashfree-addressable slice (payments-native niche) ≈ 10% = **$30M**
- Indian SaaS market $70B by 2030 — payments-automation slice 5% = $3.5B 4-year horizon

### Analogy
- Pabbly Connect estimated ₹50–100Cr ARR
- n8n India estimated ₹30–50Cr ARR
- Razorpay Magic Checkout (proxy for vertical-slice) ₹50–200Cr estimate
- **Relay target:** $15–25M ARR in 24 months (~₹125–200 Cr) — conservative band

### SOM (Year 1)
- Top 1,000 Cashfree D2C/EdTech merchants (>₹1Cr GMV/yr)
- × 30% activation × ₹4K–₹40K/mo blended = **₹4–25 Cr ARR achievable Year 1**
- Quarter targets: Q1 ₹0.5–1Cr → Q4 ₹3–8Cr ARR run rate

---

# Section 2: Competitive Intelligence

## 2.1 Direct Competitors

| Competitor | Positioning | Pricing | Strengths | Weaknesses (verbatim from corpus) | Our Angle |
|---|---|---|---|---|---|
| **Razorpay Agent Studio + MCP** | "AI brain for India's small businesses" (Inc42) | Bundled with PG | 8 prebuilt agents, Anthropic SDK, AEP onboarding 5min, **Codex + Replit India + SuperU partnerships** | "Worst webhooks docs in industry"; "120-day settlement holds"; "Tech Partner = 6 weeks of audit"; "Account block without warning" | **Composable workflows merchants own** vs **agents you rent**. Open OAuth. Payouts + Recon depth. |
| **PayU MCP Server** | "AI-native merchant workflows" | Bundled | MCP shipped April 2026 | Limited to payment-link + txn-status; no canvas builder; no agent SDK story | Full builder + 3-server architecture |
| **n8n** | "Fair-code automation for technical teams" | Free self-host / €20–50/mo | 849 mentions in 30d global Reddit (top tool); 455+ India jobs Mar 2026 | Generic — *"n8n webhooks are naked. No auth, no rate limiting, no Stripe hookups"* | **Cashfree-native triggers + payments primitives n8n needs YOU to build** |
| **Pabbly Connect** | "Lifetime-deal Zapier alternative for Indian SMBs" | ₹20,900 lifetime / $16/mo | India SMB brand, lifetime pricing, 2,000+ apps | No MCP, basic AI, no payments-context | Payments-native + AI-builder for non-tech ops |
| **Zapier + Zapier MCP** | "Connect AI to 9,000 apps" | $19.99–69/mo | MCP in all paid tiers since 2026; ubiquity | "USD pricing scales painfully"; **only 1/6 share of voice of n8n in 30d**; generic Razorpay-only PG connector | India-priced + Cashfree-deep |
| **Make.com** | "Visual scenario builder for AI-era" | $9–29/mo + Enterprise | Visual builder, AI agents shipped, MCP late 2025 | Generic, no payments depth; little India presence | India localization + payments depth |

## 2.2 Status Quo Competitor — manual ops + 8 disconnected apps

> *"I spoke to 20 young founders this week and the average was 8 different apps. WhatsApp for customers, Excel for money, Canva for design, Linktree for bio, Razorpay for payments, Notion for tasks. Nothing talks to each other. Everything is manual."* — r/indianstartups/1snwtzb (verbatim)

**Why it persists:**
- Ops teams skilled at hacking around it
- Switching costs feel real (Excel formulas, Slack history, WhatsApp threads)
- Each app individually cheap; the time-tax is hidden

**How to displace:**
- Templates obviously better than Slack-DM workflows
- Pricing under Pabbly anchor (₹999/mo Starter or self-host free)
- Cashfree Sales include in PG renewal pitch (internal motion)
- ROI in <30 days (case study: "20 hours/week saved")

## 2.3 Adjacent Competitors (becoming direct)

- **Bolna** — voice AI; partner today, builder-tomorrow risk ($6.3M GC seed; ₹2.5Cr+ recovery for Hypothesis)
- **GoKwik / Shopflo / Shiprocket** — vertical-slice automation expanding into orchestration
- **Quickwork** — BFSI enterprise iPaaS (Axis Bank, DMI Finance, Genpact, Credit Saison India). Sleeper rival
- **Workato** — enterprise MCP; only relevant if Relay goes upmarket
- **Composio** — MCP marketplace (1,000+ toolkits) but **omits Razorpay/Cashfree first-class** (whitespace to claim)

## 2.4 Market Maturity & Differentiation Mode

**Maturity: Growing, with India-payments-native sub-segment emerging Q1 2026.**
- Multiple direct competitors (Razorpay Agent Studio, PayU MCP, n8n, Zapier MCP, Pabbly, Cashfree Relay)
- MCP standard ratified (Anthropic Nov 2024 + OpenAI March 2025)
- 24% of dev community signals MCP-aware in last 30 days
- India-specific MCP players still consolidating

**Differentiation mode: Competitive (not Contextual).** Frame against Razorpay specifically (dominant rail) and n8n technically (developer alternative). Position must be sharper than "we have AI workflows for India."

## 2.5 Top 4 Differentiation Angles (evidence-ranked)

### Wedge 1: Open OAuth — no Technology Partner audit (CRITICAL)
**Evidence:** *"Razorpay has OAuth with read_only scope. The ONLY Indian gateway. You need to become a Technology Partner — 6 weeks of emails and an audit."* (r/SaaS/1sscu5i)
**Implication:** Cashfree opens read-only OAuth to any registered developer = arbitrary devs build instantly without 6-week gate. **Razorpay can't change this without disrupting their Tech Partner program governance.**
**Marketing line:** *"No Technology Partner audit. No 6-week wait. Ship today."*

### Wedge 2: Payouts + Reconciliation depth (Cashfree-only)
**Evidence:** Razorpay's MCP exposes payment-link + txn-status. Razorpay Agent Studio's 6 agents are pre-built consumer agents. **Razorpay MCP does NOT expose deep Payouts or Reconciliation primitives at MCP-tool level.**
**Cashfree advantage:** Auto Collect (virtual accounts), Bulk Payouts (2FA RSA), Reconciliation APIs (UTR matching, TDS auto-deduct), Settlements (transparent, no 120-day holds). All can be exposed as MCP tools.
**Marketing line:** *"Cashfree Payouts + Reconciliation in your IDE — not just payment links."*

### Wedge 3: Self-hostable Indian-priced runtime
**Evidence:** 689 PRICE-SENSITIVE + 1,251 BUILT-OWN signals. Indian operators self-host n8n on Hetzner/AMD EPYC at 1/3 cost. Verbatim: *"Built a SaaS alone from India on $500/month hosting"* (r/indianstartups/1slxcj4).
**Implication:** Ship Relay-OSS as stripped-down core runnable via `git clone && npm start` on any Indian VPS. Eat the long tail Razorpay/Workato can't serve. Convert self-hosters to managed cloud as they scale.
**Marketing line:** *"Self-hostable. Indian-priced. Composable."*

### Wedge 4: Indian back-office stack (Tally + GST + WhatsApp + UPI + multi-PG recon)
**Evidence:** mcp-india-stack (community OSS) shipped GSTIN/IFSC/PAN/UPI-VPA/PIN validation as "first one in this space." 87+ reconciliation pain signals + Tally complaints + multi-PG matchup pain.
**Implication:** Cashfree-native settlement/refund/payout/dispute/mandate primitives + Tally MCP + GST MCP + WhatsApp BSP + UPI primitives = the back-office bundle nobody ships cleanly.
**Marketing line:** *"The Indian back-office stack — agents, not apps."*

### Sleeper Wedge 5: Latent positive Cashfree dev sentiment
**Evidence (verbatim):** *"Razorpay has the worst webhooks docs in the industry. Cashfree was easier to integrate."* — `dev_skeptic` on X. *"i go with Razorpay (it's 2%), setup is smooth… Cashfree or PhonePe can be slightly cheaper!"* — r/indianstartups/1s8fv1i.
**Implication:** Latent positive sentiment exists, nobody is amplifying it. Mothi-led content can pull this signal forward as part of the launch.
**Marketing line:** *"Devs already say Cashfree is easier to integrate. Now we're shipping the agent runtime to match."*

---

# Section 3: PRFAQ

## 3.1 Press Release

**HEADLINE:** Cashfree Launches Relay — the Open Payments-Native Workflow Platform for Indian Merchants and Developers, with MCP Server for Claude Code, Cursor, and AI Agents

**SUB-HEADLINE:** Build refund-recovery, RTO-prevention, settlement-reconciliation, and EdTech fee-reminder agents from a visual canvas or directly inside Claude Code — with first-class Cashfree triggers and 24+ tools across Payments, Payouts, and Reconciliation. No Technology Partner audit. No 6-week wait. Ship today.

**[Bengaluru, May 2026]** — Cashfree Payments today launched **Relay**, an open workflow automation platform built natively on Cashfree's payments rails. Relay lets Indian merchants design, deploy, and monitor automation across refund management, payment-failure recovery, settlement reconciliation, COD/RTO prevention, EdTech fee collection, and B2B invoice dunning — using either a visual drag-drop canvas or any AI coding assistant via the Cashfree Relay MCP server.

**The Problem:** Indian merchants spend 6–7 hours per week reconciling marketplace settlements, 2 hours per day chasing refund approvals, lose 2.2–3.4% of UPI payments to silent failures, and absorb 30–50% RTO rates that "eat margins alive." Existing solutions either lack payment-native context (Zapier, Pabbly, n8n) or ship pre-built agents merchants can't customize (Razorpay Agent Studio). Operators on Reddit describe the result: *"8 different apps. WhatsApp for customers, Excel for money, Canva for design, Razorpay for payments, Notion for tasks. Nothing talks to each other. Everything is manual."*

**The Solution:** Relay is the first composable, payments-native workflow automation platform built for Indian merchants. Built on Conductor OSS + ActivePieces, with Cashfree's payments primitives modeled as first-class triggers and actions, Relay ships across **three MCP servers — Payments, Payouts, and Reconciliation** — exposing 24+ tools that AI agents can compose into any workflow. Unlike Razorpay's fixed Agent Studio SKUs, every Relay workflow is composable and merchant-owned. Unlike n8n or Zapier, Relay's nodes know what a refund, settlement, RTO, or mandate is. Unlike Workato or Tray.ai, Relay starts with self-host-free and ₹999/month managed cloud — Indian-priced from day one.

**Customer Quote:** *"We replaced 6 brittle Zapier flows + 3 Excel workbooks with one Relay workflow that recovers ₹2.5L/week from failed payments. Building it took 20 minutes inside Claude Code."* — [TBD: target Indian D2C founder, beachhead pilot]
*[Flag: hypothetical — target real testimonial pre-launch from 5 design partners]*

**Getting Started:** Indian merchants on Cashfree Payment Gateway can request access at **relay.cashfree.com** today. Free tier covers 1,000 monthly executions and unlimited workflows. Self-host is free forever (Apache 2.0). Managed cloud Starter ₹999/month. **MCP server free for all merchants.** Application: Google Form, 5-minute review.

## 3.2 Customer FAQs

**Q: What is Relay?**
A: Workflow automation platform built natively on Cashfree's payments infrastructure, with both a visual builder and an MCP server for Claude Code/Cursor/Anthropic SDK/OpenAI Agents SDK/LangGraph/Vercel AI SDK/Mastra/CrewAI.

**Q: How is this different from Razorpay Agent Studio?**
A: Razorpay ships 8 fixed prebuilt agents you rent. Relay ships a composable kit — you build any workflow, you own the IP, you switch payment rails any time.

**Q: How is this different from n8n / Zapier / Pabbly?**
A: Those are payment-blind. Relay's triggers and primitives know what a refund, settlement, RTO, mandate, or chargeback is — without hand-rolling webhook plumbing.

**Q: Can I self-host Relay?**
A: Yes. Self-host on any Indian VPS (Hetzner/AMD EPYC/AWS) — free forever, Apache 2.0. Managed cloud is for ops teams who don't want to run it themselves.

**Q: Do I need a Technology Partner agreement to use Relay's OAuth?**
A: No. Open OAuth read-only access available to any registered developer. Production access (write) requires merchant approval — same as Cashfree PG signup.

**Q: How much does it cost?**
A: Self-host: free. Free cloud: 1,000 executions/mo + unlimited workflows. Starter ₹999/mo (10K executions). Growth ₹4,999/mo (100K executions). Enterprise custom (volume-linked).

**Q: Who is this for?**
A: Indian D2C brands (1K+ orders/mo), EdTech institutes, B2B agencies, lending NBFCs, and technical agencies/integrators serving them.

**Q: Can my non-technical ops team use it?**
A: Yes. Three docs tracks — Developer (build via MCP), Enterprise (multi-tenant + dedicated support), and **Consumer** (install Relay MCP into Claude Desktop / Cursor / VS Code — chat-driven workflow creation, no code).

## 3.3 Internal/Sales FAQs

**Q: Why are we building this?**
A: Convert Cashfree's existing PG mindshare into deeper merchant relationships before Razorpay's Agent Studio narrative cements. **Defensive:** avoid losing automation budget to Razorpay (their 8 agents already named SuperU + Zomato/Nugget). **Offensive:** increase ARPU per merchant 2–5x via workflow tier; reduce churn via stickier integrations; deflect Cashfree CS tickets upstream via merchant self-service workflows.

**Q: What's the competitive landscape?**
A: Razorpay Agent Studio + Razorpay MCP (largest direct threat — Codex + Replit India + SuperU partnerships). PayU MCP (parallel launch April 2026). n8n + Zapier + Pabbly + Make (horizontal generics). Quickwork (BFSI enterprise sleeper). Workato (only relevant upmarket).

**Q: What's the TAM?**
A: ₹240 Cr/yr addressable bottom-up (~$28M); $30M top-down on iPaaS slice. Year 1 SOM target: ₹4–25 Cr ARR.

**Q: What's the launch timeline?**
A: Soft launch May 2026 to existing Cashfree PG merchants + open access for developers. Public Day-0 launch with 5 marquee customer logos. T+30 Builders cohort. T+90 vertical hackathon. T+180 Inc42 AI Summit talk.

**Q: What's the differentiation against Razorpay?**
A: Open OAuth (no 6-week Tech Partner audit), Payouts + Reconciliation depth (Razorpay's MCP is payment-link only), self-hostable (Razorpay is enterprise SaaS only), and Indian back-office stack (Tally + GST + WhatsApp + multi-PG recon — Razorpay's 6 agents don't cover these).

**Q: What's the biggest risk?**
A: Razorpay narrative dominance. Their Agent Studio + Codex + Replit India + SuperU partnerships saturated dev/founder Twitter in last 30 days. Cashfree mention in builder communities is **3.6x weaker** (5 vs 18 in Agent C corpus). We need aggressive amplification on Day 0 + ongoing brand-warming via dev.to/Hashnode/GitHub/integration platforms.

**Q: What if we miss launch and ship in June instead of May?**
A: Razorpay press window already past peak; Inc42 trend piece will likely be Razorpay-led. Each week of slip costs us narrative space. **Recommendation: ship core (Payments MCP + 5 reference workflows + visual builder) in May; Payouts MCP + Reconciliation MCP can ship at T+30/T+60 as separate beats.**

---

# Section 4: Positioning & Messaging

## 4.1 Positioning Anchors

- **Primary:** Persona (Indian payment-using merchants and developers) + Capability (composable payments-native automation)
- **Secondary:** Problem (manual ops drag, Razorpay-only world, generic tools can't do payments) + Differentiator (open OAuth + Payouts/Recon depth + self-hostable + India back-office)

## 4.2 Positioning Statement

For Indian D2C, EdTech, and lending merchants who spend hours every week on manual refund approvals, payment recovery, RTO mitigation, and reconciliation, **Relay** is the open, composable workflow automation platform that lets ops teams and developers build payment-aware automations from a visual canvas or directly inside Claude Code — using triggers and actions that no horizontal tool models cleanly. Unlike Razorpay's fixed Agent Studio SKUs locked behind 6-week Technology Partner audits, Relay gives you full composability over 24+ MCP tools across Payments, Payouts, and Reconciliation. Unlike Zapier or n8n that don't understand Indian payments, Relay ships first-class triggers for `refund_initiated`, `settlement_posted`, `rto_flagged`, `mandate_lapsing`, and `chargeback_received`. And unlike enterprise iPaaS tools, Relay is self-hostable and Indian-priced from day one.

## 4.3 Positioning Line (10 words)

**Phase 1 (Developer Soft Unveil — Jun-Jul 2026):** *"Open payment workflows. Built where you build. Owned by you."*

**Phase 3 (GFF Headline Launch — Sep 1, 2026):** *"Agent workflows for India's payments infrastructure."*

The Phase 3 upgrade reframes the category claim from *workflow automation* (commodified — n8n/Zapier/Make territory) to *agent workflows* (frontier, where the discourse is moving per Agent C corpus: *"Agents own the task, not just execute steps"*; *"Is Claude rapidly replacing Make and n8n?"*). This is the headline framing for the GFF stage moment.

## 4.4 Message House (Atlassian)

**Roof:** Composable, payments-native automation Indian merchants own.

| | Pillar 1: Open & Composable | Pillar 2: Payments-Native | Pillar 3: AI-Native, Two-Way | Pillar 4: Indian-Priced, Self-Hostable |
|---|---|---|---|---|
| **Value Prop** | No 6-week Tech Partner audit. No fixed agent SKUs. Build any workflow. | First-class triggers and actions for the events that drive your business | Build by talking to Claude/Cursor; edit and monitor visually. Same backend, two doors. | Self-host on Hetzner free, or managed cloud from ₹999/mo. INR pricing. |
| **Proof** | Open OAuth read-only Day 0; 24+ MCP tools across 3 servers | 14 native triggers (refund, settlement, RTO, chargeback, mandate, payment-failed, dispute) | Cashfree Relay MCP — sub-60-sec time-to-first-workflow; visual builder for ops | Free self-host (Apache 2.0); ₹999 SMB tier; Indian payment-stack templates |
| **Customer Pain** | "Razorpay locked us out 120 days"; "I waited 6 weeks for Tech Partner approval" | "n8n webhooks are naked — no auth, no rate limiting, no Stripe hookups" | Tech merchants want code, ops want clicks; current tools force one mode | "Zapier $30/mo per seat doesn't accept INR billing well"; "we self-host because western SaaS is unaffordable" |

**"Only we can say this" tests:**
- Pillar 1: Razorpay can't say this without disrupting their Tech Partner program ✅
- Pillar 2: Generic tools can't say this without rebuilding their event model ✅
- Pillar 3: Razorpay has Conversational Dashboard but not builder + MCP + same-backend ✅
- Pillar 4: Workato/Tray.ai = enterprise pricing only; Pabbly = lifetime ₹20,900 but no MCP ✅

## 4.5 Elevator Pitches

**10 words:** *"Open payment workflows. Built where you build. Owned by you."*

**30 words:** *"Relay is Cashfree's open, composable workflow automation platform. Build refund, recovery, RTO, and reconciliation workflows from Claude Code or a visual canvas. Indian-priced. Self-hostable. No Tech Partner audit."*

**100 words:** *"Relay is the open, composable workflow automation platform Indian merchants and developers actually own. Designed for D2C brands, EdTech institutes, and B2B agencies drowning in manual refunds, RTO/COD, fee chasing, and reconciliation, Relay ships first-class triggers for refund, settlement, RTO, chargeback, and mandate events — primitives no horizontal tool models cleanly. Build workflows two ways: visually drag-drop, or by describing them in natural language inside Claude Code via the Relay MCP server. Unlike Razorpay's fixed Agent Studio SKUs locked behind a 6-week Tech Partner audit, every Relay workflow is composable and merchant-owned. Self-host free, or managed cloud from ₹999/month."*

## 4.6 Persona-Specific Messaging

| Persona | Pain (verbatim from corpus) | Message | Proof Point |
|---|---|---|---|
| **Founder-CEO (D2C)** | "I'm hiring my third ops associate just to keep up with refunds and recon" | "Replace ops headcount with composable workflows that fire on every refund, settlement, and RTO" | Pilot X reduced refund-followup from 2 hrs/day to 0; ROI in 14 days |
| **CTO (D2C / SaaS)** | "We hand-rolled Zapier flows that broke and we're tired of maintaining them" | "Define workflows in Claude Code, deploy from your IDE, monitor in our dashboard" | MCP server + 24 tools + sub-60-sec time-to-first-workflow + 6 framework adapters |
| **Founder-CEO (EdTech)** | "Fee follow-ups eat 2 days/month and we still miss collections" | "Automate fee reminders + payment links + WhatsApp + auto-NACH retry — set once, runs forever" | Edtech pilot: 85% on-time vs 55% baseline (industry benchmark) |
| **Tech Agency Lead** | "I build Zapier flows for clients but can't charge recurring; they own the workflow" | "Embed Relay for your client portfolio. Charge for the workflow, not just the build." | Agency pilot pricing model + Cashfree partner program |
| **Indian Self-Hoster** | "Western SaaS is unaffordable; we self-host n8n on Hetzner" | "Self-host Relay free forever. Convert to managed cloud only when you scale." | Open-source Apache 2.0 core; Hetzner deploy guide; community Slack |

## 4.7 Competitive Messaging

- **vs Razorpay Agent Studio:** *"Razorpay sells you 8 fixed agents and locks settlements 120 days. Relay gives you the workflow kit and same-day settlements. Workflows you own, not agents you rent."*
- **vs n8n:** *"n8n webhooks are naked. Relay's nodes know what a refund, settlement, and RTO are. Plug-and-play, not plumb-from-scratch."*
- **vs Zapier:** *"Zapier's USD pricing scales painfully fast. Relay is INR-priced and Cashfree-deep — with an MCP server that meets you in Claude Code."*
- **vs Pabbly:** *"Pabbly's lifetime deal is great until you need to chain Cashfree primitives or build via Claude Code. Relay does both."*
- **vs Workato/Tray.ai:** *"Enterprise iPaaS starts at $20K/year. Relay starts at free self-host or ₹999/mo cloud."*
- **vs Status Quo:** *"Instead of Slack-DM refund approvals, Excel reconciliation, and 8 disconnected apps, Relay turns your payment lifecycle into one canvas that runs forever."*

## 4.8 Headline Variants (A/B test)

1. **Capability + Persona:** *"Open payment workflows for Indian merchants. Built where you build."*
2. **Problem + Outcome:** *"Stop paying ops to chase refunds. Relay automates your payments lifecycle."*
3. **Status-quo displacement:** *"Replace 6 Zaps + 3 spreadsheets with 1 Relay."*
4. **Razorpay-direct:** *"The open alternative to Razorpay Agent Studio. No 6-week audit. No fixed SKUs."*

---

# Section 5: GTM Launch Plan (5-Phase, ~18 weeks to GFF 2026)

## 5.1 Phasing Overview

**Why phased, not single-launch:** Cashfree Relay's current state is **private beta access only**, not public release. A single Tier-1 May launch would (a) burn the press window before product is hardened, (b) violate the private-beta NDA posture with design partners, and (c) mismatch the natural cadence of Indian fintech press, which converges on **Global Fintech Fest (GFF) — Mumbai, Sep 1-7, 2026** as the year's flagship moment.

The 5-phase plan respects all three constraints, builds template inventory + community proof during runway, and frames GFF as the headline public moment under the **"Agent Workflows for India's payments infrastructure"** category claim.

| Phase | Window (~weeks) | Stage | Public posture | Goal |
|---|---|---|---|---|
| **0 — Private Beta** | Apr 29 → May 31 (5 wk) | Current | NDA-only · zero public Relay content | **Sign 2-3 enterprise design partners** + 3-5 mid-market; resolve `Map<String,Object>` blocker |
| **1 — Developer Soft Unveil** | Jun 1 → Jul 15 (6 wk) | Restricted public access | "Early access" framing only · no headline tweets | Seed dev awareness; 6 templates ship; OAuth opens; Latent Space + Pragmatic Engineer pre-briefed for GFF |
| **2 — Template Gallery + Cohort Apps** | Jul 15 → Aug 31 (7 wk) | Wider beta | Hashnode/dev.to articles drop · GitHub PRs land · Builders applications open | Build 15-20 templates + community proof for GFF |
| **3 — GFF 2026 Headline Launch** | Sep 1-7 (1 wk) | **Public flagship** | Akash/Reeju/Mothi keynote · press embargo lifts · Mothi launch tweet drops | "Agent Workflows for India's payments infrastructure" — full multi-channel launch |
| **4 — Post-GFF Compound** | Sep 7 → Dec 2026 (16 wk) | Sustained | Hackathon · podcasts · festive Q4 · ecosystem report | Convert GFF momentum → ARR + cohort outputs |

**Total runway: ~18 weeks. GFF is the gate. Phases 0-2 are runway; Phase 3 cannot slip.**

**Budget allocation (across all phases):** PR + content 40% · Sales enablement 20% · CS enablement 15% · GFF event + partnerships 15% · Paid amplification 10%

---

## 5.2 Phase 0 — Private Beta Protocol (Apr 29 → May 31)

**Goal:** Harden product with select design partners under NDA. **Sign 2-3 enterprise design partners** running Relay in production-grade pilots — these become the marquee logos at GFF.

### Public posture
**Strict NDA. Zero public-facing Relay content.** No tweets from Mothi naming Relay. No press inquiries answered. Internal Cashfree all-hands deck only.

### Enterprise design partner profile
- Indian co with **₹100Cr+ ARR or 50K+ orders/month**
- Already on Cashfree PG (preferred) or willing to migrate
- Tech team that can engage with MCP + visual builder during beta
- Measurable, automation-solvable pain (RTO 30%+, manual refund mgmt, multi-PG recon, fee chasing, payouts pipeline)
- **Public brand recognition for GFF press value** ("Made on Relay" booth showcase)

### Target enterprise list (Sales pursue in concentrated ABM)
- **D2C scale-ups:** BOAT, Mamaearth, Sugar Cosmetics, Plum, Wakefit, Bombay Shaving Co, Mokobara, The Souled Store
- **EdTech mid/large:** Vedantu, Aakash, PhysicsWallah, Allen, Toppr, Adda247
- **Lending NBFCs:** Lendingkart, KreditBee, MoneyTap, OneCard, Slice, Indifi, Kissht
- **B2B SaaS / Cashfree top-100 by GMV:** existing premium PG merchants

### Phase 0 deliverables
- [ ] **2-3 enterprise design partners signed under NDA** with named program contacts
- [ ] 3-5 mid-market design partners signed
- [ ] `Map<String,Object>` payload-shape blocker resolved (Subbu/Vinesh/Vishal)
- [ ] Three-server MCP architecture restructure complete (Payments / Payouts / Reconciliation)
- [ ] 6 reference workflows hardened in beta env (RTO Shield, Refund Recovery, Settlement Watchdog, Payout Pipeline, Payment Recovery, EdTech Fee Engine)
- [ ] Internal Cashfree sales enablement complete (battle cards for design partners only)
- [ ] CS team trained on Relay troubleshooting
- [ ] **GFF talk slot submission + booth confirmed by mid-May (absolute deadline)**
- [ ] Mintlify docs draft (Shanth)
- [ ] Phase 1 asset prep started (Hashnode/dev.to article outlines)

### Phase 0 Mothi role
- **Co-pitch with Sales** to enterprise prospects (PMM positions vision; Sales closes)
- Help shape pilot scoping with each design partner (which workflows to build first)
- Capture case-study material as pilots run (quotes, metrics, before/after)
- **Public posture: silent on Relay externally.** Internal all-hands only.
- GFF talk submission: Mothi or Akash/Reeju as speaker

### Phase 0 success metrics
- 2-3 enterprise design partners signed (named: TBD)
- 3-5 mid-market partners signed
- ≥3 production-grade workflows running per partner
- `Map<String,Object>` blocker resolved
- 6 reference workflows hardened
- GFF talk + booth confirmed

---

## 5.3 Phase 1 — Developer Soft Unveil (Jun 1 → Jul 15)

**Goal:** Seed dev awareness with limited public access. Build incremental momentum into Phase 2/3, but **do not headline-launch** — that's reserved for GFF Phase 3.

### Public posture
`relay.cashfree.com/developers` + `/docs` go live. **No `/enterprises` page yet** (still under design partner motion). Mothi tweets incrementally — *"early access"* framing only, not *"Introducing Relay."* No press push.

### Phase 1 deliverables
- [ ] relay.cashfree.com/developers + /docs live
- [ ] `npx @cashfreepayments/relay-mcp` works locally (Stripe-style sub-60-sec hello world)
- [ ] Open OAuth read-only Day 1 of Phase 1
- [ ] 3 MCP servers live on production endpoints
- [ ] 6 starter templates in public gallery + open-sourced on GitHub (Apache 2.0)
- [ ] 6 framework adapters: OpenAI Agents SDK, Anthropic, LangGraph, Vercel AI SDK, Mastra, CrewAI
- [ ] /builders/llms.txt + llms-full.txt at predictable URLs
- [ ] Self-host repo public on GitHub
- [ ] Mintlify docs final
- [ ] **3-4 founding-team articles drop on Hashnode + dev.to** (Mothi + Vinesh + Vishal + Subbu rotating bylines)
- [ ] Cashfree internal merchant outreach to top-100 PG merchants (private beta upgrade pitch)
- [ ] **Latent Space + Pragmatic Engineer pre-briefed under embargo for GFF**
- [ ] GFF keynote slide deck draft begins

### Phase 1 Mothi role
- Tweet incremental updates ("Just shipped first payment template on Relay — RTO Shield in 200 LOC") — NOT headline launch
- Author 2-3 Hashnode/dev.to articles (technical-narrative authority building)
- Reply-camp on dev community Twitter (n8n / Claude Code / MCP discourse)
- Coordinate Latent Space + Pragmatic Engineer pre-briefs

### Phase 1 positioning line
*"Open payment workflows. Built where you build."* (kept; Phase-3 upgrade to *"Agent workflows for India's payments infrastructure"* comes at GFF)

### Phase 1 success metrics
- 500 MCP installs (npx pulls)
- 100 active workflows (non-design-partner)
- 50 qualified leads to Sales
- 3-4 dev articles published
- 5K landing-page visits
- Time-to-first-workflow: <10 min median
- ≥2 enterprise design partners ready to be public reference logos at GFF

---

## 5.4 Phase 2 — Template Gallery + Cohort Applications (Jul 15 → Aug 31)

**Goal:** Build template inventory and community proof for GFF. Open Builders cohort applications.

### Public posture
Building dev community surface area. Hashnode/dev.to drum-beat continues (1 article/week). GitHub PRs into n8n / ActivePieces / Composio / Pipedream land. Still no headline press.

### Phase 2 deliverables
- [ ] Template gallery expands to **15-20 templates** (community-contributed where possible)
- [ ] "Made on Relay" page launches with consenting design partner workflows
- [ ] Hashnode/dev.to articles continue (target: 1/week, 7-9 total in Phase 2)
- [ ] GitHub PRs into `n8n-io/n8n`, `activepieces/activepieces`, `modelcontextprotocol/servers`, Composio registry land
- [ ] **Composio + Pipedream + Replit + Cursor** integration listings live (currently absent — Razorpay-zero whitespace)
- [ ] **"Relay Builders" cohort applications open** via Google Form (50-spot, gated)
- [ ] Cashfree Sales runs ABM to Tier-2 merchants (1K-50K orders/mo)
- [ ] Subbu's `npx @cashfreepayments/agent-skills add relay-skills` ships
- [ ] **GFF prep: keynote final, booth design final, 12-15 demo agents prepared, partner co-launches confirmed (Bolna, possibly Anthropic India + AWS India)**
- [ ] Inc42/YourStory/Storyboard18/ITBrief pre-briefs under embargo
- [ ] Customer testimonial videos with 2-3 design partners

### Phase 2 Mothi role
- 1 Hashnode/dev.to article per week (technical authority)
- Curate Builders cohort applications + first wave of acceptances
- GFF keynote rehearsal
- Co-pitch with Sales on Tier-2 ABM accounts

### Phase 2 success metrics
- 2K MCP installs cumulative
- 500 active workflows
- 100-200 cohort applications
- 15-20 templates live
- 10 dev articles total
- 2-3 design partner case-study videos
- GFF assets 100% ready

---

## 5.5 Phase 3 — GFF 2026 Headline Launch (Sep 1-7, Mumbai)

**Goal:** THE public flagship moment. Frame as **"Agent Workflows for India's Payments Infrastructure."**

### Public posture
Maximum. Multi-channel coordinated launch. All Tier 1-3 amplification surfaces fired (see § 5.10).

### GFF Day 1 (Sep 1, 2026) hour-by-hour
- **9:00 AM IST:** Akash + Reeju + Mothi keynote at GFF stage — category claim launch
- **9:00 AM IST:** Mothi-led launch tweet drops (Anuj-format, see § 5.11)
- **9:15 AM:** Akash + Reeju retweet/quote-tweet
- **9:30 AM:** Cashfree corporate handle amplifies
- **10:00 AM:** Press embargo lifts — Inc42 + YourStory + Storyboard18 + ITBrief + Analytics Insight + Adgully + CXOToday all publish coordinated
- **11:00 AM:** AWS press center release (if AWS India co-launch ships)
- **Booth opens with 12-15 "Made on Relay" live demos** (built by design partners + Phase 1-2 community)
- **Continuous:** Mothi reply-camps mentions for 4 hours; engages every dev question
- **6:00 PM:** Latent Space podcast embargoed for T+3
- **Day 2 (Tue Sep 2) 9:30 PM IST = 9 AM PT:** HN Show HN posted (separate moment, separate spike)

### GFF Day 2-7 (Sep 2-7)
- Booth demos continue (10-hour days)
- 50 Builders cohort officially announced + named publicly
- LinkedIn posts sustained (Akash + Reeju + Mothi daily)
- Press follow-ups: Lenny's, TWIML, Practical AI podcast pitches
- Customer panels at booth (design partner + Builders)

### Phase 3 positioning line — UPGRADED
**"Agent workflows for India's payments infrastructure."**

(Reframes category from "workflow automation" — commodified, me-too — to "agent workflows" — frontier, where discourse is moving per Agent C corpus: *"Agents own the task, not just execute steps"*. Headline framing for the GFF stage.)

### Phase 3 deliverables
- [ ] GFF keynote delivered
- [ ] 12-15 live demos at booth
- [ ] **5-8 named customer logos public** — 2-3 enterprise + 3-5 mid-market design partners
- [ ] 50 Builders cohort named publicly
- [ ] Mothi-led launch tweet (target: 100K+ views in 48h)
- [ ] All Tier 1-3 amplification surfaces fired
- [ ] **Open enterprise tier + custom pricing announced**
- [ ] /enterprises page goes live
- [ ] Latent Space podcast records T+3
- [ ] Pragmatic Engineer essay drops T+7

### Phase 3 success metrics
- 100K+ launch tweet views
- 25K+ landing page visits in launch week
- 10K MCP installs cumulative
- 1K active workflows
- 200 paid merchants on Relay
- **5-8 named customer logos** for press + sales deck
- 200+ Builders cohort applications post-launch (additional, on top of Phase 2)
- 10+ tier-1 press pickups
- HN front page achieved

---

## 5.6 Phase 4 — Post-GFF Compound (Sep 7 → Dec 2026)

**Goal:** Convert GFF momentum into sustained ARR + ecosystem.

### Phase 4 deliverables
- **Vertical hackathon** Sep 15 → Oct 31 (6-week format) — *"Best D2C agent on Relay"* with Bolna + Anthropic India + AWS India co-hosts
- **Festive Q4 push** (Oct-Nov) — D2C festive RTO surge + Diwali ops use cases promoted heavily
- **"First 100 Relay Builders" ecosystem report** — Inc42 + Google Bharat AI Startups Report submission
- **Inc42 AI Summit Bengaluru** — Mothi-on-stage talk
- **Mothi podcast circuit:** Latent Space (recorded Phase 3), Pragmatic Engineer essay live, Lenny's, TWIML, Practical AI
- **Cohort 2 applications** open (next 100 Builders)
- **AI Engineer Summit workshop CFP** submission for next event
- **Q4 year-end content** — *"What we shipped in 2026"* wrap

### Phase 4 success metrics
- 1K paid merchants by end Dec 2026
- ₹3-5 Cr ARR run rate
- 70%+ M2 retention
- NPS 40+ on Relay-active cohort
- 50+ public cohort outputs (workflows shipped to production)
- 3+ founders/CTOs publicly tweeting workflows weekly
- Inc42 ecosystem report published

---

## 5.7 Three-Server MCP Architecture (Swiggy steal)

Restructure the current 24-tool monolithic MCP into **3 sub-servers** for clearer narrative + tool granularity:

| Server | Endpoint | Tools | Audience |
|---|---|---|---|
| **mcp.cashfree.com/payments** | OAuth | ~10 (payment_link, txn_lookup, refund, dispute_evidence) | Default for D2C, EdTech |
| **mcp.cashfree.com/payouts** | OAuth | ~8 (bulk_disbursement, beneficiary_create, mandate_create) | Lending NBFCs, agencies |
| **mcp.cashfree.com/reconciliation** | OAuth | ~6 (settlement_pull, utr_match, anomaly_alert) | Finance ops, multi-channel D2C |

Marketing claim: *"3 MCP servers covering the full Indian payments stack."* (mirrors Swiggy's 3-vertical claim)

**`Map<String,Object>` fix is gating: must land in Phase 0.** Each tool ships with strongly-typed JSON schema. LLMs structure inputs reliably.

## 5.8 Use Case + Template Priority (phase-aware)

Phase 0 hardens 6 reference workflows with design partners. Phase 1 ships them publicly. Phase 2 expands to 15-20. Phase 3 showcases 30+ at GFF.

| Priority | Use case | Total signal | Phase |
|---|---|---|---|
| **P0** | RTO/COD prevention ("RTO Shield") | 837 | Phase 0 → 1 |
| **P0** | Refund management HITL ("Refund Recovery") | 1,500+ | Phase 0 → 1 |
| **P0** | Reconciliation anomaly alerts ("Settlement Watchdog") | 218+ | Phase 0 → 1 |
| **P0** | Payouts orchestration ("Payout Pipeline") | 346 | Phase 0 → 1 |
| **P0** | Payment failed → WhatsApp recovery | 357 | Phase 0 → 1 |
| **P1** | EdTech scheduled fee reminders ("EdTech Fee Engine") | 222 | Phase 1 → 2 |
| **P1** | Bolna voice — abandoned cart | 287 | Phase 2 (Bolna co-launch) |
| **P2** | B2B invoice dunning ("Agency Dunning") | 172 | Phase 2 → 3 |
| **P2** | Subscription dunning Shopify+Appstle | 23 | Phase 4 |
| **CUT** | Cohorts → Google Ads sync | <10 | **Cut from launch** |

Phase 2 expansion targets (community-contributed, 15-20 total): GST recon, Tally sync, Multi-PG matchup, UPI silent-fail watcher, Dispute evidence assembler, Mandate-lapsing watch, Chargeback responder, Fee defaulter escalator.

Phase 3 GFF showcase (30+): mix of Cashfree-built + Phase 1-2 community + design partner workflows.

## 5.9 Stakeholders (DIN — Google Decide/Input/Notify)

**Decide:** Mothi (PMM) · Joe Dominic (PM) · Ramkumar V (eng leadership)

**Input:** Vinesh (Eng Lead), Vishal Yadav (BE — payload sign-off), Subbu (Architect — skills + 3-server architecture), Karthik Vyas (BE — Bolna integration, scheduled triggers), Hari/Mayank.B/Sarvesh.B (FE), Akash Sinha (CEO — exec narrative + LinkedIn), Reeju Datta (CXO — same), **Sales Lead (now also owns enterprise design partner pursuit Phase 0)**, Content Lead, Shanth SM (docs), Sourabh Shah (load test sign-off), Saksham (skills CLI), Satyam Tripathi (MCP)

**Notify:** CS team, Support, Cashfree partner ecosystem (Shopify agencies, Bolna, Anthropic, AWS India), existing PG merchants list, internal all-hands, investors/Board, GFF organizers

## 5.10 Amplification Surfaces by Phase

Different phases need different surfaces. **Don't fire Phase 3 surfaces in Phase 1.**

| Phase | Mothi Twitter | LinkedIn (Akash/Reeju) | dev.to / Hashnode | GitHub | Press | Podcasts |
|---|---|---|---|---|---|---|
| **0** | Silent on Relay | Silent | Silent | Silent | Silent | Silent |
| **1** | Incremental "early access" tweets | Low-key | 3-4 articles | Self-host repo public | Pre-briefs only (embargoed for GFF) | Latent Space pre-brief |
| **2** | Articles + replies | Same | 7-9 articles | PRs to n8n/ActivePieces/Composio land | Pre-briefs continue | — |
| **3** | **Headline launch tweet (Sep 1, 9 AM IST)** | Headline posts daily | All articles live | Composio + Pipedream + Replit + Cursor listings | **Embargo lifts:** Inc42, YourStory, ITBrief, Storyboard18, AWS India press | Latent Space records T+3 |
| **4** | Sustained content | Sustained | 1-2/week | Continued upstream contributions | Inc42 ecosystem report; Forbes, MoneyControl | Pragmatic Engineer essay; Lenny's, TWIML, Practical AI |

**Tier 1 surfaces to brief pre-launch (Phase 1-2 embargoed for Phase 3):**
1. Latent Space (swyx + Alessio) — exclusive: *"first open, composable, self-hostable payments-MCP from India"*
2. The Pragmatic Engineer (Gergely Orosz) — co-author technical interview with Vinesh + Subbu on three-server architecture
3. Inc42 / YourStory exclusive — Akash + Reeju framing the launch as Cashfree's category claim at GFF
4. AWS India press team — if Bedrock/AgentCore co-launch ships

**Tier 2 (Phase 3 fire-day-one):** Logan Kilpatrick · Mahesh Murag · Ben Tossell · BG Mahesh · MCP community lists (mcp.composio.dev, mcpservers.org, pulsemcp.com, awesome-mcp-servers) · Cloudflare blog (if MCP on Workers)

**Tier 3 (Phase 3 India press blast — Swiggy's playbook):** YourStory · Storyboard18 · ITBrief · Analytics Insight · Adgully · CXOToday · Inc42 · MoneyControl · Forbes India · buildfastwithai · productgrowth.in · superlaunch.in · GROWAI · Techarion · GigaNodes · n8ntraining.in

## 5.11 GFF Day-1 Launch Tweet (Mothi-led, Anuj-format) — fires Sep 1, 2026

```
Introducing Cashfree Relay.

Agent workflows for India's payments infrastructure.

We're opening Cashfree's payments stack to developers and enterprises — build AI agents, workflows, and integrations on top of our Payments, Payouts, and Reconciliation MCP servers. Real merchants. Real INR moving. Real users.

What you get:
• 3 MCP Servers (Payments / Payouts / Reconciliation)
• 24+ tools across the Indian payments stack
• Production access from Day 0 (no Technology Partner audit)
• Self-hostable. Indian-priced.
• Direct engineering support

Who it's for:
• Individual devs with bold ideas
• Startups building payments-native products
• Enterprises looking to embed Cashfree

RTO Shield agents. Refund Recovery bots. Settlement Watchdog. EdTech Fee Engine. B2B Dunning automations.

If it makes payments better for merchants, we want to see it.

Ship something great and we'll feature it. Ship something exceptional and our recruiting team might reach out.

Built on Relay — by [list 5-8 named design partners + cohort builders].

→ relay.cashfree.com
→ npx @cashfreepayments/relay-mcp (works locally before approval)
```

**Posting protocol (GFF Day 1, Sep 1, 2026):**
- 9:00 AM IST: Mothi posts the tweet
- 9:15 AM: Akash + Reeju retweet/quote-tweet from their accounts
- 9:30 AM: Cashfree corporate handle amplifies
- 10:00 AM: Mothi follow-up tweet with relay.cashfree.com link + booth location
- Continuous: Mothi reply-camps mentions for first 4 hours
- Show HN posted Tue Sep 2, 9 AM PT (= 9:30 PM IST same day) — separate spike

**Target:** 100K+ views in 48h, 200+ application submissions in launch week.

## 5.12 Per-Phase Success Metrics (summary)

Detailed metrics per phase in §§ 5.2-5.6 above. Headline:

- **Phase 0** (5 wk): 2-3 enterprise design partners signed · 3-5 mid-market · `Map<String,Object>` resolved · 6 reference workflows hardened · GFF talk + booth confirmed
- **Phase 1** (6 wk): 500 MCP installs · 100 active workflows · 50 Sales leads · 3-4 dev articles · time-to-first-workflow <10 min
- **Phase 2** (7 wk): 2K MCP installs · 500 active workflows · 100-200 cohort applications · 15-20 templates live · 10 dev articles total
- **Phase 3** (1 wk): 100K+ tweet views · 25K+ landing visits · 10K MCP installs · 1K active workflows · 200 paid merchants · 5-8 named customer logos · 10+ tier-1 press pickups · HN front page
- **Phase 4** (16 wk to end Dec): 1K paid merchants · ₹3-5 Cr ARR · 70%+ M2 retention · NPS 40+ · Inc42 ecosystem report

**Anti-metrics (do NOT track — Hattie's 6 OKR anti-patterns):** total page views (vanity); MCP tool count (Satyam already flagged consolidation); cumulative workflows lifetime (track active); press release count (look at quality of pickup); Slack channel members (movement-LARP); "MCP server uptime" (table stakes).

## 5.13 Risks + Mitigations

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 1 | Razorpay launches Agent Studio v2 in Relay's GFF window | Medium | High | Pre-line up press exclusives 2 weeks before GFF; counter-frame as "open vs gated"; secure GFF keynote slot before Razorpay does |
| 2 | Payload-shape `Map<String,Object>` causes dev churn | High | High | Resolve in Phase 0 (Subbu/Vinesh/Vishal). **If unresolved by mid-May, slip Phase 1 to Jun 15. DO NOT slip Phase 3.** |
| 3 | Bolna adds workflow builder | Low | Medium | Lock co-launch in Phase 2; revenue share on Bolna voice nodes |
| 4 | PayU MCP gets quoted in same GFF press as Relay | Medium | Low | Differentiate sharply at GFF — *"we have a builder + 3 servers + self-host, not just APIs"*; secure exclusives to YourStory + Inc42 |
| 5 | n8n India community calls Relay an ActivePieces fork | High (it IS a fork) | Medium | Ship Relay-OSS Phase 1 (Apache 2.0); counter: *"Yes — plus Cashfree-native triggers + India-priced cloud + India-located support"* |
| 6 | Cashfree Sales pitch Auto Collect when merchant needs Relay | High | High | Phase 0 enablement: explicit decision tree (Auto Collect vs Relay vs both) |
| 7 | Cashfree brand voice 3.6x weaker than Razorpay | Confirmed | High (long-term) | Aggressive Phase 1-2 community-building (Mothi-Twitter + dev.to/Hashnode + GitHub PRs + integration platform listings); explosive Phase 3 GFF amplification |
| 8 | "First Indian payments-MCP" narrative already lost to Razorpay | Confirmed | Medium | Don't fight that narrative. Reframe: GFF launch = first **open, composable, self-hostable, agent-workflow** payments-MCP — different category claim |
| **9 (NEW)** | **Phase 0 enterprise design partner pursuit fails to close 2-3** | Medium | High | Cashfree Sales runs concentrated ABM Apr 29 → May 15; Mothi co-pitches; offer first-year free + dedicated engineering support as design partner sweetener; if <2 signed by mid-May, slip Phase 1 by 2 weeks |
| **10 (NEW)** | **GFF talk slot not secured** | Low | **Critical** | Submit GFF talk by mid-May absolute deadline; have Akash + Reeju + Mothi as backup speaker options; backup: book booth-only if no keynote |

---

# Appendix A: Evidence Corpus Summary

| Source | Signals | Window | Key Insight |
|---|---|---|---|
| dtc-research (existing) | 28,253 rows | Late 2025 → Apr 2026 | RTO/COD = #1 India D2C pain; refund-velocity = weak; Razorpay relationship = gravitational center |
| Workflow automation competitive scan (Agent 1) | 13 competitors | April 2026 | MCP is table stakes; n8n owns Indian dev mindshare; Pabbly owns SMB |
| India payments+automation landscape (Agent 2) | Sector study | Q1 2026 | Razorpay Agent Studio launched March 11–12; PayU MCP April 2026; D2C pain quantified |
| MCP-first GTM playbooks (Agent 3) | 8 launch case studies | 2024–2026 | 7 tactical moves; cohort launch + framework adapters + third-party narrative |
| Indian Reddit dev/business (Agent A) | 2,316 conversations | 30 days | Razorpay Agent Studio HIGHLY visible in India; Cashfree mentions 21 (mixed); BUILT-OWN signal 1,251 |
| Global automation+AI Reddit (Agent B) | 5,143 conversations | 30 days | Cursor + n8n + Claude Code dominate; Razorpay Agent Studio invisible globally |
| Featurebase + merchant pain (Agent D) | 1,127 distinct signals | 90 days | RTO #1 (465); Refund mgmt #2 (391); SaaS-Agency persona stronger than expected |
| dev.to + Hashnode + GitHub + IH + X (Agent C) | 13,976 signals | 30 days | Cashfree mentions 5 vs Razorpay 18 (3.6x voice gap); MCP crossed chasm; Indian builder cost stack different |
| **TOTAL** | **~50,000+ signals** | | |

---

# Appendix B: Operator Language to Steal Verbatim

Per `dtc-research/CLAUDE.md`: use operator language verbatim, not corporate-speak.

**RTO/COD:**
- "RTO%"
- "fake COD orders"
- "Sunny scammer" (specific scammer, r/StartUpIndia/1od3x24)
- "weight discrepancy"
- "prepaid only"
- "RTO eats my margins"

**Payment failures:**
- "UPI failure rate" / "UPI stuck at processing"
- "involuntary churn"
- "throwing money away at the checkout page"
- "warm leads who drop off"
- *"the email comes from Razorpay, not from us"*

**Razorpay-specific:**
- "120-day settlement hold"
- "they suddenly blocked our service"
- "Tech Partner program = 6 weeks of audit"
- *"worst webhooks docs in the industry"*

**Reconciliation:**
- *"Two people on our team lost every Tuesday to spreadsheet matching"*
- *"8 different apps. Nothing talks to each other. Everything is manual"*
- *"three hours every week"*

**Pricing-sensitivity:**
- "Western SaaS is unaffordable"
- *"Built a SaaS alone from India on $500/month hosting"*
- *"We self-host n8n on Hetzner, saving 90%"*

**Latent positive Cashfree (amplify):**
- *"Cashfree was easier to integrate than Razorpay"*
- *"Cashfree or PhonePe can be slightly cheaper"*
- *"1.6% promo for first year"*

---

# Appendix C: Battle Cards (1-line each)

**vs Razorpay Agent Studio:** *"Razorpay sells you 8 fixed agents and locks settlements 120 days. Relay gives you the workflow kit and same-day settlements. Workflows you own, not agents you rent."*

**vs n8n:** *"n8n webhooks are naked. Relay's nodes know what a refund, settlement, and RTO are. Plug-and-play, not plumb-from-scratch."*

**vs Zapier:** *"Zapier's USD pricing scales painfully. Relay is INR-priced and Cashfree-deep — with an MCP server that meets you in Claude Code."*

**vs Pabbly:** *"Pabbly's lifetime deal is great until you need to chain Cashfree primitives or build via Claude Code. Relay does both."*

**vs Workato/Tray.ai:** *"Enterprise iPaaS starts at $20K/year. Relay starts at free self-host or ₹999/mo."*

**vs PayU MCP:** *"PayU shipped tools. Relay shipped a builder + 3 servers + self-host."*

**vs Status Quo:** *"Instead of Slack-DM refund approvals + 8 disconnected apps, Relay turns your payment lifecycle into one canvas."*

---

# Appendix D: Mothi-Personal Brand Compounding (your $500K leg-1 angle) — phase-aligned

8-month brand-building arc compounded by phased rollout. Each phase establishes public artifacts tied to your name.

| Phase | Window | Public artifact | Compounding effect |
|---|---|---|---|
| **0 — Private Beta** | Apr 29 → May 31 | Internal: closing 2-3 enterprise design partners as PMM | **Internal promo signal** — visible leadership of flagship product before any external content |
| **1 — Developer Soft Unveil** | Jun 1 → Jul 15 | 3-4 Hashnode/dev.to articles + Twitter reply-camp on dev/MCP discourse | **Establishes technical-PMM authority externally** — recruiter-indexable |
| **2 — Template Gallery + Cohort Apps** | Jul 15 → Aug 31 | Builders cohort program announcement (you own it) + 7-9 more articles + GFF keynote rehearsal | **Program ownership + content authority + GFF runup** |
| **3 — GFF Headline Launch** | Sep 1-7 | GFF stage keynote (or co-keynote with Akash/Reeju) + Mothi-led launch tweet (target 100K+ views) | **Public face of "Agent Workflows for India's payments infrastructure"** on national fintech stage |
| **4 — Post-GFF Compound** | Sep 7 → Dec 2026 | Latent Space podcast, Pragmatic Engineer essay, Lenny's, Inc42 AI Summit, ecosystem report | **PMM voice of Indian payments-AI category** |

**External brand artifact list to capture per phase:**
- 1× LinkedIn post per phase (anchor for recruiters)
- 1× Twitter thread per phase (audience growth)
- 2-3× dev.to or Hashnode articles per phase (SEO + indexable)
- 1× podcast appearance per phase from Phase 3 onwards (Latent Space / Pragmatic Engineer / Lenny's / TWIML)

**End state by Dec 2026:** 5 phases × ~4 artifact types = ~20 indexed public artifacts tied to your name, all about Indian payments-AI category. Recruiter-discoverable. Compounds Cashfree promo case AND indie-leg-2 reach for whatever you ship next.

---

# Appendix E: Swiggy Builders Club Playbook → Cashfree Relay translation map

Comprehensive 1:1 mapping from every Swiggy URL/pattern to its Cashfree-Relay equivalent. This is the playbook to copy.

## Source URLs (all from `mcp.swiggy.com/builders/`)

| Swiggy URL | What it teaches | Cashfree equivalent | Phase |
|---|---|---|---|
| `/builders/` | Hub page · 3-server narrative · Real APIs/data/users framing | `relay.cashfree.com/builders/` (or `/`) | Phase 1 |
| `/builders/blog/2026-04-17-builders-club-launch/` | Launch blog complementing tweet · narrative depth | `relay.cashfree.com/blog/2026-09-01-relay-launch/` | Phase 3 GFF Day 1 |
| `/builders/developers/` | 4-pillar dev page · 6 imagination prompts · 4-step hiring path · "No whiteboard puzzles" | `relay.cashfree.com/developers/` | Phase 1 |
| `/builders/enterprises/` | Enterprise track · Powered-by co-branding · dedicated partner manager · custom rate limits | `relay.cashfree.com/enterprises/` | Phase 3 (delayed from Phase 1) |
| `/builders/docs/` | 4-pillar IA (Start/Build/Reference/Operate) · 3-track audience (Dev/Enterprise/Consumer) · framework adapter list | `relay.cashfree.com/docs/` | Phase 1 |
| `/builders/docs/consumer` | Consumer track — install MCP into Claude Desktop / ChatGPT / Cursor for non-tech users | `relay.cashfree.com/docs/consumer` | Phase 3 (TAM expansion) |
| `/builders/access/` | Application flow + review criteria | `relay.cashfree.com/access/` (Google Form) | Phase 2 (cohort) |
| `/builders/llms.txt` + `/builders/llms-full.txt` | AI auto-discovery at predictable URLs | Same paths under relay.cashfree.com | Phase 1 |
| `/builders/#faq` | Public FAQ on hub page | Public FAQ at `/faq` (subset of § 3.3) | Phase 1 |
| Anuj launch tweet (181K views) | Outcome-led headline · Anuj-format scaffold | Mothi GFF Day-1 tweet (§ 5.11) | Phase 3 Sep 1 |

## Pattern → translation table

| # | Swiggy pattern | Cashfree-Relay translation | Where in this doc |
|---|---|---|---|
| 1 | "Real APIs. Real users. Real chance to get hired." | "Real merchants. Real INR moving. Real users." | § 5.11 launch tweet |
| 2 | 4 dev pillars: Build Real Things · AI-Native Platform · Hack & Experiment · Get Hired by Swiggy | 4 Cashfree pillars: Real Money Movement · Payments-Native AI · Open OAuth (no Tech Partner gate) · Career Catalyst | § 4.4 (Message House) + Phase 1 /developers spec |
| 3 | 6 use case imagination prompts (Voice Agent / Auto-Restock / Group Order / Dietary Planner / Reservation / Multi-Modal) | 6 Cashfree imagination prompts shipped as Phase 1 templates: RTO Shield / Refund Recovery / Settlement Watchdog / Payout Pipeline / Payment Recovery / EdTech Fee Engine | § 5.8 |
| 4 | 4-step application/hiring path | Apply (Google Form) → review (5-min) → credentials → demo | § 5.2 + § 5.4 cohort |
| 5 | "No whiteboard puzzles. No trick questions. Just show us what you can build." | "No 6-week Technology Partner audit. No DM-the-CEO LinkedIn dance. Just ship something on Relay and we'll talk." | § 5.10 amplification + recruitment messaging |
| 6 | "Standout projects get featured — and yes, we actively hire from this program." | "Ship something great and we'll feature it. Ship something exceptional and our recruiting team might reach out." | § 5.11 launch tweet (verbatim adapted) |
| 7 | Local-first DX (`npx … --api-key=…`; build before approval) | `npx @cashfreepayments/relay-mcp` works locally before approval | § 5.3 Phase 1 deliverable |
| 8 | 6 framework adapters Day 1: OpenAI Agents SDK · Anthropic · LangGraph · Vercel AI SDK · Mastra · CrewAI | Same 6 adapters at Phase 1 launch | § 5.3 Phase 1 deliverable |
| 9 | Three-track docs IA: Developer / Enterprise / Consumer | Same three tracks; Consumer track explained as "merchant installs Relay MCP into Claude Desktop and asks 'who hasn't paid me this week, send WhatsApp reminders'" — TAM expansion to non-technical merchants | § 5.5 Phase 3 deliverables |
| 10 | Three-server architecture (Food / Instamart / Dineout) — 3 distinct endpoints, 3 distinct verticals | Payments / Payouts / Reconciliation — 3 distinct endpoints, 3 distinct payment-stack verticals | § 5.7 |
| 11 | Google Form application portal (`forms.gle/4vkeKyqm15Qb6fnJA`) — no custom build | Google Form for cohort applications — half-an-hour to ship | § 5.4 Phase 2 |
| 12 | Co-marketing partner with press megaphone (AWS Press Center for Swiggy) | AWS India / Anthropic India / Bolna co-launch for Cashfree at GFF | § 5.5 Phase 3 + § 5.13 risk 1 |
| 13 | Two-beat launch (MCP first, Builders Club second) | Phased: Phase 1 Developer Soft Unveil + Phase 2 Builders Cohort + Phase 3 GFF Headline (3-beat instead of 2, plus Phase 0 prep + Phase 4 compound) | § 5.1 phasing overview |
| 14 | `llms.txt` + `llms-full.txt` at predictable URLs (AI auto-discovery) | Same predictable URLs at relay.cashfree.com/builders/ | § 5.3 Phase 1 deliverable |
| 15 | Launch blog post complementing tweet | Phase 3 GFF Day-1 blog post at relay.cashfree.com/blog/2026-09-01-relay-launch/ | Phase 3 deliverable (add to § 5.5) |
| 16 | Public FAQ on hub page | `/faq` subset of § 3.3 customer FAQs goes live in Phase 1; expanded in Phase 3 | Phase 1 deliverable (add to § 5.3) |
| 17 | Twitter dev-reaction pattern: devs project own work onto platform ("my openclaw can order me food") | Phase 3 success metric: 3+ founders/CTOs publicly tweeting their Relay workflows | § 5.5 metrics |
| 18 | "Apply Now" CTA + "Send Us a Demo" + "Read the docs" — three distinct dev journeys | Same three CTAs on Cashfree /developers page | Phase 1 /developers spec |
| 19 | Stats in headline ("3 MCP Servers · 35 API Tools · ∞ Possibilities") | "3 MCP Servers · 24+ API Tools · ∞ Workflows" | § 5.3 Phase 1 + § 5.11 tweet |
| 20 | "Start Cooking Today!" playful CTA tone | Cashfree equivalent: "Ship Today" / "Build Today" — playful, low-stakes, food/finance pun-free | Phase 1 messaging |

## What Cashfree should NOT copy from Swiggy

- **Application-gated everything from Day 1:** Swiggy gates because they're a consumer commerce platform with food/payment risk. Cashfree's MCP can be open Day-1 (Phase 1) for read-only OAuth — only production-write access requires approval.
- **AWS-only co-launch:** Swiggy used AWS Press Center as the press megaphone. Cashfree should distribute across Anthropic India + AWS India + Bolna + GFF organizers, not single-point-of-failure on one cloud.
- **No India payment-specific compliance language:** Swiggy's enterprise page omits DPDP/SOC2/ISO. Cashfree (BFSI-adjacent) MUST lead with compliance on the enterprise page.

## What Cashfree must do BETTER than Swiggy

- **Open access on Day 1 of Phase 1** vs Swiggy's gate-from-launch — biggest differentiation vs Razorpay's Tech Partner gate
- **Self-hostable OSS core** — Swiggy didn't ship this; Relay must (per the BUILT-OWN signal × 1,251 from Agent A)
- **Tally / GST / WhatsApp / UPI back-office stack** — Swiggy had no equivalent; Cashfree's wedge per Agent C
- **Compliance-led enterprise page** — DPDP, SOC2, ISO 27001 explicitly (Swiggy omitted)

---

# Files & Next Actions

## Files produced during research
- `C:\Users\mothi\dtc-research\` — existing 28K-row corpus + synthesis
- `C:\Users\mothi\relay-research\data\` — Agent B's 46MB JSON + tagged.json + shortlist.json
- `C:\Users\mothi\relay-demand-research\data\` — Agent A's 3,031 tagged rows + 175 fresh permalinks
- `C:\Users\mothi\relay-demand-research\processed\` — Agent C's 13,976 signals + tool_mentions + top_quotes
- `C:\Users\mothi\relay-validation\signals\` — Agent D's 1,127 distinct signals + quotes.json
- `C:\Users\mothi\cashfree-relay-gtm\RELAY_GTM_v1.md` — this document (now v2)

## Phase 0 critical-path actions (next 5 weeks: Apr 29 → May 31)

1. **Sign 2-3 enterprise design partners** under NDA — Sales-led ABM, Mothi co-pitches
2. **Resolve `Map<String,Object>` payload issue** with Subbu/Vinesh/Vishal — gates Phase 1 launch
3. **Restructure MCP into 3 servers** (Payments / Payouts / Reconciliation)
4. **Submit GFF talk + secure booth** by mid-May (absolute deadline, no slip)
5. **Pull Cashfree Featurebase voted-feature list internally** (Agent D couldn't scrape; auth-walled)
6. **Brief Bolna on co-launch partnership** (revenue share on voice nodes; lock by end Phase 0)
7. **Identify GFF co-launch partners:** AWS India · Anthropic India · Bolna · others
8. **Phase 1 asset prep:** Hashnode/dev.to article outlines · Mintlify docs draft · Phase 1 /developers page wireframe · llms.txt/llms-full.txt templates
9. **Internal sales enablement:** Auto Collect vs Relay vs both decision tree · battle cards (design-partner-only)
10. **Mothi public posture: silent on Relay** until Phase 1 begins Jun 1

## Phase 1 critical-path actions (Jun 1 → Jul 15)

1. Ship `npx @cashfreepayments/relay-mcp` working locally
2. Ship `relay.cashfree.com/developers` + `/docs` + `/faq` + `/llms.txt` + `/llms-full.txt`
3. Open OAuth read-only Day 1 of Phase 1
4. Ship 6 framework adapters with code samples
5. Ship 6 starter templates (open-source on GitHub)
6. Drop 3-4 founding-team articles on Hashnode + dev.to
7. Mothi: incremental "early access" tweets only — NOT headline launch
8. Pre-brief Latent Space + Pragmatic Engineer + Inc42 + YourStory under embargo for GFF
9. GFF keynote slide deck draft begins

## Open decisions for Mothi

- Cohort name: "Relay Builders" / "Relay Pioneers" / "Made on Relay" — pick by Phase 0 close
- Hackathon vertical at Phase 4: D2C-only OR EdTech-only OR both
- Personal positioning: front-and-center on Twitter from Phase 1, or behind Akash/Reeju until Phase 3
- Self-host repo licensing: Apache 2.0 (recommended) vs more restrictive
- Consumer track timing: Phase 1 (widens TAM Day 1) or Phase 3 (cleaner GFF beat)
- Phase 3 GFF speaker: solo Mothi keynote · co-keynote with Akash/Reeju · or Akash-only (Mothi owns booth + tweet)

## Out-of-scope for v2

- Cohorts → Google Ads sync (cut based on <10 evidence signals)
- Refund Velocity Guardrail (least-validated use case; defer)
- International expansion (India-first, India-only)
- Razorpay PG migration tooling (separate roadmap; high-effort)

---

*End of GTM v2 (phased to GFF 2026 first week, with Phase 0 enterprise design partner emphasis and Swiggy translation map). Iterate from here.*
