# 01 — Workflow Automation Competitive Scan

**Run:** 2026-04-29 · **Window:** April 2026 · **Scope:** 13 vendors with India relevance · **Method:** WebFetch + WebSearch on vendor sites, G2, Crunchbase, recent press

---

## Zapier
- **Positioning:** "Connect AI to 9,000 apps" — the ubiquitous SMB automation layer, now repositioning as the AI-orchestration default.
- **ICP:** Ops/marketing at SMB-to-mid-market; non-developer "citizen automators."
- **Pricing:** Free 100 tasks; Pro $19.99/mo (750 tasks, annual); Team $69/mo; Enterprise custom. **MCP calls = 2 tasks each, no separate SKU.** No India-localised pricing — INR via card at USD rate (~₹1,700/mo for Starter equivalent cited by Indian reviewers).
- **India presence:** No India entity, but heavy SMB pull; native Razorpay connector; Capterra India listings; standard reference workflow on Indian blogs is "Razorpay → Sheet → Slack → HubSpot."
- **Recent moves:** Bundled Tables, Forms, and **Zapier MCP** into every paid tier; consolidated SKU count.
- **AI/MCP story:** Hosted MCP server live (`mcp.zapier.com`) exposing 9,000+ apps; GitHub repo `zapier/zapier-mcp`. This is Relay's most dangerous head-on competitor for the "MCP from Claude Code" pitch.

## Make.com (ex-Integromat, owned by Celonis)
- **Positioning:** Visual scenario builder for AI-era workflow automation.
- **ICP:** Prosumer + SMB ops; growing mid-market via Celonis.
- **Pricing:** Core $9/mo, Pro $16/mo, Teams $29/mo (10K credits each, monthly billing); Enterprise custom. No India SKU.
- **India presence:** Heavy in D2C/agency stack; recommended in Indian blogs as the "graduate from Zapier" tier; native Razorpay connector.
- **Recent moves:** Launched **Make AI Agents** (Spring 2025); shipped own **MCP Server** late 2025; on-prem agents added to Enterprise.
- **AI/MCP story:** Mature — agents + MCP both GA. Visual builder is closest analog to Relay's drag-drop canvas.

## n8n
- **Positioning:** "Fair-code" automation for technical teams — flexibility of code, speed of no-code.
- **ICP:** Technical founders, SaaS engineering, agencies; explodes via self-host.
- **Pricing:** Cloud Starter €20/mo, Pro €50/mo; **self-host free forever.** Pay-per-execution model on cloud.
- **India presence:** **Strongest dev mindshare in India of any global player.** Active service ecosystem — Aroopa Tech (Jaipur), InfyOm, AI India Innovation, Softlabs Group, CloudMinister hosting. 455+ n8n jobs in India in March 2026; salaries ₹12-35L; D2C/fintech SaaS hiring most.
- **Recent moves:** AI Agents node GA, Self-hosted AI Starter Kit on GitHub, MCP nodes shipped, RAG primitives.
- **AI/MCP story:** Native MCP client + server nodes; multi-agent orchestration first-class. **This is Relay's primary technical competitor in India.**

## Activepieces (Relay's underlying fork)
- **Positioning:** "Open-source AI-first Zapier alternative" — MIT core + commercial EE.
- **ICP:** Devs who want to self-host or embed; YC-backed.
- **Pricing:** Cloud Free / Plus $25/mo / Business $150/mo; self-host free; embedded/EE custom.
- **India presence:** Tracked by Indian dev blogs as the "open-source pick"; no India entity.
- **Recent moves:** Activepieces 2.0 (mid-2025) major Agents revamp; ~400 MCP servers exposed; GPT-5 support; new flow builder UI; Agent Builder v2.
- **AI/MCP story:** Aggressively positioned — repo tagline literally "AI Agents & MCPs." Since Relay forks this, the differentiation conversation is about Cashfree-native triggers/payments depth, not engine.

## Pabbly Connect
- **Positioning:** Lifetime-deal Zapier alternative for Indian SMBs.
- **ICP:** Indian solopreneurs, agencies, bootstrapped D2C.
- **Pricing:** **₹20,900 one-time (Standard) / ₹41,800 (Pro)** — lifetime, not subscription. Or $16/mo for 10K tasks. This pricing is the moat.
- **India presence:** **HQ Bhopal (Magnet Brains).** Default automation tool for Indian marketing/agency YouTube ecosystem; very high brand recall in tier-2/3 SaaS-buyer India.
- **Recent moves:** App-catalog expansion to 2,000+; lifetime-deal-led growth playbook continues.
- **AI/MCP story:** Weak — no MCP server, AI features are basic OpenAI step nodes. Vulnerability Relay can exploit on the dev side.

