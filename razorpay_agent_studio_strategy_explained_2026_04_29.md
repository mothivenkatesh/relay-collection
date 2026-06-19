# Razorpay Agent Studio — strategy, explained

> **Audience:** Cashfree leadership, PMM, Product. Internal-only.
> **Author:** Mothi Venkatesh
> **Date:** 2026-04-29
> **One-line summary:** Razorpay is not building an AI product. They are building an MDR-replacement business model with an AI wrapper. Reading the strategy that way changes how Cashfree should respond to it.

---

## BLUF

Three sentences:

1. **MDR is compressing.** UPI ate card-MDR margin in India and there is no recovery path on volume.
2. **Razorpay's actual strategic move is a second take-rate** — outcome-based fees on recovered revenue (RTO, disputes, abandoned carts, failed renewals) that compound *on top of* the shrinking MDR.
3. **Agent Studio is the delivery vehicle for that pricing model**, not the product. The AI is the wrapper; the take-rate is the innovation.

Every other observation about Razorpay's launch — the 7 agents, the Claude SDK, the NPCI pilot, the Anthropic endorsement — clicks into place once you read it through this lens. Miss the lens, and Cashfree spends the next 18 months losing a feature war it didn't need to fight.

---

## 1. The strategic context — why now, why this shape

Indian payment processors face a structural margin problem. UPI turned the average MDR for digital payments toward zero. Card-MDR is regulated in shrinking bands. Wallet-MDR isn't materially different. The unit economics of "process a payment, take a basis-point cut" only work at scale, and the scale game has effectively two winners (Razorpay, Cashfree) and three near-winners (PayU, Paytm, BillDesk).

So every Indian processor is running the same internal calculation: **where does the second take-rate come from?**

The candidate answers, ranked roughly by the size of the pool:
- Banking-as-a-service / RazorpayX-style current accounts (margin: float + spread)
- Lending / capital products (margin: interest spread, but heavy on capital + risk team)
- Working capital / receivables (margin: factoring spread)
- **Agentic operations on the merchant's payment lifecycle** (margin: % of recovered/prevented value)

The fourth category is new, uncapped, and software-margin. RTO recovery alone is a 20-30% loss line for Indian D2C — a 5% take-rate on recovery converts to real revenue. Multiply across disputes, subscriptions, abandoned carts, fake-order prevention, and you have a meaningful second P&L line that doesn't depend on volume at all.

That is the pool Razorpay is racing to capture. Agent Studio is how they show up to the race.

---

## 2. The five layers of the strategy

Razorpay Agent Studio is doing five things at once. Most analysis stops at layer 1 or 2. The compounding moat is in 3, 4, and 5.

### Layer 1 — Defensive moat against LLM disintermediation
**The threat:** as LLMs become the merchant's primary interface, the payment processor risks becoming a commodity API call inside someone else's agent. The merchant asks Claude to "issue a refund" — and Claude doesn't care if Razorpay or Cashfree is underneath, as long as the API exists.

**Razorpay's defense:** be present at every layer where the merchant might conceivably interact. Their stack:
- **NPCI + OpenAI + Claude pilot** (October 2025 + February 2026) — when a ChatGPT user pays via UPI in India, Razorpay is the rail. Bigbasket on ChatGPT. Zomato, Swiggy, Zepto on Claude. The processor *is* the agentic payment.
- **Agent Studio** — when the merchant uses pre-built agents inside their own ops, those agents run inside Razorpay's UI.
- **MCP server** (217 GitHub stars, April 2025) — when a developer wires Razorpay into their own custom agent, the tools are first-class.

This is not three separate products. It is one strategy expressed at three layers of the merchant's AI stack. Cashfree must be present at all three layers or accept disintermediation in two of them.

### Layer 2 — Take-rate expansion via agentic outcomes
**The play:** pre-built agents like Dispute Responder, Subscription Recovery, RTO Shield, Abandoned Cart Conversion are not features. They are SKUs.

