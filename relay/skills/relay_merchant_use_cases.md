# Cashfree Relay — Merchant Use Case Notes

Brief summaries for merchant conversations. Each note covers what it does, who it's for, and what to watch out for.

---

## Shipped

### Use Case 1: Calendar event every time a customer pays

**What it does:** When a payment succeeds, Relay automatically creates a Google Calendar or Cal.com event — with the customer name, amount, order ID, and a direct link back to the Cashfree dashboard.

**Who it's for:** Founders running cohort courses, webinars, consulting, event ticketing, B2B-SaaS — anywhere each payment is a meaningful moment worth blocking on the calendar. Not for high-volume merchants (quick commerce, marketplaces) — the calendar floods.

**Set up:** Pick your calendar, set filters (amount, product, SKU), and customise the event title/description template.

**Watch out for:** If order metadata doesn't carry the customer name, the event title falls back to the order ID.

---

### Use Case 2: Alert on every big-ticket payment

**What it does:** When a payment crosses your threshold, Relay fires a real-time notification to WhatsApp, Slack, SMS, or email — with amount, customer name, payment method, order ID, and a dashboard link.

**Who it's for:** Founders who want instant visibility on high-value orders. Install twice — founder gets ₹2L+ alerts on WhatsApp; ops team gets ₹50K+ alerts on Slack.

**Set up:** Set your threshold per channel. Different people can have different thresholds on different channels from the same account.

**Watch out for:** WhatsApp notifications use pre-approved Meta templates — no free text. Multi-currency merchants: threshold is per-currency, not converted.

---

### Use Case 3: Auto-sync payments to Google Sheets

**What it does:** Every successful payment (and optionally, every refund) appends a new row to a Google Sheet you choose. Columns map to amount, currency, payment method, order ID, customer name, status, and timestamp.

**Who it's for:** Founders and finance teams who still export the morning CSV. Replaces the daily copy-paste ritual for merchants up to ~80K transactions/day.

**Set up:** Connect Google Sheets, map your columns, and optionally add refund tracking.

**Watch out for:** Card numbers and bank account numbers never appear — by design. Customer phone/email is opt-in, off by default. Above 80K rows, the workflow self-warns before Sheets limits cause silent failures.

---

### Use Case 4: Hourly digest of failed payments

**What it does:** On a schedule you choose (hourly, 4-hourly, or daily), Relay sends one message — total count, ₹ impact, and a breakdown of failures by reason code (UPI timeout, insufficient funds, 3DS failed, etc.), each with a deep-link to the dashboard for that group.

**Who it's for:** Ops and finance at merchants where checkout health matters but real-time per-failure alerts aren't practical. Typical install: founder gets the daily digest; ops Slack channel gets hourly.

**Set up:** Pick cadence, pick channels, and configure whether to send a message for empty windows.

**Watch out for:** This is a reporting workflow. It does not retry payments or notify customers.

---

## Roadmap

### Use Case 5: Recover the dropped checkout automatically

**What it does:** When a customer drops at checkout, Relay generates a fresh Cashfree payment link and sends it via WhatsApp or email after a short delay (default: 5 min for PG drop, 30 min for cart). A configurable reminder ladder sends up to 3 follow-ups. Once the customer pays, chasing stops.

**Who it's for:** D2C and e-commerce brands where abandoned checkouts are a daily bleed. Especially relevant if you're paying a BSP platform (Interakt, AiSensy, Pragma) for abandoned cart automation — this sits in the same gap.

**Set up:** Pick your trigger (Cashfree Payment Dropped, or cart-abandoned webhook from Shopify / WooCommerce / Wix), set the delay, configure the reminder ladder, and choose your WhatsApp template.

**Watch out for:** Relay only sends to the verified customer phone/email from order metadata — not arbitrary contacts. One link per dropped event. Industry benchmarks show 15–25% recovery; Cashfree will publish its own validated number once live.