## Pipedream
- **Positioning:** Code-first workflow runtime + 10,000+ MCP tools for agents.
- **ICP:** Developers building integrations into product or agents.
- **Pricing:** Free 100 credits; Basic $45; Advanced $74; **Connect $150** (embed integrations into your app); Business custom.
- **India presence:** Dev-niche but well-known among Indian SaaS engineers; no India go-to-market.
- **Recent moves:** **Acquired by Workday Nov 2025**, closing Q4 FY26 — but pricing/free tier preserved; hosted MCP servers shipped Mar 2025 with 10K+ tools.
- **AI/MCP story:** **Strongest MCP catalog of any vendor** — `mcp.pipedream.com` free for personal use. Direct overlap with Relay's "MCP from Cursor" pitch.

## Albato
- **Positioning:** Cheapest unlimited-automations iPaaS; AppSumo darling.
- **ICP:** SMBs, marketers, AppSumo buyers.
- **Pricing:** Pro $15/mo annual (1K transactions, scaling to 2M); Teams $65/mo; AI billed at 1 transaction per 2K tokens.
- **India presence:** Minimal — no Indian customer signals, no INR pricing.
- **Recent moves:** Native AI agents inside workflows ("coming soon" → shipping in 2026); multi-LLM routing across GPT/Claude/Gemini.
- **AI/MCP story:** AI step-blocks yes; MCP server **not announced**. Lagging.

## Workato
- **Positioning:** "Industry's first **Enterprise MCP** Platform for Agentic AI" — #1 iPaaS Magic Quadrant Leader, 8th year.
- **ICP:** Fortune 500 / enterprise IT, BPO, large fintech.
- **Pricing:** Custom-only (workspace-based, no public price card).
- **India presence:** **Bangalore engineering office;** customers include Indian arms of HSBC, Visa-tier enterprises; serves half the Fortune 500.
- **Recent moves:** **Enterprise MCP GA Oct 2025** (BusinessWire press release Oct 1); 12,000+ governed apps for agents; Recipes catalog at 400K+.
- **AI/MCP story:** Strongest enterprise governance story — MCP with verified user access, audit, RBAC. Relay won't fight this segment in v1.

## Tray.ai (formerly Tray.io)
- **Positioning:** AI orchestration platform — Merlin Agent Builder + Agent Gateway (managed MCP).
- **ICP:** Mid-market to enterprise; revenue $50-100M range.
- **Pricing:** Pro $99/mo, scaling to $599/mo published; per-step task billing + Merlin sold separately. Enterprise custom.
- **India presence:** Asia footprint mentioned, **no confirmed Bangalore office** — HQ San Francisco.
- **Recent moves:** Merlin Agent Builder + Agent Gateway (MCP delivery layer); ITSM accelerator pack with 50K tasks.
- **AI/MCP story:** Agent Gateway is essentially their MCP product; sold as governance layer. Mid-market pricing makes them less of a direct Relay threat than Workato is in enterprise.

## Boost.space
- **Positioning:** "Single source of truth + agentic AI" — data-unification + automation hybrid.
- **ICP:** SME teams already using Make/Zapier/n8n, wanting unified data layer.
- **Pricing:** Pro from $15/mo annual; **50% lifetime discount running until Feb 2026** (TADEAS50). Tiered up to Enterprise.
- **India presence:** Negligible.
- **Recent moves:** **v5.0 launched Feb 2026** with agentic AI + 50% lifetime SME deal; AI Credits SKU (validation, transformation, enrichment).
- **AI/MCP story:** AI Credits for inline data ops; runs automations on Make/Zapier/n8n/own engine. **MCP not yet shipped publicly** — agentic positioning is about data layer, not tool exposure.

---

## Indian-built workflow automation startups
- **Quickwork** (Mumbai) — enterprise iPaaS, 1,500+ connectors, customers include **Axis Bank, DMI Finance, Genpact, Credit Saison India**. Listed AWS Marketplace IN. The most credible local enterprise rival.
- **Konnectify** — visual-builder iPaaS with AI Copilot (text-to-workflow); 100+ apps; SMB-tier.
- **Integrately** (founded Ritesh Sahu, India HQ) — 1,400+ apps, 20M one-click recipes; pricing $19.99-$239/mo. SMB-tier, Pabbly-adjacent.
- **Aroopa Tech / InfyOm / AI India Innovation** — services layer building n8n practices, not products, but they shape the buyer narrative.
- **Bolna** (relevant adjacency, not direct) — voice-AI, ₹5/call, $6.3M General Catalyst seed Jan 2026; explicitly markets payment-recovery use cases (Hypothesis recovered ₹2.5Cr+). **Already in Relay's spec as an action — could become a meta-competitor if they add a workflow builder.**

## Who has shipped MCP / agent-friendly APIs in 2025-2026

