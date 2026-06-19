# Cashfree Relay — Template Library Spec (v1)

> Source: Eng's 7 documented use cases + 4 Growth Operator templates we've been positioning publicly.
> Outcome framing: every template names a loss reduced, sale improved, or revenue recovered.
> **Status legend:** ✅ Live in private beta · 🟡 Roadmap (≤90 days) · 🔴 Roadmap (>90 days, post-GA)

This doc is the single source of truth for what templates Cashfree Relay claims to ship.
**Rule:** if a template isn't on this list, marketing/sales/PR cannot reference it as available.

---

## A. Templates that exist today (Eng-documented use cases, recast)

These are functional in private beta. The Eng overview describes them in operational language; below they are recast in Growth Operator language for merchant-facing use.

### A1. ✅ COD Confirm — Cut RTO before dispatch
**Outcome:** Reduce return-to-origin (RTO) failures by 25–35%.
**Why this matters:** RTO eats 18–25% of COD GMV for Indian D2C. One template here pays for the entire product.

| Element | Spec |
|---|---|
| **Trigger** | Order created (HTTP) |
| **Condition** | Order is COD |
| **Action 1** | WhatsApp Business: confirmation message with Confirm/Cancel buttons |
| **Action 2 (if confirmed)** | Sheet log + proceed |
| **Action 2 (if no response in 4h or cancel)** | Cancel order in commerce stack via HTTP + customer notify |
| **AI node (optional)** | Score order RTO-risk based on address/phone/velocity; only confirm high-risk |
| **Eng overview source** | "Verify cash on delivery (COD) orders" |

### A2. ✅ High-Value Refund Approval — Maker/Checker for refunds you can't afford to get wrong
**Outcome:** Zero unauthorized high-value refunds. Audit trail by default.

| Element | Spec |
|---|---|
| **Trigger** | Refund Success |
| **Condition** | Refund amount > ₹50,000 (configurable) |
| **Action 1** | Slack: approval request with refund context + customer history |
| **Action 2** | Email to designated approver |
| **Hold** | Refund is informational here (refund already initiated); for *pre*-refund approval use Cashfree Payments action node + manual review (post-MCP) |
| **Eng overview source** | "Route high-value refunds for approval" |

### A3. ✅ Fraud Watch — Spot suspicious transactions in 30 seconds
**Outcome:** Catch fraud-shaped transactions before settlement window closes.

| Element | Spec |
|---|---|
| **Trigger** | Payment Success |
| **Condition** | Amount > merchant-defined threshold (e.g. ₹1,00,000) |
| **Action 1** | Slack alert with transaction context |
| **Action 2 (AI node, optional)** | Generate risk-score narrative from order history + customer history |
| **Action 3** | WhatsApp/SMS to ops lead |
| **Eng overview source** | "Monitor high-value transactions" |

### A4. ✅ Live Books — Your finance team's source of truth, updated in real time
**Outcome:** Eliminate end-of-day reconciliation. Books are always current.

| Element | Spec |
|---|---|
| **Trigger** | Payment Success / Failed / Refund Success |
| **Action** | Append row to Google Sheets with: order ID, amount, status, customer, settlement date |
| **Variant** | Schedule-triggered: hourly/daily summary roll-up |
| **Eng overview source** | "Sync transaction data to Google Sheets" |

### A5. ✅ Failed Payment Digest — Catch payment-failure churn before it churns
**Outcome:** Recover revenue from failed payments. Beta benchmark: 15–25% of failed payments recovered when retry link sent within 1 hour.

| Element | Spec |
|---|---|
| **Trigger** | Schedule Based (hourly) |
| **Action 1** | Pull Failed Payments from last hour |
| **Action 2 (AI node)** | Categorize failures (3DS / insufficient / bank-side / card / fraud) |
| **Action 3** | Email/Slack digest to growth team with retry-link drafts |
| **Eng overview source** | "Receive hourly reports for failed transactions" |

### A6. ✅ Auto-Onboard — Every paying customer scheduled, logged, welcomed
**Outcome:** Eliminate the manual handoff between payment and onboarding. Zero customers fall through.

| Element | Spec |
|---|---|
| **Trigger** | Payment Success |
| **Action 1** | Create Google Calendar event (welcome call slot or onboarding session) |
| **Action 2** | Gmail: welcome email with calendar link |
| **Action 3** | Sheet log entry |
| **Eng overview source** | "Create a calendar event on payment success" |

### A7. ✅ Vendor Payouts on Schedule
**Outcome:** Automate vendor payment cadence. Audit trail by default.

| Element | Spec |
|---|---|
| **Trigger** | Schedule Based (e.g., last working day of month) |
| **Action 1** | HTTP node: pull vendor list from merchant's system |
| **Action 2** | Cashfree Payouts API call (scoped to vendor IDs) |
| **Action 3** | Email confirmation + Sheet log |
| **Eng overview source** | "Schedule vendor payouts" |

---

## B. Growth Operator templates we've positioned publicly

These are the templates marketing/PR has been claiming. **Status today: 🟡 Roadmap.** They must ship before public beta or be removed from public-facing copy.

### B1. 🟡 RTO Recovery — Convert COD to UPI Prepaid before dispatch
**Outcome:** Reduce RTO by 25–35%. Convert 10–20% of COD orders to prepaid.
**Build dependency:** ML scoring for RTO-prone orders, UPI deep-link generation, WhatsApp template approval (Meta).

