# Launch Email Sequences — Cashfree Relay

> 4 emails total: (1) Founder outreach to flagship merchants, (2) CSM outreach to top SMB merchants, (3) Dashboard banner → applicant follow-up, (4) Welcome email after beta acceptance.
> All emails optimized for India SMB merchant tone — direct, concrete, no fluff.

---

## EMAIL 1 — Founder-to-Founder (Reeju → flagship merchants)

**From:** Reeju Datta (Co-founder, Cashfree)
**To:** Top 30 flagship merchant founders
**Subject:** A small thing we built for you
**Send:** Personalized, BCC'd, sent over 3 days from Reeju's actual inbox

---

Hi [Founder first name],

Quick one. We've been building something internally for the past few months called **Relay**, and I want you to be one of the first 50 merchants on it.

In short: it's a no-code automation layer inside Cashfree. You pick a payment event ("payment failed", "refund issued", "dispute created") and pick what should happen ("Slack alert", "WhatsApp the customer", "log to Sheets"). The workflow runs forever after that. No developers, no Zapier, no webhooks.

I'm telling you about it because [Company name] runs the kind of ops volume where a few automations would actually move the needle — not just save time, but recover revenue from dropped checkouts and failed payments.

Beta is free, hands-on (one of our SEs will co-build your first 3 workflows with you), and we'll close the cohort at 50.

If interested, reply with a yes and I'll have the team set you up. If not, no worries — just wanted you to see it first.

Reeju

---

## EMAIL 2 — CSM-to-Ops (sent to existing SMB merchant ops/finance leads)

**From:** [Merchant's CSM]
**To:** Top 200 SMB merchant ops contacts (active in last 90 days)
**Subject:** Stop emailing every refund confirmation manually
**Send:** Personalized hook based on merchant's vertical / volume

---

Hi [Ops manager first name],

You probably saw our team mention this in our last QBR — we've launched **Relay**, a no-code automation built into your Cashfree dashboard, in private beta.

Honestly, the easiest way to explain it is with what your team would actually use it for:

- **Auto-confirm refunds:** When a refund completes, Relay sends a Gmail confirmation to the customer + drops a row in your finance Sheet. You stop doing it manually.
- **Recover dropped checkouts:** When a customer abandons checkout, Relay sends them a WhatsApp message with the cart link. We've seen 5–7% recovery on this with beta merchants.
- **Slack on every dispute:** New chargebacks ping your #ops channel within seconds, with the dispute amount + customer details.

You don't need a developer. You don't need Zapier. You don't need to set up webhooks. It's free during beta.

We're capping the beta at 50 merchants. I've reserved a slot for [Company]. Ready to pick a 30-min call this week to set you up?

[CSM name]
Customer Success, Cashfree Payments

---

## EMAIL 3 — Inbound applicant follow-up (after dashboard banner click)

**From:** Cashfree Relay Team
**To:** Anyone who applies via cashfree.com/relay
**Subject:** Your Relay private beta application — 2 questions before we set you up
**Send:** Within 24 hours of application
**Goal:** Qualify, not gate. Filter out non-fits politely.

---

Hi [First name],

Thanks for applying for the Cashfree Relay private beta. I'm [PMM name], part of the team building Relay.

Two quick questions before we get you set up — should take you 2 minutes:

**1. What's the #1 payment workflow you want to automate first?**
(Examples: send invoice on payment success, recover dropped checkouts via WhatsApp, alert ops on disputes, daily settlement summary, etc.)

**2. What are you using today for payment ops automation, if anything?**
(Examples: Zapier, Make, custom scripts, manual work, Google Sheets gymnastics)

Reply directly to this email. Once we've got your answers, we'll set up a 30-min onboarding call where one of our Solution Engineers will co-build your first workflow with you live.

A heads-up: we're capping private beta at 50 merchants. We're prioritizing merchants who:
- Have at least 3 months of Cashfree payment history
- Have a clear workflow to automate (not "I just want to play around")
- Can give us 30 minutes/week of feedback for the first month

You should hear back from us within 5 working days.

[PMM name]
Cashfree Relay Team

---

## EMAIL 4 — Welcome email (after beta acceptance)

**From:** Cashfree Relay Team
**To:** Accepted beta merchants
**Subject:** Welcome to Cashfree Relay — let's build your first workflow
**Send:** Immediately after acceptance

---

Hi [First name],

You're in. Welcome to the Cashfree Relay private beta.

Here's what happens next:

**Step 1 — Activation (today)**
Relay is now live in your Cashfree dashboard. Log in → look for the "Relay" tab in the left nav. (If you don't see it within 30 minutes, reply to this email.)

**Step 2 — Onboarding call (this week)**
[CSM/SE name] from our team will reach out to schedule a 30-min co-build session. We'll use the workflow you mentioned in your application as the first one we ship together.

**Step 3 — Workflow #2 and #3**
After your first workflow is live, we'll suggest two more based on your business model. Most beta merchants ship 3 workflows in the first 2 weeks.

**Step 4 — Feedback**
We'll add you to our private Slack channel for beta merchants. Drop questions, share workflow ideas, see what other merchants are building.

**A few things to know:**

- **It's free during beta.** No card required, no usage caps for now.
- **You're shaping the product.** The connectors we ship next, the templates we build, the pricing model — your feedback drives all of it.
- **Some things are still rough.** No template gallery yet (we co-build with you), conditional branching coming later, only 10 connectors today. We'll be transparent about gaps.
- **Workflows run on Cashfree's infrastructure.** Same RBI/PCI-DSS compliance as your payments core.

If you have questions before your onboarding call, reply directly to this email or ping us in the beta Slack (link in your dashboard).

Excited to build with you.

[PMM name]
Cashfree Relay Team

---

## Subject line variants (A/B testing bank)

For Email 1 (Founder):
- "A small thing we built for you" *(recommended — soft, founder-to-founder)*
- "Want to be one of the first 50 on this?"
- "Built this with [Company] in mind"

For Email 2 (CSM):
- "Stop emailing every refund confirmation manually" *(recommended — pain anchor)*
- "[Company]'s payment ops, on autopilot"
- "Reserved a beta slot for [Company]"

For Email 3 (Applicant):
- "Your Relay private beta application — 2 questions" *(recommended — clear CTA)*
- "Quick check before we set up your Relay account"
- "Confirming your Relay beta interest"

For Email 4 (Welcome):
- "Welcome to Cashfree Relay — let's build your first workflow" *(recommended — action-oriented)*
- "You're in. Here's what happens next."
- "Welcome to Relay — your first workflow in 30 minutes"