| Vendor | MCP server | Shipped |
|---|---|---|
| Zapier | mcp.zapier.com (9K apps) | 2025, bundled into all tiers 2026 |
| Pipedream | mcp.pipedream.com (10K+ tools) | Mar 2025 |
| Workato | Enterprise MCP Platform | Oct 1, 2025 |
| Make.com | Make MCP Server | Late 2025 |
| n8n | MCP client + server nodes | 2025 |
| Activepieces | ~400 MCP servers exposed | 2025-2026 |
| Tray.ai | Agent Gateway (managed MCP) | 2025 |
| Boost.space | Not shipped | — |
| Albato | Not shipped | — |
| Pabbly | Not shipped | — |
| Quickwork / Konnectify | Not shipped | — |

---

## Strategic implications for Relay's launch
1. **MCP is table stakes by April 2026** — every serious global vendor has shipped. Your 24-tool MCP needs depth, not breadth, to win: payments-native triggers (refund initiated, settlement posted, RTO flagged) that no global vendor models cleanly.
2. **The India-positioned dev gap is real** — n8n owns Indian developer mindshare via self-host + service ecosystem; Pabbly owns Indian SMB mindshare via lifetime deals. **No Indian-built dev-first MCP-native automation product exists yet.** That's Relay's wedge.
3. **Quickwork is your sleeper enterprise rival** — Axis, DMI, Genpact references give them BFSI credibility you'll need to match if Relay goes upmarket.
4. **Workday-Pipedream and Celonis-Make** signal that platform consolidation is the macro — Cashfree-Relay is consistent with this thesis.

---

## Sources
- [Zapier Pricing](https://zapier.com/pricing) | [Zapier MCP](https://zapier.com/mcp) | [zapier/zapier-mcp GitHub](https://github.com/zapier/zapier-mcp)
- [Make.com Pricing](https://www.make.com/en/pricing) | [Make 2025 Reflections / 2026 Predictions](https://www.make.com/en/blog/2025-reflections-2026-predictions)
- [n8n Pricing](https://n8n.io/pricing/) | [n8n AI Agents](https://n8n.io/ai-agents/) | [n8n India hosting (CloudMinister)](https://cloudminister.com/blog/n8n-hosting-in-india-everything-you-need-to-know-for-powerful-workflow-automation/) | [N8N AI Automation Career 2026 (GrowAI)](https://growai.in/n8n-ai-automation-career-2026/)
- [Activepieces GitHub](https://github.com/activepieces/activepieces) | [Activepieces Crunchbase](https://www.crunchbase.com/organization/activepieces) | [ActivePieces Review 2026](https://blackbearmedia.io/activepieces-review/)
- [Pabbly Connect](https://www.pabbly.com/connect/) | [Pabbly Review 2026 (productgrowth.in)](https://productgrowth.in/tools/ai-automation/pabbly/) | [Pabbly Pricing 2026](https://bloggerspassion.com/pabbly-connect-pricing/)
- [Pipedream Pricing](https://pipedream.com/pricing) | [Pipedream MCP (Generect)](https://generect.com/blog/pipedream-mcp/) | [Best MCP Server Platforms 2026 (Truto)](https://truto.one/blog/best-mcp-server-platform-for-ai-agents-connecting-to-enterprise-saas)
- [Albato Pricing](https://albato.com/pricing) | [Albato Review 2026 (Lindy)](https://www.lindy.ai/blog/albato-review)
- [Workato](https://www.workato.com/) | [Workato Enterprise MCP press release](https://www.businesswire.com/news/home/20251001259763/en/Workato-Delivers-Industrys-First-Enterprise-MCP-Platform-for-AI-Agents) | [Workato Enterprise MCP product page](https://www.workato.com/agentic/mcp)
- [Tray.ai Pricing](https://tray.ai/pricing) | [Tray.ai Merlin Agent Builder](https://tray.ai/platform/agent-development/merlin-agent-builder)
- [Boost.space v5.0 launch](https://www.globenewswire.com/news-release/2026/02/23/3242792/0/en/Boost-Space-Launches-version-5-0-with-50-Lifetime-Discount-for-SMEs-Embracing-Agentic-AI.html) | [Boost.space Pricing](https://boost.space/pricing)
- [Quickwork](https://www.quickwork.co/) | [Konnectify iPaaS](https://www.konnectify.co/product/ipaas) | [Integrately Pricing](https://integrately.com/pricing)
- [Bolna AI](https://www.bolna.ai/) | [Bolna YC profile](https://www.ycombinator.com/companies/bolna-ai) | [Bolna $6.3M seed (GC)](https://www.generalcatalyst.com/stories/seeding-the-future-with-bolna)
- [Best Automation Tools India 2026 (Parikshit Khanna)](https://www.parikshitkhanna.com/post/best-automation-no-code-workflow-tools-in-india-2026-top-picks-compared-zapier-make-n8n-pabbl) | [Razorpay × Zapier App Store](https://razorpay.com/app-store/zapier/)
