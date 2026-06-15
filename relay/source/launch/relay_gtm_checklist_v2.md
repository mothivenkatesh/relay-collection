# Cashfree Relay — GTM Checklist v2
**Owner:** Mothi Venkatesh
**Last updated:** 2026-05-13
**Sources:** Cashien AI GTM (internal template) · Relay Positioning Doc · MStack DevRel Playbook (27 skills)
**Status:** `[ ]` Not started · `[~]` In progress · `[x]` Done · `[!]` Blocked

---

## WAVE 1 TARGETS (Public Preview → end May)

| # | Goal | Owner | Tracking |
|---|---|---|---|
| 1 | 100 merchants running ≥1 workflow | Mothi | Internal dashboard |
| 2 | 1,000 MCP installs | Satyam | Directory analytics |
| 3 | 500 Agent Skills installs | Satyam / Saksham | npm downloads |
| 4 | 3 merchant case studies | Mothi | — |
| 5 | 5 directory listings live | Satyam | Manual check |
| 6 | 30%+ organic Discord joins (no outreach) | Mothi | Discord analytics |

---

## DEVELOPER GTM FUNNEL (from DevRel Playbook Skill 27)
Every activity below maps to one of these 8 stages:

```
NEED → DISCOVER → JOIN → UNBLOCK → BUILD → GO LIVE → GROW → ADVOCATE
```

---

## 1. SOCIAL MEDIA

| Activity | Timeline | POC | Funnel Stage | Status |
|---|---|---|---|---|
| Leadership endorsement — Ram LinkedIn post | Week 3 | Mothi writes, Ram posts | DISCOVER | [ ] |
| Leadership endorsement — Reeju LinkedIn post | Week 3 | Mothi writes, Reeju approves | DISCOVER | [ ] |
| Launch video — 60–90 sec (LinkedIn native) | Week 3 | Aakanksha + Mothi | DISCOVER | [ ] |
| LinkedIn article — "Introducing Cashfree Relay" | Launch day | Mothi | DISCOVER | [ ] |
| "What is Relay" carousel — 5 slides | Week 3 | Mothi + designer | DISCOVER | [ ] |
| Template demo posts — 1 per template (4 posts) | Weeks 3–6 | Mothi | DISCOVER | [ ] |
| Build-in-public clips (Aakanksha series) | Weekly | Aakanksha | DISCOVER | [ ] |
| Bolna partner spotlight post | After webinar | Mothi | DISCOVER | [ ] |
| Event teaser — June closed-room | Week 5 | Mothi | DISCOVER | [ ] |
| Post-event recap | Post June event | Aakanksha + Mothi | ADVOCATE | [ ] |

**Notes:**
- Stagger leadership posts by 24–48 hours — don't fire same day
- All posts posted natively on LinkedIn (no YouTube links)
- All posts approved before scheduling — no surprises on positioning
- Don't lead with "AI" — lead with merchant outcome (DevRel Principle: technical value > marketing)

---

## 2. COMMS — NEW MERCHANTS

| Activity | Timeline | POC | Funnel Stage | Status |
|---|---|---|---|---|
| Relay block in activation/onboarding email | 20th May | Vijay / CRM team | DISCOVER | [ ] |
| Relay mention in tech support docs shared to new merchants | 20th May | Shanth | DISCOVER | [ ] |
| Dashboard notification — "New: Automate with Relay" | May 13–27 | Subbu / Hari | DISCOVER | [ ] |
| Pulse app push notification (2 A/B variants) | Week 3 | App team | DISCOVER | [ ] |

**Notes:**
- Dashboard notification gated behind `relay_enabled` unleash flag — cohort rollout
- Pulse: segment to merchants >50 txn/month (ops-pain audience)
- Onboarding email placement: after first payment received (merchant has context)
- A/B test: developer framing vs. operator framing

---

## 3. COMMS — EXISTING MERCHANTS

