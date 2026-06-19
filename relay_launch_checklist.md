# Cashfree Relay — Launch GTM Checklist
**Owner:** Mothi Venkatesh (Developer Tool GTM)
**Last updated:** 2026-05-13
**Status legend:** `[ ]` Not started · `[~]` In progress · `[x]` Done · `[!]` Blocked

**Stakeholders:** Shritama, Priyam, Kumar Anubhav, Harshit Pai, Satyam, Shanth
**Final approvers:** Ram, Mayank
**Tiered launch sequence:** Reeju → Ram & Leadership → Team → PR → Influencers

---

## WAVE 1 GOALS (Public Preview, now → end May)
- [ ] 100 merchants running ≥1 workflow
- [ ] 1,000 MCP installs across directories
- [ ] 500 Agent Skills installs
- [ ] 3 merchant case studies with quantified outcomes
- [ ] 5 host-directory listings live

---

## PHASE 0 — Foundation
> Everything else is blocked until these are done.

### Selective Merchant List
- [ ] Define criteria: active merchant (>100 txn/month), ops-heavy, segments — D2C / NBFC / EdTech / B2B SaaS
- [ ] Pull list from Gopi (dashboard access + segment filter)
- [ ] Target: 15–20 for closed-room event, 100 for Wave 1 outreach
- [ ] Ram sign-off on final list
- [ ] Personal 1:1 invite to each — not mass email

### Product Brief & Positioning Lock
- [ ] Core narrative agreed: *"Your payments stack, now inside the AI tools you already use"*
- [ ] 3 messaging pillars confirmed (ref: `relay/docs/relay-positioning-gtm-wip.md`):
  - Agent-native, not dashboard-bolted-on
  - India-first templates (RTO, COD, refunds, recon — solved day 1)
  - Secure by design — PCI/SOC perimeter, HITL on every irreversible action
- [ ] "What NOT to say" doc signed off:
  - Don't call it "workflow tool" or "Zapier for payments"
  - Don't call it "Claude plugin" or "AI feature"
  - Don't promise full autonomy on refunds/payouts
  - Don't lead with "AI" — lead with merchant outcome
- [ ] Ram + Reeju sign-off before any design or copy starts

---

## PHASE 1 — Design

### Design Brief (Mothi → Designer)
- [ ] Write brief: developer-first tone, Stripe/Swiggy MCP aesthetic, not AI-washed
- [ ] Screens needed: landing page, partner page, social templates, event invite, email header
- [ ] Share `relay/mockups/relay-product-mockups.html` as reference
- [ ] Designer assigned and briefed

### Relay Public Landing Page
**URL:** `cashfree.com/relay` or `relay.cashfree.com`

**Sections (from positioning doc):**
- [ ] **Hero** — headline + sub-text + CTA (`npx` install command) + hero illustration
- [ ] **Launch video** (embedded — see Phase 2)
- [ ] **How it works** — 3 surfaces: Cashfree MCP / Agent Skills / Relay Workflow Builder
- [ ] **4 template cards** — each with demo GIF + one-click CTA
- [ ] **Connector logos strip** — 11 live + "coming soon" row (Shopify, Tally, CRM)
- [ ] **Value props** — 3 pillars (agent-native / India-first / secure by design)
- [ ] **Social proof** — merchant quote or "500+ on waitlist"
- [ ] **FAQ** — 5 Qs (What is MCP? Do I need to code? Data safe? Which AI tools? How to access?)
- [ ] Copy doc written by Mothi, reviewed by PMM (Shritama / Priyam)
- [ ] Dev build (start from `relay/source/cashfree-relay-landing-v2.html`)
- [ ] Mobile responsive + analytics (UTM: utm_source=relay-landing)
- [ ] Beta label for Wave 1, removed at GA

### Partner / Connector Page
**URL:** `cashfree.com/relay/partners`
- [ ] Hero: "Build on Relay. Reach 8L+ merchants."
- [ ] 3 partner tiers: Connector / Featured / Launch Partner
- [ ] 11 live connectors as proof
- [ ] Partner intake form (Typeform) — company, contact, API docs, use case
- [ ] Bolna + Sarvam placeholders as "Featured Partners" (pending confirmation)

### In-Product — Merchant Dashboard
- [ ] Banner on dashboard home → CTA to Relay in-product page
- [ ] In-product Relay page: what it is + 4 template cards + MCP install CTA
- [ ] Dashboard notification: contextual nudge after payment events
- [ ] Coordinate with Subbu / Hari for placement + `relay_enabled` unleash flag rollout
- [ ] UTM: utm_source=dashboard

---

## PHASE 2 — Content & Social

### Demo Video
**Script (from positioning doc — keep it tight):**
- [ ] Run a timer top-right corner
- [ ] Open Claude, voice-prompt the use case
- [ ] MCP responds → workflow gets generated → link shown
- [ ] Show workflow visually → click Test Run
- [ ] No showing MCP upload, Agent Skills setup, etc. — just the output moment
- [ ] Length: 60–90 seconds max
- [ ] Aakanksha to produce, Mothi / Vinesh on screen
- [ ] Ready before landing page goes live

