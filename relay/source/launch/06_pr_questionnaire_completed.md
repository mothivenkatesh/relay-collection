# PR Questionnaire — Completed Draft

> Filled gaps marked **[NEW]**, sharpened existing answers marked **[REWRITTEN]**, kept-as-is marked **[KEEP]**. Critical answers (4.2 vs Razorpay, 6.2, 6.3) drafted from scratch.

---

## Section 1: The Basics

### 1.1 What is the official product name?

**Recommendation: Relay.**

| Name | Verdict | Why |
|---|---|---|
| **Relay** ⭐ | Recommend | Distinct, simple, payments-adjacent ("relay" = passing things along). "Cashfree Relay" rolls off the tongue. Doesn't echo Razorpay. |
| Agent Fabric | Avoid | Too close to Razorpay "Agent Studio" — sounds derivative. "Fabric" reads enterprise/dev, not SMB. |
| AI Fabric | Avoid | "AI" branding ages fast. Generic. Same Razorpay-derivative problem. |
| Pipes | Avoid | Niche dev nostalgia (Yahoo Pipes). Doesn't communicate value. |
| Automate | Avoid | Microsoft Power Automate already owns this lexically. Bland. |
| Streams | Avoid | Reads as data-engineering (Kafka, Kinesis). Wrong audience signal. |
| Chain | Avoid | Crypto + LangChain overload. Confusing. |

**Tagline candidates** (test in beta):
- *Automation that speaks payments.*
- *Turn payment events into business actions.*
- *Your payments, on autopilot.*

### 1.2 In one sentence, what does this product do? **[REWRITTEN]**

> **Cashfree Relay is a no-code AI workflow platform that lets merchants automate payment, ops, and growth tasks — using a visual builder, AI agents, or both — running securely inside Cashfree's RBI/PCI-compliant infrastructure with native access to your orders and payments data.**

*(Why rewritten: tightens to one sentence; leads with the new category "AI workflow platform"; emphasizes the visual + agent dual-mode; surfaces the security/native-data wedge against generic tools and against Razorpay.)*

### 1.3 Who is this product available to? **[NEW]**

**Phased rollout:**

| Phase | Audience | Who | Approx. timing |
|---|---|---|---|
| **Private Beta** (now) | Invite-only | 15–20 hand-picked Cashfree merchants who pass the 4-filter selection (technical capability, ₹10L+/month volume, engagement willingness, trustworthy operator) | Weeks 1–6 |
| **Closed Public Beta** | Waitlist | All Cashfree merchants who apply via cashfree.com/relay; capped at ~500 | Weeks 7–10 |
| **GA** | All Cashfree merchants | Self-serve in dashboard | Week 11+ |
| **MCP / external AI agents** | Any AI agent (Claude Desktop, Cursor, etc.) | Via MCP server | Post-GA |

**Pricing:** Free during private + public beta. GA pricing TBD — likely free tier (limited workflows + runs) + Pro tier (₹999–1,999/month) + usage-based for high volume.

---

## Section 2: The Problem this Solves

### 2.1 What specific problem does this solve? **[REWRITTEN]**

