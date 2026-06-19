# Launch Readiness — Questions Tracker

> Mix of (a) PMM-owned answers I've drafted, (b) sharpened engineering questions, (c) additional questions to surface before private beta opens.

---

## A. PMM-OWNED — drafted answers (validate, don't ask Eng)

### A1. Which merchants are we targeting for the beta?
**Answered in [03-gtm-strategy.md §4–8](03-gtm-strategy.md).** Short version:
- **15–20 merchants**, hand-picked, all 4 filters must pass:
  1. Technical capability (someone has used Zapier/Make/n8n, or in-house dev, or technical founder)
  2. Active payment volume + ops pain (>₹10L/month + manual ops they want to automate)
  3. Engagement willingness (30-min weekly calls × 6 weeks, share screens, give feedback)
  4. Trustworthy operator (good standing, not a competitor)
- Portfolio mix: D2C 5–6, SaaS 3–4, Marketplace 2–3, EdTech 2–3, Fintech 1–2, Services 2

### A2. What's the success criteria?
**Answered in [03-gtm-strategy.md §2](03-gtm-strategy.md).** Single launch goal:
> 15+ merchants build and run their own workflow end-to-end, unprompted, within 14 days.

3 sub-goals: ≥75% activation, 15–20 unique workflows discovered, ≥30% with workflow firing 5×/week 2.

**Not the success criteria:** signups, total runs, NPS, revenue.

### A3. Since not agentic — AI use cases to position as "AI-powered payments automation platform"
**5 strong use cases that justify the AI-powered framing today** (each uses Gemini/OpenAI as a node, not as orchestrator):

| Use case | Trigger | AI node does | Output node |
|---|---|---|---|
| **Smart payment failure triage** | Payment Failed | Classify failure reason from gateway response into "card issue / bank issue / 3DS / insufficient / fraud" | Slack with category-specific playbook |
| **Personalized cart-recovery WhatsApp** | Payment Dropped | Generate empathetic message in customer's likely language (English/Hindi/Tamil/etc.) referencing their cart items | WhatsApp Business send |
| **Dispute summary for ops** | Dispute Created | Summarize dispute reason + customer history + suggested evidence in 3 bullets | Gmail to ops + Slack alert |
| **High-value refund safety check** | Refund > ₹50K | Use AI to detect anomaly patterns (rapid refunds, unusual customer, mismatched amount); flag if suspicious | Slack to founder for approval before refund completes |
| **Customer-tone reply drafting** | Inbound query (Sheet trigger) | Draft an empathetic reply matching customer sentiment | Gmail draft (human approves before send) |

**Positioning line:** *"Cashfree Relay puts AI inside your payment workflows — so failures get triaged smarter, customers get messages in their language, and ops teams get summaries instead of raw events. Without giving up control to a black-box agent."*

### A7. How to maximize PPI (Product-Penetration-Index) with Relay?
**PPI logic:** existing Cashfree merchant → adopts Relay → expands wallet share + lowers churn risk.

**5 levers, ranked by leverage:**

1. **Lifecycle email → Top 200 SMB cohort** with vertical-specific use cases ("D2C? Recover dropped checkouts." / "SaaS? Auto-dunning failed renewals.") — feeds into `cf-cross-sell-detector` per gtm-ops
2. **In-dashboard nudge on payment events** — when a merchant has 50+ Failed Payments in a month, show "Automate this with Relay" inline. Highest intent moment.
3. **Bundle into renewal conversations** — Sales/CS adds Relay as "free during beta" sweetener at renewal. Stickiness compounds.
4. **Tie GA pricing to free tier of existing Cashfree plans** — every Cashfree merchant gets X workflows free, no separate upgrade decision
5. **Solution Engineering motion** — for top 50 merchants, SE proactively co-builds first 3 workflows. Same playbook as private beta, scaled.

**The PPI metric to track at GA:** % of active Cashfree merchants who have ≥1 active Relay workflow firing weekly. **Target: 25% in Year 1, 50% in Year 2.**

---

