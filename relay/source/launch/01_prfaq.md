# PRFAQ — Cashfree Relay (Private Beta)

> Format: Amazon Working Backwards. Press release written first to force clarity. FAQ addresses customer + internal questions.

---

## PRESS RELEASE

### Cashfree launches Relay — the first payments-native workflow automation built for Indian merchants
**Bengaluru, [Launch date]** — Cashfree Payments today announced **Relay**, a no-code workflow automation platform built directly into the Cashfree dashboard. Relay turns every payment, refund, and dispute event into a trigger that merchants can use to automate invoicing, customer notifications, ops alerts, and reconciliation — without writing code or hiring a developer.

#### The problem
Indian SMB merchants spend 5–8 hours every week on repetitive payments-related tasks: emailing invoices after every successful payment, manually following up on dropped checkouts, copy-pasting refund details into Tally, alerting ops when a dispute hits. Existing automation tools — Zapier, Make, n8n — solve part of this, but they require a developer to set up webhooks, parse payloads, handle authentication, and maintain the integration. For a 10-person D2C brand, that's a 2-week project just to get an invoice email working.

#### The solution
Relay eliminates that work. Payment events from Cashfree are first-class citizens — `Payment Success`, `Payment Failed`, `Payment Dropped`, `Refund Success`, `Dispute Created`, and 4 more — available the moment a merchant turns Relay on. Connect them to Google Sheets, Slack, Gmail, WhatsApp Business, Zoho Invoice, Calendly, or any HTTP endpoint, and the workflow runs forever.

> "We built Relay because our merchants kept asking the same question: *can Cashfree just send the invoice for me?* Relay is our answer — but bigger. It's not just invoices. It's every workflow that follows a payment event. And we've made it so simple that the person who handles your customer support can build it." — **Reeju Datta, Co-founder, Cashfree Payments**

#### Available in private beta
Relay ships with **9 native payment triggers**, **1 schedule trigger**, **10 connectors** (Google Sheets, Slack, Gmail, WhatsApp Business, Calendly, Google Calendar, Zoho Invoice, Gemini, OpenAI, Cashfree Payments), and an **HTTP request node** for everything else. Two LLM connectors — Google Gemini and OpenAI — let merchants generate personalized customer messages, summarize disputes, and triage failures intelligently.

> "We were paying ₹6,000/month for Zapier and a freelance developer to maintain three workflows. Relay replaced all of it in an afternoon. Our refund confirmations now go out in 30 seconds, not an hour." — **[Beta merchant quote — TBD]**

Relay is available in **private beta** to select Cashfree merchants today. Apply at cashfree.com/relay.

---

## FAQ

### Customer-facing FAQ

**Q1. What is Relay?**
Relay is a no-code workflow automation platform built into Cashfree. You pick a payment event ("when a customer's payment fails"), pick what should happen ("send them a WhatsApp retry link and post in #ops Slack"), and Relay runs it forever.

**Q2. Who is Relay for?**
Indian SMBs and D2C brands using Cashfree to accept payments — typically 5–200 employees. The person setting up workflows is usually an ops, finance, or growth manager — not a developer.

**Q3. How is this different from Zapier or n8n?**
Three things:
- **Payments are typed events, not webhooks.** Zero webhook setup, no payload mapping, no auth headaches.
- **Built into the Cashfree dashboard.** Same login, same access controls, same support team.
- **AI-ready out of the box.** Gemini and OpenAI are connectors, so workflows can write personalized messages, summarize disputes, or classify failures without extra tools.

**Q4. What can I automate?**
Common workflows our beta merchants are running today:
- Send a Zoho invoice + Gmail receipt + Sheets log entry on every successful payment
- WhatsApp retry link to customers whose payment failed
- WhatsApp recovery message to customers who dropped checkout
- Slack alert + evidence-gathering email on every new dispute
- Daily settlement summary to founder Gmail at 9am
- Auto-update Tally (via HTTP request) on refund success

**Q5. What does it cost?**
Free for all Cashfree merchants during private beta. Pricing tiers TBD at GA — likely a free tier (X workflows, Y runs/month) and paid tiers based on workflow volume.

**Q6. Do I need to know how to code?**
No. The Simple Schedule trigger doesn't even use cron syntax — pick "every 4 hours" from a dropdown. The HTTP request node exists for power users who want to hit a custom API; you can ignore it if you don't need it.

**Q7. What about data privacy?**
Workflow data stays inside Cashfree's infrastructure (the same that processes your payments — RBI, PCI-DSS compliant). Third-party connectors (Google, Slack, etc.) authenticate via OAuth and only see data you explicitly send them.

