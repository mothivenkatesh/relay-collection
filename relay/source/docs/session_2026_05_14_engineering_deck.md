# Session Log — Engineering Deck + Discovery Brief (May 14, 2026)

**Trigger:** Tuesday call with Aditi + Priyam left positioning unresolved. Slack thread with Vinesh confirmed engine feasibility for memory + LangGraph. Need to (a) build engineering-aligned narrative for what to ship next, (b) lock customer discovery sprint for the next 4 weeks.

**Owner:** Mothi Venkatesh

---

## Output Files

| File | Purpose | Status |
|---|---|---|
| `relay/decks/relay-engineering-deck-v2-2026-05-14.html` | **22-slide engineering deck** · honest assessment + 90-day plan + GFF urgency · written in Mothi's voice · framed through implicit business/ROI lens | Final |
| `relay/decks/relay-customer-discovery-brief-2026-05-14.html` | **16-slide customer discovery brief** · 5 ICPs · 25 calls · 8–10 design partners · 4-week sprint | Final |
| `relay/decks/relay-deck.html` | Original positioning deck (April) | Reference only |

---

## Decisions Reached in This Session

### 1. Relay positioning is locked
> An honest look at what we've shipped, the four gaps that stand between us and the merchants paying for n8n + Interakt + Zapier today, and what the next 12 weeks could earn back.

Drops "agent studio" language until memory ships. Avoids the dark-pattern risk Razorpay is taking. Positions Relay as a foundation that's already valuable — even before Layer 4.

### 2. What Relay *actually* does today (the wedge)
A payment event happens. Something useful happens next. All of it stays inside Cashfree — no exports, no extra tools, no new vendor. This is the only thing Relay does today that nothing else can match, and it's already enough to charge regulated merchants for it.

### 3. The 4 missing pieces (each on top of existing engine)
1. **No memory or goals** — workflows forget everything, can't take "reduce RTO by 20%" as input
2. **No agent packaging** — 4 templates show up as configurable workflows, not products
3. **No outcomes layer** — execution logs only, no business KPI in schema
4. **Wrong connectors for the buyer** — missing Tally, Shopify, AiSensy, Shiprocket

### 4. Five things a real agent platform does (we have 1)
- Goal-driven (we have steps, not goals)
- Memory (workflows forget after each run)
- Dynamic tool selection (channel hardcoded today)
- Self-healing (failed step retries with same params)
- Outcome accountability (we have audit trail = half of this)

Need 4/5 to match Razorpay. Memory + goals + dynamic tools + self-healing.

### 5. 90-day plan to GFF parity
- **Days 0–30** — Foundation polish + repackaging (MCP to prod, Tally/Shopify/AiSensy connectors, repackage 4 templates as named Agents, install card view, KPI schema)
- **Days 30–60** — Agent library + outcomes (ship 4 new agents, 7-day trial activation, KPI dashboard, internal dogfooding)
- **Days 60–90** — Agent brain (LangGraph on Conductor, pgvector memory, goal-setting input, RTO Shield v1 "agentic")

### 6. The 8-agent Cashfree Agent Studio (Day 90 ship)
1. RTO Shield · −10pt RTO in 30 days
2. Failed Payment Rescue · 10–15% recovery in 5 min
3. Cart Recovery · 5–8% drop-to-purchase
4. Refund Triage · −90% cycle time
5. Recon Agent · 95% auto-reconciled
6. KYC Orchestrator · 30 min → 5 min onboarding
7. Subscription Recovery · 15% renewal recovery
8. Dispute Defender · 24-hr response · +30% win rate

### 7. The 4 UX gaps (none touch the engine)
| Gap | Engineering effort | Business lever |
|---|---|---|
| Skill Library — templates as homepage carousel | 3 weeks UI only | Activation rate |
| Agent Thread — replace email approvals with thread UI | 5 weeks (needs memory) | Daily active use |
| Outcomes Dashboard — KPI schema + per-agent ROI | 4 weeks | Renewal rate |
| Agent Install Cards — 3-field config, social proof | 4 weeks UI only | Time-to-value |

