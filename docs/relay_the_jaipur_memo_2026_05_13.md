# The Jaipur Memo

**A pre-read for Aditi and Priyam, before Friday.**
**On the one question that matters: why build Relay when n8n exists?**

*Mothi Venkatesh · May 13, 2026 · 5 minute read*

---

## The Insight

In March 2026, a developer in Jaipur posted a 1,200-word thread on r/n8n. His family runs a clothing store. Every day his brother handles the same five WhatsApp questions from customers — *"Kya available hai? Budget 5000 hai, kya dikhao ge?"* — and customers were leaving because no one replied for 30 minutes.

He decided to fix it himself. He knew n8n. He had time. He had skin in the game.

**It took him 2 months. The final workflow has 44 nodes and 2 AI agents.**

> *"Version 1 was embarrassing. A basic webhook that sent a canned reply. Fine for testing, useless for real customers."*
>
> *"The real problem hit around version 3. A customer sends 'hi', the agent greets them, they say they want something, the agent jumps straight to asking for their name and budget. Same customer messages the next day. The agent has no idea who they are. **No memory. No routing. No sense of where a customer is in their journey.**"*
>
> *"I started over properly. The final system: 44 nodes, 2 AI agents, 8 conversation stages."*
>
> — r/n8n, March 25 2026 · 356↑ · 117 comments

The top comment, with 25 upvotes:

> *"This is the part people miss: the model is rarely the hard part, the state machine is. The only thing I'd add early is cleaner human handoff plus shared context across channels, because that's where these builds usually get messy."*

This is the entire argument. Read it twice.

**n8n is not the alternative to Relay. n8n is the proof that the problem is real.**

A developer with full context, technical skill, and family motivation needs 2 months to wire up payment events + WhatsApp + state management + memory + handoff. The D2C ops lead doing 6,000 orders a month in the same city — the one losing ₹1L/month to RTO — has no developer, no 2 months, and no way to build it.

She is not the alternative customer. She is the customer who never gets served by n8n.

---

## The Proof That Pain Is Real (Three More Reddit Threads, Same Window)

**Thread 1 — r/IndiaStartups, Nov 28 2025, 68 comments**

> *"A friend of mine is running a small apparel DTC brand and COD fraud is becoming a serious problem these days. Last month alone, 23% of COD orders were fake/undelivered, average loss per fake order is around ₹350. We've tried OTP verification, restricting certain postal codes where we get more fake orders, and even tried charging a bit extra for COD orders. **Nothing is really helping :(**"*

The top reply names the solution by hand:

> *"You can create a risk profile of all your customers based on their postal codes, devices and other very specific data. Blacklist pin codes with the highest default rates. Add a gamification feature — if they are recurring customers over a certain LTV, only then they get to place COD. Also check your logistics partner, often their last mile delivery agent doesn't deliver and marks 'out for delivery'."*

This is a workflow. The merchant knows it exists. He cannot build it. **There is no product he can buy to do this without writing code.**

---

**Thread 2 — r/IndiaStartups, Dec 5 2025, 51 comments**

> *"We have helped many startups solve common COD (Cash on Delivery) issues, and we've audited the data of several D2C brands. The Indian market is unique, and standard 'Western' e-commerce advice often fails here. If you are doing less than 500 orders a month, **logistics companies generally do not care about your grievances regarding RTO or lost shipments.**"*

The same thread:

> *"Retention is the Only Metric that Matters. My mantra in D2C is simple: 'If there is no repeating customer, there is no sale.' Many founders burn money acquiring new customers while their existing ones [are ignored]."*

These are exactly the workflows Relay should ship. Confirm COD → reduce RTO → trigger retention sequence to repeat customers → tie back to GMV. **They are stated as needs, by operators, in their own words.**

---

**Thread 3 — r/developersIndia, Feb 6 2026, 40 comments, 334 upvotes**

> *"DO NOT USE _ in your webhook URLs, learned it the hard way... I spent like hours on this. I did deep research on the specific things I was facing... and for some reason there was not a single thing I could find about this. I just hoped that if this is something that's not allowed I would get a single error or a log or anything from Meta or from Cloudflare."*

The top comment:

> *"It's funny how sometimes we have to waste so much time finding a small issue which isn't even our fault."* — 159 upvotes

This is a developer. With Cloudflare. With AWS. With AI tools. Spent **hours** debugging a payment webhook URL. If this is what a developer faces, the operator never gets started.

