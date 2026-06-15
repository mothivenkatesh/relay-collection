# Session Log — Relay Positioning Prep (May 13, 2026)

**Trigger:** Tuesday call with Aditi Olemann, Priyam Shankar Jha, Yashasvi Chaudhary. Friday alignment call follow-up.
**Mothi's ask:** Build the positioning doc, identify the product need vs n8n, deliver "greatest ever PMM work."

---

## Session Output Files Created

| File | Purpose | Status |
|---|---|---|
| `relay/docs/relay-positioning-doc-v1-2026-05-13.md` | Full 11-section positioning doc | Final |
| `relay/docs/relay-the-jaipur-memo-2026-05-13.md` | 5-min pre-read built around r/n8n Jaipur thread | Final |
| `relay/docs/relay-friday-doc-mothi-2026-05-13.md` | Master doc in Mothi's voice, plain language, answers every Tuesday Q | Final — primary Friday read |
| `reddit_d2c_india_scraper.py` | Working scraper, subreddit-specific (replaces broken global-search scrapers) | Working |
| `reddit_d2c_india.json` | 271 posts scraped, 40 with comments, 6-month window | Raw data |
| `reddit_d2c_india_report.md` | Markdown report of all scraped posts + verbatim comments | Reference |

---

## Key Decisions Reached in Session

### The Positioning
> **Cashfree Relay turns Indian payment events into business actions in 30 minutes — without code, without webhooks, without a developer.**
>
> **It is the only payment-native workflow product built for the operator who will never open n8n.**

### The ICP — Three Specific Personas
1. **Neha** — D2C Ops Lead, 6,000 orders/month, pays ₹36,700/month across Interakt + Pabbly + manual ops
2. **Suresh** — Web Dev Agency in Coimbatore, 9 D2C clients, rebuilds same n8n flow each time
3. **Arjun** — Indie Builder on Cashfree MCP, wants payment event primitives + distribution

**Primary ICP for launch:** Neha. Developer is secondary unlock via MCP layer.

### The "Why Not n8n + MCP" Answer (Settled)
n8n is not the competitor. n8n is the proof the problem exists.

**Evidence:** A Jaipur developer posted on r/n8n in March 2026. Spent 2 months building a 44-node WhatsApp AI agent for his family's clothing store. 356 upvotes, 117 comments. His v3 broke because of "no memory, no routing." → If a developer needs 2 months, the non-technical operator never builds it.

The real competition: Interakt (₹8–18K/month) + Pabbly/Zapier (₹4–12K/month) + manual ops hire (₹20–35K/month) = ₹40–80K/month. That's the budget Relay competes for.

### What Relay Is Today (Honest)
- Workflow builder + MCP server
- **Not** an agent — no memory, no goal-setting, no self-correction
- Rule engine that runs deterministic workflows
- AI = MCP creates workflows by prompting in Claude; workflows themselves run rules

**Stop calling it "agentic" in marketing** until memory + goal-setting ships next cycle. Medianama already called out Razorpay's dark pattern risk in agent demos — we don't need that.

---

## The 9 Use Cases (3 per Persona)

### Neha (Ops Lead) — Day-1 templates
1. **COD Confirm via WhatsApp** — RTO drops from 28–32% to 16–20% in 30 days
2. **Failed Payment Recovery** — 10–15% of failures recovered within 5 min
3. **Settlement to Google Sheets Daily** — 2–3 hrs/day manual work eliminated

### Suresh (Agency) — Resellable templates
4. **Post-Payment Calendar Booking** (service businesses) — agency charges ₹5K/month
5. **Big-Ticket Alert + CRM Update** — B2B clients
6. **Multi-Client COD-to-Prepaid** — RTO cut 30% in 60 days promise

