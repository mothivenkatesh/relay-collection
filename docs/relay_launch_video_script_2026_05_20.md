# Cashfree Relay — Launch Video Script
**Date:** 2026-05-20
**Context:** Written in reference to Justpay (Breeze Automatic) product launch video as visual/narrative benchmark.

---

## Reference: Justpay "Automatic" Video Analysis

**Product:** Breeze Automatic by Justpay — AI analytics sidekick for D2C merchants.
**Target:** D2C founders/merchants (direct buyer, non-technical)
**Format:** Two-voice conversation (merchant + AI), floating questions opening, humorous insight moment, quick demo, tagline close.

**What works:**
- "47 times before breakfast" is the insight — not a joke, an observation about real behaviour
- Two distinct personalities: anxious founder vs calm AI
- Questions floating in space = cognitive overload made visual
- Demo is casual, fast, confident — never a feature list

**Overlap with Relay:** Same buyer anxiety (merchant obsessively tracking payments/data), different product layer (Justpay = analytics/intelligence; Relay = automation/action).

---

## Relay Target Audience (Confirmed)

- **Who builds it:** Developers who set up Cashfree PG links, payment events, webhook logic
- **Who benefits:** Business/growth/revenue heads at ecommerce/D2C companies
- **The dynamic:** Developer sets it up once → business outcome runs continuously

---

## Final Script — Developer builds it, Business benefits

### OPENING — The Slack Thread That Never Ends

**[VISUAL: Slack messages floating in, all from business/growth/ops side to the developer]**

Floating text:
- *"Can you add a WhatsApp message when payment fails?"*
- *"Marketing wants a Slack ping for every ₹1L+ transaction"*
- *"How long to build a COD confirmation flow?"*
- *"Settlement recon is still manual — can we automate it?"*
- *"The recovery sequence broke in prod again"*

---

### ACT 1 — The Setup

**Voice 1 (Developer — composed, not complaining):**
Every payment event has a business ask attached to it.
A failure? That's a recovery sequence.
A big ticket? That's a finance alert.
A COD? That's a confirmation flow.

Each one is straightforward to build.
Once.
The second time, it's maintenance.
The tenth time, it's your entire week.

**Voice 2 (Relay):**
Build it once. Own it forever.

---

### ACT 2 — The Insight Moment

**[VISUAL: Large highlight card — orange or purple]**

**Voice 1:**
*"Is it normal that failed payment recovery is a campaign your marketing team runs manually... every Monday morning?"*

**Voice 2:**
No. That's just what happens before the payment events are connected.

---

### ACT 3 — Use Cases as the Demo

**[VISUAL: Payment event fires → chain of actions auto-triggers → business outcome appears on screen as a result panel]**

---

**Use Case 1 — Failed Payment Recovery**

**Voice 1:** Payment fails on checkout.

**Voice 2:** WhatsApp recovery goes out in 15 minutes. Gmail backup at 2 hours. Ops alert on Slack if unpaid by end of day.

**[VISUAL OUTCOME CARD: "₹2.3L recovered this week. Zero manual follow-ups."]**

---

**Use Case 2 — COD Confirmation**

**Voice 1:** COD order placed.

**Voice 2:** Confirmation sent immediately. 4-hour nudge if no response. RTO flag raised before dispatch.

**[VISUAL OUTCOME CARD: "RTO rate down 18%. Ops team untouched."]**

---

**Use Case 3 — High-Value Transaction Alert**

**Voice 1:** ₹1.5L payment just came in.

**Voice 2:** Finance got the Slack ping. Sheets row appended. 40 seconds ago.

**[VISUAL OUTCOME CARD: "Revenue head sees it in real time. No morning report needed."]**

---

**Use Case 4 — Settlement Recon**

**Voice 1:** Daily settlement done.

**Voice 2:** Zoho synced. Sheets updated. Every line item. No cron job needed.

**[VISUAL OUTCOME CARD: "3 hours of manual finance work. Now 0."]**

---

### ACT 4 — The Close

**Voice 1:**
You set up the trigger once.
Your growth team sees recovered revenue.
Your ops team sees fewer RTOs.
Your finance head sees live settlement data.

**Voice 2:**
And you stop maintaining webhook handlers for requests that come in on Slack.

**Voice 1:**
Describe the workflow. Relay builds it.
Payment event fires. The business outcome happens.

**Voice 2:**
That's it.

---

### TAGLINE FRAME

**[VISUAL: Dark. Clean. Cashfree wordmark + Relay.]**

```
Cashfree Relay.
You set it up once.
The business runs on it.
```

*Free in beta. Start building at cashfree.com/relay*

---

## Visual Beat Map (for storyboard)

| Beat | Visual | Duration |
|---|---|---|
| 1 | Floating Slack messages from business to developer, staggered fade-in | 8s |
| 2 | Messages crowd the frame — chaos peak | 3s |
| 3 | Clean cut. "Relay" wordmark enters | 2s |
| 4 | **Highlight card: "Is it normal that recovery is a Monday morning campaign?"** | 4s |
| 5 | Payment event fires → action chain → outcome card (x4 use cases) | 16s |
| 6 | "40 seconds ago" — freeze on finance ping notification | 2s |
| 7 | "3 hours of manual finance work. Now 0." — outcome card hold | 3s |
| 8 | Close dialogue — two voices, alternating | 6s |
| 9 | Tagline. Dark frame. Wordmark. | 4s |

**Total runtime estimate: ~50s**

---

## Structural Logic

The Justpay video had one person talking to an AI.
This one has a **handoff built into every use case** — developer triggers → business outcome appears as a result card.

That visual beat (trigger → outcome card) is the differentiator from a generic automation demo.

**The floating Slack messages in the opening are the real insight:**
Every payment event is already a pending business ask sitting in someone's inbox.
Relay closes the loop without the developer being the loop.

---

## Earlier Draft — Ops Lead Persona (archived)

*Written before audience was confirmed as developers + business heads. Kept for reference.*

### Floating chaos (ops version)
- "Why didn't the COD confirmation go out?"
- "Which orders failed payment this week?"
- "Can someone chase the ₹2.3L settlement?"
- "Dev is busy. Can you handle the WhatsApp sequence?"
- "The Zapier flow broke again."

### Insight line (ops version)
> *"Is it normal that our failed-payment recovery workflow is a Slack message that says... 'please check'?"*
> "That's not a workflow. That's a prayer."

### Tagline (ops version)
> Cashfree Relay. Every payment event. Automated.

---

## What Changed Across Versions

| Element | Ops version | Dev/PM version | Final (Dev builds, Biz benefits) |
|---|---|---|---|
| Opening chaos | Slack "please check" | Jira tickets, GitHub issues | Slack asks FROM biz TO developer |
| Insight line | "prayer" | "Jira ticket for Slack alert" | "Monday morning campaign" |
| Demo structure | Feature walkthrough | MCP mode shown | Use case → outcome card |
| Payoff | "what ops should always be" | "finish the actual sprint" | "You set it up once. Business runs on it." |
| Tone | Relief | Respect | Hero handoff |
