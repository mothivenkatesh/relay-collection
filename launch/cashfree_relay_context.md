# Cashfree Relay — Full Context Document

| Field | Value |
| :---- | :---- |
| Author | Mothi Venkatesh (PMM) |
| Owners | Vinesh Kumar, Subramanian K |
| Stakeholders | Shritama Saha, Priyam Shankar Jha, Kumar Anubhav, Harshit Pai, Satyam Tripathi, Shanthalingaiah S M |
| Final Approver | Ramkumar Venkatesan, Mayank Juneja |
| Document version | v1.0 (consolidated context) |
| Anchoring thesis (current) | **Cashfree Relay is the Payments MCP. Position underneath the agent layer, not on top of it.** |

---

## Purpose of this document

This is the single canonical context document for Cashfree Relay. It captures every strategic decision, every framework applied, every competitive intelligence finding, every artifact built, and every honest course-correction across the launch planning arc. Future PMM, Product, Sales, or leadership conversations should anchor here first.

The document is organized so a new reader can drop in cold and reach decision-readiness in 30 minutes. Sections build on each other. The strategic thesis — Payments MCP — sits at the top because it's the most recent and most important reframe.

---

## TL;DR — The Strategic Thesis

**Cashfree Relay is positioned as the Payments MCP, not as an Agent Studio.** This is a deliberate strategic choice that mirrors Workato's positioning move (Enterprise MCP, not Agent Studio).

The principle: *position underneath the layer everyone is fighting over. Be the thing they all need.*

Razorpay took the Agent Studio category at FTX 2026. Following them into that category guarantees #2. Going one layer down — claiming Payments MCP as the protocol-level land grab — is defensible because:

- Cashfree's moat is payments rails, not LLM UX
- The agent layer is being commoditized by OpenAI / Anthropic / Google / Microsoft / Salesforce
- Every AI agent will eventually need to move money — Stripe is the only real comp in this lane
- MCP is developer-native, which matches Cashfree's developer-first DNA
- Relay can live underneath this thesis as the SMB on-ramp, not the headline

**One-liner:**
> Razorpay built an Agent Studio. Cashfree built the payment rails every agent runs on.

**Hero claim:**
> Power any agent that handles money.

---

## Section 1 — The Three Forces Driving Strategy

Every Indian payment processor faces the same three forces. Strategy is how each company chooses to respond.

### Force 1 — MDR compression
UPI killed card-MDR margin. Regulated bands compressed traditional take rates further. The processing-fee business is a declining margin pool with no recovery on volume.

### Force 2 — AI disintermediation
When the merchant asks Claude to issue a refund, Claude doesn't care which processor sits underneath. Without presence at the agent layer, Cashfree becomes a commodity API call inside someone else's agent.

### Force 3 — Pre-IPO valuation pressure
AI-native fintech multiples run 3-5x ahead of MDR-arbitrage fintech multiples in 2025-26. Razorpay is on a public-listing path. Every quarter spent narrating "AI-native payments leader" compounds the valuation gap before lockup. Cashfree is private — this force matters less, but the next funding round still benefits from the AI-native narrative.

The strategy must defend MDR margin, prevent disintermediation, and tell the right narrative simultaneously.

---

## Section 2 — Competitive Intelligence Summary

### Razorpay Agent Studio (the primary competitor)

**Launch:** Sprint 2026 / FTX, March 2026. Public preview gated by Typeform.

**Architecture:** Hosted runtime inside Razorpay's UI. Built on Anthropic's Claude Agent SDK. Confirmed by CPO Khilan Haria in the FTX demo: *"Agent studio is where the agents themselves are sitting inside our framework. The connections are private in nature. They don't run the same MCP framework."*

**Eight pre-built agents (seven unique — SuperU and Nugget are the same Cart Abandonment agent co-branded twice):**
1. Dispute Responder
2. Subscription Recovery
3. Cart Abandonment Conversion (×2 with Nugget/SuperU)
4. RTO Shield
5. RTO Insights
6. Cashflow Forecaster
7. Settlement Insights

**Three-tier framework:**
- Customize a Prebuilt Agent (no-code)
- Onboard as an AI Partner (ISV/build partner program)
- Build From Scratch (beta, code-first)
- Implicit fourth tier: custom agents on request for top 50 enterprise merchants

**Razorpay MCP server:** Live since April 29, 2025. ~217 GitHub stars. Go, MIT-licensed. ~45 tools. Static base64 token auth. **Architecturally separate from Agent Studio** — Khelan confirmed Agent Studio uses private connections, not MCP.

**Pricing:** Hidden. Free trial period during early access. Khelan: *"In that time frame, we'll figure mechanics of the pricing."*

**Persona segmentation:** CRO / COO / CFO. Three buyer personas, three persona-themed agent buckets. **Deliberately walked past the Founder / Owner-Operator persona** (the 5-50 person team where one person is all three roles).

**The big newsletter (April 23):** Razorpay platform rebrand into 4 layers:
1. AI-Native Merchant Experience (conversational onboarding/integration/dashboard)
2. Agentic Payments Stack (NPCI + ChatGPT/Claude pilots — Bigbasket, Zomato, Swiggy, Zepto)
3. Agent Studio (the studio + custom agents)
4. AI-Native Builder Distribution (Codex, Replit, Emergent, n8n native integrations)

