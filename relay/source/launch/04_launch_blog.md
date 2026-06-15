# Launch Blog — Cashfree Relay (Private Beta announcement)

> Audience: Cashfree merchants (founders, ops/finance/growth managers).
> Goal: drive private beta applications + position the category.
> Length target: ~900 words. Reading time: 4 min.
> Tone: confident, specific, no marketing fluff.

---

# Introducing Relay: automation that speaks payments

**TL;DR** — Relay is a no-code workflow automation platform built right into the Cashfree dashboard. It turns every payment, refund, and dispute event into a trigger you can connect to Slack, Sheets, Gmail, WhatsApp, and more — without writing code or hiring a developer. Today we're opening private beta to 50 select merchants. [Apply here](https://cashfree.com/relay).

---

## The problem nobody admits to

Talk to any ops manager at a D2C brand and ask what they did yesterday afternoon. The honest answer:

- Forwarded refund confirmations to 12 customers
- Updated a spreadsheet with the day's failed payments
- Pinged Slack manually because someone's chargeback hit
- Messaged 20 customers on WhatsApp who'd dropped checkout

This is unglamorous, repetitive work. It's also what holds the business together. And it scales linearly with order volume — the very thing every founder is trying to grow.

Most teams know they should automate this. Most don't, because the alternatives all have a catch:

- **Zapier or Make:** powerful, but you need a developer to wire up webhooks, parse JSON payloads, handle auth tokens, and maintain the integration when something changes. Three weeks of engineering for an invoice email.
- **Custom scripts:** brittle. The dev who built it leaves, and now nobody can change anything.
- **Doing it manually:** what most merchants land on, by default.

We watched this pattern play out across thousands of Cashfree merchants. So we built a third option.

---

## Meet Relay

**Relay is the automation layer built into Cashfree.** Pick a payment event. Pick what should happen. Done.

It looks like this:

> **WHEN** a customer's payment fails
> **DO** post in #ops Slack + send a WhatsApp retry link to the customer

That's a workflow. You build it once in the Cashfree dashboard, and it runs forever — every time a payment fails, no developer required.

### What's in the box

**9 native payment triggers:**
- Payment Success / Failed / Dropped
- Refund Success / Cancelled / Auto-Refund Success
- Dispute Created / Updated / Closed

**1 schedule trigger:**
- Simple Schedule — repeating intervals (no cron syntax, just pick "every 4 hours")

**10 connectors + an HTTP escape hatch:**
- Google Sheets, Slack, Gmail, WhatsApp Business, Calendly, Google Calendar, Zoho Invoice
- Google Gemini and OpenAI (for AI-powered messages, summaries, triage)
- Cashfree Payments (refund, payment link, cashgram)
- HTTP Request node — hit any REST API for everything else

---

## Why "payments-native" matters

If you've used Zapier, you know the drill: paste a webhook URL into Cashfree, write a parser, map every field, set up auth, test it, deploy it, fix it when something breaks.

Relay skips all of that. Payment events are **typed** — they show up in the dropdown the moment you turn Relay on. Cashfree owns the integration end-to-end, so when our APIs change, your workflows don't break. You don't think in webhooks. You think in business events.

This is the same shift that made **Shopify Flow** so sticky for e-commerce sellers, and **HubSpot Workflows** so sticky for marketing teams. The native version of a workflow tool, built by the platform you already use, beats the bolt-on every time — for the 80% of workflows that don't need custom logic.

---

## What our beta merchants are building

We've been quietly testing Relay with a handful of design partners over the past few months. Here's what they're running today:

**A subscription SaaS company** runs an automation that catches every failed payment, posts a Slack alert to their CS channel with the customer's contact info, and emails the customer a one-click retry link via Gmail — within 30 seconds of the failure. Their CS lead estimates this saves 6 hours a week and recovers about 40% of failed renewals that used to silently churn.

**A D2C apparel brand** runs a dropped-checkout recovery workflow. Every time a customer abandons checkout, Relay sends them a WhatsApp Business message with the cart link and a small discount code — all without a marketing automation tool. They're seeing 5–7% recovery on dropped checkouts, which translates to a meaningful chunk of monthly revenue.

**An ed-tech founder** runs a payment-success workflow that pushes a Zoho Invoice automatically, drops a row in their student tracker Sheet, and sends a Calendly link for the student's first session — all in one workflow. The founder used to do all three steps manually for every enrollment.

What's notable: none of these merchants wrote a single line of code. None of them had a developer set this up.

---

## What's not in private beta (yet)

We're being deliberate about scope. Things that aren't ready today:

- **Ready-to-use templates.** Right now you build workflows from scratch — we'll co-build the first 3 with you during beta. The template library lands before public beta, sourced from what beta merchants build.
- **CRM, accounting, e-commerce connectors.** Tally, HubSpot, Shopify, QuickBooks — coming in the next few months.
- **Subscription, payout, KYC event triggers.** Beta covers core payment lifecycle. More triggers expand surface at GA.
- **Conditional branching, error-recovery UX.** Today's workflows are linear. Visual branching is on the roadmap.

---

## Who Relay is for

Relay is built for the merchant who's already on Cashfree and feels like 30% of their week is repetitive payment ops. If you're:
- A D2C founder watching ops manually email refund confirmations
- A finance manager copy-pasting payment data into Tally every evening
- A growth manager whose dropped-checkout recovery is "I'll get to it when I have time"
- A SaaS ops lead whose churn is partly self-inflicted because failed payments don't trigger anything automatically

…Relay was built for you.

---

## How to get in

Private beta is invite-only. We're onboarding ~50 merchants over the next 4 weeks, with a CSM and a Solution Engineer to co-build your first workflows. Free during private beta — pricing tiers will land at GA.

**Apply here:** [cashfree.com/relay](https://cashfree.com/relay)

If you're already a Cashfree merchant, your application gets fast-tracked. We'll get back to you within 5 working days.

We're building Relay alongside our merchants. Your feedback shapes which connectors we ship, which templates we build, and how we price. If you've got a workflow you've been wanting to automate for months — let's build it together.

---

*— The Cashfree Relay team*