| Activity | Timeline | POC | Funnel Stage | Status |
|---|---|---|---|---|
| Email to all merchants using integrated APIs | Week 4 | Vijay / CRM | DISCOVER | [ ] |
| Developer-specific email — MCP angle + npx CTA | Week 4 | Mothi + CRM | DISCOVER | [ ] |
| MoEngage monthly newsletter block (150 words, 1 CTA) | Lock slot this week | PMM / CRM | DISCOVER | [ ] |

**Notes:**
- Developer segment: merchants with active API keys
- MoEngage slot fills up — lock with PMM this week
- Subject line test: *"Your Cashfree now works inside Claude and ChatGPT"* vs. *"Automate payment ops — no code"*

---

## 4. PRODUCT-LEVEL INCLUSIONS

| Activity | Timeline | POC | Funnel Stage | Status |
|---|---|---|---|---|
| Day-0 onboarding flow — Relay card on dashboard home | 13th May | Subbu / Hari | DISCOVER | [ ] |
| In-product Relay page (4 templates + MCP CTA) | Week 2 | Subbu / Hari | DISCOVER → JOIN | [ ] |
| DevStudio / developer portal inclusion | 16th May | Shubhi / Mothi | DISCOVER | [ ] |
| Help docs live (Overview, Create, Connections, Manage) | 13th May | Shanth | UNBLOCK | [ ] |
| MCP install guide (Claude Desktop + Cursor) | Week 2 | Satyam + Shanth | JOIN → BUILD | [ ] |
| Skills install guide (`npx @cashfreepayments/agent-skills`) | Week 2 | Satyam / Saksham | JOIN → BUILD | [ ] |
| Discord server — #relay channel + pinned thread | 7th May | Mothi + Raj | JOIN → UNBLOCK | [~] |
| Link from API docs → "Automate this with Relay" | Week 3 | Shanth | DISCOVER | [ ] |

**Notes (from DevRel Playbook Skill 27):**
- New Discord members need 3 meaningful interactions within 48 hours or they ghost
- Sub-4-hour response time in #relay-support (Cashfree engineer present, not just community)
- "Tribal knowledge" answers — things not in the docs — are what keep developers returning
- Discord-exclusive: early access to 1 upcoming template (COD confirmation) for members who activate a workflow

---

## 5. VIDEO

| Activity | Timeline | POC | Funnel Stage | Status |
|---|---|---|---|---|
| Launch video — 60–90 sec hero (timer, prompt, output, done) | Week 2 | Aakanksha + Mothi | DISCOVER | [ ] |
| How-to video — 4–5 min YouTube walkthrough | 15th May | Mothi / Vinesh + Aakanksha | UNBLOCK → BUILD | [ ] |
| BTS Ep 1 — "What we're building and why" | Week 3 | Aakanksha + Mothi | DISCOVER | [ ] |
| BTS Ep 2 — "How the MCP works" | Week 3 | Aakanksha + Satyam | DISCOVER | [ ] |
| BTS Ep 3 — "Building cart abandonment workflow live" | Week 4 | Aakanksha + Vinesh | BUILD | [ ] |
| BTS Ep 4 — "What beta merchants told us" | Week 5 | Aakanksha + Mothi | ADVOCATE | [ ] |
| BTS Ep 5 — Closed-room event recap | Post June event | Aakanksha | ADVOCATE | [ ] |

**Launch video script (from Relay positioning doc):**
- Timer running top-right corner
- Open Claude → voice prompt the use case
- MCP starts responding → workflow generated → link shown
- Show workflow visually → click Test Run
- No setup / installation screens — start at the output moment

**How-to video structure:**
- 00:00 What Relay is and why it matters
- 00:30 4 template walkthroughs (screen + commentary)
- 03:00 MCP install + first workflow in Claude live
- 04:00 What's coming (Bolna voice, COD confirmation)
- 04:30 CTA: install + join Discord

---

## 6. BLOG