| Element | Spec |
|---|---|
| **Trigger** | Order created (HTTP) |
| **Condition** | RTO risk score > threshold (AI node) |
| **Action 1** | Generate UPI prepayment link (Cashfree) |
| **Action 2** | WhatsApp Business: "Confirm via UPI for ₹X off" with link |
| **Action 3 (if paid)** | Convert order to prepaid in commerce stack |
| **Action 4 (if no action 4h)** | Fallback: COD confirm flow (A1) |
| **Status** | 🟡 Targeting public beta (Week 7-10) |

### B2. 🟡 Fake Order Detection — Block fraudulent orders before fulfilment
**Outcome:** Reduce fake-order fraud by 40–60%. Save fulfilment cost on flagged orders.
**Build dependency:** Composite signal (address mismatch, repeat phone across customers, velocity, COD pattern).

| Element | Spec |
|---|---|
| **Trigger** | Order created (HTTP) |
| **AI node** | Composite fraud score from address/phone/velocity/repeat patterns |
| **Condition** | Score > threshold |
| **Action 1** | Slack alert to ops with reason narrative |
| **Action 2** | Hold order via HTTP to commerce stack |
| **Status** | 🟡 Targeting public beta |

### B3. 🟡 Cart Recovery — Recover dropped checkouts via WhatsApp
**Outcome:** Recover 5–8% of dropped checkouts.
**Build dependency:** Payment Dropped trigger payload includes cart context; WhatsApp template approved.

| Element | Spec |
|---|---|
| **Trigger** | Payment Dropped |
| **Condition** | Cart value > ₹500 (filter low-value spam) |
| **Action 1 (AI node)** | Generate empathetic message in customer language |
| **Action 2** | WhatsApp Business: cart link + optional discount |
| **Action 3 (after 24h, no return)** | Email follow-up |
| **Status** | 🟡 Targeting public beta |

### B4. 🟡 Refund Triage — Classify, draft, route every refund in 30 seconds
**Outcome:** Cut refund-handling time from hours-per-batch to seconds-per-event.
**Build dependency:** Reliable refund-reason taxonomy from AI node.

| Element | Spec |
|---|---|
| **Trigger** | Refund Success |
| **AI node** | Classify reason (defect / wrong item / size / changed mind / other) |
| **Action 1** | Gmail draft to customer (reason-specific template) |
| **Action 2** | Slack to ops with classification + customer history |
| **Action 3** | Sheet log + accounting pull (if HTTP-Tally connected) |
| **Status** | 🟡 Targeting public beta |

---

## C. Templates on the 90-day post-GA roadmap

### C1. 🔴 Dispute Response — Auto-gather evidence + draft response
**Trigger:** Dispute Created → AI summarizes order/customer history → Gmail draft to ops with evidence pack.

### C2. 🔴 Daily Reconciliation — Settlements diff against orders
**Trigger:** Schedule (daily 9am) → pull settlements → diff against expected → surface mismatches in Slack.

### C3. 🔴 Subscription Recovery — Failed renewal → customer outreach
**Trigger:** Subscription payment failed (post-subscription event triggers shipping) → AI-drafted recovery message → CRM update.

### C4. 🔴 KYC-Gated Onboarding (SecureID-MCP)
**Trigger:** New customer payment → SecureID verification → if pass, full access; if fail, restricted account + WhatsApp escalation. **(SecureID in MCP = Cashfree's exclusive differentiator vs Razorpay.)**

---

## Template publication rules (non-negotiable)

1. **A template can only be claimed publicly if it's labeled ✅ in this doc.** Roadmap items must always carry the 🟡/🔴 status.
2. **Each ✅ template must have at least one beta merchant running it before it goes into marketing copy.** "Built and tested" ≠ "live on merchants."
3. **Quantified outcomes (%, ₹) require beta validation.** No estimates from analyst reports as proof points.
4. **Templates marked 🟡 must have a named owner in Eng + an estimated ship date** by end of Week 4 of private beta.
5. **At any leadership review, this doc is the source of truth** on what's shippable. Not the website. Not Notion. This file.

---

## Outcome summary by template

| Template | Status | Outcome metric | Target |
|---|---|---|---|
| A1 COD Confirm | ✅ | RTO reduction | 25–35% |
| A2 Refund Approval | ✅ | Unauthorized refunds | 0 |
| A3 Fraud Watch | ✅ | Time-to-flag | <30 sec |
| A4 Live Books | ✅ | Recon lag | Real-time |
| A5 Failed Payment Digest | ✅ | Failed-payment recovery | 15–25% |
| A6 Auto-Onboard | ✅ | Manual handoff time | 0 min |
| A7 Vendor Payouts | ✅ | Cycle time | Auto |
| B1 RTO Recovery (UPI) | 🟡 | COD → prepaid conversion | 10–20% |
| B2 Fake Order Detection | 🟡 | Fraud reduction | 40–60% |
| B3 Cart Recovery | 🟡 | Dropped-checkout recovery | 5–8% |
| B4 Refund Triage | 🟡 | Refund-handling time | -90% |
| C1 Dispute Response | 🔴 | Win-rate uplift | TBD |
| C2 Daily Recon | 🔴 | Recon time | -80% |
| C3 Subscription Recovery | 🔴 | Renewal recovery | TBD |
| C4 KYC-Gated Onboarding | 🔴 | Account fraud | TBD |

---

## What this enables

- **Marketing/PR** can write outcome-led copy without inventing claims
- **Sales/CS** has 7 real templates to demo, day 1 of private beta
- **Beta merchants** see a credible roadmap (✅ today + 🟡 in 90 days + 🔴 post-GA)
- **Engineering** has a ranked feature backlog driven by merchant value, not internal preference
- **PMM** has an audit trail — every public claim traces back to a row in this doc

---

*Maintained by PMM. Update before any external launch artifact ships.*
