# Research — Demand-Signal Corpus

This folder contains the synthesized outputs from 8 research streams used to ground every claim in [`../RELAY_GTM_v1.md`](../RELAY_GTM_v1.md).

**Total corpus:** ~50,000 demand signals across Reddit, dev.to, Hashnode, GitHub, IndieHackers, ProductHunt, Twitter/X, Cashfree Featurebase, PissedConsumer, Capterra, SoftwareSuggest, FinQfy, and direct competitor websites + press.

---

## Methodology

Each research stream was a parallel sub-agent run, scoped to a specific question and given a hard volume target (≥1.5K conversations for dev forums, ≥1K signals for merchant pain).

Sources per stream:

| # | Stream | Sources | Method | Volume target | Actual |
|---|---|---|---|---|---|
| 01 | Workflow automation competitive scan | 13 vendor websites + G2 + Crunchbase + recent press | WebFetch + WebSearch | 13 vendors covered | 13 ✅ |
| 02 | India payments+automation landscape | Razorpay/PayU/Decentro/Setu/Juspay press, blogs, reviews | WebSearch + targeted WebFetch | Sector study | Done ✅ |
| 03 | MCP-first GTM playbooks | Swiggy, Stripe, Composio, Arcade, Anthropic, Linear, Zapier, Notion/Slack MCP launches | WebFetch on launch posts + press | 8 case studies | 8 ✅ |
| A | Indian Reddit dev/business | r/SaaS, r/indianstartups, r/StartUpIndia, r/DigitalMarketing, r/IndiaBusiness, r/IndiaTech, r/d2c, etc. | Reddit JSON + StealthyFetcher fallback | ≥1.5K conversations | 2,316 ✅ |
| B | Global automation+AI Reddit | r/n8n, r/zapier, r/automation, r/ai_agents, r/ClaudeAI, r/cursor, r/mcp, r/LocalLLaMA, etc. | Reddit JSON | ≥1.5K | 5,143 ✅ |
| C | Builder voice (non-Reddit) | dev.to, Hashnode, GitHub Issues/Discussions, IndieHackers, ProductHunt, Twitter/X | dev.to API + Hashnode GraphQL + GitHub REST + WebFetch | ≥1.5K | 13,976 ✅ |
| D | Merchant pain validation | Cashfree Featurebase (auth-walled, internal pull required), PissedConsumer, Capterra, SoftwareSuggest, FinQfy, Reddit-corpus filtered | WebFetch + Reddit JSON filter | ≥1K | 1,127 ✅ |
| 08 | Swiggy launch dynamics | mcp.swiggy.com `/builders`, `/developers`, `/enterprises`, `/docs`, `/blog/2026-04-17-builders-club-launch/`, FAQ, public launch tweet | WebFetch | Launch case study | Done ✅ |

Plus pre-existing [`dtc-research`](https://github.com/mothivenkatesh) (28,253 rows scraped earlier April 2026) — Indian D2C operator pain corpus, 20 subreddits + 27 keyword searches + 388 deep-dived threads.

---

## How to use

- **Each `0X-…md` file** is the agent's synthesis report — read it for narrative + evidence.
- **Each `agent-X-…/` subfolder** contains the structured artifacts (`top_quotes.json`, `summary.json`, etc.) used to back the synthesis. Useful for verifying specific claims or pulling more quotes.
- **Cross-stream patterns** (a claim corroborated by 2+ streams) are reliable; **single-stream patterns** are flagged in the GTM doc as such.

---

## Key cross-cutting findings

1. **MCP is table stakes by April 2026.** 24% of dev community signals are MCP-aware. Every serious global vendor (Zapier, Pipedream, Workato, Make, n8n, ActivePieces, Tray.ai) has shipped MCP. Razorpay + PayU shipped India-payments MCPs in March/April.

2. **The "first Indian payments-MCP" narrative is gone.** Razorpay Agent Studio + Razorpay MCP launched March 11–12 with Anthropic Claude SDK substrate. Confirmed by Agent A (highly visible in Indian dev Reddit) and Agent 2 (Inc42 + Tribune + The Paypers + MediaNama coverage).

3. **Cashfree brand voice is 3.6x weaker than Razorpay** in builder communities. Agent C: 5 vs 18 mentions in 13,976-signal corpus. Agent A: 21 mostly-mixed Cashfree mentions vs heavy Razorpay/Codex/Replit chatter.

4. **Latent positive Cashfree dev sentiment exists, unamplified.** Multiple verbatim: *"Razorpay has the worst webhooks docs in the industry. Cashfree was easier to integrate."* / *"Cashfree or PhonePe can be slightly cheaper."*

5. **Indian D2C operator pain is concentrated in RTO/COD** (465+372=837 signals across Agents A+D, plus 170 in pre-existing `dtc-research`). This is the dominant pain, not "automation" in the abstract.

6. **The 4 wedges Cashfree Relay can defensibly claim** (each grounded in specific quote evidence):
   - **Open OAuth — no Technology Partner audit** (vs Razorpay's 6-week gate; r/SaaS/1sscu5i)
   - **Payouts + Reconciliation depth in MCP** (Razorpay's MCP is payment-link only)
   - **Self-hostable Indian-priced runtime** (689 PRICE-SENSITIVE + 1,251 BUILT-OWN signals)
   - **Indian back-office stack** (Tally + GST + WhatsApp + UPI + multi-PG recon — Razorpay's 6 agents don't cover)

---

## What's NOT in this corpus

- Cashfree Featurebase voted-feature list — auth-walled, requires internal Cashfree session to pull. Action item before launch.
- Real merchant 1:1 interviews — Reddit/forum signal validates "what merchants complain about publicly," not necessarily "what they'd pay for."
- LinkedIn discussions — minimal scraping; LinkedIn search API is gated.
- WhatsApp / Telegram private group conversations — out of scope.
- Refund Velocity Guardrail validation needs CFO/finance-leader interviews, not Reddit (corpus is too thin).

---

## Regenerating raw data

Raw scrape dumps are `.gitignore`d to keep this repo lean. Regenerate via:

- **Reddit:** `~/.claude/skills/reddit-scraper/` ([mothivenkatesh/reddit-scraper](https://github.com/mothivenkatesh/reddit-scraper))
- **Twitter/X:** `~/.claude/skills/tweet-harvest/` ([mothivenkatesh/twitter-scraper](https://github.com/mothivenkatesh/twitter-scraper))
- **G2 / Clutch:** `~/.claude/skills/review-scrape/` ([mothivenkatesh/review-scraper](https://github.com/mothivenkatesh/review-scraper))
- **dev.to:** public REST API at `https://dev.to/api/articles?tag=<tag>&per_page=100`
- **Hashnode:** GraphQL `tag(slug:"...").posts(filter:{sortBy:recent})`
- **GitHub:** REST API `repos/<owner>/<repo>/issues?since=<iso>`