| Post | Timing | POC | Funnel Stage |
|---|---|---|---|
| *"Introducing Cashfree Relay: Agentic payment operations for India"* | Launch day | Mothi → Shritama → Ram | DISCOVER |
| *"How Cashfree Relay works: an MCP server for UPI, settlements, and refunds"* | Launch day | Mothi / Satyam | UNBLOCK |
| *"Relay Payment Guardrails: what Relay will and won't do autonomously"* | Launch day | Mothi / Vinesh | UNBLOCK |
| *"How Cashfree teams use Relay internally"* | Day 7 | Mothi | DISCOVER |
| *"How [Design Partner X] cut payment integration time with Relay"* | Day 14 | Mothi `[→ needs case study merchant]` | ADVOCATE |
| *"Cashfree Relay is now a one-click extension for Claude and Codex"* | Day 21 | Mothi / Satyam | DISCOVER |
| *"How to recover abandoned carts with an AI voice call (Relay + Bolna)"* | Post webinar | Mothi | BUILD |

**Production process:** Mothi drafts → PMM (Shritama / Priyam) edits → Ram approves → publish
**Repurpose every blog:** 1 LinkedIn carousel + 1 short video clip + 1 Discord thread

Checklist:
- [ ] Launch day blogs (3) — written and approved before launch
- [ ] Day 7–21 blogs — drafted in Week 2–3
- [ ] Bolna blog — drafted after webinar date confirmed

---

## 7. DOGFOODING (DevRel Playbook Skill 8)

> *"Use your product as community infrastructure."* — Cashien AI hit 25 installs pre-launch. Same bar for Relay.

| Activity | Timeline | POC | Status |
|---|---|---|---|
| All Cashfree devs install MCP + Agent Skills | Week 1 | Raj + Mothi | [ ] |
| Internal Slack post: step-by-step install guide | Week 1 | Mothi | [ ] |
| Internal "show and tell" — team demos first Relay workflow | Week 2 | Mothi | [ ] |
| Collect internal feedback — bugs, UX friction, confusing copy | Week 1–2 | Vinesh | [ ] |
| Fix critical issues before public launch | Week 2 | Vinesh | [ ] |
| Target: 25 internal installs before external launch | Week 2 | Raj | [ ] |

---

## 8. PR & THOUGHT LEADERSHIP

| Activity | Timeline | POC | Status |
|---|---|---|---|
| Product description (1 para) approved for press | Week 2 | PMM comms | [ ] |
| CTO / Ram interview pitch — "Why MCP-first, not dashboard-first" | Week 3 | Comms team | [ ] |
| Razorpay counter-narrative — arm Ram / Reeju for interviews | Week 2 | Mothi | [ ] |
| Embargo brief to 1–2 journalists (YourStory, Inc42, AIM) | Week 5 | Comms | [ ] |

---

## 9. DEVELOPER COMMUNITY (DevRel Playbook — Seeding Phase)

### Super Fan Identification (Skill 1)
- [ ] Search Twitter, YouTube, Reddit for organic Cashfree developer mentions `POC: Mothi`
- [ ] Identify top 20 developers already using Cashfree APIs extensively
- [ ] Score by: engagement level + audience size + creative product usage
- [ ] Personalized 1:1 outreach to top candidates — not a blast

### Ambassador Program (Skill 2)
- [ ] Invite top 10–15 super fans to private #ambassador channel in Discord
- [ ] Give them early access to upcoming templates (COD, Bolna, reconciliation)
- [ ] Offer: direct team access + founder AMA + early feature access + public recognition
- [ ] Open applications to broader audience after seed group is active
- [ ] Target: 50+ ambassadors by Month 6 (from DevRel playbook metric)

### Community Seeding (Skill 11 — 3-month nurture)
- [ ] HN Show HN post on launch day — *"Show HN: We built an MCP server for Indian payments"* `9 AM IST`
- [ ] Reddit: r/ChatGPTCoding, r/ClaudeAI, r/developersIndia, r/fintech
- [ ] Dev.to / Hashnode: technical deep-dive on MCP architecture `POC: Satyam / Vinesh`
- [ ] Developer newsletter mentions: TLDR, ThisWeekInIndie, ByteByteGo India
- [ ] Partner co-announcements: Bolna (post webinar), Sarvam (post confirmation)
- [ ] Target 5 Indian tech creators — send free access, no pitch for 3 months (Skill 11)