Razorpay has not published pricing yet, but the architecture telegraphs the model:
- **Per-recovery fees** — 5–10% of $ recovered (industry-standard for cart recovery and dispute response)
- **Per-prevention fees** — % of $ prevented (RTO Shield "saved" you ₹X, we take 5%)
- **Subscription tier** — flat ₹/month per agent (predictable layer for CFO buyers)
- **Outcome bundles** — discount when bundled into MDR negotiation (compresses procurement to one contract)

The Cashfree response cannot be "we have agents too." The response has to be "here is our take-rate model, and here is why it's better." Free-tier MCP, transparent pricing, outcome-cap visibility — these are the levers that matter, not agent count.

### Layer 3 — Lock-in through workflow ownership
**The compounding mechanic:** an agent doesn't just run a workflow. It accumulates training signal on the merchant's history.

Within 90 days of running RTO Shield, Razorpay has a dataset of:
- Which orders this merchant's customers tend to RTO
- Which intervention messages worked
- What time-of-day, channel, language converts best
- Which customer segments are unrecoverable

That dataset is the merchant's, technically. But it's stored, processed, and refined inside Razorpay's infrastructure. Switching to Cashfree means losing 90 days of agent intelligence and starting again. By month six, the switching cost is no longer the integration — it's the *learning curve*.

This is the same mechanic that made Salesforce un-displaceable in CRM and Datadog un-displaceable in observability: the data the system accumulates becomes the moat. Razorpay is building toward this for payments.

### Layer 4 — Distribution via Anthropic
**The endorsement:** Irina Ghose (MD Anthropic India) named in launch coverage. Claude Agent SDK as the build framework. Listing in Anthropic's MCP directory.

This is more expensive to replicate than it looks. Anthropic's India GTM team — small, high-leverage — now has commercial incentive to mention Razorpay every time an Indian fintech opportunity comes up. Replicating this with OpenAI alone doesn't suffice; OpenAI's enterprise GTM in India is thinner. Replicating it across Anthropic + OpenAI + Google requires three separate executive relationships, each with its own pace.

The wedge against Anthropic-exclusivity isn't louder Anthropic co-marketing. It's **multi-vendor neutrality** — being equally listed on Anthropic, OpenAI, Google, and Cursor directories so the merchant's choice of LLM doesn't determine their choice of payment processor.

### Layer 5 — Narrative for valuation
**The least-discussed layer.** Razorpay is on a path to public listing. AI-native fintech multiples > MDR-arbitrage fintech multiples. Every press cycle that frames Razorpay as "agentic payments leader" compounds the narrative valuation gap.

Cashfree, as a private competitor, doesn't have the same valuation imperative. But this means Razorpay can afford a louder, less-shipped launch — the narrative is doing financial work even before the product does customer work. The strategic implication: **don't try to out-narrate them.** Out-ship them.

---

## 3. The architecture — three surfaces, one strategy

Razorpay's Agent Studio page reveals a three-tier framework. It is the closest articulation of an "Open Composable" architecture from any payments player to date:

| Tier | Surface | Buyer | Strategic role |
|---|---|---|---|
| **1. Customize a Prebuilt Agent** | Razorpay UI (no-code) | Ops manager / dept head | Capture take-rate on recovered revenue. The SKU layer. |
| **2. Onboard as an AI Partner** | Razorpay ISV program | Build partner / agency | Distribute via third-party builders. Marketplace flywheel. |
| **3. Build From Scratch** | Razorpay MCP + SDK (beta) | Developer / CTO | Anti-disintermediation defense. Stay relevant when the merchant builds their own agent. |

Tier 1 is the cash cow. Tier 2 is the distribution flywheel. Tier 3 is the developer hedge.

What this tells you about their architecture: **the agents and the MCP are not the same product**. The agents run in Razorpay's hosted runtime. The MCP runs anywhere. They are two different bets on where the agentic action will live, and Razorpay is hedged across both.

The implication for Cashfree: a single-architecture bet (only MCP, or only visual builder) is strictly worse than Razorpay's hedge. Cashfree Relay must be present at all three tiers or concede the tier where it isn't.

