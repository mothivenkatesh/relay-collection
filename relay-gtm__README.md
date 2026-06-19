# Cashfree Relay — GTM v2 (phased to GFF 2026)

Go-to-market plan for **Cashfree Relay**, the open payments-native workflow automation platform. Headline public launch at **Global Fintech Fest 2026 — Mumbai, Sep 1-7** under category claim *"Agent Workflows for India's payments infrastructure."*

This repo contains the SuperPMM-structured launch plan plus the demand-signal corpus (~50,000 signals across 8 sources) that grounds every claim in it.

---

## Entry point

**[`RELAY_GTM_v1.md`](./RELAY_GTM_v1.md)** — full GTM doc (v2 content; filename retained for git history). Read this first.

Sections (per [SuperPMM methodology](https://github.com/mothivenkatesh/pmm-ops)):
1. ICP + TAM (FletchPMM scorecard, SPICED diagnostic, triangulated TAM)
2. Competitive Intelligence (Direct / Status Quo / Adjacent + 4 differentiation wedges)
3. PRFAQ (working-backwards press release + customer/internal FAQs)
4. Positioning + Atlassian Message House (4 pillars, persona/competitive messaging, Phase 1 vs Phase 3 positioning lines)
5. **Launch Plan — 5-phase rollout** (Phase 0 Private Beta · Phase 1 Developer Soft Unveil · Phase 2 Template Gallery + Cohort Apps · Phase 3 GFF Headline Launch · Phase 4 Post-GFF Compound) · three-server MCP architecture · GFF Day-1 tweet · per-phase metrics · 10 risks

Plus appendices: corpus map · operator language to steal verbatim · battle cards · Mothi-personal brand-compounding (phase-aligned) · **Swiggy Builders Club → Cashfree Relay translation map** (every Swiggy URL/pattern explicitly mapped).

## v2 highlights

- **Phased rollout** respects current private-beta-access posture (no public Relay content until Phase 1)
- **Phase 0 (Apr 29 → May 31):** sign **2-3 enterprise design partners** under NDA + 3-5 mid-market; resolve `Map<String,Object>` blocker
- **Phase 3 GFF (Sep 1-7, Mumbai):** headline public launch under *"Agent workflows for India's payments infrastructure"*
- **Appendix E:** explicit Swiggy → Cashfree translation map covering all `mcp.swiggy.com/builders/*` URLs and 20 patterns to copy / 3 to skip / 4 to do better than Swiggy

---

## Evidence

[`research/`](./research) — synthesis outputs from 8 research streams + structured quote artifacts.

| Stream | Signals | Window | Key finding |
|---|---|---|---|
| [01 — Workflow automation competitive scan](./research/01-workflow-automation-competitive-scan.md) | 13 competitors | Apr 2026 | MCP is table stakes; n8n owns Indian dev mindshare; Pabbly owns SMB |
| [02 — India payments+automation landscape](./research/02-india-payments-automation-landscape.md) | Sector study | Q1 2026 | Razorpay Agent Studio launched March 11–12; PayU MCP April 2026 |
| [03 — MCP-first GTM playbooks](./research/03-mcp-first-gtm-playbooks.md) | 8 launch case studies | 2024–2026 | 7 tactical moves; cohort launch + framework adapters + third-party narrative |
| [04 — Indian Reddit dev/business](./research/04-indian-reddit-dev-business.md) | 2,316 conversations | 30 days | **Razorpay Agent Studio HIGHLY visible in India**; Cashfree mentions 21 (mixed); BUILT-OWN signal 1,251 |
| [05 — Global automation+AI Reddit](./research/05-global-automation-ai-reddit.md) | 5,143 conversations | 30 days | Cursor + n8n + Claude Code dominate; Razorpay Agent Studio invisible globally |
| [06 — Builder voice (dev.to / Hashnode / GitHub / IH / X)](./research/06-builder-voice-devto-hashnode-github-x.md) | 13,976 signals | 30 days | Cashfree mentions 5 vs Razorpay 18 (**3.6x voice gap**) |
| [07 — Merchant pain validation](./research/07-merchant-pain-validation.md) | 1,127 distinct signals | 90 days | RTO/COD #1 (465); Refund mgmt #2 (391); SaaS-Agency persona stronger than expected |
| [08 — Swiggy launch dynamics deep-dive](./research/08-swiggy-launch-dynamics-deep-dive.md) | Launch case study | Apr 2026 | 181K-view tweet → 500+ apps in 2 days; local-first DX; 3-track docs IA |
| **Existing** [`dtc-research/`](https://github.com/mothivenkatesh) (separate workspace) | 28,253 rows | Late 2025 → Apr 2026 | RTO/COD #1 India D2C pain; "Razorpay relationship is the gravitational center" |
| **TOTAL** | **~50,000+ signals** | | |

Each agent's subfolder contains the structured quote artifacts (`top_quotes.json`, `summary.json`, `tool_mentions.json`) used to ground the synthesis.

Raw scrape dumps (47MB+ CSVs / multi-MB JSONs) are `.gitignore`d — they're regenerable from the scraper skills (`reddit-scraper`, `tweet-harvest`, `review-scrape`).

---

## Methodology

**SuperPMM 5-step workflow** (from [pmm-ops](https://github.com/mothivenkatesh/pmm-ops)):
- ICP + TAM (FletchPMM ICP Scorecard, Winning by Design SPICED, triangulated TAM)
- Competitive Intelligence (FletchPMM 3-phase differentiation, status-quo mapping)
- PRFAQ (Amazon working-backwards)
- Positioning (FletchPMM Anchors, April Dunford "Obviously Awesome", Atlassian Message House)
- Launch Plan (AWS Tier-1 conventions, Google DIN stakeholder framework, leading/lagging/anti-metrics per Hattie's 6 OKR anti-patterns)

**Operating principle (per [`dtc-research/CLAUDE.md`](https://github.com/mothivenkatesh)):** Stay on pain / persona / TAM / WTP / evidence. Use operator language verbatim ("RTO%", "fake COD orders", "warm leads who drop off") rather than corporate-speak. Lead with what the corpus most strongly supports.

---

## Status

- **v1** — Apr 29 2026 — initial GTM, 50K-signal evidence-grounded
- Iterate from this baseline. Open decisions tracked in `RELAY_GTM_v1.md` § "Open decisions for Mothi"

---

## Repo structure

```
cashfree-relay-gtm/
├── README.md                                      ← you are here
├── RELAY_GTM_v1.md                                ← the GTM (entry point)
├── research/
│   ├── README.md                                  ← research methodology + corpus map
│   ├── 01-workflow-automation-competitive-scan.md
│   ├── 02-india-payments-automation-landscape.md
│   ├── 03-mcp-first-gtm-playbooks.md
│   ├── 04-indian-reddit-dev-business.md
│   ├── 05-global-automation-ai-reddit.md
│   ├── 06-builder-voice-devto-hashnode-github-x.md
│   ├── 07-merchant-pain-validation.md
│   ├── 08-swiggy-launch-dynamics-deep-dive.md
│   ├── agent-a-indian-reddit/   (top quotes, fresh permalinks, deep threads)
│   ├── agent-b-global-reddit/   (shortlist, summary)
│   ├── agent-c-builder-voice/   (top quotes, summary, tool mentions)
│   └── agent-d-merchant-pain/   (quotes)
└── .gitignore
```