### MCP Directory Submissions (high-leverage, zero cost)
- [ ] Claude MCP directory (Anthropic) `POC: Satyam`
- [ ] ChatGPT plugin store `[!] needs Plus/Pro subscription`
- [ ] Cursor directory `POC: Satyam`
- [ ] Gemini tool marketplace `POC: Saksham`
- [ ] 2 long-tail AI tool directories

### Developer Feedback Loop (Skill 13 — Measurement)
- [ ] GitHub repo issues open for MCP feedback `POC: Vinesh / Satyam`
- [ ] Discord #relay-feedback channel — weekly digest to product team
- [ ] Office hours / AMA: 30-min weekly session in Discord for Wave 1 `POC: Mothi / Vinesh`
- [ ] Feedback → changelog visible in docs + Discord weekly update

---

## 10. LANDING PAGE

| Item | Owner | Status |
|---|---|---|
| Copy doc (hero, 3-surface, templates, FAQs) | Mothi | [ ] |
| PMM review (Shritama / Priyam) | PMM | [ ] |
| Ram approval | Ram | [ ] |
| Design brief to designer | Mothi | [ ] |
| Dev build from `relay/source/cashfree-relay-landing-v2.html` | Dev | [ ] |
| Mobile responsive + UTM analytics | Dev | [ ] |
| Launch video embedded | Dev | [ ] |
| 4 template cards with demo GIFs | Designer | [ ] |
| Connector logo strip (11 live + coming soon) | Designer | [ ] |
| Partner page CTA → `cashfree.com/relay/partners` | Dev | [ ] |
| Beta label on (remove at GA) | Dev | [ ] |

**Landing page sections (from positioning doc):**
1. Hero — headline + `npx` CTA + hero illustration
2. Embedded launch video
3. How it works — MCP / Skills / Workflow Builder
4. 4 template cards with demo GIFs
5. 3 value pillars (agent-native / India-first / secure by design)
6. Connector logos strip
7. Social proof
8. FAQ
9. Partner CTA

**Partner page:** `cashfree.com/relay/partners`
- [ ] "Build on Relay. Reach 8L+ merchants."
- [ ] 3 tiers: Connector / Featured / Launch Partner
- [ ] Typeform intake

---

## 11. EVENTS

### Bolna LinkedIn Live Webinar
- [~] Outreach drafted `2026-05-13`
- [ ] Outreach sent + Bolna confirms
- [ ] Date locked `[!] blocked on call completion webhook — Karthik/Ishaan ETA?`
- [ ] Co-branded banner + LinkedIn event page created
- [ ] Speakers: Mothi (or Vinesh) + Bolna rep
- [ ] Demo rehearsed + backup recording ready
- [ ] Promotion: company pages + Discord + MoEngage D2C segment
- [ ] Post-webinar: recording, blog, follow-up email, case study

### Closed-Room Merchant Event — June 1st Week (Skill 4 — Event Strategy)
> *"Community-organized beats company-organized"* — but for v1, run it yourself to control quality.

- [ ] Merchant list confirmed (15–20) `[→ Gopi dashboard pull]`
- [ ] Date + venue locked, Ram sign-off
- [ ] 1:1 personal invites — not mass email
- [ ] Min 10 RSVPs before locking venue
- [ ] Relay in prod for live demos
- [ ] Agenda: welcome + demo (20 min) + hands-on (30 min) + Bolna spot (15 min) + open conversation (20 min)
- [ ] Aakanksha filming BTS for Episode 5
- [ ] Feedback form same evening (3 questions max)
- [ ] Post-event: thank-you notes (1:1, same day), 2–3 merchant quotes, Episode 5 posted within 3 days

---

## 12. TIERED LAUNCH SEQUENCE

```
Reeju (private 1-pager briefing)
      ↓
Ram + Leadership (live demo session)
      ↓
Team (internal Slack + "what NOT to say" FAQ + demo recording)
      ↓
Sales / BD enablement (3 talking points + Razorpay objection handler)
      ↓
PR (embargo brief → 2 journalists)
      ↓
Influencers / builders (Discord, HN, Reddit, creators)
      ↓
Full external launch
```