---

## 4. The persona segmentation — and the gap they left

Razorpay sliced the agent portfolio across three buyer personas:

| Bucket | Agents | Buyer |
|---|---|---|
| **Revenue Recovery** | Dispute Responder, Subscription Recovery, Abandoned Cart (×2 with Nugget/SuperU) | CRO / Marketing |
| **Logistics** | RTO Shield, RTO Insights | COO / Operations |
| **Cash Management** | Settlement Insights, Cashflow Forecaster | CFO / Finance |

Notice what's missing.

There is no agent for the **Founder / Owner-Operator** persona — the small-team D2C, EdTech, or SaaS founder who *is* the CRO, COO, and CFO simultaneously. Razorpay's segmentation makes commercial sense for ₹100Cr+ merchants who have a separate CRO, COO, and CFO. It leaves the 5–50 person team — where one person makes every decision — under-served.

This is not an oversight. It is a deliberate up-market move. Razorpay's enterprise GTM has always been stronger than their SMB GTM, and Agent Studio's "contact sales" pricing reinforces the choice. They are pricing themselves into the upper half of the market.

The gap is large. The Indian D2C ecosystem has thousands of merchants in the 5–50 person band, growing fast, AI-curious, and explicitly under-served by both Razorpay's enterprise framing and the global tools (Stripe Agent Toolkit, n8n) that don't speak Indian payments. **This is where Cashfree wins or loses.**

---

## 5. The take-rate math — what's actually at stake

Worked example to make the strategy concrete.

**Merchant:** mid-market D2C apparel brand. ₹10Cr/month GMV. 60% COD orders. Industry-standard 25% RTO rate.

**Without RTO Shield:**
- Monthly COD GMV: ₹6Cr
- Monthly RTO loss: ₹1.5Cr (25% of ₹6Cr)
- Annual RTO loss: ₹18Cr

**With RTO Shield reducing RTO by 30%:**
- Monthly RTO loss: ₹1.05Cr (was ₹1.5Cr)
- Monthly recovery: ₹0.45Cr
- Annual recovery: ₹5.4Cr

**Razorpay take at 5% of recovered value:**
- Monthly: ₹2.25L
- Annual: ₹27L per merchant

**For comparison, Razorpay's MDR on the same merchant:**
- Monthly UPI MDR (assume 0.4% effective): ₹4L on ₹10Cr GMV
- Annual: ₹48L

**The agent take-rate is ~56% of the MDR take-rate from a single agent on a single use case.**

Stack three agents (RTO + Dispute + Cart Recovery) on the same merchant and the agentic take-rate exceeds MDR. This is what "MDR replacement" looks like in numbers. It is not a marketing line. It is a P&L line that is going to show up in Razorpay's pre-IPO disclosures.

If Cashfree doesn't compete on this layer, Cashfree's per-merchant ARPU stays flat while Razorpay's grows. Over a 3-year window, that diverges to a step-change in margin and valuation.

---

## 6. The Anthropic moat — why it's worth what they paid

Most companies underweight model-vendor co-marketing as a strategic asset. Razorpay didn't.

Anthropic, OpenAI, Google, and Cursor all run a small set of "officially listed" or "partner-tier" integrations that get surfaced in marketing materials, conference talks, default-recommended-tool lists, and (most importantly) GTM conversations between their enterprise teams and Indian customers.

Anthropic India's MD personally endorsing Razorpay Agent Studio means:
- Every Indian fintech customer Anthropic touches in 2026 hears "Razorpay" as a default recommendation
- Razorpay shows up in Anthropic's case-study materials and Builder Day events
- The two companies' GTM teams coordinate on shared deals
- Razorpay's MCP server gets surfaced first in Anthropic's directory

The cost of replicating this for Cashfree, if it's even possible at this stage, is high. Anthropic typically partners with one anchor per category, especially in regional markets where their team is small. The window for Cashfree to be that anchor in India closed when Razorpay shipped first.