### Build-in-Public Video Series (with Aakanksha)
**Narrative:** The team building India's payments AI layer. Honest, builder-credible, not a product ad.

- [ ] Brief Aakanksha: tone = raw + honest, not polished ad
- [ ] Shoot schedule agreed before June 1st week
- [ ] **Episode 1** — "What we're building and why" (Mothi or Vinesh, 90 sec)
- [ ] **Episode 2** — "How the MCP works" (screen + voiceover walkthrough)
- [ ] **Episode 3** — "Building the cart abandonment workflow live" (raw screen + commentary)
- [ ] **Episode 4** — "What merchants told us in beta" (2–3 quotes, minimal editing)
- [ ] **Episode 5** — Closed-room event recap (shoot at event, post within 3 days)
- [ ] All episodes distributed: LinkedIn native video (primary) + Cashfree Discord

### Blogs
**Launch-day (3):**
- [ ] *"Introducing Cashfree Relay: Agentic payment operations for India"*
- [ ] *"How Cashfree Relay works: an MCP server for UPI, settlements, and refunds"*
- [ ] *"Relay Payment Guardrails: what Relay will and won't do autonomously"*

**Day 1–30 (3):**
- [ ] *"How Cashfree teams use Relay"*
- [ ] *"How [Design Partner X] cut payment integration time from 2 weeks to 4 minutes"*
- [ ] *"Cashfree Relay is now a one-click extension for Claude and Codex"*

All blogs: Mothi drafts → PMM edits → Ram approves before publish

### Social Media Brief
- [ ] Write social brief: builder-first tone, show don't describe, no AI hype
- [ ] Content calendar: 2 posts/week launch week, 1/week ongoing
- [ ] All posts approved before scheduling

