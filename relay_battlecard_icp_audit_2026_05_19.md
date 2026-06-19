# Relay Battlecard and ICP Audit

**Date:** May 19, 2026  
**Inputs checked:** `mstack` GitHub repo, local Relay workspace, Razorpay Agent Studio research packet, and `/Users/mothi.venkatesh/Downloads/Relay [Sales Battlecard].xlsx`.

## MStack Skills and Context Used

Relevant MStack skills identified:

- `pmm-ops/sales-enablement` — battlecard quality, swords/shields, co-creation, objection handling.
- `pmm-ops/pmm-messaging` — competitor audit before messaging, JTBD, message house, "only we can say this" test.
- `gtm-ops/icp-scout` — fit scoring, tiering, evidence trail, disqualification logic.
- `opb-curriculum/wedge-finder` — narrow wedge validation and 100-customer reachability.
- `opb-curriculum/icp-tam-research` — ICP structure by industry, size, geography, pain.
- `product-ops/pm-go-to-market-ideal-customer-profile` — demographics, behaviors, JTBD, pains, disqualification.
- `product-ops/pm-market-research-user-personas` — persona synthesis from research.
- `product-ops/pm-go-to-market-competitive-battlecard` — competitor overview, quick comparison, objections, landmines, win/loss patterns.

The most important MStack takeaway: this artifact should behave like a sales asset, not a positioning scratchpad. It needs sharper ICP filters, a live-vs-roadmap use-case boundary, and true battlecard "swords and shields."

## What Relay Is Solving

Relay solves the deployment gap between a Cashfree payment event and the next business action.

Current merchant state:

- A payment succeeds, fails, drops, refunds, or settles.
- The merchant then manually sends WhatsApp messages, updates Sheets, pings Slack, creates calendar events, checks refunds, or reconciles records.
- Generic tools can help, but they require webhook setup, payload mapping, auth handling, retries, monitoring, and ongoing maintenance.

Relay's job:

- Turn Cashfree payment lifecycle events into controlled workflows across ops, finance, growth, support, and partner tools.
- Keep the execution payment-aware, auditable, and safer than free-form autonomous agents.
- Let operators run templates without code while giving builders and partners MCP/skill surfaces for extension.

Best one-line problem statement:

> Every payment event creates work. Relay turns that work into a controlled workflow before it becomes another dashboard task, CSV export, or developer ticket.

## Category Decision From May 19

Use **Agentic Workflow Builder** everywhere.

This is the sharper category frame because it lets Relay claim the agentic shift without pretending to be a black-box autonomous Agent Studio. The distinction is:

- Razorpay Agent Studio is a hosted, 100% agentic stack built with Claude Agent SDK.
- Cashfree Relay is Cashfree's own indigenous agentic orchestration layer with HITL controls, built for secure and compliant merchant customer journeys across payment flows.
- The merchant gets control over every step of the workflow: trigger, branch, action, approval, retry, log, and activation gate.

Why this approach is better for merchants:

- **Cost:** Relay reduces the total cost of running payment-led operations because merchants do not need separate point tools, custom webhook scripts, or repeated engineering tickets for every follow-up workflow. Native Cashfree context also reduces setup and maintenance effort.
- **Reliability:** Relay is built around structured payment events, workflow branches, retries, approvals, logs, and test runs. That makes execution more repeatable than free-form autonomous agents and less brittle than generic automation stitched together outside the payment stack.
- **Control:** Relay keeps sensitive money and customer-trust journeys merchant-controlled. Teams decide exactly which steps run automatically, which steps need HITL approval, and when a workflow is safe to activate.

Scrutinized BYO AI angle:

- The claim should not be "bring your own AI is always cheaper." That can be challenged because merchants may still carry model usage, procurement, security review, prompt/eval upkeep, and vendor support costs.
- The stronger claim is **model choice and cost control**. Relay can let merchants bring preferred AI models/providers for selected workflow steps while Cashfree owns the payment event context, orchestration, HITL, logs, retries, and activation controls.
- Best cost framing: simple steps should remain deterministic rules, routine classification can use lower-cost models, and premium models should be reserved for high-value reasoning or exception handling.
- Best reliability framing: BYO AI only works well when the model is surrounded by structured workflow controls, model pinning, fallbacks, test runs, and human approvals for sensitive payment actions.
- Best control framing: the merchant controls the AI vendor/model and the workflow policy; the model does not control the full customer journey.

