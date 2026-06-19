# Positioning & Messaging — Cashfree Relay

> Frameworks: April Dunford "Obviously Awesome" + FletchPMM Positioning Anchors + Atlassian Message House.

---

## 1. Positioning Statement (Dunford canvas)

| Element | Relay |
|---|---|
| **Competitive alternatives** | (1) Manual ops work in spreadsheets/email, (2) Generic automation tools (Zapier, Make, n8n) glued via webhooks, (3) Custom-built scripts maintained by a developer |
| **Unique attributes** | Native, typed payment events (no webhooks); built into Cashfree dashboard; AI connectors out-of-box; no cron syntax; HTTP escape hatch |
| **Value (and proof)** | Workflow setup time drops from days to minutes; ops staff (not devs) can build and maintain automations; no integration drift |
| **Target market** | Indian SMB merchants on Cashfree (5–200 employees), with an ops/finance/growth manager owning daily payment ops |
| **Market category** | **Payments-native workflow automation** (new category — borrows credibility from "embedded automation in vertical SaaS" — Shopify Flow, HubSpot Workflows, Stripe Workflows) |

### One-line positioning
> **Relay is the no-code automation built into Cashfree — turn every payment, refund, and dispute event into business actions, without writing a single line of code.**

---

## 2. Category Frame

**Don't say:** "Cashfree's Zapier" — anchors to a generic competitor and undersells the wedge.

**Do say:** "Payments-native workflow automation."

**Why this matters:** Generic horizontal automation forces merchants to think in webhooks and APIs. Payments-native means the *primitives are payment events*. The category Relay creates is closer to **Shopify Flow** (e-commerce-native automation that won the Shopify ecosystem) than to Zapier.

---

## 3. Message House (Atlassian model)

```
                    ROOFLINE (one-line promise)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       Turn payment events into business actions — no code,
                  no developers, no waiting.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
   │   PILLAR 1      │  │   PILLAR 2      │  │   PILLAR 3      │
   │  PAYMENTS-      │  │  BUILT FOR      │  │   AI-READY      │
   │   NATIVE        │  │     OPS         │  │                 │
   │                 │  │                 │  │                 │
   │ 9 typed events. │  │ No cron. No     │  │ Gemini + OpenAI │
   │ Zero webhook    │  │ webhooks. No    │  │ as connectors.  │
   │ setup. No       │  │ developer       │  │ Smart messages, │
   │ payload         │  │ tickets.        │  │ smart triage,   │
   │ mapping.        │  │                 │  │ smart summaries.│
   └─────────────────┘  └─────────────────┘  └─────────────────┘

      FOUNDATION: Hosted by Cashfree. Your payment data stays inside
      the same RBI/PCI-DSS-compliant infrastructure. OAuth-only for
      third-party connectors.
```

---

## 4. Audience-specific value props (FletchPMM anchors)

### A. Founder / CEO of D2C or SMB
> **"Stop paying a developer to send invoices."**
- Anchor: cost of ops + cost of integration drift
- Proof point: "Beta merchants replaced ₹6K/mo Zapier + freelancer setups in one afternoon."

### B. Ops / Finance Manager
> **"The payment workflows you keep doing by hand — automated in 10 minutes."**
- Anchor: time + repetitive work
- Proof point: "Refund confirmations now go out in 30 seconds, not 1 hour."

### C. Growth / Marketing Manager
> **"Recover dropped checkouts and failed payments with WhatsApp, automatically."**
- Anchor: revenue recovery
- Proof point: "Merchants recovering 3–8% of dropped checkouts via auto-WhatsApp retry."

### D. Developer / CTO
> **"You shouldn't be writing Zapier zaps for payment events. We built the integration so you don't have to."**
- Anchor: engineering opportunity cost
- Proof point: "Native triggers replace webhook + parser + retry-handler boilerplate."

---

## 5. Headline & Tagline Bank

**Primary tagline (recommended):**
> **Automation that speaks payments.**

**Backup taglines:**
- Turn payment events into business actions.
- Your payments, on autopilot.
- From transaction to action — without writing code.
- The automation layer for Indian merchants.

**Hero headlines (for landing page A/B testing):**
- "Every payment event is a workflow you don't have to build."
- "9 payment triggers. 10 connectors. 0 code."
- "Your ops team can finally automate Cashfree — without IT."
- "What used to need a developer + Zapier + 3 webhooks now takes 3 clicks."

**Sub-headlines:**
- "Built into Cashfree. No setup, no webhooks, no developer tickets."
- "Trigger Slack alerts, send invoices, recover checkouts, log refunds — automatically."

---

## 6. Proof Points (FAB framework — Feature → Advantage → Benefit)

| Feature | Advantage | Benefit |
|---|---|---|
| 9 typed payment triggers | No webhook setup, no payload mapping | Setup in minutes vs days |
| Built into Cashfree dashboard | Same login, same access controls | Zero onboarding friction |
| Gemini + OpenAI as connectors | LLM-powered messages, summaries, triage | Workflows that "think" — not just trigger |
| HTTP request node | Hit any REST API | Power user escape hatch |
| Simple Schedule (no cron) | Drop-down intervals | Anyone can build periodic workflows |
| WhatsApp Business connector | Direct retry/recovery messages | 3–8% revenue recovery, no SMS provider needed |
| OAuth-only third-party auth | No tokens floating around | Security team sign-off in days, not weeks |

---

## 7. Common objections & responses

| Objection | Response |
|---|---|
| "We already use Zapier." | Zapier costs ₹2K+/mo and needs a developer to wire payment webhooks. Relay is built-in, free during beta, and ships payment events as typed triggers. Most beta merchants kept Zapier for non-payment workflows and moved payment ones to Relay. |
| "Will this work for my volume?" | Beta covers up to 100K events/month per merchant. GA tiers will scale beyond. |
| "What if Cashfree goes down?" | Workflows queue and retry; no event lost. Same SLA as the payments core. |
| "I don't trust AI for customer messages." | AI connectors are optional. Use them for drafting, keep human approval before send. |
| "What about my custom Tally integration?" | HTTP request node + Schedule trigger lets you push data to any system on a schedule. CRM/Tally native connectors on GA roadmap. |
| "Razorpay does this too, right?" | No. As of [launch date], no Indian payment processor offers native, no-code workflow automation with payment events as typed triggers. |

---

## 8. What Relay is NOT (positioning guardrails)

- **Not a Zapier replacement.** It's a Cashfree-native automation layer. Use Zapier for non-payment workflows.
- **Not an iPaaS for enterprises.** Mid-market and enterprise should stay on MuleSoft/Workato.
- **Not an AI agent platform.** Today, LLMs are connectors inside workflows, not autonomous agents. (That's v2.)
- **Not a payments analytics tool.** Relay automates *actions*; analytics stay in the Cashfree dashboard.
- **Not a developer SDK.** Devs can use webhooks + APIs directly. Relay is for non-devs.