- [ ] Reeju 1-pager ready and briefing done
- [ ] Ram demo session done + positioning approved
- [ ] Internal FAQ + "what NOT to say" doc circulated
- [ ] BD 3-point cheat sheet + objection handler vs. Razorpay
- [ ] PR embargo sent
- [ ] Seeded: Discord + HN + Reddit + 5 creators

---

## 13. PARTNER OUTREACH

| Partner | Category | Status | Use Case | Next Step |
|---|---|---|---|---|
| **Bolna** | Voice AI | [~] Outreach drafted | Cart abandonment voice call | Send today, lock webinar date |
| **Sarvam** | Voice AI | [~] Outreach drafted | Voice AI connector | Find DevRel contact, send |
| Govardhan | L1/L2/L3 partners | [ ] | Launch partners | Connect with Govardhan |
| Interakt / AiSensy | WhatsApp BSP | [ ] | Abandoned cart | — |
| Shiprocket / Delhivery | Logistics | [ ] | COD confirmation + RTO | — |
| Shopify India | E-commerce | [ ] | E-commerce trigger | — |
| Zoho CRM | CRM | [ ] | CRM connector | — |
| n8n | No-code | [ ] | Plugin listing | — |

---

## MEASUREMENT DASHBOARD (DevRel Playbook Skill 13 + Skill 27)

| Funnel Stage | Metric | Current | Wave 1 Target |
|---|---|---|---|
| DISCOVER | Landing page visits | — | Track from Day 1 |
| DISCOVER | Directory listing submissions | 0 | 5 |
| JOIN | MCP installs | 0 | 1,000 |
| JOIN | Skills installs | 0 | 500 |
| JOIN | New Discord members/month | ~60 | 500+ |
| ACTIVATE | Discord members posting within 48hrs | ~10% | 30% |
| UNBLOCK | Avg response time in #relay-support | Not tracked | <4 hours |
| BUILD | Merchants with ≥1 workflow live | 0 | 100 |
| GO LIVE | Discord → MTU attribution | Not tracked | Track |
| GROW | Workflows per active merchant (month 1) | 0 | 3 |
| ADVOCATE | Case studies published | 0 | 3 |
| ADVOCATE | Organic Discord joins (no outreach) | ~0% | 30% |
| PARTNER | Partner page enquiries | 0 | 5+ |

---

## SEQUENCING

```
Week 1 (now)     Merchant list. Bolna outreach sent. Dogfooding starts (25 installs).
                 Positioning locked with Ram. Reeju briefing.
Week 2           Design brief + landing page copy. MCP submissions filed.
                 Help docs drafted. Dogfooding feedback loop.
Week 3           Landing page live (beta). Launch video done.
                 BTS Ep 1–2. Discord #relay live + pinned thread.
                 Super fan identification starts.
Week 4           Bolna webinar (LinkedIn Live). Social launch posts go live.
                 Onboarding email inclusion. Dashboard notification.
                 How-to video on YouTube.
Week 5           Partner page live. Merchant 1:1 invites sent (June event).
                 MoEngage newsletter. BTS Ep 3–4.
                 PR embargo to journalists.
Week 6 (June 1) Closed-room merchant event.
                 Tiered launch: Reeju → Ram → Team → PR → influencers.
Post-event       Ep 5 posted. Case studies drafted. HN / Reddit seeded.
                 Ambassador program opens. Creator outreach (3-month nurture begins).
                 Wave 2 planning.
```

---

## REFERENCE DOCS

| Doc | Path |
|---|---|
| Cashien AI GTM (internal template) | `relay/docs/cashien-ai-gtm-reference.md` |
| MStack DevRel Playbook (27 skills) | `github.com/mothivenkatesh/MStack` |
| Relay Positioning & GTM WIP | `relay/docs/relay-positioning-gtm-wip.md` |
| Relay Product Note | `relay/docs/relay-product-note.md` |
| Slack log Apr 28–May 6 | `relay/docs/slack-log-wf-discussion-apr28-may6.md` |
| Previous checklist | `relay/launch/relay-launch-checklist.md` |