Recommended line:

> Cashfree Relay is the Agentic Workflow Builder for payment-led business operations. It turns Cashfree payment events into secure, compliant, merchant-controlled workflows across ops, finance, growth, support, and partner tools.

## Productization Diagnosis

The right diagnosis is not "Relay lacks the capability." The sharper diagnosis is:

> Relay has the payment primitives. Razorpay has packaged them as outcome-specific agents.

That makes this a positioning and productization gap, not necessarily a core capability gap.

Relay currently risks sounding like:

> Here are powerful payment workflow building blocks.

Razorpay sounds like:

> Here is a Dispute Responder. Here is Subscription Recovery. Here is RTO Shield. Install it and recover money.

The buyer understands the second faster. Relay should therefore lead with named, use-case-specific workflows and use the builder only after the buyer understands the outcome.

Messaging fix:

> Start with a ready workflow. Customize every step. Approve sensitive actions. Track every run.

Blunt battlecard line:

> Razorpay Agent Studio is agent-first. Cashfree Relay is workflow-first: the same high-value payment use cases, but with merchant-controlled steps, approvals, audit trails, and open extensibility.

Immediate workflow packaging:

| Workflow | Outcome | Relay angle |
|---|---|---|
| Dispute Response Workflow | Reduce dispute handling time and missed deadlines | Evidence packet + approval + audit trail |
| Subscription Recovery Workflow | Recover failed recurring revenue | Retry orchestration + customer nudges + escalation rules |
| Abandoned Checkout Recovery Workflow | Recover dropped checkouts | Payment-link generation + WhatsApp/email follow-up + conversion tracking |
| COD/RTO Protection Workflow | Reduce avoidable RTO losses | COD confirmation + risk rules + shipping hold/release + ops queue |
| Cashflow & Settlement Insights Workflow | Remove daily finance reporting toil | Settlement summaries + shortfall alerts + Sheets/Slack reports + exception handling |

## Recommended ICP

The attached workbook's ICP is directionally right but too broad:

> "Indian mid-market D2C and ecommerce merchants using Cashfree PG..."

Recommended sharper primary ICP:

| Dimension | Recommended ICP |
|---|---|
| Segment | Cashfree PG merchants in D2C/ecommerce and adjacent high-frequency payment businesses |
| Size | ₹30L-5Cr monthly GMV for main launch; >₹10L monthly payment volume for private beta learning |
| Order volume | 1,000-20,000 orders/month |
| COD / payment ops signal | COD share >40%, RTO >20-25%, payment failures/drops visible during sale windows, or recurring refund/recon workload |
| Team | 5-200 employees; ops/finance/growth team exists but is stretched |
| Stack | Cashfree PG, Shopify/WooCommerce/custom storefront, Shiprocket/Delhivery, Interakt/AiSensy/WhatsApp tool, Sheets/Tally/Zoho |
| Buyer | Founder, Head of Ops, Growth/CRM Head, Finance/Ops Head |
| User | Ops lead, growth manager, finance operator, support lead |
| Disqualify for sales-led motion | Non-Cashfree merchant with no migration intent; <₹10L monthly volume; no repeated payment ops pain; needs enterprise SLA/custom procurement immediately |

Secondary ICPs should stay, but not lead the sales battlecard:

- **Integration agencies / SIs:** useful partner channel, especially for Shopify + Cashfree automation retainers.
- **Developers / technical founders:** useful for MCP and Agent Skills adoption, but not the primary business buyer for the sales battlecard.
- **EdTech, services, coaching, clinics:** strong use cases around payment success to appointment/onboarding, but not the main competitive wedge against Razorpay Agent Studio.

## Personas