---

### Use Case 6: Generate a payment link from a DM

**What it does:** When a customer sends a buying intent on WhatsApp or Instagram, your chatbot platform calls Relay with the intent and customer phone. Relay generates a Cashfree Payment Link or UPI Link and returns it to the chatbot, which replies in the same thread — no manual dashboard login.

**Who it's for:** Home-based businesses, social-commerce brands, Instagram-first sellers, and D2C brands running chat-led sales via Wati, AiSensy, Interakt, Haptik, or Yellow Messenger.

**Set up:** Connect your chatbot platform, map intents to products and amounts, and pick link type (UPI or Payment Link).

**Watch out for:** UPI Link doesn't work on iOS — Relay auto-falls back to Payment Link. Chatbot platform owns intent detection; Relay handles link generation and audit only. Latency target: link returned in under 5 seconds.

---

### Use Case 7: Run your monthly collection cycle on autopilot

**What it does:** Upload or connect your customer master (borrowers, students, society members, subscribers). On a schedule you set, Relay generates a Cashfree Payment Link per customer, sends it via their preferred channel (WhatsApp, SMS, email), and runs a configurable reminder ladder for unpaid links. Paid status syncs back via Payment Success webhook.

**Who it's for:** NBFCs, schools, coaching institutes, societies, RWAs, utility billing, B2B subscription businesses — anyone running link-based recurring collections where customers pay manually each cycle.

**Set up:** Upload your customer master, set the schedule and reminder ladder, and configure whether bulk sends need maker-checker approval before firing.

**Watch out for:** This is for link-based collection — not mandate-based auto-debit (that's Cashfree Subscriptions/NACH/UPI Autopay). RBI Fair Practice Code applies to NBFC collection messaging — compliance team must review templates. Supports batches up to 10,000 customers per cycle.

---

### Use Case 8: Confirm every COD order on WhatsApp before it ships

**What it does:** When a new COD order comes in, Relay sends a WhatsApp confirmation to the customer within 10 minutes. Confirmed orders ship; no-response orders go to a manual call queue or get a second message (merchant's choice). Optional: include a prepaid discount offer — if the customer pays the Cashfree link, the COD order is cancelled and a prepaid order is created.

**Who it's for:** D2C brands where COD is 50%+ of orders and RTO is a daily cost. At 1,000 orders/day with 60% COD and 20% RTO, unrecovered shipping costs run ₹15K–₹100K/day.

**Set up:** Connect your Shopify/WooCommerce/OMS webhook, pick your WhatsApp template, configure the no-response action, and optionally set a COD-to-prepaid discount.

**Watch out for:** WhatsApp messages use pre-approved Meta templates. Check marketplace policy before pitching to Amazon/Flipkart/Meesho sellers — some don't allow confirmation flows. Industry benchmark: 40% RTO reduction (CampaignHQ figure; not a Cashfree claim).

---

### Use Case 9: Auto-reconcile Cashfree settlements against your books

**What it does:** When Cashfree settles funds to your bank, Relay pulls the transaction breakdown, queries open invoices in Tally or Zoho Books by order ID, applies match logic, and flags mismatches with a reason (amount mismatch, missing invoice, duplicate). A weekly digest goes to your finance team. Write-back to accounting requires manual approval by default.

**Who it's for:** Finance teams at merchants doing ₹50L+/month in GMV where manual reconciliation is hours per week. External CAs and accounts managers are the day-to-day users.

**Set up:** Connect Tally or Zoho Books, configure match rules (amount tolerance, fee handling, multi-day settlement window), and choose flag-only or approve-then-write-back mode.

**Watch out for:** Chargebacks are flagged only — no auto-write (compliance review needed). Multi-currency merchants need FX handling configured or mismatches go to manual. Wave 1 supports Tally and Zoho Books only.

---

*4 shipped · 5 on roadmap · Always label roadmap use cases as such in merchant conversations.*