## B. ENGINEERING QUESTIONS — sharpened versions of yours

### B3. How can a merchant communicate to us if they face issues?
**Sharpen to:**
1. Is there an in-product "Report Issue" button on each workflow / run?
2. What's captured when a merchant reports — workflow ID, run ID, payload (with PII redacted), error trace?
3. Where does it route — same Zendesk/Freshdesk as core Cashfree, or a separate Relay-only queue?
4. What's the SLA for beta merchants? (Recommend 4 hours given they're giving us feedback in exchange.)
5. Is there a Slack/Discord channel pre-built for beta cohort, or do we have to set one up?

### B4. Is there a feedback form built inside? How to access FeatureBase?
**Sharpen to:**
1. Is FeatureBase already integrated into the Cashfree dashboard, or are we adding it new for Relay?
2. Is there a `+ Suggest a feature` button per node / per workflow / global only?
3. Public roadmap visibility — yes/no? (Recommend: yes for beta, signals transparency)
4. Vote-count + status (planned/in-progress/shipped) visible to merchants?
5. Who triages incoming requests — PMM, Product, or Engineering Lead?

### B5. How do `cf-icp-scout`, `cf-outreach-writer`, `cf-stage-mover` (gtm-ops Agent skills) and Cashfree Relay work together?
**This is the most important architectural question.** Sharpen to:
1. Do gtm-ops agents (n8n + Claude Max) and Relay (Cashfree dashboard workflows) share an execution runtime, or are they separate stacks?
2. Can a Relay workflow *call* a gtm-ops agent (e.g., Relay detects high-value dispute → invokes `cf-churn-saver` to generate a save brief)?
3. Can a gtm-ops agent invoke a Relay action (e.g., `cf-cross-sell-detector` finds a fit → triggers a Relay workflow that sends a personalized in-product nudge)?
4. Are merchant data (Salesforce/Postgres) and Relay event streams accessible from each other?
5. Long-term: is the plan to converge them, or keep them as **internal automation (gtm-ops)** vs **merchant automation (Relay)**?

### B6. Pre-built templates timeline — vs Google Agent Studio, HubSpot, Razorpay
**Sharpen to:**
1. Is template library on the GA-blocking critical path, or post-GA?
2. Engineering target: how many templates by GA? By GA+90 days?
3. Will templates be **first-party** (Cashfree-built) only, or **third-party submitted** (merchant-built, vetted)?
4. Will there be a marketplace UI like Razorpay's Agent Marketplace, or just an in-product gallery?
5. Versioning — when a template updates, do existing merchant copies auto-update or stay pinned?
6. Realistic dates: when can we promise public beta merchants ≥10 templates? When ≥50?

---

## C. ADDITIONAL ENGINEERING QUESTIONS — high-signal, not yet asked

### Reliability & SLA
1. **Uptime SLA** during beta and GA? Is it tied to core Cashfree dashboard SLA or separate?
2. **Latency SLO** from event → workflow execution start? P50 / P95 / P99?
3. **Retry policy** for failed workflow runs — exponential backoff? Max retries? Dead-letter queue?
4. **Burst handling** — what happens if a merchant gets 1,000 payments/min during a flash sale? Do workflow runs queue, throttle, or drop?
5. **Idempotency** — if Cashfree retries a webhook event, does the workflow run once or twice?

### Limits & quotas (must know to set free tier pricing)
6. **Beta limits** — max workflows per merchant? Max steps per workflow? Max concurrent executions?
7. **Connector rate limits** — esp. WhatsApp Business (BSP-imposed), OpenAI (token budget), Gmail (send quota). What happens when hit?
8. **Payload size limits** per node?
9. **What happens when a merchant hits a limit** — hard fail, soft warning, queue and slow?