**Q8. What's missing today?**
Conscious gaps in private beta — coming to GA:
- CRM connectors (HubSpot, Salesforce, Zoho CRM)
- Accounting (Tally, QuickBooks, Xero, Zoho Books)
- E-commerce (Shopify, WooCommerce)
- Payouts, subscription, KYC event triggers
- Conditional branching, error handling improvements

**Q9. How do I get access?**
Apply at cashfree.com/relay. We're onboarding ~50 merchants per week through private beta. Approval criteria: existing Cashfree merchant in good standing, at least 3 months of payment history, willingness to give feedback.

**Q10. Will this replace my developer?**
No. Relay handles the 80% of workflows that don't need custom logic. For complex, high-volume, or business-critical workflows, your developer still wins. Relay frees them to work on those instead of invoice emails.

---

### Internal FAQ

**Q1. Why are we building this? Cashfree is a payments company.**
Three reasons:
1. **Stickiness.** Merchants who automate workflows around Cashfree events don't churn. Switching cost compounds with every workflow built.
2. **Wedge into ops/finance buyer.** Cashfree historically sells to founders/CTO. Relay creates a beachhead with the ops/finance buyer who controls renewal conversations at scale.
3. **AI moat.** With Gemini + OpenAI baked in, Relay becomes the surface where AI meets payments for SMBs. No competitor (Razorpay, PayU) is positioned for this.

**Q2. Why now?**
- AI workflow tools (Lindy, Cassidy, Relay.app) are validating that no-code + AI is mainstream.
- Indian SMB digital adoption is at an inflection point post-UPI/ONDC maturity.
- Razorpay has not launched a comparable product. **18-month window before competitors copy.**

**Q3. What's the revenue model?**
TBD at GA. Working hypothesis:
- **Free tier** (5 workflows, 500 runs/month) — adoption driver, retention play
- **Pro tier** (~₹999–1,999/month) — unlimited workflows, premium connectors, AI credits
- **Business tier** — usage-based for high-volume merchants
- Long-term: Relay becomes a **distribution channel for partner products** (Zoho Invoice, WhatsApp Business templates, etc.) — take rate on installs.

**Q4. How do we measure success at private beta?**
**The north star metric (Successful Workflow Runs per Active Merchant per Month) does NOT apply yet.** Private beta is a learning sprint, not a growth sprint — runs will be tiny and misleading without templates.

**Single launch goal:** 15+ merchants build and run their own workflow end-to-end, unprompted, within 14 days of access.

**Three sub-goals stacked under it:**
- **Activation:** ≥75% build a workflow (15 of 20)
- **Use case discovery:** 15–20 distinct workflows built (becomes our template library)
- **Stickiness signal:** ≥30% have a workflow firing ≥5× in week 2 (separates "tried it" from "using it")

**Explicitly NOT optimizing for:** signups, total runs, NPS, revenue, press coverage. See 03-gtm-strategy.md §3.

The north star metric goes live at GA, not beta.

**Q5. What's the biggest risk?**
**Workflow setup is too hard for non-devs.** If beta merchants need a Cashfree CSM to build their first workflow, the model breaks. **There are no ready-to-use templates yet** — every beta merchant builds from scratch. Mitigation for private beta: white-glove onboarding (CSM + ops team co-builds first 3 workflows per merchant) + Loom walkthroughs for the top 5 use cases. Template library is the #1 dependency for GA.

**Q6. Build vs buy vs partner — why build?**
- **Buy** (acquire n8n/Make): too expensive, kills product velocity for our use case.
- **Partner** (Zapier integration): leaves margin and stickiness on the table; Zapier owns the relationship.
- **Build:** native triggers + native UI + native auth = 10x experience for the 80% workflow case. Long-term defensible.

**Q7. Why limit private beta — why not open it up?**
Three reasons:
1. **Quality of feedback.** 50 engaged beta merchants > 5,000 silent signups.
2. **Scarcity creates demand.** Waitlist signal builds GA momentum.
3. **Connector + trigger gaps.** We need to learn which connectors merchants ask for *most* before GA pricing.

**Q8. What does the GA bar look like?**
- ≥10 ready-to-use templates published, each with documented beta-merchant adoption
- ≥70% beta merchant retention at day 60
- ≥3 case studies with quantified time-saved
- Pricing model validated against ≥10 willingness-to-pay conversations
- Roadmap-locked Tier-1 connectors: HubSpot, Tally, Shopify
- Self-serve activation rate ≥40% (merchant ships first workflow without CSM help)