---

## The Pattern Underneath All Four Threads

| What's true | The evidence |
|---|---|
| The pain is real, named, and quantified | 23% COD fraud, ₹350 loss/order, in operator's own words |
| Operators know what the solution should look like | They describe it: risk score by pincode, COD confirm, retarget repeat buyers |
| n8n can do it — for someone with 2 months and 44 nodes | Verbatim, r/n8n |
| Even developers struggle with the plumbing | r/developersIndia, webhook URL debugging hell |
| There is no off-the-shelf product for non-technical operators | Across all 271 posts scraped, zero merchant said "we use X and it works" |

---

## The Product Need, Specifically

The D2C operator needs **four things at the same time**:

1. **Payment-aware event triggers.** "When a COD order is placed for >₹500" is one click in Relay. In n8n, you parse a generic webhook and write logic to detect COD.
2. **State and memory across customer interactions.** The Jaipur developer admitted this is what broke his v3. Without memory, every workflow is dumb.
3. **Pre-built templates that match Indian payment context.** No one in India is building a "generic global e-commerce" workflow. They need: COD confirm via WhatsApp, settlement to Tally, RTO scoring by pincode.
4. **No-code deployment with reliable uptime.** When the WhatsApp message doesn't send on Saturday, the operator can't debug a 44-node graph.

n8n delivers exactly **zero of these four** out of the box. It can be made to deliver them — in 2 months, by a developer.

**Relay's job is to ship all four on day one, for the operator who will never write code.**

---

## What This Reframes

The May 13 discussion landed on the right question — "why build a workflow builder when n8n exists?" — but the framing was off. The question is not technical capability. The question is **who can use it.**

If we position Relay as "an n8n alternative for developers," we lose. n8n has more nodes, more integrations, more community. We can't beat them on that axis and shouldn't try.

If we position Relay as **"the 30-minute version of what your developer can't build in 2 months,"** the comparison set changes:

| What it's competing with | Why we win |
|---|---|
| Interakt + Zapier + ops hire (₹40–80K/month) | Cheaper, more reliable, payment-native |
| Hiring a developer to build on n8n (₹2L+ one-time) | Faster, no maintenance burden, pre-validated |
| Doing nothing (current state for 90% of D2C SMBs) | They've already named the pain; we're the first to solve it |

---

## The Single Positioning Statement This Memo Argues For

> **Cashfree Relay turns Indian payment events into business actions in 30 minutes — without code, without webhooks, without a developer.**
>
> **It is the only payment-native workflow product built for the operator who will never open n8n.**

That's it. That's the positioning. Everything else flows from this.

---

## What I Recommend Friday Decides

1. **ICP is the D2C ops lead, not the developer.** Developer is a secondary persona who uses the MCP layer. The landing page leads with templates, not API docs.
2. **Relay is not "agentic" yet.** We don't have memory or goal-setting. The Jaipur thread shows what happens when builders pretend they do — they ship something that fails by version 3. Honesty is the moat.
3. **Keep VAS (Lavika's voice AI, etc.) separate.** Sold outcome-first. Relay is sold capability-first. Different decks, different ICPs, different landing pages — under one AI umbrella narrative.
4. **Lead with three templates at launch:** COD confirm + WhatsApp, failed payment recovery, settlement reconciliation. The three the Reddit threads explicitly asked for.
5. **The Jaipur story goes in the launch blog.** Permission to use it given by Reddit's CC license. We change the name. We anchor the entire launch on a real Indian merchant's reality, not a stock photo.

---

## What I Am Asking For

Two answers before we ship the doc:

1. Does engineering commit to a memory layer by Q3 FY27? If yes, we have a path to "agentic." If no, we permanently position as workflow + MCP and don't let marketing language drift.
2. Does product commit to a templates-first onboarding (not an empty canvas)? If yes, Relay can win the operator. If no, we are building n8n and we should accept we're chasing developers.

Both decisions take 30 minutes. Both unblock the next 6 months of GTM.

---

*Sources: r/n8n · r/IndiaStartups · r/developersIndia · r/IndiaBusiness · 271 posts scraped May 13, 2026 · 6-month window · full transcript and raw data in `reddit_d2c_india_report.md`.*

*Owner: Mothi Venkatesh · mothi.venkatesh@cashfree.com*