### Arjun (Indie Builder) — Developer hooks
7. **Programmable Payment Event Hooks via MCP** — 3 API calls → 1 prompt
8. **Template Distribution** — publishes workflow as Relay template, gets Cashfree merchant base as customers
9. **Multi-Product Orchestration** — PG + Secure ID + Payouts in one flow (Razorpay can't do this)

---

## Competitive Map

| | Razorpay Agent Studio | n8n + Cashfree MCP | Cashfree Relay |
|---|---|---|---|
| Built on | Claude Agent SDK | OSS workflow engine | Workflow engine + MCP |
| Persona | Merchant who trusts AI autonomy | Developer | Operator + agency + indie builder |
| Setup | Per-agent activate | 2 months (per Jaipur evidence) | 30 min with template |
| Compliance | Generic | Generic | KYC + Secure ID + RBI built-in |
| Scope | PG only | API-only | PG + Payouts + Secure ID + Verify |
| Pricing | Per-outcome, opaque | Self-hosted | Workflow-based (TBD) |
| Open MCP | No | Yes (but they parse) | Yes (native) |

**Cashfree's wedge:** regulated, full-stack, operator-friendly. Not agent-first.

---

## Aditi's Three Tracks — Where Relay Fits

| Track | What | Owner |
|---|---|---|
| 1. End-user AI | Consumer discovers + pays in LLMs | Cashfree Here (not Relay) |
| 2. Payment Ops VAS | Packaged AI products (voice agent, cart recovery) | Lavika |
| 3. Developer Workflow Builder | Build any payment workflow, payments at center | **Relay** |

**Don't merge these.** One umbrella narrative for AI, three distinct landing pages.

---

## 5 Decisions for Friday Meeting

1. Launch ICP = D2C Ops Lead. Developer secondary.
2. Drop "agentic" from headline. Use "payment-native workflow automation."
3. Keep VAS (Lavika) separate from Relay in GTM.
4. Launch with 3 templates: COD confirm, failed payment recovery, settlement reconciliation.
5. Pin date for memory layer commitment with Ram + engineering.

---

## Open Questions Still Unresolved

1. Product name resolution: "Relay" covers MCP + Workflow Builder. One brand or two surfaces?
2. Pricing model: Free with Cashfree? Per workflow? Per execution?
3. White-label/reseller path for Suresh-persona agencies?
4. When does engineering commit to memory + goal-setting?
5. Landing page lead — templates (operator) or MCP docs (developer)?

---

## Reddit Research Findings (271 Posts, Feb–May 2026)

### Subreddit Distribution
- r/IndiaStartups: 47 posts (D2C founder pain)
- r/IndiaBusiness: 38 (SMB ops reality)
- r/developersIndia: 36 (dev integration pain)
- r/n8n: 28 (technical builders)
- r/smallbusiness: 14
- Others: 108

### The Three Killer Verbatims

**Verbatim 1 — r/n8n, March 2026, 356↑, 117💬, Jaipur developer:**
> "Version 3 had no memory, no routing, no sense of where a customer is in their journey. I started over properly. The final system: 44 nodes, 2 AI agents."
**→ 2 months to build, by a developer, for his family. Proof n8n is not for non-technical operators.**

**Verbatim 2 — r/IndiaStartups, Nov 2025, 78↑, 68💬, D2C apparel founder:**
> "23% of COD orders were fake/undelivered, average loss per fake order is around ₹350... we've tried OTP, restricting postal codes, charging extra for COD. Nothing is really helping :("
**→ The pain is named, quantified, and operators know they can't solve it alone.**

**Verbatim 3 — r/IndiaStartups, Dec 2025, 188↑, 51💬, D2C consultant:**
> "If you are doing less than 500 orders a month, logistics companies generally do not care about your grievances regarding RTO."
> "If there is no repeating customer, there is no sale."
**→ The workflows operators want already named: COD confirm → reduce RTO → retarget repeat buyers.**

---

## Tool/Method Notes

### Reddit Scraping
- **Don't use global search** (`reddit.com/search`) — returns viral garbage for niche India topics
- **Use subreddit-specific search** (`reddit.com/r/X/search.json?restrict_sr=1`)
- Reddit JSON API works fine with standard User-Agent header
- Existing scrapers in `/Documents/` (`reddit_mcp_scraper.py`, `agent_browser_reddit_mcp.py`) were pointed at MCP/agent topics, not D2C India payments — built for different research
- New scraper `reddit_d2c_india_scraper.py` is the working version for D2C India

### PMM Methodology Used
1. Outside-in not inside-out (Aditi's explicit ask)
2. Behavior questions not opinion questions in merchant calls
3. Lead with verbatim evidence, not paraphrase
4. One killer insight beats 50 data points (the Jaipur thread)
5. Pre-read memo before Friday so meeting starts at insight level, not summary level

---

## Next Steps Mothi Owns

| Task | Due | Status |
|---|---|---|
| 5–6 merchant validation calls | May 16 (Friday) | 1 done (Zosell voice AI), 4–5 pending |
| Friday pre-read sent to Aditi + Priyam | May 14 (Thursday) | Ready to send |
| Decision on 5 Friday items | May 16 (Friday) | In meeting |
| Update positioning doc with merchant call inputs | May 19 | Pending Friday decisions |
| Landing page brief + launch blog | May 23 | Pending positioning lock |

---

## Files in This Session

```
/Users/mothi.venkatesh/Documents/relay/
├── docs/
│   ├── relay-positioning-doc-v1-2026-05-13.md  [full doc, 11 sections]
│   ├── relay-the-jaipur-memo-2026-05-13.md     [5-min pre-read]
│   ├── relay-friday-doc-mothi-2026-05-13.md    [master doc, Mothi's voice]
│   └── session-2026-05-13-positioning-prep.md  [this file]
└── research/
    ├── reddit_d2c_india_scraper.py             [working scraper, reusable]
    ├── reddit_d2c_india.json                   [raw data, 271 posts, 596K]
    └── reddit_d2c_india_report.md              [verbatim quotes report, 116K]
```

**Note:** Original copies of the research files also exist at `/Documents/` root from when they were first scraped. The canonical versions for this project are in `relay/research/`.

---

*Session: 2026-05-13 · Owner: Mothi Venkatesh · Saved for future reference*