**All 4 sit on top of the engine Vinesh built. UI team + 2 backend engineers · 6 weeks parallel · nothing rebuilt.**

### 8. Customer Discovery sprint (May 16 – June 14)
**5 ICPs · 25 calls · 8–10 design partners · 5 verbatim case studies**

| ICP | Persona | Acute Pain |
|---|---|---|
| D2C Commerce | Neha — Ops Co-founder | RTO eating 18–25% of COD GMV · ₹40–80K/month on stitched tools |
| Fintech SaaS / Subscriptions | Aditi — Head of Growth | UPI AutoPay failures · NPCI 4-attempt rule unused |
| Lending / NBFC | Vishal — Head of Credit Ops | 4 vendors stitched for disbursal+KYC+mandate+repayment · **Razorpay can't match here** |
| Marketplaces / Platforms | Meera — Head of Payments | Sub-merchant KYC + split payouts + TDS — outside any non-PG tool's reach |
| Integration Agencies | Suresh — Web Dev Agency founder | Rebuilds same n8n flow per client · weekend debugging |

**Each ICP has:** 5 use cases, 5 questions to ask, 5 specific companies to call.

---

## Deck Structure — Engineering Deck (22 slides)

```
01 · Cover (navy)
02 · Foundation is in · engine, triggers, MCP
03 · 4 gaps · each unlocks a revenue lever
04 · Why this is a new revenue line, not a feature
05 · Why we built this ourselves · n8n would have cost us the moat
06 · Who we're playing against · competitive scan
07 · Why the market is wide open · Jaipur Reddit evidence
08 · The pricing we're competing with · Razorpay Agent Studio
09 · Where the price lives · 5 things buyers pay premium for
10 · Voice without building voice · Bolna/Osvi pattern
11 · 90-day scorecard · feature → category leader
12 · 6-layer architecture
13 · 90-day build plan · 3 phases
14 · Day 90 · 8 named agents · 8 SKUs
15 · Section break · 4 UX gaps between us and renewal
16 · Skill Library · Activation rate
17 · Agent Thread · Daily active use
18 · Outcomes · Renewal rate
19 · Agent Install · Time-to-value
20 · GFF urgency · A GFF launch compounds
21 · 7 commitments · FY27 revenue story
22 · Closing (navy)
```

---

## Deck Structure — Customer Discovery Brief (16 slides)

```
01 · Cover (navy)
02 · The Goal · 4-week sprint
03 · The Filter · must pass 3 of 4
04 · Section: 5 ICPs (navy)
05 · ICP 1 · D2C "Neha"
06 · ICP 2 · Fintech SaaS "Aditi"
07 · ICP 3 · Lending "Vishal"
08 · ICP 4 · Marketplaces "Meera"
09 · ICP 5 · Agency "Suresh"
10 · Section: Sourcing + Execution (navy)
11 · Sourcing Playbook · Internal first
12 · Outreach Principles · the verbatim one-page pitch
13 · 4-week sprint timeline
14 · Output per call · 5 artifacts
15 · Success metrics
16 · Closing (navy)
```

---

## Research Sources Used

### From earlier sessions (preserved in `relay/research/`)
- 271 Reddit posts scraped May 13 across r/IndiaStartups, r/IndiaBusiness, r/n8n, r/developersIndia
- The Jaipur r/n8n thread (356↑) — 2 months, 44 nodes, still broken

### New research from this session
- Beam AI · Workato · n8n · Lindy · Sintra · Make.com · Zapier Agents · Gumloop · Manus AI · Claude Code · Bolna · Osvi UX patterns
- Skill libraries, conversational UI, agent threads, outcome dashboards, install flows
- Workato Action Board (GA Nov 2025) · n8n AI Workflow Builder (Oct 2025) · Razorpay Agent Studio (Sprint 2026 March 12)

---

## Voice + Style Notes Applied

This session's deck rewrite landed on a few principles worth keeping for future Relay docs:

1. **Plain language over marketing words** — "Forget the agentic word for a minute" > "Strip away the agent narrative"
2. **Engineer-to-engineer voice** — "Two reasons. The buyer can't use it, and we can't afford it." not "The obvious counter-question"
3. **Implicit ROI lens** — every slide carries a business outcome (activation rate, renewal rate, contract value, time-to-value) but never preaches
4. **Specific over abstract** — "₹40–80K/month on Interakt + Zapier + manual ops" not "stitched workaround economy"
5. **Humble cover, sharp body** — opening line is grounded ("An honest look at..."), body slides do the persuading
6. **No "what I need from engineering" demand slide** — let the 7-commitments table speak

---

## What Vinesh Confirmed (Slack · May 13–14)

> "oh yes sure ... we own everything here ... build anything ... from existing open source and Claude."

> "Today discussed with team on building a copy of it for internal use and replace few of existing tools with this one ... dogfooding."

> "We are already using Botpress ... it's too limiting with its enterprise plan ... we pay 3x of our committed cost as top-up for everything as separate plan or pay-per-use. So for Relay we own everything here."

These quotes anchor the architecture and dogfooding slides. They're not marketing — they're the engineering team's own commitment language.

---

## What's Open

1. **Memory + LangGraph timeline** — Vinesh confirmed feasibility, needs concrete quarter commit
2. **3 connectors priority** — Tally, Shopify, AiSensy/Interakt — who owns each, what's the order
3. **Internal dogfooding kickoff** — replace 1 n8n flow + 1 botpress flow by end-June
4. **Pricing model** — free with Cashfree account? Per workflow? Per outcome?
5. **Bolna voice channel** — first-class inside Relay, not parallel product
6. **Customer discovery sprint** — 25 calls starting May 16, design partners signed by June 14

---

## Next Steps (Mothi Owns)

| Task | Due |
|---|---|
| Walk Aditi + Priyam through engineering deck | May 16 (Friday) |
| Send engineering deck to Vinesh + Ram pre-Friday | May 15 |
| Pull D2C ICP list from Cashfree dashboard (25 names) | May 15 |
| First 3–4 discovery calls scheduled | May 16–17 |
| Friday alignment call · lock 5 decisions | May 16 |
| Memory layer commit conversation with Vinesh | May 19 |
| 4 design partners flagged | End of May |
| Positioning doc final + landing page brief | May 23 |
| 8–10 design partners signed | June 14 |

---

## Files In This Session (Final State)

```
/Users/mothi.venkatesh/Documents/relay/
├── README.md
├── docs/
│   ├── cashien-ai-gtm-reference.md
│   ├── relay-feature-brief.md
│   ├── relay-friday-doc-mothi-2026-05-13.md       [Mothi voice doc, May 13]
│   ├── relay-positioning-doc-v1-2026-05-13.md     [Full 11-section, May 13]
│   ├── relay-positioning-gtm-wip.md
│   ├── relay-product-note-vinesh-qa.md
│   ├── relay-product-note.md
│   ├── relay-the-jaipur-memo-2026-05-13.md        [5-min pre-read, May 13]
│   ├── relay-workspace.md
│   ├── session-2026-05-13-positioning-prep.md     [May 13 session log]
│   ├── session-2026-05-14-engineering-deck.md     [THIS FILE]
│   ├── session-context-2026-05-13.md
│   └── slack-log-wf-discussion-apr28-may6.md
├── decks/
│   ├── relay-deck.html                            [Original April deck]
│   ├── relay-engineering-deck-v2-2026-05-14.html  [22 slides · engineering]
│   └── relay-customer-discovery-brief-2026-05-14.html  [16 slides · discovery]
├── launch/
│   └── (all launch artifacts from earlier work)
├── mockups/
└── research/
    ├── reddit_d2c_india_scraper.py
    ├── reddit_d2c_india.json
    └── reddit_d2c_india_report.md
```

---

*Session: May 14, 2026 · Saved by: Mothi Venkatesh · For future reference and continuity.*