> Indian merchants spend hours every week stitching together payment events to downstream actions — emailing invoices, updating Sheets, alerting ops on disputes, recovering dropped checkouts on WhatsApp, reconciling refunds in Tally. Three options exist today, all bad: **(1) do it manually** (slow, error-prone, breaks at scale), **(2) build custom scripts** (brittle, dev-dependent, hard to maintain), or **(3) buy a generic workflow tool** like Zapier/n8n/Make (requires webhook setup, payload mapping, auth, ongoing dev maintenance, plus introduces data-sharing/compliance risk because sensitive payment data leaves Cashfree's infrastructure).

*(Sharpened the "external workflow products" point — the data-sharing/compliance angle is the strongest differentiator vs Razorpay.)*

### 2.2 How common is this problem? **[REWRITTEN]**

> Workflow orchestration is a category problem with proven scale. **Shopify Flow alone has 10,000+ ratings on the Shopify App Store** — meaning tens of thousands of e-commerce merchants actively use a native, platform-embedded automation layer. **Zapier serves 2M+ businesses globally.** The pattern is consistent: every major SaaS platform (Shopify, HubSpot, Salesforce, Stripe) has shipped a native automation surface — because the third-party generic alternatives leave value on the table for both merchant and platform.

> For Indian payment merchants specifically, every Cashfree merchant doing >₹10L/month has at least one repetitive payment workflow they're handling manually or with a fragile script. That's tens of thousands of merchants in the addressable base today.

### 2.3 Specific merchant requests **[KEEP, lightly polished]**

> Tens of merchants told us they want custom workflows to streamline processes, secure them, and eliminate manual errors. Three asks came up repeatedly:
>
> - **Branded WhatsApp support** — sending payment-event messages from the merchant's own WhatsApp Business account, not a Cashfree-branded one
> - **Maker/Checker flows for security** — payments are sensitive; some merchants want a human approval node before high-value refunds, payouts, or chargebacks are auto-actioned
> - **Real-time Cashfree → Google Sheets sync** — Sheets is the universal SMB ops tool, and merchants want payment data flowing there continuously, not via end-of-day exports

---

## Section 3: How It Works

### 3.1 Step-by-step merchant experience **[NEW — draft pending product team validation]**

> 1. **Open Relay** from the left nav of the Cashfree merchant dashboard.
> 2. **Pick how to build:** "Use a template" (post-GA), "Build with visual builder," or "Describe in plain English to AI" (Agent mode).
> 3. **In the visual builder:** drag a trigger node (e.g., *Payment Failed*), drag connector nodes (e.g., *Slack: post message*, *WhatsApp: send retry link*), and connect them visually. No code.
> 4. **Configure each node** with a fill-in-the-blank form (e.g., choose Slack channel, write message template — you can `{{insert}}` payment data fields).
> 5. **Add an AI node** (optional) to write personalized customer messages, summarize disputes, or classify failures using Gemini/OpenAI.
> 6. **Test the workflow** with a sample event from the dashboard (no real payment needed).
> 7. **Publish.** The workflow runs automatically every time the trigger fires.

### 3.2 What does the AI do? **[NEW — draft]**

> AI shows up in two places:
>
> - **AI as a node inside any workflow** (Gemini or OpenAI): writes personalized customer messages, summarizes long dispute threads, classifies failure reasons into categories, generates ops alerts in plain English. The merchant controls when to invoke it; outputs feed downstream connectors.
> - **AI Agent mode (alternate build path):** the merchant describes the desired automation in plain English ("Every time a payment fails over ₹5,000, alert ops on Slack and email the customer a retry link with apologies"). The agent composes the workflow scaffold, which the merchant reviews and edits visually before publishing.
>
> What this replaces: rigid templates, copy-paste customer messaging, manual triage of failure reasons, hand-written ops summaries.

### 3.3 How does a merchant set it up? **[NEW — draft]**

> - **Time to first workflow:** ~10 minutes for a non-technical user with a clear use case.
> - **Technical setup needed:** none. No webhooks, no API keys for Cashfree (it's native). Third-party connectors (Slack, Sheets, WhatsApp) authenticate via one-click OAuth.
> - **Who can set it up:** anyone comfortable with Sheets formulas or basic ops tools. We've designed for ops/finance/growth managers, not developers.
> - **Developer required for:** the HTTP Request node (custom REST APIs) and complex conditional logic. Most merchants will never need either.

### 3.4 Where does this work? **[KEEP, expanded]**

> - **Visual builder:** Cashfree Merchant Dashboard (web)
> - **MCP server:** post-GA — connect any external AI agent (Claude Desktop, Cursor, custom agent) to Relay's workflow primitives via Model Context Protocol
> - **API:** post-GA — for power users who want to trigger or read workflow runs programmatically

### 3.5 Is it like a vibe-coding platform? **[REWRITTEN]**

> No. Vibe-coding platforms (Lovable, Bolt, Cursor) generate application *code* from prompts. Relay generates *workflows* — composable, visual, debuggable, with deterministic execution. Closer to Shopify Flow or Zapier than to a code generator.

### 3.6 Open source? **[KEEP]** No.

---

## Section 4: What Makes It Different

### 4.1 Single most important differentiator **[REWRITTEN]**

> **It runs inside Cashfree's RBI/PCI-compliant infrastructure with native access to payment data — meaning zero webhook setup, zero data leakage, and zero compliance review. Generic tools (Zapier, n8n) require all three, every time.**

### 4.2 How is this different from Razorpay's Agent Studio? **[NEW — critical answer]**

> Razorpay's Agent Studio and Cashfree Relay solve adjacent problems but choose opposite philosophies. Razorpay leads with **autonomous AI agents** — pre-built agents for cart conversion, dispute handling, subscription recovery — that the merchant deploys from a marketplace. The merchant trusts the agent to make decisions.
>
> Cashfree Relay leads with **composable workflows** — a visual builder where the merchant designs each step explicitly, with AI available as a node inside the workflow when they want it. The merchant trusts themselves to define the logic, and uses AI only where it adds value (like writing a customer message). For sensitive payment operations, this is often what merchants prefer — they want full visibility into what's running, not a black-box agent.
>
> Three concrete differences:
>
> | Dimension | Razorpay Agent Studio | Cashfree Relay |
> |---|---|---|
> | **Primary metaphor** | AI agent that acts on your behalf | Workflow you design, AI helps where useful |
> | **Trust model** | Trust the agent's decisions | Trust your own logic; AI is opt-in per node |
> | **Best for** | Pre-defined high-volume use cases (cart, dispute, subscription) where agent reliability is proven | Custom workflows specific to your business, including Maker/Checker, branded WhatsApp, custom Sheets sync |
> | **Build path** | Pick from marketplace, configure, deploy | Build visually OR describe in plain English (AI Agent mode) — both produce the same editable workflow |
> | **Compliance posture** | Agent acts autonomously | Human approval nodes (Maker/Checker) by default for sensitive actions |
>
> **Why both can win:** Razorpay's agents are right for merchants who want a proven recipe deployed fast. Relay is right for merchants who want to design automations specific to *their* business — and want full control over what runs.

### 4.3 What technology makes this possible? **[REWRITTEN]**

> Relay is a software product, not a tech moat. The differentiator isn't the underlying tech (workflow engine + LLM nodes) — it's that the workflow engine is **embedded inside Cashfree's payments infrastructure**, with payments events as typed first-class triggers, and merchant data never leaves Cashfree's compliance boundary.

### 4.4 Are we using existing LLMs? **[REWRITTEN, expanded]**

> Yes. The AI node uses Google Gemini and OpenAI as connectors today. Merchants choose which model to invoke per workflow. Roadmap: support for Anthropic Claude (esp. for the AI Agent build mode), and merchant's-own-key options for compliance-sensitive customers.

---

## Section 5: The Impact

### 5.1 Measurable outcomes **[REWRITTEN]**

> - **Time saved on manual ops:** 5–15 hours/week per merchant (first 3 workflows live)
> - **Revenue recovered:** 3–8% of dropped checkouts via auto-WhatsApp recovery (beta benchmark)
> - **Faster failure response:** payment failure → customer retry email in <30 seconds (vs hours/days manual)
> - **Eliminated data leakage risk:** no payment data sent to third-party automation tools
> - **Compliance saved:** no security review needed for Cashfree-native workflows (vs weeks for Zapier/Make)

### 5.2 Adoption targets **[REWRITTEN]**

> - **Internal target:** 100 active merchants by Month 6 (private + public beta cohort)
> - **External target:** 2,000–5,000 active merchants by end of Year 1 post-GA
> - **North-star metric:** Successful Workflow Runs per Active Merchant per Month
> - **Stickiness cut:** % of active merchants with ≥1 workflow firing daily (target: 40%+ at GA)

---

## Section 6: Additional Materials

### 6.1 Demo / Screenshots **[KEEP]**

Demo video and screenshots in production. Recommend the demo show **one specific use case end-to-end** (suggested: "Payment Failed → Slack alert + WhatsApp retry") rather than a feature tour. Concrete > comprehensive.

### 6.2 Genuinely exciting / significant **[NEW]**

> Three things worth surfacing that the questionnaire doesn't otherwise capture:
>
> 1. **MCP support is on the roadmap.** This means a merchant's existing AI agent (Claude Desktop, internal copilot, Cursor) can plug into Relay and operate on payment workflows. We're not just an AI workflow tool — we're becoming AI-agent-ready infrastructure for the merchant's broader AI stack.
>
> 2. **Maker/Checker for AI is unique to us.** Razorpay's agents act autonomously. We let merchants put a human approval node in front of any AI-generated action. For Indian fintech compliance teams who are wary of autonomous agents touching payments, this is the difference between "fascinating but blocked by legal" and "shipped this quarter."
>
> 3. **The beta merchants are co-building the template library.** We're not shipping with pre-built templates. Every workflow built during private beta becomes a candidate template at GA — meaning launch templates are 100% based on real merchant problems, not Cashfree imagination.

### 6.3 What to avoid saying **[NEW]**

> **Avoid these claims and framings:**
>
> 1. **Don't claim "world's first" or "India's first."** Razorpay claimed "world's first AI Agent Studio for payments" at Sprint 2026. Cashfree is a fast-follower in market timing. Lead on substance, not firsts.
> 2. **Don't position as "Razorpay killer" or compare directly.** Stay above the fight. Differentiate by approach (composable workflow vs autonomous agent), not attack.
> 3. **Don't oversell AI autonomy.** Today's AI is a node, not the orchestrator. Calling it "autonomous AI agents" creates expectations the product won't meet at launch and erodes trust if a workflow misbehaves.
> 4. **Don't say "hosted n8n for Cashfree merchants."** Accurate internally, but undersells the AI + native-data + compliance wedge externally.
> 5. **Don't promise pre-built templates at private beta.** They don't exist yet. Set expectations: "We're co-building your first workflow with you."
> 6. **Don't share specific roadmap dates** for connectors, MCP, or AI Agent mode until product-locked.
> 7. **Don't reference specific beta merchant names** without explicit, written permission. Quote anonymously by category ("a D2C apparel brand", "a SaaS subscription seller") until case studies are formally signed off.
> 8. **Avoid the word "agent" as the lead noun.** "Workflow" is the lead noun for Cashfree Relay; "agent" is one feature inside it. Conflating the two = blurring the line with Razorpay.
