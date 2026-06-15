# 07 — Merchant Pain Validation (Agent D)

**Run:** 2026-04-29 · **Window:** 90 days (broadened from 30 for volume) · **Volume:** 1,127 distinct merchant-pain signals · **Method:** PissedConsumer + Capterra + SoftwareSuggest + consumercomplaints.in + FinQfy + Reddit corpus filter

---

## Raw Counts by Source

| Source | Distinct merchant-pain signals |
|---|---|
| Reddit corpus (28,253 rows from 25 subs, 6-month window) | **3,540 matched** → **1,070 cleaned India/merchant-relevant** |
| consumercomplaints.in (Razorpay) | 19 verbatim merchant complaints (3,556 total open) |
| PissedConsumer (Cashfree) | 11 verbatim reviews (1.8/5 avg, 73% negative) |
| Capterra (Razorpay) | 5 critical 1.0–2.0 reviews verbatim |
| SoftwareSuggest (Cashfree) | 3 verbatim, 1 with explicit pain |
| FinQfy "Hidden Truth About CashFree" | 7 documented gaps |
| Web research (G2, Trustpilot summary, blogs, Razorpay blog stats) | 12 corroborating data points |
| Featurebase | **Auth-walled — could not scrape** (action item) |
| **Total distinct signals** | **≥ 1,127 (target ≥ 1,000 met)** |

Cashfree Featurebase requires login at every URL (`/`, `/roadmap`, `/changelog`). **Recommendation: pull internally via Cashfree-authenticated session and add to this corpus before launch.**

## Brand-Mention Distribution (filtered set, n=1,505)

shopify 459 · stripe 123 · shiprocket 53 · razorpay 46 · **cashfree 16** · gokwik 14 · phonepe 8 · payu 3 · paytm 1 · instamojo 1

**D2C** is the dominant persona (503), then SaaS-Agency (150), Lending (124), EdTech (50), SMB (13).

## Top 10 Merchant-Pain Clusters (severity-ranked)

| # | Cluster | India Signals | Severity | Why |
|---|---|---|---|---|
| 1 | RTO / COD management | 465 | **Critical** | 35–40% RTO rates; ₹180–240 cost per failed COD; 142-brand benchmark |
| 2 | Refund management (merchant-side) | 391 | **Critical** | Refunds delayed weeks; manual approvals; bank chargebacks pile up |
| 3 | Failed-payment recovery | 287 | **High** | 20-25% payments fail; half won't return without nudge (Razorpay) |
| 4 | Disputes / chargebacks | 242 | **High** | UPI chargebacks "most complicated"; manual evidence pulling |
| 5 | Workflow automation gap | 176 | **High** | Founders running 8 disconnected apps, "nothing talks to each other" |
| 6 | Fee / invoice chasing | 172 | **High** | Agencies, EdTech, SMBs floating payroll waiting for client/student fees |
| 7 | Reconciliation across rails | 87 | **High** | 3+ hours/week even at small scale; 50K txns/day at large |
| 8 | WhatsApp + payment flow | 70 | **Medium-High** | 95%+ open rates vs 15% email; 60% recovery uplift documented |
| 9 | Settlement / payout opacity | 44 | **High** | Merchants discover missing payouts only by manual checking |
| 10 | Subscription dunning / autopay fail | 23 | **Medium** | Shopify+Appstle subs failing silently with vague reasons |

## 30+ Verbatim Quotes (with sources, persona-tagged)

### Refund management (merchant-side pain)

1. **D2C / Cashfree:** *"Without any prior notice, Cashfree has stopped working… we've already lost almost 30 orders because of this."* (PissedConsumer, 1.0★, 2024-12-24)
2. **D2C / Cashfree:** *"Worst customer service, no human POC for queries. I've been trying to whitelist a domain for a week, but it's not happening."* (PissedConsumer, 1.0★, 2024-11-16)
3. **D2C / Razorpay:** *"Following up for months, but I have not received the refund."* — Usha_Rani, ₹7,299 stuck (consumercomplaints.in, 2025-08-01)
4. **D2C / Razorpay:** *"We immediately initiated a refund through Razorpay"* — then customer filed cyber-crime complaint instead. (r/StartUpIndia, score 24, gifting brand Vishal)
5. **D2C / Shopify:** *"Be sure to check your payouts for missing payments… an order from the 16th still did not have a pending payout."* (r/shopify)

