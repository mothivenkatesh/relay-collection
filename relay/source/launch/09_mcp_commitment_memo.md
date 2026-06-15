# Decision Memo — Cashfree MCP Server commitment

**To:** Vinesh Kumar, Subramanian K (Product Owners) + Eng leadership
**From:** Mothi Venkatesh (PMM)
**Date:** 2026-04-29
**Decision needed by:** End of Week 1, private beta
**Stakes:** Public-facing positioning of Cashfree Relay

---

## TL;DR

PMM is leading public positioning of Relay as a **Growth Operator Agent** with **Cashfree MCP** as the spine. The current private beta surface is the no-code workflow builder — MCP is on the roadmap.

This memo asks Eng for a **written commitment to ship Cashfree MCP within 6–8 weeks of private beta opening** (i.e., before public beta), or to formally pause the MCP-first public positioning until Eng can commit a date.

If Eng cannot commit, we fall back to a smaller positioning ("no-code payment workflow automation") and lose the strategic differentiation against Razorpay's Agent Studio + NPCI agentic payments rails.

---

## Why this needs a decision now

**Three artifacts already in flight reference MCP as core:**
1. Positioning doc v2 (lead with MCP-first; private beta as wedge, public beta requires MCP live)
2. Template library spec (B1–B4 templates are designed to be MCP-callable; some require MCP for full value)
3. PR questionnaire (Section 4.2 differentiates against Razorpay on "open MCP vs walled garden")

**If MCP slips past public beta**, all three need to be rewritten and the strategic positioning shrinks to "another workflow tool." The cost of finding out late is far higher than the cost of asking now.

---

## What Eng is being asked to commit

### Tier 1 — Hard commitment (required for current positioning)
- [ ] **MCP server live in production** (Claude Desktop minimum) within **6–8 weeks** of private beta opening
- [ ] **At least 15 read tools** exposed (orders, payments, refunds, payouts, settlements, subscriptions, customer data, dispute lifecycle, webhook events, payment links + 5 more)
- [ ] **At least 3 action tools** exposed with Maker/Checker default (create payment link, initiate refund with cap, register webhook)
- [ ] **OAuth-style scoped consent flow** in Cashfree dashboard (better than Razorpay's static API key auth)
- [ ] **Audit trail visible to merchant** for all MCP calls
- [ ] **Public GitHub repo** (cashfree/cashfree-mcp already exists — bring to production parity)
- [ ] **Documentation + install path** for Claude Desktop
- [ ] **One end-to-end demo workflow** (e.g., "ask Claude to summarize last week's failed payments") working

### Tier 2 — Stretch commitment (required for GA, not public beta)
- [ ] Cursor + Claude Code support
- [ ] SecureID/KYC tools added to MCP (this is our exclusive differentiator vs Razorpay)
- [ ] BYOK (bring your own LLM key) for compliance-sensitive merchants
- [ ] MCP rate limits + quota dashboard for merchants
- [ ] OpenAI Agent SDK + LangChain compatibility examples in repo

### Tier 3 — Post-GA roadmap (acknowledged, not committed)
- [ ] Subscription management tools
- [ ] Webhook management tools
- [ ] Vendor payment / Route tools
- [ ] Marketplace of pre-built agent templates (mirrors Razorpay's marketplace pattern)

---

## Why 6–8 weeks, not 12

- **Razorpay launched their MCP April 2025.** They have a 12-month head-start. Every additional week we wait widens the gap.
- **Cashfree's MCP repo already exists** (cashfree/cashfree-mcp on GitHub, 13 stars, TypeScript, ~37 tools). We're not building from zero. The work is hardening + production deployment + scoped consent flow.
- **Public beta gate is approximately Week 7–10** of the launch plan. MCP needs to be live before public beta opens — otherwise the positioning we've already locked in becomes vapor by week 7.
- **Razorpay's NPCI + Claude pilot (February 2026)** moved their agentic-payments narrative to national infrastructure. Cashfree cannot match NPCI rails, so we have to win on the merchant-side MCP layer faster.

---

## What happens if Eng cannot commit

Three downside paths, ranked by acceptability:

### Path A — Slip 6–8 weeks to 10–12 weeks (acceptable)
Push public beta gate to Week 12. Continue MCP-first positioning. Use the extra weeks to ship more templates and more beta merchants. Marginal credibility cost.

### Path B — MCP not live until GA (concerning, manageable)
Reposition private beta + public beta as "no-code workflow automation." Reserve "Cashfree MCP" as the GA-launch headline. Two announcements instead of one. Loses some narrative momentum but stays honest.

### Path C — MCP unscheduled (positioning collapses)
Drop MCP-first framing entirely. Compete with n8n/Zapier on connector breadth and Indian payment triggers. Razorpay's Agent Studio + NPCI rails take the agentic payments category. Cashfree becomes a follower in workflow tools. **This is the path I want to avoid.**

---

## What PMM is committing in exchange

If Eng commits Tier 1, PMM commits:

1. **No public Razorpay comparisons.** No GitHub-stars optics, no "first" claims, no "unlike Razorpay" framing in PR. Stay focused on category, not competitor.
2. **Templates that exist today are claimed; templates on roadmap are labeled.** Template library spec ([08-template-library-spec.md](08-template-library-spec.md)) is the source of truth. No marketing claim outside it.
3. **MCP launch as a separate Tier-1 announcement** (not buried in the workflow product launch). Founder LinkedIn post, separate press cycle, dev community engagement.
4. **Beta merchant feedback loop on MCP scope** — what tools they actually want first. Eng builds against merchant signal, not internal preference.
5. **No scope creep beyond the Tier 1 list above** during the 6–8 week window. Stretch items wait.

---

## Decision request

Please respond with one of three answers by **end of Week 1, private beta**:

1. **"Commit Tier 1 within 6–8 weeks"** → PMM proceeds with MCP-first positioning across all artifacts.
2. **"Commit Tier 1 within 10–12 weeks"** → Path A. PMM adjusts public beta date, keeps positioning.
3. **"Cannot commit a date"** → Path B or C. PMM pauses MCP-first artifacts and rebuilds positioning around what's actually shippable.

Silence = Path C by default. Please don't let it default.

---

## Open questions for the meeting

1. What's blocking MCP today? (Engineering capacity, security review, compliance signoff, OAuth flow design?)
2. Is the existing cashfree/cashfree-mcp GitHub repo production-ready, or does it need to be rebuilt?
3. Who owns OAuth-style scoped consent UX in the Cashfree dashboard? (Product team, dashboard team, or new hire?)
4. What's the security review timeline for exposing payment primitives via MCP?
5. Can we use Razorpay's auth model (base64 token) as a temporary launch posture and upgrade to OAuth later, or is OAuth required from day one?

---

## Source references

- [Positioning doc v2](positioning-cashfree-relay-v2-2026-04-29.md) — current public-facing framing
- [Template library spec](08-template-library-spec.md) — what's claimed vs roadmap
- [Razorpay MCP intelligence brief](.) — competitor depth
- [GTM strategy](03-gtm-strategy.md) — phased launch plan, public beta gate

---

*This memo is the contract between PMM and Eng for the launch positioning. Either party can re-open it; neither can act unilaterally against it.*