### 1. Neha, D2C Ops / Growth Lead

Primary persona.

- Runs daily payment ops for a D2C brand.
- Uses Cashfree dashboard, Sheets, WhatsApp, Shiprocket, Interakt/AiSensy.
- Pain: failed payments, COD confirmation, RTO, refunds, reconciliation, manual follow-ups.
- Wants: template she can run in minutes, visible logs, no API keys, no developer dependency.
- Success metric: recovered revenue, fewer manual hours, lower RTO, faster refund handling.

### 2. Finance / Ops Owner

Primary for finance-led workflows.

- Cares about refunds, settlement visibility, high-value alerts, reconciliation, audit.
- Wants control, approval gates, traceability, and exception handling.
- Success metric: fewer errors, faster exception review, less daily reporting toil.

### 3. Suresh, Integration Agency / Partner

Secondary GTM channel.

- Builds Shopify/Cashfree/WhatsApp automations for multiple merchants.
- Wants reusable templates, multi-client management, uptime, and a way to resell vertical workflows.
- Success metric: deploy template in 20 minutes instead of rebuilding n8n flows for every client.

### 4. Arjun, Developer / Technical Founder

Developer channel, not main sales ICP.

- Wants Cashfree primitives as MCP tools.
- Extends templates, wires to internal systems, builds custom agents.
- Success metric: no webhook boilerplate, faster integration, programmable payment context.

## Use Case Truth Table

The workbook needs a status column. Right now it mixes live, beta, and roadmap use cases, which creates sales risk.

| Use Case | Sales Status | Notes |
|---|---|---|
| Calendar / appointment on payment success | Live/private beta | Strong for edtech, services, clinics, classes. |
| High-value payment alerts | Live/private beta | Good founder/finance visibility use case. |
| Payments to Google Sheets / Live Books | Live/private beta | Good operational wedge, low AI overclaim risk. |
| Failed payment digest | Live/private beta | Current live claim should be digest/reporting. Customer retry/nudge automation should be clearly marked if not live. |
| COD confirmation | Live/private beta if only confirmation/hold flow | Do not overclaim "RTO recovery" or COD-to-UPI conversion unless that specific flow is shipped. |
| Vendor payouts on schedule | Live/private beta if built | Needs maker-checker language because payouts are irreversible. |
| Abandoned cart conversion | Roadmap / public-beta target unless shipped | Razorpay has a strong public demo here. Do not claim parity unless product can actually trigger and message with cart context. |
| Refund triage / approval | Split carefully | Approval workflow may be live; AI refund classification / customer drafting appears roadmap. |
| Dispute response | Post-GA roadmap | Razorpay has a strong lead here. For Relay, frame as future payment-ops template, not current sales wedge. |
| Subscription recovery | Post-GA roadmap | Relevant, but not a current Relay wedge unless subscription triggers exist. |
| KYC-gated onboarding | Future differentiator | Strong Cashfree-only angle through Secure ID, but should be positioned as roadmap/strategic differentiator. |

## Battlecard Review

### What Is Good

- The workbook correctly avoids saying Relay is a full autonomous Agent Studio.
- It uses the safer line: "workflow-first, agentic where useful."
- The comparison against generic automation tools is directionally strong.
- The Selling Risk tab has useful discovery questions and does not overpromise autonomy.
- The Ecom tab is practical and sales-readable.

### What Needs Correction

1. **Use "Agentic Workflow Builder" as the default category.**
   - Avoid the weaker generic phrase "workflow automation layer."
   - Avoid the vague phrase "AI workflow builder."
   - Recommendation: use "Agentic Workflow Builder" consistently, then immediately anchor it in merchant control, HITL approvals, and payment-grade auditability.

2. **Add a status column to every use case.**
   - Suggested values: `Live/private beta`, `Roadmap <90 days`, `Post-GA`.
   - This prevents sales from demoing or promising roadmap items.

3. **Sharpen the ICP in the Overview tab.**
   - Current ICP is okay for broad marketing, not for sales qualification.
   - Add GMV, order volume, COD/RTO/payment-failure signals, current stack, and disqualifiers.

