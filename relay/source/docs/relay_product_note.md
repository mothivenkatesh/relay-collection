# Cashfree Relay

# Cashfree Relay

**Product note · Draft**

---

## **TL;DR**

Every merchant on Cashfree runs payment operations through some combination of three surfaces — a **dashboard**, **glue code**, and **manual stitching across SaaS tools**. Agentic AI is collapsing all three into a fourth surface: the AI assistant the merchant's team is already inside (Claude, ChatGPT, Cursor). Cashfree Relay is our bet that the right place to meet that shift is the **MCP layer, not another dashboard**.

* Relay is three things in one product: a **Cashfree MCP** (payments primitives exposed as agent-callable tools), **Agent Skills** (India-payments expertise encoded as reusable instruction packs), and a **Visual Workflow Builder** (managed orchestration with audit, retries, and human-in-the-loop). They are distinct surfaces with shared substrate — not three separate products, and not one monolithic agent.  
* The competitive picture has two distinct opponents with different reasons to take it seriously. **Razorpay Agent Studio** is a walled-garden, hosted, outcome-priced bet aimed at MDR-replacement and pre-IPO valuation. **n8n** is the open, dev-loved workflow automation layer that already owns Indian operator mindshare. We are not racing either head-on; we are claiming the slice neither owns — *open MCP \+ payments-native \+ India templates \+ Cashfree's compliance perimeter*.  
* The biggest near-term lever is **distribution into Claude/ChatGPT/Cursor directories**, not feature depth. Wave 1 (Public Preview, now → end May) is a quiet recruit-and-instrument phase. Wave 2 (GA, Q3) is the loud moment, gated on outcome pricing, 6 specialist agents, and 8 named launch partners.  
* Several foundational design and pricing questions (workflow vs. agent primacy, take-rate vs. usage pricing, maker–checker calibration, Skills authoring rights, PCI scope across third-party connectors) need to be closed before GA. §5 surfaces these as work items rather than papering over them.

---

## **1\. The framing: where AI shows up in a merchant's payment operations**

Every recurring operational task a Cashfree merchant runs today happens on one of three surfaces. Framed from the **merchant operator's** perspective:

| Surface | Operator question | Cashfree's position today |
| ----- | ----- | ----- |
| **Dashboard** | "Show me what happened, let me act on it." | Mature. Cashfree dashboard handles reporting, refunds, payouts, settlements. |
| **Glue code / SaaS automation** | "Wire this event to that system without me touching it." | Thin. Webhooks and APIs exist; the orchestration layer is owned by n8n, Zapier, Make, or in-house code. |
| **AI assistant** | "Just do this for me, in plain English, where I already work." | Greenfield. No native presence in Claude, ChatGPT, Cursor. **This note.** |

**Everything below is about the third surface.** The first is mature and not the discussion. The second is what Relay's Visual Workflow Builder participates in, but the *strategic* unlock is the third — **meeting the merchant's team inside the AI tool they already opened this morning**.

## **Who we're building Relay for**

Relay is built for **three personas inside the same merchant account** — not one. They use Relay differently, on different surfaces, for different jobs. A sales rep should be able to name all three on the call.

| Persona | Where they work today | What Relay is for them | Day-1 use case |
| :---- | :---- | :---- | :---- |
| **The Operator** — Ops lead, Founder's Office, Finance/RevOps at SMB or D2C | Cashfree dashboard, Google Sheets, WhatsApp, Slack, increasingly Claude or ChatGPT | The AI ops teammate that runs the boring, repetitive payment work in plain English | Threshold alerts, hourly failed-payment digest, transaction summary to Sheets |
| **The Builder** — Developer, founding engineer, technical PM | Cursor, Claude Code, the merchant's own codebase | The MCP that turns Cashfree into tool calls in their AI IDE — extend templates, wire to internal systems, build custom agents | Custom workflow on top of Cashfree MCP, ERP/CRM wiring, internal automation |
| **The Partner** — Web agency, freelance integrator, indie builder, System Integrator | Their own consulting practice, multiple merchants' Cashfree accounts | The platform to package and resell verticalised Skills (e.g., "RTO recovery for jewellery D2C") | Authoring and distributing Skills; reselling Relay-powered automation as a service |

### The primary persona is the “Operator”

Builders and Partners matter — **but the Operator is who Relay is built for first**, and who every product decision is calibrated against. Three reasons:

1. **They're the ones drowning in repetitive work today**. The CSV-export-paste-WhatsApp routine happens every morning at 800,000 merchants. Builders have other tools. Operators don't.  
2. **They're the ones already shifting to AI assistants**. The ops lead at a D2C brand who used to open the Cashfree dashboard first now opens Claude first. We don't have to teach a new behaviour; we have to plug into one already forming.  
3. **They're the ones our messaging is hardest with**. Builders understand "MCP" without explanation. Operators don't — and shouldn't have to. Every UX call (templates over canvases, plain-English over JSON, Skills over SDKs) is biased toward the Operator. Builders get power tools as a side effect; Operators get the product.

**Practical implication for sales**: when you're qualifying a merchant, ask who in their team will use Relay. If the answer is "our developer" — great, but route them to MCP \+ Claude Code. If the answer is "our ops lead / founder's office / finance" — that's the bullseye, lead with the four native templates and the Workflow Builder.

### Who Relay is not for in v1

Three personas we are explicitly not designing for in v1, and reps should redirect rather than promise:

* **Enterprise risk and compliance teams as a buying centre**. The AI-action-on-payments story is real, but enterprise procurement needs RBI-grade artefacts, custom maker–checker, dedicated tenancy. v1 doesn't carry those yet — that's a Wave 2 conversation.  
* **Non-Cashfree merchants**. Relay only knows the merchant's payments operations because it sits on Cashfree's data. If they're on Razorpay or PayU, this isn't the entry point — that's a payments-migration conversation.  
* **Customers (the merchant's end users)**. Relay is internal-facing. The end customer never talks to Relay directly. Cart abandonment voice (Bolna) is the closest, and even there the merchant configures the call — the customer doesn't.

---

## **2\. Why this is a big problem**

### **2.1 The leak, sized**

Payment operations on the merchant side are not one job — they are a long tail of repetitive, low-judgment tasks that sit between Cashfree's primitives and the merchant's actual goals. RTO triage on COD orders. Refund approval queues. Daily reconciliation between settlement reports and accounting tools. Failed-payment digests to ops Slack. Customer-side payment-link generation when checkout breaks. Thresholded alerts on suspicious spikes.

Most of these tasks are done in one of three ways today, none of them good:

1. **Manually, in the dashboard.** Ops opens 4 tabs, exports a CSV, eyeballs it, copies cells into Sheets, pastes into WhatsApp. Repeat every morning. Cost is bandwidth, not money — but the bandwidth is finite and the tasks are dull.  
2. **Through glue code or no-code (n8n, Zapier, Make, in-house Python).** Works, but every merchant rebuilds the same patterns. The integration is brittle (webhook signatures, retries, idempotency), the auth is the merchant's problem, and the compliance posture is whatever the merchant's contractor cobbled together.  
3. **Not at all.** The task gets dropped because it doesn't clear the bar of "worth automating." This is the largest bucket and the least visible.

We don't currently have a clean internal number for how many recurring operational tasks the median Cashfree merchant runs in a week, or what share of them are automated vs. manual vs. dropped. This figure is directional and is listed in §5 as a validation work item. The qualitative shape — *long tail, low judgment, currently expensive to wire up* — is well-attested in merchant interviews.

The point is structural: the value pool sitting underneath payment operations is large, fragmented, and currently captured almost entirely outside Cashfree (by n8n, Zapier, in-house engineering, or human time). Agentic AI is the first interface cheap enough to reach the long tail.

### **2.2 Who is doing what in this space**

This is a contested space. A short map of what exists today, referenced as context:

| Player | Product | Surface | Pricing | India fit | Notes |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **Cashfree** | Relay (Preview) | MCP \+ Skills \+ Workflow Builder | Free in preview; TBD at GA | India-native | 4 shipped automations, MCP live, public preview. **This note.** |
| **Razorpay** | Agent Studio (Mar 2026\) | Hosted in-dashboard agent runtime | Outcome-based take rate (5–10% of recovered revenue), bundled MDR for enterprise | India-native | 8 listed agents, Claude Agent SDK underneath, walled garden. Ties to MDR-replacement and pre-IPO valuation narrative. |
| **n8n** | Workflow automation | Self-hosted / cloud canvas | Per-execution / seat | Strong dev mindshare in India | Owns the Indian operator-automation imagination. Not payments-native; merchants build payment patterns themselves. |
| **Zapier / Make** | Workflow automation | SaaS canvas | Per-task | Generic | Low payments specificity; weak India connector coverage; high price-per-task at scale. |
| **Pipedream / Workato** | Dev-leaning automation | API-first canvas | Per-execution | Limited India presence | Stronger for dev personas, irrelevant for non-technical ops. |
| **Bolna, Sarvam, ElevenLabs** | Voice / agent infra | Underneath agent products | Usage | India-aware (Bolna, Sarvam) | Picks-and-shovels layer. Likely Relay partners, not opponents. |
| **Stripe Agent Toolkit, Plaid, Adyen** | Global agent toolkits | MCP-ish or SDK | Bundled with PG | Not India | Useful as a reference for shape, not as in-market competition. |

What this tells us:

1. **Razorpay is fighting a different war.** Their motion is MDR replacement and IPO valuation — the agent stack is downstream of that. They will price aggressively (free trials, outcome-based take rate, enterprise bundles into MDR) because every basis point of merchant retention matters more to them than per-agent revenue. We should not match that pricing reflexively. We should pick a model that fits *our* book — usage-priced infrastructure with optional outcome upgrades for specific specialist agents, not a blanket take-rate model.  
2. **n8n is the harder strategic competitor for the operator persona.** Razorpay competes for *enterprise narrative*. n8n competes for *the SMB merchant's automation reflex*. Operators who already think "I'll wire this up in n8n" are the ones we most need to redirect to Relay — and the way we redirect them is by being measurably better at the *payments-specific* slice, not by trying to out-canvas n8n.  
3. **MCP is the protocol-layer leverage.** Razorpay's own CPO has confirmed Agent Studio runs on private connections, not their own MCP server. Their MCP exists separately, for "customers using agents in their workflows." That gap is real: their default consumer is locked inside Razorpay's UI, not inside the merchant's Claude or Cursor. Cashfree leading on open MCP is a narrow but defensible position they cannot easily mirror without contradicting their own walled-garden pitch.  
4. **Our structural advantages are protocol openness, India connector depth, and merchant compliance posture.** Cashfree's PCI DSS Level 1 / SOC perimeter combined with native triggers across the full payment lifecycle (Payment Success/Failed/Dropped, Refund, Webhook, Schedule) is hard to replicate by either a horizontal automation tool or a closed agent runtime.

### **2.3 Why agentic — and specifically MCP — changes the economics**

Two questions come up every time we discuss Relay internally. Both deserve direct answers.

**Q1. "Why MCP and not a hosted agent runtime like Razorpay's?"**

A hosted runtime is the right choice if your goal is to lock the merchant's automation surface inside your own dashboard and meter it. It is the wrong choice for three reasons that matter to Cashfree's merchants specifically:

* **The merchant's team is not in the Cashfree dashboard. They are in Claude, ChatGPT, or Cursor.** Putting the agent in our dashboard means the operator has to remember to switch contexts to use it — the exact friction we should be removing. MCP inverts this: Cashfree shows up where the work already happens.  
* **Lock-in is an explicit anti-feature for the kind of merchant we want.** Cashfree's growth thesis is partly built on merchants who chose us *over* Razorpay because of less platform tax. A walled-garden agent runtime is a platform tax of a new kind. An open MCP is the consistent move.  
* **The compliance perimeter is the same in both cases, but the trust story is different.** A hosted runtime requires the merchant to trust Razorpay's agent to act on their behalf inside Razorpay's UI. An MCP-based design lets the merchant audit which tool calls fire from which client, with the audit trail living inside Cashfree. Same security posture, more legibility — which matters more to risk and finance teams than the demo audience usually credits.

We are not proposing MCP *instead of* a managed surface. The Visual Workflow Builder is exactly that managed surface, for operators who want a canvas, scheduling, retries, and a single place to monitor runs. The point is that the **default substrate is open**, and the managed surface is a layer on top that the merchant can opt into without locking themselves to it.

**Q2. "Why not just n8n? Don't Indian operators already use it?"**

They do, and that's the sharpest threat — but n8n's win is on the *general* automation imagination, not on the *payments* slice. Three structural gaps:

* **Payments primitives are not first-class.** In n8n, "create a refund" is an HTTP request the merchant configures. In Relay, it is a tool call with the right idempotency, signature, and audit handling baked in. The first time a merchant double-issues a refund because their n8n retry logic was wrong, the cost outruns a year of automation savings.  
* **India-specific workflows are not pre-built.** RTO/COD recovery, fake-order detection, daily settlement reconciliation, UPI-prepayment-link nudges — these are not on n8n's template gallery and the merchant has to assemble them from scratch. Relay ships them as Skills.  
* **Compliance overhead lands on the merchant.** When a merchant's n8n workflow handles payment data, the merchant inherits the PCI scope. With Relay, the agent operates inside Cashfree's compliance perimeter and only sees the answers it's allowed to. This shifts a real burden the merchant currently carries silently.

n8n will continue to be the right answer for the *long tail* of non-payment automation a merchant runs. Relay is the right answer for the payments slice. Co-existence is the realistic equilibrium, not displacement.

### **2.4 What's newly possible**

Until roughly 12 months ago, building an "AI ops teammate" for payments was a science project. That has changed:

* **MCP has converged.** Anthropic, OpenAI, and now most major agent surfaces support a shared tool-calling protocol. One MCP server reaches every important AI tool the merchant might use, present and future. This is the single biggest shift — building agent integrations is no longer per-vendor work.  
* **Agent Skills as portable expertise.** Encoded instruction packs (webhook signatures, refund flows, RTO heuristics) travel with the merchant across tools. The expertise is no longer trapped in a vendor's UI.  
* **Distribution lives in directories.** Claude, ChatGPT, and Cursor are starting to host MCP / extension directories. Listing in those directories is now a real distribution channel — not yet at app-store scale, but on a credible trajectory.  
* **Merchants are already inside these tools.** This is the quiet shift. The ops lead at a D2C brand who used to live in the Cashfree dashboard now opens Claude first. We don't have to teach a new behavior; we have to plug into one already forming.

---

## **3\. What we're building**

A structural note first: Relay is three distinct surfaces — MCP, Skills, Visual Workflow Builder — with shared substrate. They serve different operator contexts. Trying to collapse them into one ("just an agent platform" or "just a workflow builder") will under-serve all three. The product strategy is to keep the surfaces sharp and the substrate (auth, audit, primitives, compliance perimeter) unified.

### **3.1 Cashfree MCP (foundation)**

**Problem.** A merchant's ops or engineering team wants to ask their AI assistant a question about Cashfree data — or have the assistant act on it — and today they either copy-paste from the dashboard or write glue code. Both are cost without leverage.

**Product.** A Cashfree MCP server that exposes payment primitives — orders, payments, refunds, payouts, settlements, subscriptions, payment links, customer data — as tool calls any MCP-compatible AI agent can invoke. Auth and scoping run inside Cashfree's existing compliance perimeter. The agent never sees raw payment data; it sees the answers it is authorized to receive.

**Key design calls:**

* **Open and unbranded protocol stance.** Works in Claude today, ChatGPT and Cursor next, anything MCP-compatible after that. No proprietary SDK. This is deliberate and is the single most defensible position against Razorpay's walled garden.  
* **Scoping and audit by default.** Every tool call is recorded — what fired, why, which client, which workflow version, which data was touched. 90-day retention, exportable. This is non-negotiable; without it, no risk team approves agent action on payments.  
* **Read-before-write defaults.** Read tools are enabled out of the box. Write tools (refunds, payouts, customer messages) require explicit merchant configuration and default to maker–checker. This is a posture decision, not a v2 feature — relaxing it later is much easier than tightening it.  
* **Distribution into directories.** The MCP must be listed in Claude, ChatGPT, and Cursor MCP directories on day one of GA. Wave 1 target: 1,000 installs across directories. This is a marketing surface as much as a product one and should not be deprioritised when engineering is busy.

### **3.2 Agent Skills (India-payments expertise, encoded)**

**Problem.** A generic AI assistant pointed at Cashfree's MCP knows the API surface but not the *practice* — it doesn't know that Indian COD has 30%+ RTO rates, that fake-order patterns cluster around specific BIN ranges, that refund reconciliation in Tally has its own quirks. Without Skills, every merchant rediscovers payments-specific patterns from first principles.

**Product.** A library of Skills (instruction packs) for the highest-leverage Indian payment workflows: RTO/COD recovery, refund triage, fake-order detection, abandoned-cart recovery, daily reconciliation, payout orchestration, settlement-report-to-accounting sync, threshold alerting. Each Skill is opinionated: it knows the typical inputs, the right tool sequence, the failure modes, and the human-in-the-loop checkpoints.

**Key design calls:**

* **Skills are versioned and forkable.** A merchant who wants to customize the RTO Skill for their specific category gets a fork, not a config form. This treats the Skill as code, not as a wizard.  
* **Skill authoring is a partner motion, not a Cashfree-only motion.** Web agencies, freelance integrators, and indie builders should be able to publish verticalised Skills (e.g., "RTO recovery for jewellery D2C", "Refund triage for ed-tech subscriptions"). Whether this lives behind review or is fully open is an open question (§5).  
* **Skills do not bypass the maker–checker model.** A Skill can draft a refund. It cannot fire one without the configured human approval. This is enforced at the MCP layer, not the Skill layer, so a malicious or buggy Skill cannot drain a merchant's payouts.  
* **Wave 1 ships 6–8 Skills aligned to the highest-volume operator pain.** Wave 2 expands via partner authoring. Going broader earlier is a temptation to resist; depth on a few Skills builds more trust than breadth on twenty.

### **3.3 Relay Workflow Builder (managed orchestration)**

**Problem.** Some operators don't want to live in an AI assistant. They want a canvas — visual nodes, schedules, retries, a dashboard of runs. They also want a place where workflows generated *inside* Claude can be promoted, versioned, monitored, and handed off to a teammate.

**Product.** A no-code visual workflow builder inside the Cashfree dashboard. Same primitives as the MCP. Native triggers across the payment lifecycle (Success, Failed, Dropped, Refund Success, Cancelled, Schedule, Webhook). Live integrations to Google Sheets, Slack, WhatsApp Business, Gmail, Calendar, [Cal.com](http://cal.com/), with more shipping based on preview-merchant requests.

**Key design calls:**

* **The canvas is the *managed* version of the same thing the MCP enables.** A workflow generated in Claude lands in the builder as a real, editable artifact — not a screenshot. Promotion from "I asked Claude" to "this runs every morning at 7" should be one click.  
* **Run dashboards, not just workflows.** Every run shows what fired, what was approved, what was skipped, what failed and why. Audit trail and operator dashboard are the same surface.  
* **The builder is not the differentiation.** n8n's canvas is more mature and will remain so for a long time. We win by being payments-native and by the canvas being the *least* of three surfaces a merchant uses, not the most. Trying to out-feature n8n on the canvas is the wrong fight.  
* **Confidence-gated execution.** Each step has a configurable confidence threshold; below it, the step lands in a human queue with reasoning attached. This is a Relay-level guarantee, not a per-Skill flag.

---

## **4\. How the pieces fit**

| Operator context | Primary surface | Where the work happens | Skills role | Audit |
| ----- | ----- | ----- | ----- | ----- |
| One-shot question or action | Cashfree MCP in Claude/ChatGPT/Cursor | Inside the AI tool | Optional context | Full tool-call log |
| Repeated India-specific workflow (RTO recovery, refund triage) | Skill invoked in AI tool, then promoted to builder | AI tool → Workflow Builder | Central — encodes the pattern | Workflow-level run history |
| Engineering extension (custom agent, ERP wiring) | MCP \+ custom Skill via Claude Code | IDE \+ MCP server | Authored, not consumed | Merchant-managed |
| Ops monitoring of recurring runs | Visual Workflow Builder | Cashfree dashboard | Embedded in workflow nodes | Run dashboard |
| Partner-built verticalised workflows (D2C jewellery, ed-tech) | Authored Skill \+ builder template | Partner authors, merchant installs | Partner is the seller | Same as merchant-built |

Three structural advantages hold this portfolio together: **Cashfree's payment-lifecycle event surface** (native triggers across success/failed/dropped/refund/webhook), **the existing compliance perimeter** (PCI DSS Level 1, SOC, DPDP-ready), and **the existing trust relationship with 800,000+ merchants**. None of these can be cloned by a horizontal automation tool; none can be cloned by a closed agent runtime without rebuilding payments infrastructure first.

---

## **5\. What we're proposing, and what we need to resolve first**

### **Proposals**

1. **Wave 1 — quiet preview, recruit-and-instrument (now → end May).** Ship the MCP server, 6–8 Skills, the Workflow Builder with current 4 automations, and 5 host-directory listings (Claude, ChatGPT, Cursor, plus two long-tail). Goal: 10 named merchants running ≥1 workflow, 500 MCP installs, 500 Skill installs, 3 case studies with quantified outcomes (even small ones). This wave is build-in-public with developers and partners; it is not a press cycle.  
2. **Wave 2 — flagship GA launch (Q3).** Gated on six specialist agents shipped, outcome pricing decided and tested with 8 named launch partners across L1/L2/L3, and at least one outcome-based contract signed. Tiered launch: Reeju → Ram & leadership → team → PR → influencers. This is the loud moment.  
3. **Distribution-first investment posture.** Until we hit 1,000 directory installs, every additional engineering hour spent on the Workflow Builder is the wrong hour. The bottleneck is reach, not feature depth. Reorder roadmap accordingly.  
4. **Maintain protocol openness as a strategic constraint, not a tactic.** Relay ships nothing that requires a Cashfree-proprietary client. Every capability must be reachable via standard MCP. Internal pressure to add "Relay-only" optimizations should be resisted; the open posture *is* the moat.

### **Questions to resolve before GA**

These are open questions the doc deliberately does not force an answer to. They are work items, not decisions.

* **Pricing model.** Free in preview is correct. At GA, the choice is between (a) usage-based on tool calls / workflow runs, (b) outcome-based take rate on specific specialist agents (RTO recovered, fraud prevented), (c) tiered subscription per merchant, or (d) some hybrid. Razorpay's outcome-based stance is aggressive and IPO-narrative-driven; matching it reflexively is wrong. The right answer probably mixes (a) for the platform and (b) for a small number of high-value specialist agents. Needs a separate pricing note with finance and a top-10-merchant gut check.  
* **Workflow vs. agent primacy in positioning.** The current positioning doc says "don't call it a workflow tool, it's an agent platform." This is partly defensive against being lumped with n8n, but operators *understand* workflows and don't yet understand agents. Worth pressure-testing whether the public preview lead message should be "agent platform" (aspirational, novel) or "the payments-native workflow tool that runs inside your AI" (concrete, comparable). Probably the latter for SMBs, the former for enterprise.  
* **Skill authoring rights and partner ecosystem.** Open authoring (anyone publishes a Skill) maximises long-tail coverage but exposes merchants to bad/malicious Skills. Reviewed authoring is safer but slower. Likely answer: a tiered model (verified Skills from Cashfree and named partners, community Skills with explicit warning), but the threshold for "verified" needs a clear rubric. Decision needs input from product, security, and partnerships.  
* **Maker–checker calibration.** Confidence-gated execution is a sound principle. The unresolved question is the *default* threshold for each Skill, and whether that default is set by Cashfree (paternalistic, safer) or by the merchant (autonomy, potentially riskier). Needs a small data exercise on existing payment-action error rates to calibrate where defaults should land.  
* **PCI scope across third-party connectors.** The MCP server runs inside Cashfree's perimeter. The Workflow Builder calls out to Google Sheets, Slack, WhatsApp, Gmail. When payment data flows to those connectors via a workflow, who owns the PCI scope? Likely answer: data minimisation at the edge (only non-cardholder data leaves the perimeter), but this needs an explicit security review and a written contract pattern.  
* **Build vs. partner on workflow runtime.** The Workflow Builder is currently in-house. n8n is a credible OSS runtime to fork or embed if the build path stalls. Trade-offs (control vs. velocity, differentiation vs. ecosystem leverage) deserve their own short note before we commit more engineering quarters.  
* **Operational task volume baseline.** The §2.1 sizing rests on a directional claim about how many recurring operational tasks the median merchant runs, and what share is currently manual / scripted / dropped. We don't have this number cleanly. Proposed action: instrument 20 preview merchants with a manual operational-log diary for two weeks; pair with dashboard-event logs to triangulate. Without this, we can't prove ROI to merchants, can't price defensibly, and can't measure Relay's penetration honestly.  
* **Building on prior feedback** — any internal reporting on Relay adoption needs to split external vs. internal merchants, conversation/workflow types, response times. Bake into the Wave 1 instrumentation from day one rather than retrofitting.

# Clarifying Questions

## **Engineering Product Questions: Capabilities**

* Walk me through what happens from the moment a Cashfree Payment event fires to when a workflow completes. What's the data path?  
  * **Answer**: XXX  
* What does the payload of a Payment Success event actually contain? What fields does a developer get that they wouldn't get from a generic Zapier webhook?  
* What can the HTTP Request connector do that a normal webhook integration can't?  
* Where does the AI node sit in the workflow, Is it a step, a condition, or something else? What model is it running on?  
* What's the hardest technical thing about Relay that no one outside the team knows?  
* What can Relay do today that even your internal docs don't explain well?

## **Right to Win (Differentiation)**

**If a Cashfree merchant told me they're switching to Razorpay Agent Studio because it does disputes and abandoned cart recovery out of the box, What do I tell them? What does Relay give them that Agent Studio never will?**

**Answer**: Razorpay Agent Studio & their Agents are in private Beta and they themself claim that Agents can do mistakes. Payments being critical piece of business it’s not worth migrating to a platform with unreliable Agents.

* If a developer already uses n8n self-hosted. What does Relay give them that n8n doesn't? Be specific, not generic.  
  * **Answer**: Relay is completely indigenous, with HITL support and access to Cashfree payment triggers, to build payment & revenue ops workflows.  
* What does being inside the Cashfree ecosystem give Relay that no external automation tool can replicate?  
  * **Answer**: Access to entire Cashfree Payements & KYC Stack.  
* Razorpay Agent Studio feeds their entire network's dispute history into agent context. What Cashfree-native intelligence does Relay inject into a workflow or AI node that only Cashfree can provide?  
  * **Answer**: RIght now, we don’t have that capability.  
* Is there anything in Relay's architecture — **Data residency, latency, reliability** that we've built specifically for Indian fintech use cases?  
  * **Answer**: Relay runs on top of the payment rails we built at Cashfree. Which serves over 1.6Million+ merchants.  
* What's the one thing you built that you're genuinely proud of and haven't seen in any competitor?  
  * **Answer**: We built an indigenous workflow builder with human-in-the-loop & enterprise-grade MCP that works on all popular LLMs so team can use in any of their preferred tools easily.

# Comparison

## **What a Razorpay Agent Can Do That Relay Can't**

### 1\. Make autonomous decisions with confidence scoring

The dispute agent calculates win probability and only auto-acts above a threshold (e.g., 70%). Below that, it routes to human review.

Relay triggers a workflow. It can't calculate "should I act or not" — that's ML inference on top of payment data, not automation.

---

### 2\. Make live voice calls

The abandoned cart recovery agent literally calls the customer and negotiates. That's a voice AI agent, not a workflow.

~~Relay has no voice surface at all.~~**This we can do with Bolna AI.**

---

### 3\. Feed Razorpay's proprietary intelligence INTO the agent

The dispute agent uses Razorpay's global learnings — dispute outcomes across all merchants, Visa/Mastercard pattern data — as context. Not just the merchant's own data.

Relay uses Cashfree events as triggers, but doesn't inject Cashfree's network-level intelligence into the AI reasoning. The AI node in Relay knows only what you pass it.

---

### 4\. Maintain agent memory across runs

Razorpay agents have persistent memory — the dispute agent learns from its own previous submissions. Relay workflows are stateless. Each run starts fresh.

---

### 5\. Run evals before acting

Before taking any action, the agent runtime runs evals. If confidence is below threshold, it drops to manual queue. This is a reliability layer built into the agent itself.

Relay has no equivalent. A workflow runs or fails — there's no "I'm not confident enough, I'll ask a human."

---

### 6\. Contextual in-product discovery

Agents surface themselves inside the existing Razorpay dashboard — if you're viewing disputes manually, the dispute agent suggests itself. It meets the operator where they are.

Relay requires the user to come to the builder and build something themselves. No in-context nudging.

---

### 7\. Third-party agent marketplace

Partners like Nugget have already published agents in Razorpay's marketplace. Merchants can install specialist agents built by third parties.

Relay has no marketplace. Skills exist (Claude/ChatGPT), but they're not payment-domain agents built by ecosystem partners.

---

### 8\. Plain English custom agent creation

Merchants can describe a new agent in natural language and Razorpay creates it.

Relay's custom motion is: open the builder, drag nodes, configure connectors. It's no-code, not natural-language.

---

### 9\. Agent health dashboard

Dedicated view: X operations processed, Y dropped, Z failed — per agent, per time period.

Relay has workflow run logs. Not the same as agent-level health monitoring with drop-off rates.

---

| Dimension | Razorpay Agent Studio | Cashfree Relay |
| :---- | :---- | :---- |
| Primary unit | Agent (autonomous, domain-trained) | Workflow (trigger → action) |
| Decision making | Confidence scoring \+ evals | Binary: runs or errors |
| Data layer | Razorpay network intelligence as context | Cashfree events as triggers only |
| Discovery | Contextual, in-dashboard | User must come to builder |
| Ecosystem | Third-party agent marketplace | No marketplace |
| Memory | Persistent across runs | Stateless |
| Voice | Yes (live calls) | No |

---

## **What This Actually Means for Relay's PMM**

Razorpay didn't build a better workflow tool. They built a different category — domain-trained payment agents. Fighting them on "agents" is a losing battle.

Relay's defensible position stays: workflow-first, not agent-first. The Cashfree-native event triggers (Payment, Refund, Dispute lifecycle) are real. The MCP surface is real. But Relay needs to be honest internally — it's an automation platform, not an agent platform yet.

# Use cases

## **Use Case 1: Get a calendar event every time a customer pays**

### Who needs this

Founders running webinar / event / cohort-based / B2B-SaaS / consulting / agency / premium D2C businesses — where each transaction is a meaningful, calendar-worthy moment. The PG Growth deck identifies these slices specifically (slides 14, 16: webinars, event registrations, education admissions). Secondary user: head of customer success / onboarding who wants a calendar nudge to start manual onboarding the moment payment clears.

Not for high-volume / low-ticket merchants (quick commerce, marketplaces) — the calendar would flood. They should use Use Case 4 instead.

### The situation today

A founder running a cohort-based business (or selling consulting hours, or ticketing webinars) cares about every transaction. Today, they hear about it from a Slack DM the ops lead sends, an email digest, or by checking the dashboard themselves. They miss some, and they don't see them in the place they actually live — the calendar app they check ten times a day.

### What the workflow does

When a customer's payment succeeds in Cashfree, a calendar event automatically gets created in the founder's Google Calendar or Cal.com. The event title carries the customer name and amount; the description has the order ID and a deep-link back to the Cashfree dashboard for that payment. The founder filters by amount, product, or any field in order metadata, so the calendar only catches the events that matter.

Configuration:

1. Pick Google Calendar or Cal.com (one connector per workflow instance).  
2. Pick the calendar (personal, shared team, or a specific Cal.com booking calendar).  
3. Set filters: amount threshold, specific product/SKU, UTM, or "all payments".  
4. Customise the event template (title, description, duration).

### How it works under the hood

* Trigger: Cashfree's Payment Success event.  
* Action: Calendar API write (Google Calendar OAuth or Cal.com API).  
* Payload: payment time, amount, currency, customer name (if present in order metadata), order ID, dashboard deep-link.  
* Latency target: under 30 seconds from Payment Success to calendar write (p95).  
* Idempotency: duplicate Payment Success events do not create duplicate calendar entries.  
* Failure handling: failed write logged in run history; payment is never blocked.

### Edge cases worth knowing

* Calendar OAuth revoked → run marked failed, surfaced in dashboard.  
* Customer name absent from order metadata → fallback to order ID in event title.  
* Cashfree retries the Payment Success event → idempotency key prevents duplicate calendar entry.

### What success looks like

* Adoption: number of merchants installing this in preview.  
* Engagement: events fired per merchant per week.  
* Failure rate: under 2% of fires fail to write.

### What we don't promise

* It does not increase revenue. Calendar events don't cause conversion.  
* No "saves X hours per week" claims. We don't have a baseline yet.  
* It does not replace the merchant's CRM. It complements.  
* Sensitive payment details (card numbers, CVV, bank account numbers) never appear on the calendar.

---

## **Use Case 2: Hear about a big-ticket order on the channel you actually check**

### Who needs this

Founders. Personal WhatsApp is the default channel; Slack DM for founders running on Slack. Secondary persona: head of revenue / business / operations / finance, configured by the founder, pointed at a team Slack channel with a lower threshold. The founder gets the ₹2L+ alerts; the team gets ₹50K+ alerts. Same use case installed twice.

Not for merchants who need anomaly detection (unusual but not necessarily large transactions) — that's a different use case on the roadmap.

### The situation today

Every founder asks the same question: "tell me when something big lands." Today they either check the dashboard manually, or rely on the ops lead pinging them in Slack, or learn about it the next morning. The high-ticket order — the ₹2L deal that just closed — needs to surface to the founder in real time, on the channel the founder actually checks, not when ops gets around to mentioning it.

### What the workflow does

When a payment crosses an amount threshold the merchant has set, a notification fires on the chosen channel (WhatsApp, SMS, email, Slack) — with the amount, customer name, payment method, order ID, and a dashboard link. Multiple thresholds can route to different channels and different people. The founder's WhatsApp gets ₹2L+; the ops Slack channel gets ₹50K+; finance gets emailed at ₹5L+. One use case, multiple installs.

### How it works under the hood

* Trigger: Payment Success event with amount-threshold filter.  
* Channels: WhatsApp Business, SMS (via Cashfree outbound), Gmail, Slack.  
* Payload: amount, customer name (if metadata), payment method (UPI/card/netbanking — never the card number), order ID, dashboard deep-link.  
* Latency target: under 15 seconds from Payment Success to dispatch (p95).  
* Idempotency: one notification per payment per threshold.  
* WhatsApp: uses merchant's pre-approved template; no free-text. Template approval is Meta's process.

### Edge cases worth knowing

* Channel auth (Slack, Gmail) revoked → log failure, surface in dashboard.  
* WhatsApp template not approved by Meta → block install with a clear error; don't let the merchant get to a half-working state.  
* Multi-currency merchant → threshold applied per-currency, not converted.

### What success looks like

* Adoption: merchants with at least one threshold configured.  
* Average installs per merchant (we expect 2+: founder \+ ops).  
* Channel mix: % WhatsApp vs Slack vs Gmail vs SMS by merchant segment.

### What we don't promise

* It is not fraud detection. Threshold notifier ≠ fraud detector. Anyone wanting fraud detection should look at Cashfree's Secure ID stack.  
* It does not stop, hold, or reverse transactions. Read-side only.  
* No sub-second latency promises. Use "the moment it clears" or "as soon as the payment succeeds."  
* Customer phone/email default off in notifications. Override is opt-in.  
* We do not notify the customer. Internal-facing only.

---

## **Use Case 3: Stop exporting the morning CSV from Cashfree to your sheet**

### Who needs this

The founder who still pivots their own MIS sheet every Monday morning. The head of finance / revenue / business / operations who inherits that sheet and uses it for daily MIS, GST reconciliation prep, or feeding into Tally / Zoho Books. The founder sets it up; finance/ops lives in it day-to-day.

Not for merchants doing more than 100K transactions per day — Google Sheets row limits become a problem above that volume. They need a BI / data warehouse path instead.

### The situation today

Every morning, the ops or finance lead opens the Cashfree dashboard, exports the previous day's transactions as CSV, opens Sheets, pastes the CSV into a working tab, and either pivots it directly or feeds it into Tally / Zoho Books via another export. Five minutes a day, every day, repeated by 800,000+ merchants. The cost is bandwidth, not money — but the bandwidth is finite and the work is dull.

### What the workflow does

Every successful Cashfree transaction appends a new row to a Google Sheet of the merchant's choice. The merchant maps which columns go where (amount, currency, payment method, order ID, customer name from metadata, status, timestamp, refund status). Refunds append as new rows with a refund flag, linked back to the original payment via order ID. The sheet stays live — finance can pivot, sort, filter, or feed it into the accounting tool.

### How it works under the hood

* Trigger: Payment Success event (and optionally Refund Success).  
* Action: Append row to a Google Sheet (append-only, no overwrites).  
* Latency target: under 30 seconds from Payment Success to row append (p95).  
* Idempotency: duplicate events do not create duplicate rows.  
* Failure handling: sheet failure (deleted, permission revoked, row cap hit) → run marked failed in dashboard with reason. Payment is never blocked.  
* Volume guard: the workflow self-disables (or warns) above \~80K rows in the target sheet, before Sheets cell limits cause silent failures.  
* PII: card data, CVV, full bank account numbers excluded from the writable column set. Customer email/phone are opt-in, default off.

### Edge cases worth knowing

* Merchant changes the sheet structure (column added/removed) → surface a warning, halt writes until they reconfirm the mapping.  
* Merchant feeds the sheet into Tally / Zoho Books — that's a downstream merchant choice, not Relay's responsibility (yet — see Use Case 9).  
* Above 100K transactions/day → recommend the BI / data warehouse path; this use case is the wrong primitive at that scale.

### What success looks like

* Adoption rate.  
* Average rows appended per merchant per day.  
* Percentage of installs that hit the volume guard (signals demand for a BI / data warehouse alternative).

### What we don't promise

* Does not replace Tally / Zoho Books / accounting software. It feeds them.  
* Not a GST tool. No HSN logic, no invoice-level fields. Don't open the tax conversation with this use case.  
* No time-saved or productivity numbers (no baseline yet).  
* Does not auto-generate invoices.  
* Does not work for unlimited volume — recommend BI path above 100K transactions/day.

---

## **Use Case 4: See the shape of failed payments every hour, not every fifteen minutes**

### Who needs this

Founders at higher-volume SMB / D2C / marketplace merchants where staring at the failures filter is impractical but checkout health is still a daily concern (founder default cadence: once-a-day to personal WhatsApp/email). Heads of operations / revenue / business at the same merchants — they get the hourly cadence to a team Slack channel because they're the ones who actually act on a gateway issue or a UPI rejection spike. Same use case, two installs typical.

Not for risk teams needing real-time per-transaction failure alerts — different use case on the roadmap (per-event, not digest).

### The situation today

Ops at a higher-volume merchant cares about patterns in failures: a gateway timeout spike at 2pm, a specific bank's UPI rejection cluster, a 3DS misconfiguration. Today they refresh the dashboard's failures filter every fifteen minutes, or scroll through 200 individual failure notifications, or miss the pattern entirely. The founder gets a vague sense from the daily standup. Nobody acts on the actual shape.

### What the workflow does

Every hour (or daily, or 4-hourly — merchant's choice), one digest fires to the chosen channel: a headline (count \+ ₹ impact \+ top reason — e.g., "47 failed payments in the last hour, ₹3.2L impacted, top reason: UPI Collect timeout — 22"), followed by a grouped breakdown by reason code, each with a deep-link to the dashboard for that group. One message instead of fifty.

### How it works under the hood

* Trigger: Schedule (hourly default; daily and 4-hour cadences supported) \+ accumulated Payment Failed and Payment Dropped events from the window.  
* Aggregation: group by reason code (gateway timeout, insufficient funds, 3DS failed, UPI rejected, customer dropped, etc.).  
* Channels: Slack, WhatsApp Business, Gmail.  
* Optional filters: amount, payment method, error code.  
* Empty windows: configurable — fire empty digest or silence.  
* Idempotency: one digest per scheduled window.

### Edge cases worth knowing

* Schedule fires while a previous run is still in flight → skip, log warning.  
* Channel rate-limit (Slack, WhatsApp) → exponential backoff, mark failed if 3 retries fail.

### What success looks like

* Adoption rate.  
* Average digests fired per merchant per week (signals cadence preference).  
* Percentage of merchants installing both founder-daily AND ops-hourly versions (validates dual-install hypothesis).

### What we don't promise

* Does not recover failed payments. Reports, don't recover. Recovery is Use Case 5\.  
* Does not diagnose the root cause. Groups by reason code; doesn't reason about why a specific bank is rejected.  
* Does not auto-retry. Retry logic is a separate workflow with idempotency considerations.  
* Does not notify the customer. Internal-facing.  
* Customer phone/email default off in digest body.  
* It's a digest by design — sub-second / real-time framing doesn't apply.

---

# **USE CASES ON THE ROADMAP**

These five are not yet shipped. They are where the money is actually bleeding for Indian D2C buyers, and where Razorpay's Agent Studio led with three of its launch agents. Order is by acute pain (highest first).

---

## **Use Case 5: Get the dropped customer back with a fresh payment link, automatically**

### Who needs this

Founders of Indian D2C / e-commerce brands doing ₹20L–₹2Cr/month in revenue — the segment currently paying ₹30K–₹1.5L/month to BSP platforms (Interakt, AiSensy, Pragma, BiteSpeed, QuickReply) for what is essentially this exact pattern. Secondary persona: the head of growth / revenue who owns the recovery KPI.

Not for merchants without first-party customer-contact data (e.g., marketplace sellers who don't have buyer phone or email). The workflow needs a contact to send the link to.

### The situation today

A customer adds to cart, hits checkout, and drops out — either at the cart step (still on the site) or at the payment gateway step (hit "Pay" but didn't complete). At ₹20L–₹2Cr GMV, this happens hundreds of times a day. Recovery currently means either (a) the merchant manually crafts WhatsApp messages with a payment link, (b) the BSP platform's "abandoned cart" automation fires a generic "complete your purchase" message that doesn't include a payment link — forcing the customer to navigate back to checkout — or (c) nothing happens and the cart is lost.

Industry benchmarks (CampaignHQ, growwwtech): 15–25% recovery on existing implementations. Cashfree does not yet have its own outcome data — the §5 instrumentation diary in the product note is needed before we can publish a Relay-specific number.

### What the workflow does

When a customer drops a cart or a checkout, the workflow generates a fresh Cashfree payment link with the original cart amount and the customer's order metadata, then sends it via WhatsApp Business or email after a configurable delay. If the customer doesn't pay within N hours, a second touch fires. If the customer pays the link, the standard Payment Success workflow fires and this workflow stops chasing.

Configuration:

1. Pick the trigger — Cashfree's Payment Dropped event, or a cart-abandoned webhook from Shopify / WooCommerce / Wix / a custom storefront.  
2. Set the delay before send (default: 5 min for PG drop, 30 min for cart).  
3. Pick the channel (WhatsApp Business or Gmail).  
4. Choose the WhatsApp template (must be merchant-approved by Meta).  
5. Configure the reminder ladder (max 3 touches).

### How it works under the hood

* Trigger: Payment Dropped event OR cart-abandoned webhook from a connected storefront.  
* Action 1: Generate Cashfree Payment Link via existing Payment Link API (with original amount and customer ID).  
* Action 2: Send via WhatsApp Business or Gmail.  
* Action 3 (optional): Reminder ladder if unpaid.  
* Idempotency: one link per (customer, dropped\_event\_id) — no duplicate links for the same drop.  
* Send-target validation: must be a verified customer phone/email from order metadata. Never an arbitrary contact field. (This is the hard line that prevents the workflow from becoming a spam vector.)  
* Rate limit: max one send per 24 hours per customer per dropped event.  
* Maker-checker on bulk send: merchant can require approval if a batch crosses N customers in a window.

### Edge cases worth knowing

* Customer drops, receives link, drops again → second drop generates a new link only after a configurable cool-down.  
* Customer's phone in order metadata is invalid → log, route to the merchant's exception queue; don't send.  
* Original cart amount changes (out-of-stock, price update upstream) → use the latest amount, not the cached amount at drop time.  
* Link expiry shorter than the reminder ladder → either extend link expiry or shorten the ladder. Flag at install time.

### What success looks like

* Adoption: 30+ merchants installed by end of Wave 1.5.  
* Engagement: average links generated per merchant per day.  
* Recovery proxy: percentage of generated links that get paid (instrumented internally; not published externally until validated against the §5 baseline).

### What we don't promise

* No 25% recovery claim as a Cashfree number. Industry benchmarks come with their source attribution; Relay's own number lands when validated.  
* Does not replace the WhatsApp BSP (Interakt, AiSensy, Pragma). Relay sits between the payment event and the BSP. The BSP still owns the WhatsApp Business API conversation and marketing broadcasts. Positioning this as a BSP killer loses the room with anyone already paying for one.  
* Does not auto-charge the customer. It generates a link the customer voluntarily pays.  
* Always label as a roadmap, never as live.  
* Cannot send to "any contact" in metadata — only the verified customer.

---

## **Use Case 6: Sell from a DM without your team writing a payment link by hand**

### Who needs this

Founders of home-based / social-commerce / Instagram-first / WhatsApp-first businesses — the segment described in PG Growth deck slides 6 and 10\. The home tutor selling courses on WhatsApp; the home-based jewellery brand on Instagram; the food micro-business taking orders via DM. Secondary persona: head of growth / customer success / sales ops at a larger D2C brand running chat-led sales through Haptik / Yellow Messenger / Wati / Interakt.

Not for iOS-only customers if the configured link is a UPI Link — UPI Intent doesn't work on iOS (PG deck slide 8). The workflow auto-falls back to a standard Payment Link in that case.

### The situation today

A customer DMs the merchant on WhatsApp or Instagram saying "I want to buy 500g of mango pickle." The merchant (or their team) manually opens the Cashfree dashboard, creates a payment link with the right amount, copies the link, and pastes it back into the DM. Multiply by every order, every day. At a busy home-based business, this is the bottleneck.

### What the workflow does

The merchant's chatbot platform (Wati / AiSensy / Interakt / Haptik / Yellow Messenger) detects the buying intent and calls the Cashfree workflow with the intent and the customer's phone. The workflow generates a payment link or UPI link via Cashfree's APIs and returns it to the chatbot, which replies in the same DM thread. The customer pays; the standard Payment Success workflow fires.

Configuration:

1. Connect the chatbot platform.  
2. Map intents to products and amounts (e.g., "buy mango pickle 500g" → ₹450; "book consultation" → ₹2,500).  
3. Pick the link type (Payment Link or UPI Link — auto-falls-back to Payment Link on iOS).  
4. Optional: maker-checker for high-value links above a configurable threshold.

### How it works under the hood

* Trigger: Webhook from the chatbot platform, or Cashfree MCP invocation from a customer-facing AI assistant the merchant runs themselves.  
* Action: Generate Cashfree Payment Link or UPI Link with the right amount and customer details.  
* Reply: link returned to chatbot for in-thread reply.  
* Latency target: under 5 seconds from intent webhook to link reply (p95). Chat is time-sensitive.  
* Idempotency: same intent in the same thread within 60 seconds reuses the existing link rather than creating a duplicate.  
* iOS detection: if the customer's device is iOS, the workflow overrides UPI Link → Payment Link.  
* Maker-checker: enforced at the MCP layer, not the workflow layer, so a buggy or malicious workflow cannot bypass approval.

### Edge cases worth knowing

* Ambiguous intent ("how much is X?") → don't generate a link; route to a human reply.  
* Customer device unknown → default to Payment Link (safer than UPI Link).  
* Chatbot platform webhook fails → exponential backoff retry, max 3 attempts.

### What success looks like

* Adoption: merchants with a chatbot platform integration live.  
* Engagement: average links generated via this workflow per merchant per day.  
* Link-pay conversion: percentage of generated links that get paid (proxy for intent detection quality — published only after baseline).

### What we don't promise

* Does not replace the chatbot platform. The chatbot still owns the conversation and the intent detection. Relay handles the link generation and audit.  
* Does not auto-debit the customer. It generates a link.  
* UPI Link does not work on iOS. Workflow auto-handles this; positioning it as a universal "1-click" option is wrong.  
* Don't pre-announce chatbot platform partnerships that aren't signed yet.

### Open questions for engineering

* Do we own intent detection or assume the chatbot platform does it? (Recommendation: assume the chatbot platform does intent detection and sends us structured intent.)  
* What's the code path for merchants running their own AI assistant via the Cashfree MCP, with no third-party chatbot in the middle?

---

## **Use Case 7: Run your monthly collection cycle on autopilot**

### Who needs this

The PG Growth deck mentions this pattern five times — the most-repeated use case in the deck. Buyers:

* NBFCs and lending fintechs collecting EMIs every month  
* K-12 schools, coaching institutes, ed-tech ERP providers collecting fees every term/month  
* Societies and RWAs collecting maintenance every month  
* Utility billing services collecting bills every month  
* B2B subscription businesses collecting recurring invoices

Secondary persona: head of finance / collections / accounts receivable, who owns the collection KPI and the escalation logic.

Not for merchants with mandate-based auto-debit already in place (Cashfree Subscriptions / NACH / UPI Autopay). This use case is for link-based recurring collection where the customer manually pays each cycle.

### The situation today

Every NBFC ops head, every school admin, every society treasurer faces the same monthly grind: open the customer master in Excel, generate a payment link per customer (in some cases hundreds, sometimes thousands), distribute via WhatsApp / SMS / email manually, track who paid, chase the unpaid ones with reminders, mark them paid in the master file. Days of work every month. The PG deck describes the school flow specifically (slide 12): bulk upload, share, reconcile — but the chasing and the ladder is still manual.

### What the workflow does

The merchant uploads (or connects) a customer master with: customer ID, name, phone, email, amount due, due date, preferred channel. On a schedule (monthly default; weekly / quarterly / custom supported), the workflow generates a Cashfree Payment Link or Payment Form per customer using the existing batch-upload API, distributes via the customer's preferred channel, and chases unpaid links with a configurable reminder ladder (default: Day 3 reminder, Day 7 escalation, Day 14 final notice; max 5 touches). Paid status syncs back to the customer master via Payment Success webhook.

Configuration:

1. Upload customer master (Google Sheet, CSV upload, or webhook from existing source).  
2. Set the schedule (monthly default; weekly / quarterly / custom).  
3. Choose link or form type.  
4. Configure the reminder ladder.  
5. Configure maker-checker if bulk send approval is needed before fire.

### How it works under the hood

* Trigger: Schedule (cron-style).  
* Action 1: Generate Cashfree Payment Link or Payment Form per customer using the existing batch-upload API.  
* Action 2: Distribute via WhatsApp Business / SMS / Gmail per customer's preferred channel.  
* Action 3 (recurring): Reminder ladder for unpaid links.  
* Action 4: Sync paid/unpaid status back to the source.  
* Idempotency: same (customer, billing\_period) generates one link per cycle.  
* Reminder ladder: respects per-customer DNC list and channel preferences.  
* Bulk send rate-limit: configurable per merchant; default conservative to avoid WhatsApp spam flagging.  
* Volume target: support batches up to 10,000 customers per merchant per cycle.

### Edge cases worth knowing

* Customer pays before reminder fires → reminder cancelled.  
* Partial payment → balance reminder routes to a separate use case (\#15 in the backlog).  
* Customer phone changes between cycles → use the latest from the customer master.  
* Merchant has Cashfree mandate-based auto-debit (Subscriptions / NACH / UPI Autopay) for the same customer → out of scope for this workflow; route to that product.

### What success looks like

* Adoption: merchants installed per vertical (NBFC / school / society / utility).  
* Volume: average cycle size per merchant.  
* Collection rate proxy: percentage of links paid within the ladder window.  
* Channel mix per vertical (signals which channels matter for which buyer).

### What we don't promise

* Does not replace the merchant's loan management system / school ERP / RWA software. It sits alongside. The customer master usually lives in the merchant's existing system.  
* Does not guarantee collection. The customer still has to pay the link.  
* Does not handle mandate-based auto-debit. Different product (Cashfree Subscriptions / NACH / UPI Autopay).  
* Messaging templates are the merchant's responsibility. RBI Fair Practice Code applies to NBFC collections. Templates must be reviewed by the merchant's compliance team — not by Cashfree.

### Open questions for engineering

* Where does the customer master live in a steady state — in the merchant's source system, in a Cashfree-managed table, or in the Google Sheet itself?  
* How do we handle reconciliation when the merchant's source system updates customer amounts mid-cycle?  
* Do we need a "preview mode" for batch sends — simulate without actually sending, so the merchant can sanity-check before fire?

---

## **Use Case 8: Confirm every COD order on WhatsApp before it ships**

### Who needs this

Founders of Indian D2C brands where COD is 50%+ of orders — typical at fashion, beauty, packaged consumables, electronics, and most marketplace-adjacent D2C. (Source: CampaignHQ, May 2026.) Secondary persona: head of operations / supply chain who owns the RTO KPI and the cost-per-RTO line item.

Not for merchants with under 20% COD orders — the pain isn't acute enough to justify setup. They should look at Use Case 5 instead.

### The situation today

For an Indian D2C brand at 1,000 orders/day with 60% COD and 20% RTO on COD, the daily RTO cost is ₹15K–₹100K in unrecovered shipping. Every fake order, every "I changed my mind", every "I wasn't home", every "I forgot" — paid for by the merchant. There is no first-class tooling for this in Zapier, Make, or n8n; merchants either run a paid BSP platform that handles WhatsApp confirmation (Interakt's COD module, Pragma's RTO suite, BeFiSc) at ₹30K–₹1.5L/month, or they don't do it.

Razorpay's Agent Studio launched with "RTO Shield" as one of its three Tier-1 agents in March 2026\. This is not a use case Cashfree can afford to leave on the roadmap indefinitely.

### What the workflow does

When a new COD order is placed (Shopify / WooCommerce / custom storefront webhook), the workflow sends a WhatsApp confirmation message to the customer within 10 minutes — using the merchant's pre-approved template — asking them to confirm intent. If the customer replies "confirm", the order is flagged "COD confirmed" in the merchant's OMS and dispatch proceeds. If the customer doesn't respond within N hours, the order is flagged for a manual call (or auto-escalates with a second message — merchant choice). If the customer prefers to prepay, the message includes a "pay now and get ₹X off" option with a Cashfree payment link; if paid, the COD order is cancelled and a prepaid order is created.

Configuration:

1. Connect Shopify / WooCommerce / custom OMS webhook.  
2. Pick the WhatsApp confirmation template (must be merchant-approved by Meta).  
3. Configure the confirmation delay (default: 10 minutes after order).  
4. Configure the no-response action (manual call queue OR auto-second-message).  
5. Optional: configure the COD-to-prepaid offer (discount amount, link expiry).  
6. Configure maker-checker on the discount policy.

### How it works under the hood

* Trigger: New order webhook with payment\_method \= COD.  
* Action 1: Send a WhatsApp confirmation message within 10 minutes (p95).  
* Action 2: Parse customer reply — confirm, decline, prepaid-preference.  
* Action 3a (confirm): Flag order "COD confirmed" in OMS; dispatch proceeds.  
* Action 3b (decline / no response): Flag for manual call OR auto-second-message.  
* Action 3c (prepaid preference): Generate Cashfree Payment Link with discount; if paid, cancel COD and create prepaid order atomically.  
* Reply parsing: false-positive on "decline" must be under 2% (false decline \= unnecessary RTO escalation).  
* DNC respected.  
* Audit: full message thread per order in run history.

### Edge cases worth knowing

* Customer doesn't have a phone in order metadata → flag for manual call, no WhatsApp send.  
* Marketplace orders (Amazon / Flipkart / Meesho) → check the marketplace's COD policy before allowing install. Some marketplaces don't permit confirmation flows.  
* Race condition: customer pays the prepaid link AND the original COD ships anyway → COD order must be cancelled atomically with prepaid creation.  
* WhatsApp delivery fails → fallback to SMS (configurable).

### What success looks like

* Adoption: merchants installed.  
* Engagement: average COD orders processed per merchant per week.  
* Confirmation rate: percentage of COD orders that get a customer reply.  
* COD-to-prepaid conversion rate.

### Industry benchmarks (context only — never quoted as Cashfree claims)

* CampaignHQ: 40% RTO reduction at brands with WhatsApp confirmation flows.  
* Growww Tech: up to 30% COD-to-prepaid conversion uplift.

### What we don't promise

* Does not eliminate RTO. Industry benchmarks are 40% reduction.  
* Don't quote 40% RTO reduction as a Cashfree number. It's a CampaignHQ industry figure; cite the source.  
* Does not replace the courier or logistics partner.  
* Does not auto-cancel orders the customer doesn't reply to. It flags for manual review.  
* Marketplace policy applies. Always check Amazon / Flipkart / Meesho rules before pitching to those merchants.  
* The merchant's WhatsApp Business account sends. Cashfree is the orchestration layer.

### Open questions

* Customer reply parsing — own NLP, or rely on the chatbot platform's NLU layer (Wati / AiSensy)?  
* Shiprocket vs Delhivery dispatch-cancel handoff?  
* This is the strongest candidate for outcome-based pricing (% of RTO recovered, or per-RTO-prevented). Decision needed in the pricing memo before build.

---

## **Use Case 9: Reconcile every Cashfree settlement against your accounting books**

### Who needs this

The founder of any Cashfree merchant doing more than ₹50L/month in GMV — at this scale, manual reconciliation is hours per week and gets dropped or done wrong. Secondary persona: head of finance / CFO / external CA / accounts manager — they own the close cycle and are the actual day-to-day user.

Not for merchants on accounting software outside the Tally / Zoho Books pair (BUSY, Marg, QuickBooks India, custom ERPs). Wave 3+ roadmap.

### The situation today

Every week, the finance lead exports the Cashfree settlement file, opens Tally or Zoho Books, and matches line by line: this settlement \= these orders, fees deducted, refunds against earlier payments, chargebacks, currency conversions. Discrepancies get flagged in a spreadsheet, chased over email, eventually resolved. The pattern repeats every settlement cycle. AI Accountant identifies this as the gap: there is no first-class tooling that handles Cashfree → Tally / Zoho reconciliation natively.

### What the workflow does

When a Cashfree settlement event fires (funds credited to the merchant's bank), the workflow pulls the underlying transaction breakdown (orders settled, fees deducted, refunds, chargebacks, net credited), queries Tally or Zoho Books for matching open invoices/orders by order ID or invoice ID, applies match logic (amount tolerance, fee handling, multi-day rolling settlement), and either marks invoices as reconciled or flags mismatches with a reason (amount mismatch, missing invoice, duplicate settlement). A weekly digest is emailed to finance with a summary and drill-down deep-links.

By default, the workflow only flags matches — finance approves before any write-back to Tally / Zoho. Maker-checker is on by default for this use case specifically because accounting writes are sensitive.

Configuration:

1. Connect Tally or Zoho Books.  
2. Configure match rules (amount tolerance, fee handling, multi-day settlement window).  
3. Choose flag-only or approve-then-write-back mode.  
4. Set the weekly digest schedule and recipient.

### How it works under the hood

* Trigger: Cashfree Settlement event.  
* Action 1: Pull transaction breakdown.  
* Action 2: Query target accounting tool's open invoices.  
* Action 3: Apply match logic.  
* Action 4 (matched): Flag — or write back as reconciled if merchant has approved write-back mode.  
* Action 5 (mismatched): Flag with reason.  
* Action 6: Weekly digest to finance.  
* Maker-checker: default ON for write-backs.  
* Match-rule conservative defaults: ₹1 amount tolerance, exact order-ID match required, fees handled separately.  
* Idempotency: same settlement processed once even if event fires multiple times.

### Edge cases worth knowing

* Settlement spans invoices from multiple billing periods → match per-invoice, not per-settlement.  
* Refund in current settlement against a payment in a previous settlement → handle as adjustment entry.  
* Chargeback debited against settlement → flag, do not auto-write (compliance review needed).  
* Currency mismatch (multi-currency merchant) → handle FX conversion or flag for manual.

### What success looks like

* Adoption: finance teams of merchants over ₹50L/month installed.  
* Match rate: percentage of settled transactions auto-matched.  
* Time-to-close (only with explicit merchant instrumentation).

### What we don't promise

* Does not replace the CA or finance team. Augments them. Reconciliation judgment calls still belong to humans.  
* Not a 100% match rate. Real-world data has edge cases (refunds, partial settlements, chargebacks, multi-day rolling).  
* Does not file GST. Feeds reconcile data into Tally / Zoho; the CA owns the filing.  
* Tally and Zoho Books in v1. Other accounting tools are Wave 3+.  
* Does not auto-correct mismatches. It flags. Correction is the merchant's call.

### Open questions for engineering

* Tally — direct API integration vs. third-party Tally Connector?  
* Do we need a "dry-run mode" so finance can preview matches before turning on write-back?  
* What's the right primitive for handling chargebacks — flag-only, or surface a separate workflow?

