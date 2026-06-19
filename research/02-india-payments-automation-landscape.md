# 02 — India Payments + Automation Landscape

**Run:** 2026-04-29 · **Window:** Q1 2026 · **Scope:** Indian payments competitors with automation/MCP plays · **Method:** WebSearch + targeted WebFetch on vendor press, blogs, reviews

---

## 1. Razorpay — the elephant in the room (already shipped)

**This is Relay's single biggest GTM risk.** Razorpay launched **Agent Studio** at FTX 2026 (March 11-12), built on **Anthropic's Claude Agent SDK** — the same substrate Cashfree Relay sits on. Eight prebuilt agents launched: Dispute Responder, Subscription Recovery (with ElevenLabs voice), two Abandoned Cart Conversion variants (SuperU + Nugget by Zomato), Cashflow Forecaster, RTO Shield, RTO Insights, Settlement Insights ([Razorpay blog](https://razorpay.com/blog/agent-studio-ai-agents-by-razorpay/), [Tribune India](https://www.tribuneindia.com/news/business/razorpay-unveils-worlds-first-agent-studio-to-automate-payments-launches-agentic-experience-platform/)).

Their Agentic Experience Platform reduces merchant onboarding from 30-45 minutes to ~5 minutes, and the Agentic Dashboard accepts natural-language commands ([The Paypers](https://thepaypers.com/payments/news/razorpay-launches-ai-agent-studio-and-agentic-experience-platform)). Inc42 framed it as **"Razorpay repositioning from payments provider to AI-powered business operating system"** ([Inc42 feature](https://inc42.com/features/razorpays-biggest-bet-from-payments-to-becoming-the-ai-brain-for-indias-small-businesses/)) — exactly the narrative Relay needs.

Separately, **RazorpayX Source-to-Pay** has shipped procurement/AP automation since 2024 (3-way matching, TDS auto-deduct, approval routing, Tally/Zoho integration) ([G2 reviews](https://www.g2.com/products/razorpayx-source-to-pay/reviews); [RazorpayX site](https://razorpay.com/x/)). And **Magic Checkout** has its own RTO Shield + Dynamic COD AI ([Magic page](https://razorpay.com/magic/)).

**Implication for Relay:** the "automation bundled with payments" narrative is *taken*. Cashfree must differentiate on (a) builder/composability vs. fixed agent SKUs, (b) non-checkout use cases (refund approvals, settlement→Sheets, fee reminders), (c) pricing transparency, or (d) developer ergonomics.

## 2. PayU India / Plural

PayU shipped two AI moves in **April 2026** — directly overlapping the Relay launch window:
- **AI-powered Outbound Voice Call Assistant** for merchant onboarding (Hindi + English, expanding to KYC drop-offs, activations, cross-sell) ([Business Standard](https://www.business-standard.com/content/press-releases-ani/payu-introduces-ai-powered-outbound-voice-call-assistant-bringing-voice-intelligence-to-merchant-onboarding-journey-126041400719_1.html))
- **MCP Server** — conversational automation of payment-link generation, txn status checks via merchant's own AI tool ([IBS Intelligence](https://ibsintelligence.com/ibsi-news/payu-unveils-ai-driven-mcp-server-for-merchant-payment-workflows/))

PayU is positioning itself as "AI-native, merchant-centric" but no full workflow-builder yet. Plural (their B2B PG arm) hasn't surfaced an automation play.

## 3. Decentro, Setu

Both are **infra plays, not workflow plays**. Decentro offers a no-code dashboard layer for stitching banking APIs faster (eNACH + UPI AutoPay just shipped Q1 2026 with YES Bank as launch partner) ([CXO Today](https://cxotoday.com/media-coverage/decentro-simplifies-recurring-payments-with-enach-and-upi-autopay-strengthening-indias-subscription-economy-ropes-in-yes-bank-as-its-first-partner-bank/); [Decentro review](https://productgrowth.in/tools/payments/decentro/)). Setu (acquired by Pine Labs 2022 for $70-75M) is API-only — Aadhaar eSign, BBPS, FASTag ([YourStory](https://yourstory.com/2022/06/pine-labs-acquire-api-fintech-startup-setu-embedded-finance)). **Neither competes with Relay's builder UX.** They are upstream of it.

## 4. Juspay

Pure **payment orchestration** — 300+ PSPs, smart routing, automated reconciliation across processors ([Juspay blog](https://juspay.io/blog/payment-orchestration-boldly-reshaping-the-infrastructure-of-payments)). 95%+ of merchants use rule-based routing. They process $1T annually. But **routing rules ≠ workflow automation** — Juspay automates *the payment*, not the surrounding ops (refund approvals, dunning, post-settlement actions). Hyperswitch (their open-source orchestrator) just expanded to US/EU/UK ([Juspay newsroom](https://juspay.io/newsroom/hyperswitch-by-juspay-world-s-first-open-source-payments-platform-expands-to-the-us)). They became India's first 2025 unicorn at $1B+. **Tangential threat unless they extend into ops automation.**

## 5. Indian no-code automation (Pabbly, n8n, Zapier)

**Pabbly Connect** (Bhopal-based, Magnet Brains): $16/mo for 10K tasks, lifetime deal $249, 2,000+ app integrations, explicitly SMB-focused ([Pabbly site](https://www.pabbly.com/connect/); [Capterra India](https://www.capterra.in/software/205994/pabbly-connect)). **The pricing benchmark Relay must beat or differentiate from on payments-context.**

**n8n** is winning Indian SME share — for 100K monthly ops, Zapier costs ~₹41,500/mo vs. n8n self-hosted free or ~₹1,600/mo cloud. n8n grew mid-market customers 10x YoY, ~80% from Zapier ([Hatchworks](https://hatchworks.com/blog/ai-agents/n8n-vs-zapier/); [Tech Arion](https://techarion.com/blog/n8n-vs-zapier-vs-make-automation-india)). EdTech teams already using n8n for lead handling + course delivery.

**The Relay insight:** Pabbly/n8n/Zapier are generic — they don't know what a "settlement file" or "refund cohort" is. Relay's wedge is **payments-native primitives** that horizontal tools can't match without bolt-ons.

## 6. D2C SaaS players with built-in workflows

- **Shiprocket** — automated order processing, RTO management, returns RMA, COD discouragement engine ([Shiprocket Checkout](https://checkout.shiprocket.in/blog/gokwik-competitors/))
- **GoKwik** — AI/ML risk scoring, RTO reduction, address quality scoring
- **Shopflo** — gamified promos, customizable checkout
- **Razorpay Magic Checkout** — already covered above

These are **vertical-slice automation** (checkout, RTO). None offer cross-flow orchestration. Relay's whitespace: chaining *across* these systems (e.g., GoKwik flag → Cashfree refund hold → WhatsApp confirm).

## 7. Cashfree's own pre-existing automation (internal cannibalization check)

Cashfree already ships:
- **Auto Collect** — virtual accounts auto-reconciling inbound bank transfers ([auto-collect page](https://www.cashfree.com/auto-e-collect/))
- **Payment Link auto-reminders** — max 3 SMS reminders, fixed schedule (1d/2d/3d/7d/14d windows), 12-6 PM only, requires AM activation ([docs](https://www.cashfree.com/docs/payments/no-code/payment-link))
- **Bulk Payouts** + Tally ERP auto-recon — claims 40% manual-effort reduction ([SoftwareSuggest](https://www.softwaresuggest.com/cashfree))
- **Split Payments**, **UPI AutoPay**, **Payment Forms**

**These are point features, not workflows.** Relay's job: surface them as composable nodes inside merchant-defined flows. Internal positioning challenge: don't let RMs or Sales pitch "Auto Collect" when a merchant needs Relay's full canvas.

## 8. Merchant pain points (cited evidence)

**Reconciliation/refund burden:** Settlement files have different formats per channel, different deduction logic, different TCS treatment — at 5,000+ orders/month across 3 channels, spreadsheets break. Ops teams spend **6-7 hours/week** on marketplace reconciliation; CX spends **2 hrs/day** on refund follow-ups ([Pragma blog](https://www.bepragma.ai/blogs/getting-48-57hrs-back-every-week-an-indian-d2c-playbook); [Terra Insight](https://www.terra-insight.com/insights/platform-settlement-reconciliation/)).

**Silent UPI failures:** 2.2-3.4% of UPI payments fail silently; 34 crore monthly UPI txns enter callback grey-zone ([Pragma](https://www.bepragma.ai/blogs/reconciling-failed-payments)). Finance teams unsure whether to auto-cancel or chase — exactly Relay's "payment-failed → WhatsApp recovery" use case.

**EdTech fee chasing:** One test prep platform reduced fee follow-up from "2 people × 3 days/month" to fully automated ([CampaignHQ](https://blog.campaignhq.co/whatsapp-for-edtech-platforms)). WhatsApp open rates >90% for edtech vs. cold calls/email ([Inc42](https://inc42.com/resources/how-indian-edtech-startups-can-use-whatsapp-to-10x-their-business-potential/)).

**Cart recovery proof:** Bolna's voice-AI recovered ₹2.5 Cr+ for Hypothesis (Shopify-first D2C), 500K+ minutes/month ([Bolna case study](https://www.bolna.ai/customer-story/hypothesis)). **Bolna is a partner candidate, not a competitor.**

## 9. Willingness to pay benchmarks

Hard data is thin, but anchors:
- Indian SMBs spend **₹6K-8K/yr** on digital security; medium businesses **₹12K-15K/yr** ([Ken Research](https://www.kenresearch.com/pov/tech-iceberg-india-smb-digital-adoption-insights))
- Tally Cloud ₹2,000/mo, Zoho CRM ₹800/user/mo — these are the SMB price anchors ([Medium overview](https://medium.com/@Anshul-goyal-bminfotrade/top-saas-solutions-for-indian-small-businesses-in-2025-32acefa44c3f))
- Pabbly ₹1,300/mo for 10K tasks — generic-automation floor
- Indian SaaS market projected to hit **$70B by 2030** at ~30% CAGR

**Implication:** Relay should benchmark against ₹999-₹4,999/mo SMB tier, with payments-volume-linked enterprise pricing — not seat-based.

## 10. Press coverage patterns

Razorpay's Agent Studio was covered by Inc42 (multiple features), YourStory (Harshil Mathur interview Feb 2026), MediaNama (critical lens on dark patterns), Outlook Business, BFSI Elets, The Paypers, Tribune ([Inc42 reposition piece](https://inc42.com/features/razorpays-biggest-bet-from-payments-to-becoming-the-ai-brain-for-indias-small-businesses/); [YourStory Harshil interview](https://yourstory.com/2026/02/razorpay-harshil-mathur-ai-bets-ecommerce-conversational-mcp-agentic)). The pattern: **flagship event + Anthropic/AI-leader co-announce + IPO narrative + customer logos** (SuperU, Zomato/Nugget already named). Inc42 AI Summit (May 28, 2026 Bengaluru) and the **Inc42 + Google Bharat AI Startups Report 2026** are the next earned-media windows ([Inc42 AI Summit](https://events.inc42.com/ai-summit/)).

**Relay launch playbook:** name 2-3 marquee D2C/edtech logos, partner co-announce (Bolna for voice, Anthropic if applicable, WhatsApp BSP), pitch a contrarian angle vs. Razorpay's fixed-agent SKU model — "composable workflows merchants own" vs. "agents you rent."

---

## Sources
- [Razorpay Agent Studio blog](https://razorpay.com/blog/agent-studio-ai-agents-by-razorpay/) | [Razorpay Sprint 2026](https://razorpay.com/sprint/26)
- [Tribune — Razorpay Agent Studio launch](https://www.tribuneindia.com/news/business/razorpay-unveils-worlds-first-agent-studio-to-automate-payments-launches-agentic-experience-platform/)
- [The Paypers — Razorpay AI Agent Studio](https://thepaypers.com/payments/news/razorpay-launches-ai-agent-studio-and-agentic-experience-platform)
- [Inc42 — Razorpay's Biggest Bet](https://inc42.com/features/razorpays-biggest-bet-from-payments-to-becoming-the-ai-brain-for-indias-small-businesses/)
- [YourStory — Harshil Mathur on AI commerce](https://yourstory.com/2026/02/razorpay-harshil-mathur-ai-bets-ecommerce-conversational-mcp-agentic)
- [MediaNama — Razorpay Agent Studio risks](https://www.medianama.com/2026/03/223-razorpay-launches-ai-agent-studio-questions-loom-dark-patterns-price-discrimination/)
- [RazorpayX Source-to-Pay G2](https://www.g2.com/products/razorpayx-source-to-pay/reviews) | [Razorpay Magic Checkout](https://razorpay.com/magic/)
- [PayU AI Voice Assistant — Business Standard](https://www.business-standard.com/content/press-releases-ani/payu-introduces-ai-powered-outbound-voice-call-assistant-bringing-voice-intelligence-to-merchant-onboarding-journey-126041400719_1.html)
- [PayU MCP Server — IBS Intelligence](https://ibsintelligence.com/ibsi-news/payu-unveils-ai-driven-mcp-server-for-merchant-payment-workflows/)
- [Decentro review](https://productgrowth.in/tools/payments/decentro/) | [Decentro eNACH+UPI AutoPay](https://cxotoday.com/media-coverage/decentro-simplifies-recurring-payments-with-enach-and-upi-autopay-strengthening-indias-subscription-economy-ropes-in-yes-bank-as-its-first-partner-bank/)
- [Pine Labs acquires Setu — YourStory](https://yourstory.com/2022/06/pine-labs-acquire-api-fintech-startup-setu-embedded-finance)
- [Juspay orchestration blog](https://juspay.io/blog/payment-orchestration-boldly-reshaping-the-infrastructure-of-payments) | [Juspay APAC merchant case](https://juspay.io/blog/why-juspay-is-the-best-payment-orchestration-provider-for-apac-enterprise-merchants-in-2026)
- [Pabbly Connect](https://www.pabbly.com/connect/) | [n8n vs Zapier — Tech Arion](https://techarion.com/blog/n8n-vs-zapier-vs-make-automation-india) | [Hatchworks n8n vs Zapier 2026](https://hatchworks.com/blog/ai-agents/n8n-vs-zapier/)
- [Cashfree Auto Collect](https://www.cashfree.com/auto-e-collect/) | [Cashfree Payment Link docs](https://www.cashfree.com/docs/payments/no-code/payment-link) | [Cashfree review — SoftwareSuggest](https://www.softwaresuggest.com/cashfree)
- [Pragma — Indian D2C playbook](https://www.bepragma.ai/blogs/getting-48-57hrs-back-every-week-an-indian-d2c-playbook) | [Pragma — Reconciling failed payments](https://www.bepragma.ai/blogs/reconciling-failed-payments)
- [CampaignHQ — EdTech WhatsApp fee reminders](https://blog.campaignhq.co/whatsapp-for-edtech-platforms) | [Inc42 — WhatsApp for Indian EdTech](https://inc42.com/resources/how-indian-edtech-startups-can-use-whatsapp-to-10x-their-business-potential/)
- [Bolna AI — Hypothesis case study](https://www.bolna.ai/customer-story/hypothesis)
- [Inc42 Fintech 3.0 2026](https://inc42.com/features/fintech-3-0-2026-preview-indias-digital-payments-ai/) | [Inc42 AI Summit 2026](https://events.inc42.com/ai-summit/)