4. **Make Razorpay comparison more precise.**
   - Current sheet says "Razorpay AI / Agentic Studio."
   - Use "Razorpay Agent Studio" and acknowledge where it is genuinely strong:
     - stronger AI narrative
     - prebuilt agents
     - partner ecosystem
     - Claude Agent SDK
     - early public proof for cart recovery and dispute response
   - Then land the Relay reframe:
     - Cashfree-native event context
     - open MCP / agent surface
     - workflow control and human approvals
     - better fit for merchants who need controlled payment operations, not autonomous agent delegation.

5. **Turn Competitor Analysis into a real battlecard.**
   MStack's sales-enablement skill says battlecards need swords and shields, not only comparison tables.

   Add for Razorpay:
   - **Deal signal:** prospect asks "Is this like Razorpay Agent Studio?" or wants abandoned cart/dispute agents.
   - **Killer question:** "Do you want a Razorpay-controlled agent inside their dashboard, or payment workflows your team can inspect, approve, and extend across your stack?"
   - **Trap to avoid:** do not argue that Relay has better AI agents. It does not today.
   - **Reframe:** "Relay is for controlled payment workflows on Cashfree events. Razorpay is betting on hosted autonomous agents inside Razorpay."
   - **Proof point needed:** beta merchant workflow with time saved or revenue recovered.

6. **Fix the live-claim mismatch around failed payments.**
   - Merchant notes say "hourly digest of failed payments" is shipped and explicitly does not retry or notify customers.
   - Battlecard says "Trigger nudges, retries, alerts, or voice/WhatsApp follow-ups."
   - Recommendation: change current claim to "failed payment digest and prioritized follow-up queue"; mark automated nudges/retries as roadmap unless already implemented.

7. **Add partner/persona rows.**
   - The battlecard has a partner email but the Overview tab does not explain partner ICP.
   - Add: agencies/SIs who manage 6-15 D2C/SMB clients and repeatedly rebuild Cashfree to WhatsApp/Sheets workflows.

## Corrected Battlecard Core

### Category

Agentic Workflow Builder for Cashfree merchants.

### Positioning

For Cashfree merchants whose ops, finance, and growth teams still turn payment events into manual follow-ups, Relay is an Agentic Workflow Builder that converts Cashfree events into secure, compliant, merchant-controlled workflows across WhatsApp, Slack, Sheets, CRM, calendars, approvals, and internal teams.

Unlike generic automation tools, Relay starts with Cashfree payment context. Unlike Razorpay Agent Studio's hosted stack built with Claude Agent SDK, Relay runs on Cashfree's own indigenous agentic orchestration layer with HITL controls for payment flows.

### Primary Sales Wedge

Do not lead with "Agent Studio." Lead with one of these:

1. Failed payment visibility and recovery workflow
2. COD confirmation and RTO reduction
3. Refund approval / maker-checker
4. Daily payment-to-Sheets / finance summary
5. High-value payment alerting

### Discovery Questions

- What happens in your team after a Cashfree payment fails?
- Who manually follows up on dropped checkouts or COD confirmation today?
- How many refunds need approval before they are processed?
- What payment or settlement report is still copy-pasted into Sheets?
- Which workflow keeps going to your developer even though it is not core product work?
- What breaks today: WhatsApp templates, Zapier/Pabbly workflows, Sheets, or manual follow-up?

## Bottom Line

The battlecard is directionally sound, but it needs tightening before broad sales use.

The safest and strongest story is:

> Relay is not Cashfree's copy of Razorpay Agent Studio. Relay is Cashfree's Agentic Workflow Builder: payment-aware, controlled, auditable, MCP-enabled, and built for Indian payment operations where every event needs a secure next action.

Primary ICP should be narrowed to Cashfree D2C/ecommerce merchants with visible post-payment ops pain. Use cases should be split by live vs roadmap. Razorpay should be treated as a strong AI-agent narrative competitor, while Relay should win on payment context, workflow control, open extension, and merchant trust.