This is why **multi-vendor neutrality** is the right Cashfree response, not Anthropic-replacement. Get listed on OpenAI, Google, Cursor, and OpenCode directories. Be the processor that works *regardless* of which LLM the merchant standardizes on. Turn Razorpay's Anthropic-exclusivity from a moat into a constraint.

---

## 7. Where the strategy breaks

Steelmanning is done. Here are the four real vulnerabilities.

**1. Hosted runtime is not truly agentic.**
Agent Studio runs agents inside Razorpay's UI. That means the merchant's AI assistant has to come *to* Razorpay. The whole point of agentic systems is that the AI runs anywhere — Claude Desktop, Cursor, an internal copilot. Razorpay's MCP server addresses this, but their flagship Agent Studio doesn't. There is a strategic tension between the two architectures inside Razorpay's portfolio that they have not yet resolved publicly.

**2. Hidden pricing creates enterprise-only friction.**
"Contact sales" pricing means the SMB merchant cannot self-serve the agentic value. This is how Razorpay loses the 5–50 person band that Cashfree should target. Transparent pricing — even a single published number — would close this gap quickly. The longer Razorpay holds out, the longer the gap stays open.

**3. Single-vendor model fragility.**
Anthropic Claude Agent SDK is great until Anthropic raises prices, changes terms, or partners with a competitor in another segment. Multi-model neutrality is more robust. Razorpay's bet that Anthropic stays the anchor for 24+ months may not hold.

**4. The duplicate-agent count.**
The Agent Studio page lists 8 agents. Two of them — SuperU and Nugget — are the same Abandoned Cart Conversion agent, co-branded twice. The real count is 7. This is a minor PR detail, but it tells you something larger: **the agent count is the moat, not the agent depth.** Each individual agent is shallower than the marketing implies. Cashfree shipping 3 deeply specified agents — with published outcome benchmarks — beats Razorpay's 7 shallow agents in a competitive evaluation. Most evaluators don't go past the count, but the ones who do will see it.

---

## 8. What this teaches us — three lessons for Cashfree Relay

**Lesson 1 — Compete on the take-rate model, not the agent count.**
Razorpay will publish 12 agents by Q3 2026. Cashfree cannot win an agent-count race on a 12-month horizon. What Cashfree can win: a more transparent, lower-friction, outcome-aligned take-rate model. Free MCP tier. Published pricing on day one. Outcome-cap visibility (we take 5% up to ₹X/month, then it's bundled into MDR). This becomes the procurement narrative. Procurement narrative wins enterprise.

**Lesson 2 — Claim the Founder persona.**
Razorpay segmented to CRO/COO/CFO and left the Founder persona empty. Cashfree should explicitly position Relay for the founder/owner-operator at the 5–50 person merchant. Different agent UX (single dashboard vs three persona surfaces), different language (revenue/saved/recovered), different pricing (transparent SMB self-serve), different distribution (Discord, Twitter, Indie Hackers, ProductHunt). This is the empty quadrant.

**Lesson 3 — Be present at all three layers.**
Razorpay's three-tier framework (Customize / Partner / Build) is the right architecture. Cashfree must be present at all three layers — pre-built templates for ops, partner program for ISVs, MCP for developers. A Cashfree Relay strategy that only ships one of three layers is strictly worse than Razorpay's portfolio. The MCP commitment memo (already drafted) is the necessary condition for layer 3. A partner program is the still-undecided condition for layer 2.

---

## Single-line takeaway

Razorpay launched a louder narrative than their product can yet support. The strategic substance underneath — take-rate replacement of compressing MDR via agentic outcomes — is real and serious. Cashfree's response should compete on the pricing model, the founder persona, and multi-vendor distribution. Trying to compete on agent count or Anthropic endorsement is a losing posture.

---

*Companion docs:*
- [Positioning v2](positioning-cashfree-relay-v2-2026-04-29.md) — applies these lessons
- [Template library spec](08-template-library-spec.md) — the 3-deep-agent response to 7-shallow-agents
- [MCP commitment memo](09-mcp-commitment-memo.md) — secures layer 3 of the three-tier response