### Reconciliation pain

6. **SMB / India:** *"Dealing with messy payment reconciliation… UPI/transfers, names don't match customer names, no clear reference, partial payments, split payments."* (r/IndiaBusiness, score 6, PAIN)
7. **D2C / Multi-channel:** *"Tracking which channel is actually profitable is becoming a nightmare… I have to manually pull reports from each platform then match them up with bank deposits and it takes me like three hours every week."* (r/ecommerce, score 57, D2C)
8. **SaaS-Agency / India:** *"Your team is matching ten thousand UPI transactions against gateway reports, NEFT narrations are cryptic, Razorpay settled yesterday but the bank credit shows tomorrow, the CFO wants books closed by the 3rd."* (aiaccountant.com)

### RTO / COD pain

9. **D2C / Streetwear / India:** *"We stopped COD after massive RTO losses, now orders have almost died."* (r/MarketingMentor, score 7, D2C, FEATURE-REQUEST + PAIN)
10. **D2C / Shiprocket:** *"I'm losing money due to fake RTO & weight discrepancies. Tried Delhivery, Bluedart, Shiprocket — each disappointing… RTO literally eats my margins alive."* (r/ecommerce, score 5, PAIN)
11. **D2C / Shopify+Shiprocket:** *"Our brand's customer data is being leaked, and delivery guys are calling them to pay for orders which are already prepaid and COD too."* (r/developersIndia, 261, D2C)
12. **D2C blog data:** *"Indian D2C brands that implement WhatsApp COD confirmation see RTO rates drop from 30-35% to 18-22% within the first month."* (CampaignHQ)

### Settlement / payout pain (Razorpay)

13. **Razorpay:** *"Razorpay held my fund however they are deducting commission."* (consumercomplaints.in, 2024-12-04)
14. **Razorpay:** *"It's been 6 months now, nothing has been credited."* (Ankush768, consumercomplaints.in, 2024-03-03)
15. **Razorpay / Director Marketing:** *"They suddenly block the service… contradictory mails, one saying approved one saying blocked. 120-day settlement hold."* (Capterra 1.0, Navin D., 2020)
16. **Razorpay / Manager:** *"Hold payments without reason. Then, they waste time on emails and calls."* (Capterra 1.0, PRAKASH R., 2024-12)
17. **Razorpay / IT Founder:** *"Support says 30 mins response time but they never reply."* (Capterra 2.0, Amit P., 2024-07)
18. **Razorpay / CEO Transport:** *"They cheated in the name of pricing plan… still they are charging."* (Capterra 1.0, Vikas S., 2024-09)

### Failed payment recovery / abandoned cart

19. **D2C blog:** *"20-25% of payments fail due to avoidable reasons, and half of those customers wouldn't return without a nudge."* (Razorpay blog)
20. **D2C / India:** *"65-80% of online shopping carts abandoned before checkout… WhatsApp open rates exceed 95%."* (Hillteck/Shopify 2026 guide)
21. **D2C / Pune supplement brand:** *"Increased cart recovery rate from 3.8% to 17.2% after switching from email to WhatsApp."* (CampaignHQ 2026)

### Fee chasing / dunning

22. **SaaS-Agency / Bangalore:** *"Right now I have 6 invoices pending. Total outstanding: ₹3.4L. Oldest one is from 67 days ago. The client still replies to my messages but never the invoice."* (r/indianstartups, score 34, FEATURE-REQUEST + PAIN)
23. **Dev agency:** *"I'm refreshing my bank account waiting for a client payment that's 3 months late so I can make payroll."* (r/Entrepreneur, score 143, SaaS-Agency)
24. **EdTech blog:** *"Institutes using WhatsApp fee reminders report 85% on-time fee collection rates, up from 55-60%."* (CampaignHQ)
25. **D2C / Shopify Subs:** *"Most of our recurring orders were failing… 'error processing payment'… error message just says 'card does not support this type of purchase'."* (r/shopify Appstle subs)