**Strategic verdict:** Razorpay is running a coordinated maneuver to replace MDR margin with outcome margin, prevent LLM disintermediation, and capture an AI-native pre-IPO valuation multiple. Agent Studio is the take-rate replacement engine. Custom agents are the enterprise services play. The whole thing is wrapped in a platform rebrand.

**Razorpay vulnerabilities:**
1. Architectural tension between hosted Agent Studio and open MCP server (unresolved)
2. Hidden pricing locks out SMB band
3. Single-vendor (Anthropic) fragility
4. Custom agents are services margin not software margin
5. Eighth agent is a duplicate (the count is 7, not 8)
6. Narrative is 90 days ahead of product

### Stripe Workflows + Agent Toolkit

**Stripe Workflows** — Public Preview since Stripe Sessions May 2025. Programmatic triggers added April 22, 2026. Hard caps: 12 steps per workflow, 50 active workflows per account, 1 trigger type per workflow, no scheduled/cron triggers. Custom actions require Stripe App packaging. **NOT AI-native** — deterministic automation only.

**Stripe Agent Toolkit** — L3 SDK for AI agents calling Stripe APIs. Multi-vendor at L1 (OpenAI Agents SDK, LangChain, CrewAI, Vercel AI SDK). **Architecturally separate from Workflows.**

**India availability:** Stripe is invite-only/preview in India. Workflows is moot for India-based businesses.

**Key insight:** Stripe smartly separated deterministic automation (Workflows) from agentic AI (Agent Toolkit). Cashfree should apply the same discipline.

### Workato Enterprise MCP (the strategic precedent)

Workato's positioning move is the template Cashfree Relay is now following.

**Why Workato chose Enterprise MCP, not Agent Studio:**
1. Their moat is the rails (1,200 connectors, enterprise auth, governance, audit logs, RBAC, data residency) — not the UI
2. Agent Studio is being commoditized by OpenAI / Anthropic / Google / Microsoft / Salesforce
3. MCP is the protocol-level land grab — neutral Switzerland between every model and every studio
4. CIOs don't buy chatbots, they buy control planes
5. Defensive against disintermediation — sitting *below* every LLM makes them unavoidable

**The principle that transfers to Cashfree:** Position underneath the layer everyone is fighting over. Be the thing they all need.

### Microsoft Foundry / Google Vertex / OpenAI Agent Builder / ElevenLabs Studio

These are L2/L3 horizontal platforms. They sell substrate (model hosting, agent SDKs). They don't ship vertical agents themselves. They are not Cashfree Relay's direct competitors — they're partners or distribution channels.

### Salesforce Agentforce / Harvey AI / SAP Joule Studio

These are L4 vertical SaaS agent platforms in CRM, legal, ERP. Same shape as Razorpay Agent Studio, different verticals. Not direct competitors but useful precedents for vertical-SaaS-L4 patterns.

### FinQub (the structural precedent)

`finqub.io` — fintech orchestration layer (KYC, KYB, payments, banking, fraud, comms). Pre-revenue, founding design partners stage.

**What's borrowable:**
1. Category-creation move: *"Workato is a certified pipe. FinQub is a certified pipe that understands the water."*
2. Cost-of-pain specificity ($540K-$1M/year, 3-6 months to switch a vendor, 2-4 weeks to respond to inquiry)
3. "Config change, not a rewrite" reveal
4. Honest stage disclosure ("pre-revenue, founding design partners")
5. "You'll need both" generosity (Workato + FinQub are complementary, not competitors)

**The single best line for Cashfree to borrow structurally:**
> Stop building your orchestration layer. Start running on it.
> → Cashfree version: *"Stop running your payment ops. Start orchestrating them."*

---

## Section 3 — The L1-L5 Functional Layers (the real framework)

Earlier in the conversation I mistakenly used an infrastructure-stack framework (foundation models / model infra / agent infra / vertical SaaS / end-user). The user corrected this. The actual framework is **functional layers of agent capability**:

| Level | Layer | What it provides | Question it answers |
|---|---|---|---|
| **L1** | Agent Skills | Domain knowledge installed into a generic AI assistant | "Does the AI know how this product/domain actually works?" |
| **L2** | MCP / Tool layer | Callable primitives the agent can invoke | "Can the AI take action on real data and systems?" |
| **L3** | Agent Workflows / Templates | Composed multi-step automations | "Can the AI orchestrate sequences of actions reliably?" |
| **L4** | Agent Applications | Vertical agent products with UX, observability, governance | "Can a non-technical operator run this without writing code?" |
| **L5** | System of Record | The authoritative database the agents act against | "Whose data does the agent actually own and operate on?" |

### How each player maps