**Post types needed:**
- [ ] Launch announcement (Cashfree company LinkedIn)
- [ ] "What is Relay" carousel — 5 slides, developer-friendly
- [ ] Template demo post — 1 per template (4 posts)
- [ ] BTS / build-in-public posts (from Aakanksha's series)
- [ ] Partner spotlight — Bolna (post after webinar date locked)
- [ ] Event teaser (closed-room, June 1st week)
- [ ] Post-event recap

### Merchant-Facing Channel Copy
- [ ] **Pulse app** — push notification copy (2 variants A/B); deep link to Relay
- [ ] **Dashboard notification** — contextual nudge after payment events
- [ ] **MoEngage newsletter** — 150-word block, 1 image, 1 CTA; coordinate with CRM team for slot
- [ ] **Discord #announcements** — longer, more technical; pin getting-started thread
- [ ] All copy reviewed by PMM before scheduling

---

## PHASE 3 — Webinar (Bolna LinkedIn Live)
**Use case:** Cart abandonment — Payment Dropped → Bolna AI voice call → payment link recovery

### Coordination
- [~] Outreach drafted to Bolna (2026-05-13)
- [ ] Outreach sent + Bolna confirms
- [ ] Date locked (target: 2 weeks before June closed-room event)
- [ ] Speakers: 1 Cashfree (Mothi or Vinesh) + 1 Bolna
- [ ] LinkedIn Live access confirmed on both company pages

### Demo Readiness
- [ ] End-to-end demo built: Payment Dropped → Bolna call → recovery link
- [ ] **Call completion report webhook gap resolved** (Karthik/Ishaan — known blocker as of May 13) `[!]`
- [ ] Demo rehearsed once minimum
- [ ] Recorded backup ready in case live demo breaks

### Webinar Outline (45 min)
- [ ] 5 min — Intros + Indian D2C cart abandonment problem
- [ ] 15 min — Live demo: build workflow in Relay, trigger Bolna call
- [ ] 10 min — Discussion: what merchants can expect, setup time, cost
- [ ] 10 min — Q&A
- [ ] 5 min — How to get started + CTAs

### Promotion
- [ ] Co-branded banner (Cashfree + Bolna)
- [ ] LinkedIn event page created
- [ ] Announcement posts — both company pages (1 week before)
- [ ] Mothi personal post + Discord + MoEngage blast (D2C / COD merchants)
- [ ] Reminder: 3 days before + day of

### Post-Webinar
- [ ] Recording clipped + posted on both LinkedIn pages (within 24 hours)
- [ ] Follow-up email to attendees — template + install link
- [ ] Blog: *"How to recover abandoned carts with an AI voice call (Relay + Bolna)"*
- [ ] Add as case study on partner page

---

## PHASE 4 — June 1st Week: Closed-Room Event
**Format:** In-person, invite-only, 15–20 merchants, Bangalore
**Goal:** 10+ merchants activate ≥1 Relay workflow live in the room

### Setup
- [ ] Date confirmed — first week of June (lock with Ram)
- [ ] Venue confirmed (Cashfree office or external)
- [ ] Relay working in prod / near-prod for live demos
- [ ] Laptops / tablets for hands-on section

### Agenda
- [ ] Welcome + what's new at Cashfree (15 min)
- [ ] Relay demo — 4 live templates (20 min)
- [ ] Hands-on: merchants build first workflow (30 min)
- [ ] Partner spotlight: Bolna demo (15 min)
- [ ] Open conversation: what would you build next? (20 min)
- [ ] Networking close

### Invites
- [ ] Final merchant list approved (Phase 0)
- [ ] Personal 1:1 invite sent to each merchant
- [ ] RSVPs tracked — min 10 confirmed before locking venue
- [ ] Confirmation + agenda sent 48 hours before

### On the Day
- [ ] Aakanksha capturing BTS (video + photos) for Episode 5
- [ ] Feedback form sent same evening (3 questions max)

### Post-Event
- [ ] Thank-you note to each attendee (same day, 1:1)
- [ ] Feedback summarised → Vinesh + Ram
- [ ] Episode 5 BTS video posted within 3 days
- [ ] 2–3 merchant quotes collected (with permission) for landing page + social
- [ ] Check who activated a workflow within 7 days of event

---

## PHASE 5 — MCP Directory Submissions
> Start now. No dependency on anything else.

- [ ] Submit to Claude MCP directory (Anthropic)
- [ ] Submit to ChatGPT plugin store (Satyam — needs Plus/Pro)
- [ ] Submit to Cursor directory
- [ ] Submit to Gemini tool marketplace (check if open)
- [ ] 2 long-tail AI tool directories (TBD)

---

## PHASE 6 — Tiered Launch Announcement
**Sequence: Reeju → Ram & Leadership → Team → PR → Influencers**

- [ ] **Reeju** — private briefing (1-pager: current state, Wave 1 metrics, what changes)
- [ ] **Ram + Leadership** — demo session before any external announcement
- [ ] **Team** — internal Slack + demo recording + FAQ + "what NOT to say" doc
- [ ] **Sales enablement** — 3 talking points, 1 objection handler (vs Razorpay Agent Studio), demo link
- [ ] **PR** — 1-para product description approved; embargo to YourStory, Inc42, AIM
- [ ] **Influencers / builders** — Discord, HN Show HN, Reddit (r/ChatGPTCoding, r/ClaudeAI, r/developersIndia)

---

## Partner Outreach Tracker

| Partner | Status | Use case | Next step |
|---|---|---|---|
| **Bolna** | [~] Outreach drafted | Cart abandonment voice call | Send message, confirm webinar |
| **Sarvam** | [~] Outreach drafted | Voice AI connector | Find DevRel contact, send |
| Govardhan's partners | [ ] | Launch partners (L1/L2/L3) | Connect with Govardhan |
| Interakt / AiSensy | [ ] | WhatsApp BSP | — |
| Shiprocket / Delhivery | [ ] | COD confirmation + RTO | — |
| Shopify India | [ ] | E-commerce trigger | — |
| Zoho CRM | [ ] | CRM connector | — |
| n8n | [ ] | Plugin listing | — |

---

## Launch Metrics

| Metric | Wave 1 Target | Tracking |
|---|---|---|
| Merchants with ≥1 workflow live | 100 | Internal dashboard |
| MCP installs | 1,000 | Directory analytics |
| Skills installs | 500 | npm download count |
| Directory listings live | 5 | Manual check |
| Case studies published | 3 | — |
| Closed-room attendees | 15–20 | RSVP tracker |
| Merchants activating at event | 10+ | Live tracking |
| Webinar registrations | 200+ | LinkedIn event |
| Partner enquiries | 5+ | Typeform |

---

## Sequencing

```
Now (Week 1)     Merchant list. Bolna outreach sent. Positioning locked with Ram.
Week 2           Design brief out. Landing page copy written. MCP submissions filed.
Week 3           Landing page live (beta). Demo video done. BTS filming starts (Eps 1–2).
Week 4           Bolna webinar (LinkedIn Live). Social goes live. Discord announcement.
                 In-product dashboard page + Pulse notification.
Week 5           Partner page live. Merchant invites sent. MoEngage newsletter slot locked.
Week 6 (June 1) Closed-room merchant event. Tiered launch: Reeju → Ram → Team → PR.
Post-event       Episode 5 posted. Follow-up. Case studies drafted. Wave 2 planning.
```

---

## Reference Docs
- Positioning & GTM WIP: `relay/docs/relay-positioning-gtm-wip.md`
- Product note (full): `relay/docs/relay-product-note.md`
- Vinesh Q&A: `relay/docs/relay-product-note-vinesh-qa.md`
- Slack log (Apr 28–May 6): `relay/docs/slack-log-wf-discussion-apr28-may6.md`
- Existing landing page: `relay/source/cashfree-relay-landing-v2.html`