### Workflow / automation gap (Relay's exact wedge)

26. **Razorpay merchant:** *"I spoke to 20 young founders this week and the average was 8 different apps. WhatsApp for customers, Excel for money, Canva for design, Linktree for bio, Razorpay for payments, Notion for tasks… Nothing talks to each other. Everything is manual."* (r/indianstartups, score 18, Razorpay-mention)
27. **SaaS-Agency:** *"We are paying for 23 separate software subscriptions… [we] just did our annual software audit and the number genuinely startled me."* (r/Entrepreneur, score 618)
28. **D2C / India:** *"Half of [foreign tools] don't support COD properly… I've been running a small D2C brand for about a year now."* (r/IndiaBusiness, score 26)
29. **Cashfree mention / EdTech fee dispute:** *"I made a payment through Zuel Pay for an education fee using my credit card to bank, amounting to 14,799… raised a dispute, and the merchant even accepted it. But the merchant's account is negative…"* (r/CreditCardsIndia, score 21, CASHFREE-MENTION)
30. **D2C founder:** *"Our prepaid card setup has been giving us problems, POS failures in smaller towns, KYC delays for new hires."* (r/IndiaBusiness, score 21, Lending)
31. **B2B SaaS:** *"Running a B2B SaaS product and getting hit with subscription chargebacks… Current process is manually pulling login data, feature usage, support tickets, everything. Takes forever and we're only winning about 45%."* (r/SaaS, dunning)
32. **D2C blog:** *Workaround built — Pabbly Connect template explicitly: 'Recover Razorpay Cart Abandonment Payment Failed - Send WhatsApp Messages to Customers.'* (Pabbly templates page — proof workflow demand exists today)
33. **Cashfree merchant:** *"None of your numbers are contactable."* (PissedConsumer, 1.0★, 2025-09-04)
34. **Cashfree integration:** *"We once had an issue with almost 40% of transactions failing, and the support we received wasn't that helpful."* (SoftwareSuggest, BytePhase T., D2C/WooCommerce)

## Featurebase top-asked features

**Could not pull voted list (auth-walled).** Ram's Slack references (WhatsApp payment links, refund automation, EdTech fee reminders, Shopify+WhatsApp integration) align tightly with Reddit signal volume above. **Action: pull voted Featurebase list internally before launch deck finalises.**

## Razorpay merchant complaints Cashfree could win on

- Settlement holds (120 days, often 6+ months) — 5 verbatim Capterra/consumercomplaints quotes
- Support 30-min SLA broken — 3 Capterra reviews
- Pricing opacity / silent fee creep — 2 Capterra
- Account blocks without explanation — 4 across sources
- "Failed Payment Recovery" exists but is sold as standalone feature, not part of a workflow — opening for Relay positioning

## Cashfree merchant complaints Relay could solve

- "No human POC", "numbers not contactable" → HITL approval flow gives merchants a Slack/Gmail audit trail without depending on support
- "Cashfree stopped working without notice" → automated failover/notification workflow
- 40% transaction-fail support incidents → automated retry + WhatsApp recovery flow
- Domain whitelisting takes a week → workflow request automation
- Forex 2% markup, currency support gap → not Relay-solvable, separate roadmap

## Use Case Validation (agreed list)