| Player | L1 Skills | L2 MCP/Tools | L3 Workflows | L4 Applications | L5 SoR |
|---|---|---|---|---|---|
| Microsoft Foundry | Generic | Multi-vendor MCP | Workflow primitives | Copilot Studio | None (runs on customer's SoR) |
| Google Vertex | Generic | Multi-vendor tools | ADK orchestration | Limited | None |
| OpenAI Agent Builder | Generic | OpenAI-tilted | Agent SDK | Apps SDK | None |
| Razorpay Agent Studio | None published | Razorpay MCP (separate) | Closed (their UI) | 7 pre-built agents | **Razorpay payments SoR** |
| Stripe Workflows + Agent Toolkit | None | Stripe Agent Toolkit | Stripe Workflows | Limited templates | **Stripe payments SoR** |
| Salesforce Agentforce | None | Salesforce APIs | Atlas Reasoning | Pre-built CRM agents | **Salesforce CRM SoR** |
| Harvey AI | None | Closed | Closed | Legal workflows | **Harvey's legal corpus** |
| SAP Joule Studio | None | SAP APIs | SAP Build | Vertical ERP agents | **SAP S/4HANA SoR** |
| **Cashfree Relay** | **Cashfree Agent Skills (live)** | **Cashfree MCP (live)** | **Visual builder + templates** | **Templates + Builder UX** | **Cashfree payments SoR** |

### The key strategic insight

**The SoR (L5) is the only un-displaceable moat.** Skills can be copied. MCPs can be copied. Workflow builders can be copied. Even agent applications can be copied. What can't be copied is the System of Record — the merchant's payment data, transaction history, refund lifecycle, dispute records, settlement reconciliation.

**Foundation-tier players (Microsoft, Google, OpenAI, ElevenLabs) play L1-L3 but don't own L5.** They sell substrate.

**Vertical SaaS players (Razorpay, Salesforce, Harvey, SAP, Cashfree) play L4-L5 deeply.** Their L1-L3 is built on top of someone else's substrate.

**Cashfree Relay's bet:** play deeply at all five layers, but stay multi-vendor at L1 (any AI model) and open at L2 (MCP for any framework). Full stack vertically integrated for Indian payments, but architecturally open above the application layer.

---

## Section 4 — What's Actually Shipped (The Honest Product Inventory)

This section exists because of a recurring failure mode in the conversation: positioning ran ahead of product multiple times. Future readers should anchor here before any external claim.

### Live today (4 automations only)
1. **Calendar invite on payment success** — Trigger: Transaction Success → Google Calendar or Cal.com event
2. **Threshold transaction alerts** — Trigger: Transaction Amount > threshold → notify on WhatsApp/SMS/email/Slack
3. **Transaction summary to Google Sheets** — Trigger: Transaction events → Sheet row appended in real time
4. **Hourly failed-payment digest** — Trigger: Hourly schedule → digest of failed transactions to email/Slack

### Live infrastructure
- Cashfree MCP server (cashfree/cashfree-mcp on GitHub, TypeScript, MIT, ~37 tools, ~13 GitHub stars at last check)
- Cashfree Agent Skills (CLI installable into Claude Code, Cursor, Codex, OpenCode, Copilot, Windsurf via `npx @cashfreepayments/agent-skills add skills`)
- Visual workflow builder in Cashfree dashboard (private beta / public preview)
- 9 payment-event triggers + 1 schedule trigger + HTTP request node
- 10 connectors (Sheets, Slack, Gmail, Zoho Invoice, Calendly, Google Calendar, WhatsApp Business, Gemini, OpenAI, Cashfree Payments)

### Roadmap (Q3 — public beta to GA)
- 6 specialist agents: RTO Recovery, Refund Triage, Cart Recovery, Dispute Response, Settlement Reconciler, Subscription Recovery
- Outcome-based pricing tier (5-8% of recovered revenue)
- Production-grade MCP with OAuth-scoped consent and Maker/Checker default
- Cursor + Claude Code MCP support
- SecureID/KYC tools added to MCP (the differentiator vs Razorpay's MCP)
- BYOK option for compliance-sensitive merchants

### Roadmap (post-GA, Q4+)
- Subscription management tools in MCP
- Webhook management tools
- Vendor payment / Route tools
- Marketplace of pre-built agent templates (mirrors Razorpay's marketplace pattern)
- Voice agents (Sarvam, ElevenLabs)
- Autonomous ops agents / multi-agent collaboration

### What is explicitly NOT shipped (the recurring positioning leak)
- RTO Recovery, Refund Triage, Cart Recovery, Dispute Response, Settlement Reconciler, Subscription Recovery — none of the named "specialist agents" are live
- Outcome-based pricing — not live
- The MCP server is live as a repo, but production-grade hardening (OAuth, Maker/Checker default, BYOK) is on the 6-8 week path

**Rule:** marketing copy must label these as "Q3 roadmap" or "shipping during public preview" — never as "live." Template Library Spec is the source of truth on what's claimable.

---

## Section 5 — The Positioning Evolution (versions and why each shifted)

| Version | Frame | Why it shifted |
|---|---|---|
| **v0.1 — v0.3** | "AI workflow platform with AI nodes" | Razorpay shipped Agent Studio. The "AI workflow builder" frame put Cashfree in n8n's category and Razorpay's slipstream. Both unwinnable. |
| **v0.4** | "MCP-first agent infrastructure" | Sharper, but still framed as a workflow tool with MCP added. Buried the agentic claim. |
| **v1 (launched)** | "Agent workflows for India's payment infrastructure" | Headline shipped to leadership for the launch positioning doc. |
| **v2** | "Cashfree Relay turns Cashfree into a Growth Operator Agent" | User correction: descriptive but flat. Pivoted to *Growth Operator Agent* — battle-tested templates that reduce losses, improve sales, recover revenue. |
| **v3** | "Agentic workflows for payment operations" | User locked headline at *"Agentic workflows for your payment operations"* — restraint as confidence. Premium register. |
| **v4** | Same hero, integrated Stripe Workflows competitive learnings | Stripe Workflows reframe: not AI-native. Cashfree's edge is AI inside workflows. |
| **v5 (current)** | **Payments MCP** | The Workato move. Position underneath the agent layer. *"Power any agent that handles money."* |

### The strategic case for the Payments MCP positioning

| Dimension | Agent Studio (Razorpay path) | Payments MCP (Cashfree wedge) |
|---|---|---|
| Moat used | Workflow UI + LLM orchestration (commodity) | PG + Payouts + Secure ID + RBI compliance (durable) |
| Buyer | PM/ops at one company | Every agent platform, every developer |
| Competitive set | OpenAI, Anthropic, Google, Razorpay, every SaaS | Almost no one — Stripe is the only real comp |
| Platform risk | Bound to one SDK/model | Neutral — works with all |
| TAM frame | "Enterprises building agents" | "Every agent that ever handles money" |
| Lock-in | UX (weak) | Rails + compliance (strong) |

**Why this fits Cashfree specifically:**
1. The moat is payments rails, not LLM UX — same logic as Workato
2. Developer-first DNA matches MCP-first positioning — Cashfree's brand is "developer-friendly payments"
3. Differentiated wedge against Razorpay — different category, different buyer, no head-to-head
4. Every AI agent will need to move money — Stripe is the only real comp; India hasn't been claimed
5. Relay can live underneath this thesis — Relay = SMB on-ramp + workflow tool; Payments MCP = the platform story

---

## Section 6 — The Three Value Pillars (locked)

These were iterated extensively. Final form below uses HITL terminology (not Maker/Checker), reads in plain operator language, and avoids the ₹2 lakh crore claim per user direction.

### Pillar 1. Run agents inside the AI your team already uses

Your ops lead opens Claude before she opens any dashboard. Your CTO is already in Cursor. Your finance team lives in ChatGPT. Cashfree Relay shows up where the work happens, not in another tab your team has to remember to open.

* Cashfree MCP runs inside any MCP-compatible AI agent. One install. No proprietary SDK. No vendor lock-in. Your AI bill stays with OpenAI or Anthropic. Not with us.
* Cashfree Agent Skills make your AI assistant fluent in Cashfree. Webhook signatures right the first time. Refund flows that don't break in production at 2 AM.
* Visual workflow builder in the Cashfree dashboard for ops leads who'd rather see the canvas. Same primitives as MCP. Five minutes to your first workflow.

### Pillar 2. Built on the rails 800,000 Indian businesses already trust

You moved to Cashfree because the rails worked. Relay sits on those same rails. Same uptime. Same compliance perimeter. Same support team you already know. New automation layer on top of infrastructure that already powers Swiggy, Cred, Cult, BookMyShow, and the rest of India's largest checkouts.

* Native triggers across the full payment lifecycle. Payment Success, Failed, Dropped, Refund Success, Cancelled, Schedule, Webhook. Zero plumbing.
* Live integrations to the apps your team already uses. Google Sheets, Slack, WhatsApp Business, Gmail, Calendar, Cal.com. More shipping every week, prioritized by merchants in public preview.
* Free during public preview. Public pricing on day one of GA. No "contact sales" to find out what it costs.

### Pillar 3. Guardrails that match the bar for AI in payments

You've been hesitant to point AI at refunds and payouts. That hesitation is correct. AI workflows are new. The compliance posture underneath Relay is not. RBI-authorised payment aggregator. PCI DSS Level 1. DPDP-ready. The AI proposes. A human approves. That's the loop.

* Audit by default. Every agent action recorded. What it did, why, which workflow version, which data it touched. 90-day retention, exportable in one click for risk, finance, or your auditor.
* Human-in-the-loop on every irreversible action. Refunds. Payouts. Customer messages. The agent drafts. Your team approves. Nothing fires unless a human says yes.
* Confidence-gated execution. Set the threshold yourself. If the agent's confidence drops below it, the action lands in your queue with the reasoning attached. The merchant sets the bar, every time.

---

## Section 7 — The Cultural Brand Decoder Insight

Three constructed meanings collide for an Indian merchant in 2026 around "AI agent for payments":

1. **"AI for payments" reads as risky** to most Indian SMBs (UPI fraud, OTP scam cultural code is dominant)
2. **"Run on AI" reads as elite/early adopter** — emerging signal of being ahead of the curve
3. **"Built on Cashfree's rails" reads as familiar safety** — stable cultural code, worth leaning on

**The cultural sweet spot:** the merchant wants to *feel* like an early adopter without *behaving* like a risk-taker. They want the status of moving fast and the comfort of moving safely.

**The cultural framing for Relay:** modern but not reckless. Premium but not precious. Fast but not unsafe.

This is the same tension Apple manages with "It just works." Cred manages it with "Pay your bill, but feel premium doing it."

---

## Section 8 — The Honest Persona Map

8 personas, 4 primary + 4 secondary. Captured in detail in the positioning CSV. Summary:

### Primary buyers (the champions)
1. **Founder / CEO** (D2C, EdTech, SaaS, services) — the empty-quadrant buyer Razorpay walked past
2. **Head of Operations** — the day-to-day user, owns reconciliation, refunds, dispute response
3. **CTO / VP Engineering** — technical decision-maker, owns vendor lock-in concerns
4. **Head of Finance / CFO** — procurement champion, owns audit trail and pricing legibility

### Secondary buyers (the influencers / hands-on users)
5. **Backend / Payments Engineer** — hands-on Skills user, influences CTO recommendation
6. **Customer Success / Support Manager** — daily user of refund triage + dispute workflows
7. **Compliance Manager / Risk Lead** — influences finance/CFO, owns the "default no" until proven safe
8. **Growth / Marketing Manager** — owns recovery workflows (RTO, cart, subscription)

**The empty quadrant Cashfree owns:** the Founder/Owner-Operator at the 5-50 person merchant. Razorpay deliberately segmented to CRO/COO/CFO and walked past this persona. Cashfree's pricing transparency, multi-vendor neutrality, and self-serve register are tuned for this buyer.

---

## Section 9 — The Wedge Inventory (six defensible moves)

These are the structurally defensible competitive moves Cashfree has. Razorpay cannot match them in 90 days because each one collides with their architectural choices.

| # | Wedge | Why Razorpay can't easily match |
|---|---|---|
| 1 | **India-payments-native primitives** in MCP (UPI, NACH, BBPS, COD, RTO scoring, KYC/SecureID) | Razorpay's MCP doesn't expose KYC primitives. Their architecture is identity-decisioning-shallow. |
| 2 | **AI as a node inside workflows, not a separate product** | Razorpay split Workflows (deterministic) and Agent Toolkit (AI). Stripe split same way. Cashfree unifies. |
| 3 | **Same engine, four surfaces** (Skills + MCP + visual builder + templates) | Razorpay is hosted-runtime-only. Stripe Workflows is Dashboard-only. Cashfree exposes one engine through four entry points. |
| 4 | **Open platform, not closed runtime** | Razorpay's hosted runtime is core to their business model — switching to MCP-first would break their take-rate engine. |
| 5 | **Secure by construction with India-specific compliance** (RBI, PCI Level 1, DPDP) | Stripe doesn't have RBI/DPDP. Razorpay does, but ships static API keys for MCP auth which won't pass enterprise security review. |
| 6 | **Transparent pricing on day one** | Razorpay's hidden-pricing model is structurally tied to their hosted-runtime architecture and per-deal outcome contracts. Publishing pricing would break the procurement-narrative protection. |

**The single most important move within Cashfree's control: publish pricing on Day 0.**

Razorpay can do everything else better than us — Anthropic relationship, agent count, Sprint event production, NPCI rails, valuation narrative. But they cannot publish pricing in 90 days because their model is hidden contact-sales tied to outcome-share contracts that depend on per-merchant baselines.

---

## Section 10 — Pricing Model

| Tier | Price | Includes | Buyer |
|---|---|---|---|
| **Free** | ₹0 | MCP server, 100 builder runs/month, all 4 starter automations, Skills CLI free forever | Developers, indie builders, evaluators |
| **Starter** | ₹4,999/mo | 5,000 runs, 5 seats, premium connectors (WhatsApp Business), observability | Solo founders, small ops teams |
| **Growth** | ₹19,999/mo | Unlimited runs, governance (HITL, audit logs), all premium templates, priority support | Growing SMB, mid-market |
| **Outcome** | 5-8% of recovered revenue | Capped at category benchmark — RTO, dispute, cart, subscription — available with specialist agents at GA | Mid-market merchants with quantifiable RTO/dispute/cart loss |
| **Enterprise** | Bundled-MDR | 0.x% effective rate, all access, named CSM, custom agent buildouts | Top 100 Cashfree merchants |

**Public preview status:** Free for everyone during public preview. No credit card. No usage caps. Pricing locks at GA. Beta merchants get preferred pricing for an extended period (12 months proposed, pending Reeju + Mayank signoff).

**Year 1 ARR ceiling:** ~₹12-15 crore (500 paying merchants).
**Year 3 ARR ceiling:** ~₹80-120 crore at software margins.

**Unit economics example (SMB):** D2C apparel brand at ₹2 cr/month GMV, 50% COD, 22% RTO. RTO Recovery template at 25% reduction recovers ₹66L/year. Cashfree take at 6%: ₹4L/year per merchant. Stack three templates → agentic take approaches MDR at SMB scale.

---

## Section 11 — The Two-Wave GTM Plan

The launch runs in two waves. This is the central GTM decision.

### Wave 1 — Public Preview (May 2026, quiet)

**Goals:**
- 100 merchants running ≥1 workflow consistently
- 1,000 MCP installs across Anthropic, ChatGPT, Cursor directories
- 500 Agent Skills CLI installs
- 3 named merchant case studies with quantified outcomes
- 5 host-directory listings live
- Zero press cycle. Quiet preview.

**Why quiet:** We have 4 honest workflows live. The specialist agents (RTO Recovery, Refund Triage, etc.) are Q3 roadmap. Going loud now sets up a credibility leak when the first beta merchant logs in expecting RTO Scorer LIVE and finds Calendar Invite. Quiet wave 1 = build the proof. Wave 2 = ship the proof.

**Wave 1 budget guidance:** ₹5-8 lakh (creator pieces, light paid LinkedIn, no major production).

### Wave 2 — Flagship launch at GA (Q3 2026, loud)

**Goals:**
- 500 paying merchants (~₹12-15 cr ARR)
- 1 outcome-based contract signed (proves the model)
- 8 named launch partners across L1/L2/L3 of the stack
- Reeju, Ram & leadership LinkedIn moment + tier-1 press cycle
- Builder's Day equivalent virtual event ("Run Cashfree Anywhere")

**Pre-conditions:**
- 4-6 specialist agents shipped
- Outcome pricing tier live
- 1 quantified case study from Bolna (build partner)
- Production MCP with OAuth-scoped consent
- ISV partner program with 3 named launch partners

**Wave 2 budget guidance:** ₹35-50 lakh (production + media + events + paid amplification).

### The single critical gate

**DIN approval is the binding path.** Per gtm-ops canonical model, no external Relay outreach can begin until DIN-RELAY-2026-Q2-001 is approved with all 9 mandatory artifacts uploaded and eSignatures from Reeju + Mayank + Ram + Mohit + Sales lead.

DIN cycle: 8-10 business days from filing to approved.

---

## Section 12 — Launch Day Cascade (Wave 2)

Tiered execution on flagship Launch Day:

| Tier | Time | Action | Owner |
|---|---|---|---|
| Tier 0 | LD-7 | Internal sneak preview all-hands | Reeju |
| Tier 1 | LD-1, 6 PM IST | Reeju quiet teaser LinkedIn post | Reeju |
| Tier 2 | LD, 9 AM IST | Reeju founder substantive LinkedIn post | Reeju |
| Tier 3 | LD, 9:15 AM IST | Ram + leadership reposts | Comms |
| Tier 4 | LD, 10 AM IST | Team broadcast + dashboard banner + in-app + Pulse | Comms + Product |
| Tier 5 | LD, 11 AM IST | PR embargo lifts (TC India, YourStory, Inc42, Moneycontrol, MediaNama, Paypers, Entrackr, AIM) | Mayank + Comms agency |
| Tier 6 | LD+1 → LD+5 | Influencer cascade (5-8 mid-sized voices, one per day) | Marketing |
| Tier 7 | LD+7, LD+14 | Webinars (Live build, Customer in production with Bolna) | Marketing |
| Tier 8 | LD+21 | Builder's Day virtual event ("Run Cashfree Anywhere") | Marketing + Govardhan |

---

## Section 13 — Content Calendar

### Launch-day blogs (3, all live LD)
1. **"Introducing Cashfree Relay: the Payments MCP for India"** — Reeju voice, narrative, 1,200-1,500 words
2. **"How Cashfree Relay Works: an MCP server for UPI, settlements, and refunds"** — Vinesh + Engineering co-byline, technical, 1,500-1,800 words
3. **"Relay Payment Guardrails: what Relay will and won't do autonomously"** — HITL trust play, Mothi + Compliance review, 1,000-1,200 words

### Day 1-30 blogs (3, staggered)
4. **"How Cashfree teams use Relay"** — eat-our-own-cooking story, LD+7
5. **"How Bolna cut payment integration time from 2 weeks to 4 minutes with Relay"** — case study with Bolna co-byline, LD+14
6. **"Cashfree Relay is now a one-click extension for Claude and Codex"** — distribution expansion, LD+21

### Tutorial blogs (1/week through LD+30)
- "Auto-onboard every paid customer with Relay"
- "Spot fraud-shaped transactions in 30 seconds with Relay"
- "Live books in Sheets with Relay"
- "Catch payment-failure churn before it churns"

### Opinion blog
- **"Why we built Relay differently from Razorpay Agent Studio"** — Reeju POV, LD+10

### SEO bait + thought leadership (Payments MCP claim)
- **"Why generic workflow tools don't speak payments — and what Payments MCP changes"** — the category-creation piece

---

## Section 14 — Launch Partners + Build Partners

### Launch partners (Govardhan owns)

Target 6 named partners by LD-2 across:
- L1 model partner (OpenAI India listing) — counter-endorsement to Anthropic-Razorpay
- L1 model partner (Google Gemini Extensions)
- L2 host partner (Cursor MCP registry)
- L4 payments-adjacent SaaS #1 (Shiprocket-tier)
- L4 payments-adjacent SaaS #2 (Chargebee India-tier)
- L5 customer reference (1 named D2C brand)

### Build partner

**Bolna confirmed.** Featured in Blog 5, webinar 2 speaker, quoted in PR.

Bolna deliverables: quantified outcome (X hours saved, Y% reduction) by LD-7, founder quote by LD-5, blog 5 co-byline by LD+10.

---

## Section 15 — Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| MCP server slips past launch | Medium | Critical | MCP commitment memo locks Eng to 6-8 week timeline. If MCP not live by T+30, public-facing positioning pauses. |
| Wrong merchants in beta = false negatives | High | Critical | Hard-gate the 4-filter selection. Don't dilute for politics. |
| No-template gap kills self-serve at public beta | High | High | Block public beta until ≥10 templates exist. Templates sourced from private beta merchant workflows. |
| Razorpay GAs Agent Studio with public pricing during our preview | Medium | High | Don't react. Their move forces them into transparent pricing — gives away their procurement narrative protection. |
| Anthropic announces exclusive Razorpay MCP partnership | Low | High | Lock OpenAI Agent Builder + Google Gemini Extensions listings before LD. |
| Beta merchants find 4 templates too narrow, churn quickly | High | High | White-glove onboarding for 30 days. Active feature solicitation feeds Wave 2 priorities. |
| Press picks up Wave 1 unprompted, asks about specialist agents | Medium | Medium | Standard reply: "Public preview, four automations live, more shipping with merchants. Flagship launch at GA." |
| Govardhan can't get 6 launch partners by LD-2 | High | Medium | Ship with 4 named, accept the slip. |
| AI node misuse leaks PII | Low | Critical | Default AI to "draft, not send" mode. HITL approval before send. Legal/DPDP signoff before LD. |
| Pricing model misjudged at GA | Medium | Medium | Late-beta WTP conversations. Anchor ₹999-1,999 Pro. |

---

## Section 16 — What to Avoid Saying

Refined across multiple iterations. These are explicit guardrails for sales, comms, and content.

1. **Don't call it a "workflow tool" or "Zapier for payments."** It's a Payments MCP — a four-surface agent platform.
2. **Don't lead with "AI."** Lead with merchant outcome — RTO recovered, refund cleared, payout shipped.
3. **Don't pitch as "Claude plugin" or "AI feature."** Infrastructure with multiple surfaces.
4. **Don't promise full autonomy on irreversible actions.** HITL default. Supervised autonomy.
5. **Don't claim "world's first" or "India's first."** Razorpay claimed it for Agent Studio. Stripe shipped Workflows globally first.
6. **Don't position against developers.** Skills + MCP = developers are extenders.
7. **Don't say "hosted n8n."** Accurate internally, undersells externally.
8. **Don't promise unshipped templates publicly.** Template Library Spec is source of truth.
9. **Don't conflate Relay with AI Suite.** Stripe's two-product discipline applies — AI Suite is consumer-side, Relay is merchant-side.
10. **Don't claim "Superintelligence" or AGI-level register.** Triggers regulatory scrutiny + collides with the operator-friendly "modest" cultural frame.
11. **Don't claim feature parity with Stripe.** They have 600+ Stripe API actions. Cashfree has India-deep payment primitives. Different shape.
12. **Don't lead with the visual builder in PR.** Lead with Skills + MCP + templates + builder as four surfaces of one platform.
13. **Don't compare directly to Razorpay in PR.** Stay above the fight. Position by reframe ("Other agent platforms…"), not attack.
14. **Don't claim Maker/Checker.** That's a banking term implying two-human approval. Use Human-in-the-loop. The product behavior is HITL, not Maker/Checker.

---

## Section 17 — The Hero Copy (locked, current state)

### Hero (landing page)
> **Agentic workflows for your *payment operations*.**
> Run them inside the AI your team already uses. On the rails that move 800,000+ Indian businesses. Without an AI markup.

### Alternative Payments MCP framing (proposed, not yet on the page)
> **The Payments MCP. Built for India.**
> The trust, the rails, and the compliance perimeter your AI needs to act on payments. Built on the rails behind 800,000 Indian businesses.

### Architecture section closer (kicker line — strongest line on the page)
> *Their AI runs on their cloud, and you pay for it. Ours runs on yours.*

### Sharpest claim (for sales/PR)
> Razorpay built a marketplace. We built the only payment rails every agent runs on.

### One-line positioning
> Razorpay: "Build agents that do things." (UI play)
> Cashfree: "Power any agent that handles money." (infrastructure play)

---

## Section 18 — Artifacts Created Across the Conversation

All in `/Users/mothi.venkatesh/Documents/relay-launch/` unless noted:

| File | Purpose |
|---|---|
| `00-README.md` | Index of all artifacts |
| `01-prfaq.md` | Press release + customer FAQ + internal FAQ |
| `02-positioning.md` | Original positioning canvas (April Dunford framework) |
| `03-gtm-strategy.md` | Phased launch plan + DIN integration |
| `04-launch-blog.md` | Public-facing launch blog (~900 words) |
| `05-launch-emails.md` | 4-email cohort recruitment sequence |
| `06-pr-questionnaire-completed.md` | Filled PR questionnaire with all gaps closed |
| `07-launch-readiness-questions.md` | Engineering readiness questions + drafted PMM answers |
| `08-template-library-spec.md` | **Source of truth on shipped vs roadmap templates** |
| `09-mcp-commitment-memo.md` | Decision memo asking Eng for MCP within 6-8 weeks |
| `positioning-cashfree-relay-v2-2026-04-29.md` | v2 positioning doc (MCP-first anchor) |
| `razorpay-agent-studio-strategy-explained-2026-04-29.md` | Five-layer Razorpay strategy decode |
| `cashfree-relay-landing-v2.html` | Live landing page in agentic-workflows register, 7 sections, italic-serif emphasis |
| `Positioning - Content Framework - Cashfree Relay - Payments MCP.csv` (in Downloads) | 8-persona positioning CSV |

### Memory files saved to `/Users/mothi.venkatesh/.claude/projects/-Users-mothi-venkatesh-Documents/memory/`
- `cashfree-relay.md` — product state and connector list
- `reference_razorpay-agent-studio.md` — Razorpay competitive intel
- `reference_gtm-ops.md` — Cashfree's GTM operating model

---

## Section 19 — Key Decisions Locked

These are decisions made during the conversation that should not be re-litigated without good reason.

| Decision | Status | Locked by |
|---|---|---|
| Position Cashfree Relay as Payments MCP, not Agent Studio | Locked | User direction (May 6) |
| Use HITL terminology, not Maker/Checker | Locked | User direction |
| Drop ₹2 lakh crore claim; lead with 800,000 businesses | Locked | User direction |
| Use "public preview," not "private beta" | Locked | User direction |
| Hero uses "Agentic workflows for your payment operations" with italic-serif emphasis on "payment operations" | Locked (current page) | User direction |
| Two-wave launch: quiet preview → loud GA | Locked | Leadership |
| Bolna confirmed as build partner | Locked | Govardhan |
| Govardhan owns launch partners | Locked | Mayank |
| Free during public preview, transparent tiered pricing at GA | Locked | Reeju + Finance |
| 4 live automations only — no overclaim of specialist agents | Locked | Eng + PMM |
| MCP server, Agent Skills, Visual builder live in public preview | Locked | Eng |
| 6 specialist agents on Q3 roadmap (RTO Recovery, Refund Triage, Cart Recovery, Dispute Response, Settlement Reconciler, Subscription Recovery) | Locked | Product |
| Don't name Razorpay in PR; reframe instead | Locked | Comms posture |
| AI Suite (Cashfree Here, Voice AI) and Relay are two separate products | Locked | Product portfolio |

---

## Section 20 — The Single Critical Path

**DIN approval → 9 artifacts → 5 eSigners → Launch Day.**

Eight to ten business days from DIN filing to launch day. Earlier requires Ram bypass with 48-hour retroactive documentation.

If artifacts slip 3 days, launch slips a full week.

---

## Section 21 — The Strategic Frame in One Paragraph

Cashfree Relay is the Payments MCP. We're not building an Agent Studio because that category is being commoditized by OpenAI, Anthropic, Google, Microsoft, and Salesforce — and Razorpay already named it for the Indian payments adjacent market. Going one layer down lets us claim the protocol-level land grab where almost no one is competing and Stripe is the only real comp. Our moat is payments rails plus India-specific compliance, not LLM UX. Our buyer is every developer building an AI agent that needs to move money — which is increasingly every agent. Our wedge is that we run on whichever AI the team already uses, with HITL by default, transparent pricing, and Indian payment primitives no global tool ships. Wave 1 is a quiet public preview that builds proof from 100 design-partner merchants. Wave 2 at GA is the loud category-claim moment with Reeju, Ram, leadership, and tier-1 press. Bolna is the build partner. Govardhan owns launch partners. Specialist agents (RTO Recovery, Refund Triage, Cart Recovery, Dispute Response, Settlement Reconciler, Subscription Recovery) ship Q3 with outcome-based pricing. The Year 1 ceiling is 500 merchants and ₹12-15 cr ARR; Year 3 is ₹80-120 cr at software margins. Don't try to win Razorpay's category. Build the adjacent one underneath.

---

## How to use this document going forward

1. **New PMM/Product/Sales conversations:** read Sections 1, 2, 5, and 9 first. That's the strategic core.
2. **Drafting any external copy:** anchor on Section 6 (pillars), Section 16 (what to avoid), and Section 17 (hero copy).
3. **Honest product claims:** check Section 4 (what's shipped) and `08-template-library-spec.md` before any external claim.
4. **Launch execution:** Section 11-15 covers the GTM, partners, content, and risks.
5. **Persona-specific copy:** Section 8 plus the positioning CSV in Downloads.
6. **Competitive context:** Section 2 plus `razorpay-agent-studio-strategy-explained-2026-04-29.md`.

When the strategic thesis itself comes up for review (Payments MCP vs alternatives), Section 5 captures the reasoning. Don't re-litigate without checking what Workato did, what FinQub did, and what Razorpay's current state of play is.

---

*End of context document. Last updated 2026-05-06.*