### Data, security, compliance
10. **Where is workflow run data stored?** Same database as Cashfree payments, or separate? Retention period?
11. **PII redaction** in logs and run history — customer phone, email, address handled how?
12. **DPDP compliance** — does Relay create any new data-subject-access-request (DSAR) surface area?
13. **LLM data flow** — when AI node runs, does merchant data go to OpenAI/Gemini? Whose API key (Cashfree's pooled vs merchant's BYOK)? Are responses logged?
14. **RBAC inside Relay** — same roles as Cashfree dashboard, or new ones? Can a "viewer" see workflows but not run history?
15. **Audit log** — who edited what workflow when? Visible to merchant admin? Required for enterprise sales later.

### Observability for merchants
16. **Workflow run debugger** — can merchant see step-by-step inputs/outputs of a failed run?
17. **Replay** — can merchant re-run a failed workflow with original payload?
18. **Workflow versioning** — can merchant see history and roll back to a prior version?
19. **Dry run / sandbox mode** — can merchant test a workflow with mock data without affecting real customers?

### Connector reliability
20. **OAuth token refresh** — what happens when merchant's Slack/Sheets token expires? Email warning? Auto-pause workflow?
21. **Third-party outage handling** — Slack/Gmail/WhatsApp down: queue, fail-fast, or fallback?

### Pricing instrumentation (need this NOW to validate WTP later)
22. **What's the metering unit** — workflow runs, step executions, AI tokens, or composite?
23. **Are AI node calls metered separately** from regular runs?
24. **Are HTTP Request node calls metered**?
25. **Free tier enforcement** — hard cap (workflow stops) or soft (warning email + grace)?

### Edge cases / payment-sensitive guardrails
26. **Max refund-via-workflow guardrail** — can a workflow auto-refund unbounded amounts, or is there a per-run cap?
27. **Circuit breaker** — if a workflow fires 100×/min unexpectedly, does anything auto-pause it?
28. **Customer-message rate limits** — to prevent a buggy workflow from spamming a customer with 50 WhatsApp messages.

### Multi-user / org structure
29. **Multiple Relay users per Cashfree merchant** — supported in beta? Permissions inherit from dashboard?
30. **Workflow ownership** — what happens if the user who created a workflow leaves the merchant team?

### Migration / portability
31. **Workflow export to JSON** (n8n-style) — supported? Important for power users + future template marketplace.
32. **If a merchant churns Relay, what happens to their workflows** — paused, deleted, archived?

### MCP roadmap
33. **MCP server timeline** — weeks, not months? What primitives exposed?
34. **Authentication for MCP** — merchant Cashfree API key, OAuth, or new mechanism?

### WhatsApp Business specifics (high-leverage connector)
35. **WhatsApp BSP** — Cashfree's pooled BSP or merchant brings their own?
36. **Template approval workflow** — who handles WhatsApp template registration with Meta? Time-to-approval?
37. **Branded sender ID** — can merchant send from their own verified WhatsApp number?

---

## D. Questions to ask **outside engineering**

### To Comms / Legal
- Are we cleared to use the phrase "AI-powered payments automation platform" given Razorpay's positioning?
- Can we publish beta merchant quotes (anonymized vs named) without legal review per quote?

### To Sales / CS
- Of the Top 200 SMB outreach budget for the quarter, what % can Relay use? (Frequency cap rule)
- Are any flagship merchants in active renewal/expansion conversations where Relay would be a useful sweetener?
- Which CSMs are bandwidth-available to white-glove 3–5 beta merchants each over 6 weeks?

### To Finance
- What's the cost-to-serve per beta merchant (mostly LLM API costs + connector infra)?
- Is there a budget cap on AI tokens during free beta — and what's our monthly spend ceiling?

### To Reeju (Decisions)
- Name lock — Relay vs other options?
- Press-light at private beta, press-heavy at GA — confirmed?
- Cross-sell to existing Cashfree merchants vs net-new acquisition for GA — primary motion?
- Free tier generosity at GA — loss leader, or break-even floor?

---

## Recommendation: send to Engineering as a single doc

Group A is for your reference — already drafted. Group B+C are the actual ask. Recommend sending engineering a single doc with **B+C combined**, asking for written answers in 5 working days. Anything not answerable becomes a flagged risk in the DIN brief.