| Use Case | Pain signals | Top quote | Persona | Recommended priority |
|---|---|---|---|---|
| Refund approval HITL (Slack/Gmail) | **391 + 11 PissedConsumer + 19 Razorpay complaints = 421** | *"Following up for months, but I have not received the refund"* (₹7,299) | D2C, lending | **P0** — strongest pain across all sources |
| Settlement → Google Sheet | 87 recon + 44 settlement + 18 manual-recon = **149** | *"I have to manually pull reports from each platform then match them up… three hours every week"* | D2C multi-channel, finance ops | **P0** — universal pain, low build complexity |
| Payment failed → WhatsApp recovery | 287 payment-recovery + 70 WhatsApp-flow = **357** | *"20-25% of payments fail… half wouldn't return without a nudge"* (Razorpay's own blog) | D2C, EdTech, subs | **P0** — Razorpay sells this standalone, Relay can wrap it as workflow |
| Abandoned cart → Bolna AI call → Slack | 287 (overlap with above) | *"Pune supplement brand — recovery 3.8% → 17.2% switching to WhatsApp"* | D2C | **P1** — Bolna AI call is differentiator vs WhatsApp-only |
| Academic institutions: scheduled fee reminders | 50 EdTech persona + 172 fee-collection = **222** | *"Institutes using WhatsApp fee reminders report 85% on-time collection, up from 55-60%"* | EdTech, coaching | **P0** for EdTech vertical |
| Cohorts → Google Ads sync | **<10 direct signals in this corpus** | (none clean) | Marketing-led D2C | **P2** — weakest evidence, deprioritise for launch |

## Features NOT in agreed list with stronger demand than "Cohorts → Google Ads"

1. **RTO/COD prevention workflow** (465 signals) — WhatsApp confirmation flow before fulfilment + Slack alert. **Strongest single signal in the corpus.** Strong P0 candidate.
2. **B2B invoice/dunning automation for agencies** (172 signals) — clients 67-90 days late, founders floating payroll. Recurring payment-link reminders + Slack escalation.
3. **Settlement-anomaly Slack alert** (44 signals) — "you've got an unexpected hold" / "payout amount is wrong." Currently merchants discover this manually.
4. **Subscription-failure investigation workflow** (Shopify+Appstle dunning thread) — automatic reason classification + customer outreach.
5. **Multi-channel revenue dashboard** (3+ hour weekly pain across Amazon/Shopify/bank) — auto-recon to Sheet.

**Recommendation:** Replace "Cohorts → Google Ads sync" in the launch lineup with **RTO/COD-prevention WhatsApp confirmation workflow**. It's the single largest pain bucket (465 signals) and maps cleanly onto Cashfree-native PG + WhatsApp flow.

## Sources

- [Razorpay complaints, consumercomplaints.in](https://www.consumercomplaints.in/razorpay-b115695)
- [Cashfree reviews, PissedConsumer](https://cashfree-payments.pissedconsumer.com/review.html)
- [Razorpay reviews, Capterra](https://www.capterra.com/p/179263/Razorpay/reviews/)
- [Cashfree reviews, SoftwareSuggest](https://www.softwaresuggest.com/cashfree)
- [The Hidden Truth About CashFree, FinQfy](https://finqfy.com/the-hidden-truth-about-cashfree/)
- [Razorpay Failed Payment Recovery blog](https://razorpay.com/blog/razorpay-failed-payment-recovery/)
- [WhatsApp abandoned cart for Shopify, Hillteck 2026](https://www.hillteck.com/blog/recover-abandoned-carts-whatsapp-shopify.html)
- [WhatsApp + Email Automation for Coaching Institutes India 2026, CampaignHQ](https://blog.campaignhq.co/coaching-institutes-whatsapp-email-automation-india)
- [Reduce RTO in Ecommerce 2026, HillTeck](https://www.hillteck.com/blog/reduce-rto-ecommerce-india.html)
- [Pabbly Razorpay Cart Abandonment Recovery template](https://www.pabbly.com/recover-razorpay-cart-abandonment-payment-failed-send-whatsapp-messages-to-customers-with-pabbly-connect/)
- [Best Payment Reconciliation India 2026, AI Accountant](https://www.aiaccountant.com/blog/payment-reconciliation-platform-india-2025)
- [India D2C Report April 2026, Unicommerce](https://unicommerce.com/india-d2c-report-2026-april/)
- [Razorpay Review 2026, ProductGrowth](https://productgrowth.in/tools/payments/razorpay/)
