# GTM Strategy — Cashfree Relay (Private Beta → GA)

> Built around three principles:
> 1. **North star = value delivered, not vanity created.** Workflow runs > workflows built.
> 2. **Private beta is a learning vehicle, not a growth vehicle.** Optimize for what to build, not how fast it grows.
> 3. **Selection is product strategy.** Who you let into beta determines what Relay becomes.
>
> **This launch plugs into Cashfree's existing GTM operating model** (per [gtm-ops](https://github.com/mothivenkatesh/gtm-ops)) — the 3-loop agent architecture, DIN approval gate, 13 reliability rules, and 3-surface BI rule. See §0 below.

---

## 0. How this launch plugs into Cashfree's GTM-Ops infrastructure

This launch does NOT bypass the existing GTM operating model. Every campaign and metric flows through:

### 0.1 — File the Relay DIN (Demand Initiative Number) before any outreach
- Single Gdoc brief with the 9 mandatory artifact uploads
- Slack-first discussion, eSignature finality (not Slack reactions)
- Status flips to approved only after all 9 artifacts uploaded
- **Agents halt if no approved DIN exists** — this means CSM/SDR outreach to beta merchants is blocked until DIN is approved
- Owner: PMM (you). Sign-offs: Reeju, Mohit, Sales Lead, Comms

### 0.2 — Map Relay launch motions to the 3 lifecycle loops
The launch is not a separate motion. It runs *through* the existing loops:

| Motion | Loop | Agent | What it does for Relay |
|---|---|---|---|
| Beta merchant sourcing (Top 200 SMBs) | **Acquisition** | `cf-icp-scout` | Score Cashfree merchants on Relay-fit using the 4 filters (technical capability + ₹10L+ volume + ops pain + good standing) |
| Beta recruitment emails | **Acquisition** | `cf-outreach-writer` | Per-tier personalized emails (founder→founder, CSM→ops, applicant follow-up, welcome) — see [05-launch-emails.md](05-launch-emails.md) |
| Reply triage on beta apps | **Acquisition** | `cf-reply-classifier` | Auto-classify applicant replies (interested / not-fit / needs-info) and route to PMM |
| Beta merchant 14-day check-in | **Nurture** | `cf-stage-mover` | Detect beta merchants who haven't built a workflow in 14 days; CSM gets a brief |
| GA cross-sell to existing Cashfree merchants | **Acquisition + Cross-sell** | `cf-cross-sell-detector` | Identify Cashfree merchants with high-volume payment ops who don't have Relay |
| Beta merchant churn signals | **Re-engagement** | `cf-churn-saver` | Composite signal (login drop + workflow run drop + support ticket sentiment) → save brief for CSM |
| 15-min skip detection | (governance) | `cf-din-watchdog` | Catches any unauthorized Relay outreach within 15 min |

### 0.3 — Apply the 13 reliability rules to Relay's launch
Specifically relevant to a private beta launch:

| Rule | What it means for Relay launch |
|---|---|
| **#3 HITL for first 100 sends** | First 100 beta recruitment emails reviewed by PMM before send (not auto-sent by `cf-outreach-writer`) |
| **#4 Frequency caps (4 touches/quarter/merchant)** | Top 200 SMB outreach budget for Relay = max 4 touches across all channels in the quarter. Burning all 4 on Relay is a strategic call — coordinate with Sales/CS |
| **#6 Kill switch** | Per-campaign disable in 30s. If beta application rate breaks expected range, pause |
| **#9 Mandatory UTMs** | Every "Apply for Relay" CTA carries unique UTM (founder-email, CSM-email, dashboard-banner, Discord, etc.) |
| **#10 Artifact uploads** | 9 artifacts in DIN before launch: 1-pager, demo video, screenshot bank, FAQ, email copy, banner copy, eligibility criteria, success metrics, kill criteria |
| **#11 3-layer skip detection** | Pre-launch gate (DIN approved) + 15-min anomaly scan + daily recon |

### 0.4 — Reporting flows into the 3 BI surfaces (no Relay-specific dashboard)
Anti-sprawl rule applies. Relay metrics live where everything else lives:

| Surface | Relay views |
|---|---|
| **Operational Sheets** (AE/CSM-facing) | Per-CSM beta merchant cohort tracker (status, last workflow built, runs this week, next check-in) |
| **Metabase** (PMM/RevOps-facing) | Activation funnel, use-case taxonomy, connector request frequency, NPS-by-segment |
| **AWS QuickSight** (Executive-facing) | Roll-up to Reeju: Relay activation rate, runs/active merchant, top use cases, GA gate readiness |

**No fourth dashboard. No Relay-only Notion page that becomes the "real" report.**

### 0.5 — The org-wide north star ("AE calendar fill rate ≥80%") still wins
Relay's product north star (Successful Workflow Runs / Active Merchant / Month) is a **product metric**. The GTM-Ops north star (AE calendar fill rate) is the org metric. Relay supports the org metric by:
- Beta cohort generates 3–5 hero case studies → AE pitch ammunition → calendar bookings
- GA campaign generates inbound demo requests → AE calendar fill
- Cross-sell loop converts Cashfree-only merchants → Relay → expansion ARR
Relay PMM does not own AE calendar fill. PMM owns: hero stories, demo enablement, inbound volume.

---

## 1. The North Star (and why most workflow tools get it wrong)

For workflow automation platforms, **"workflows created" is a vanity metric.** Workflows get built and abandoned constantly. The platforms that win track delivered value.

**Relay's north star:**
> **Successful Workflow Runs per Active Merchant per Month**

**Why this metric pulls the right levers:**

| Property | What it forces the team to care about |
|---|---|
| **"Successful"** | Reliability — a workflow that runs but errors doesn't count |
| **"Runs"** | Real value delivered — a workflow firing 1000×/month is 1000× more valuable than one firing once |
| **"Per active merchant"** | Normalizes for growth, exposes depth of usage, surfaces dead accounts |
| **"Per month"** | Faster than quarterly — catches engagement decay before retention reports do |

**Secondary metric:** **% of active merchants with ≥1 workflow firing daily.** This is the activation/stickiness cut — the difference between "they tried it" and "they're using it for something real."

**How peers frame the same idea:**
- Zapier — "Tasks" (their billing unit)
- n8n — "Workflow executions"
- Make — "Operations" (each module step counts)
- Lindy / Gumloop — "Successful agent runs" or "Agent actions completed"

**Future-state nuance:** As Relay adds AI connectors that do real work (write the customer message, summarize the dispute), task *count* will under-represent value. v2 metric to watch: **hours of human work automated** or **revenue recovered per merchant per month**.

---

## 2. Private Beta — the launch goal is NOT the north star

**The north star metric does not apply yet.** With no templates and 50 merchants, "runs per merchant per month" will be tiny and misleading. Private beta is a **learning sprint**, not a growth sprint.

**The single launch goal for private beta:**

> **15+ merchants build and run their own workflow end-to-end, unprompted, within 14 days of access.**

(Pick 15 because it's small enough to white-glove. Aim for 12+ to actually hit it.)

**Why this and not signups, runs, or NPS?** Without templates, every successful workflow is a signal of three things at once:
1. A real problem worth automating (motivation to build from scratch)
2. The primitives are good enough (connectors, UX, docs cleared the gap)
3. A template you should ship at GA (their workflow becomes your library)

**Three sub-goals stacked under the launch goal:**

| Sub-goal | Measure | Target |
|---|---|---|
| **Activation** | % of beta merchants who build any workflow | ≥75% (15 of 20) |
| **Use case discovery** | # of distinct problems being solved | 15–20 unique workflows |
| **Stickiness signal** | % whose workflow ran ≥5× in week 2 | ≥30% |

**The third one is the most important.** It separates "they tried it" from "they're using it for something real."

---

## 3. What private beta is explicitly NOT optimizing for

Make these explicit so leadership doesn't measure beta against the wrong yardstick:

- ❌ **Total signups / waitlist conversion** — vanity at this scale
- ❌ **Total workflow runs** — will be tiny and misleading without templates
- ❌ **NPS / CSAT** — sample too small, too early
- ❌ **Revenue / pricing validation** — that's late beta, not launch
- ❌ **Press coverage** — Tier 2 launches stay press-light until GA

**The real deliverables from private beta are qualitative:**
- 10–15 documented use cases → these become your launch templates
- A connector priority list (what merchants asked for that you didn't have)
- 3–5 hero workflows with merchant quotes for GA launch
- A clear answer to: **is Relay positioned as ops automation (refunds, recon, alerts) or growth automation (cart recovery, payment link drips, WhatsApp follow-ups)?** Beta is how you find out before you commit.

---

## 4. Beta Merchant Selection — 4 Filters (all must pass)

Selection is product strategy. The wrong 20 merchants give you false negatives and waste 6 weeks. Use this as a hard gate.

### Filter 1 — Technical capability
- ✅ Has someone on team who's used Zapier / Make / n8n before, OR
- ✅ Has a developer in-house, OR
- ✅ Founder is technical

**Why:** Without templates, they need to figure things out. Non-technical merchants will churn and give false negatives ("the product is too hard" when really they were the wrong ICP for *this stage*). They become the GA audience, not beta.

### Filter 2 — Active payment volume + ops pain
- ✅ Doing >₹10L/month in payment volume on Cashfree (real merchant, real problems)
- ✅ Currently doing some ops manually that's clearly automatable: reconciliation, refund workflows, customer messaging, abandoned cart, COD verification

**Why:** "Hair on fire" problem = they'll push the product. Low-volume merchants don't have enough ops to need automation.

### Filter 3 — Engagement willingness
- ✅ Founder or ops lead willing to take 30-min weekly calls for 6 weeks
- ✅ Will share workflow screenshots, screen recordings, and feedback in a shared Slack/Discord

**Why:** The output of beta is the qualitative learning. If they ghost you, the slot is wasted.

### Filter 4 — Trustworthy operator
- ✅ Existing Cashfree merchant in good standing (no payment disputes, no risk flags)
- ✅ Not a direct competitor or someone likely to leak

**Why:** They'll see the roadmap, raw connectors, broken UX. You need merchants who stay in the tent.

---

## 5. Portfolio Mix — diversity of use cases (don't pick 20 of the same)

Aim for spread across these axes — this is how you discover use case clusters instead of overfitting to one segment:

| Segment | Slots | Why include |
|---|---|---|
| D2C brands (Shopify, custom storefronts) | 5–6 | Highest automation appetite — abandoned cart, WhatsApp, RTO, refunds |
| SaaS / subscription | 3–4 | Recurring billing, dunning, churn workflows, payment failure recovery |
| Marketplaces / aggregators | 2–3 | Multi-party reconciliation, vendor payouts |
| EdTech / coaching | 2–3 | Lead-to-payment funnels, Calendly + WhatsApp drip |
| Fintech / lending adjacent | 1–2 | Compliance workflows, KYC handoffs |
| Services / agencies | 2 | Invoice → payment link → reminder flows |
| **Total** | **15–20** | |

**This spread guarantees you don't end up with 20 D2C cart-recovery workflows and zero insight on B2B use cases.**

---

## 6. Sourcing — priority order (cheapest signal first)

| # | Source | Owner | Why this priority |
|---|---|---|---|
| 1 | **CSM/AM intro list** — ask Mohit's SMB team for "10 merchants who keep asking for automation/workflows" | CSM team | Pre-qualified by repeated asks |
| 2 | **Recent support tickets** — mine for "can you do X automatically?" or merchants with janky scripts on Cashfree | Support + PMM | High-pain signal, very cheap |
| 3 | **Top n8n/Zapier users in Cashfree base** — correlate Cashfree webhook traffic spikes (weekday 9–6) with merchants whose API logs show automation patterns | Solution Engineering + Data | Behavioral signal — they're already automating, just doing it elsewhere |
| 4 | **Reeju + Mohit founder-to-founder asks** — reserve 2–3 slots | Reeju | Convert at 80%+, brand-positive |
| 5 | **Discord cohort** (later, once Discord scales) | DevRel | Technical merchants here are perfect — flag for public beta |

---

## 7. Screen-OUTS — explicit DO NOT include

These will give you false signal:

- ❌ Merchants who say **"we just need pre-built templates"** — they're the GA audience, not beta
- ❌ Merchants who want **SLA / uptime guarantees** — beta will break, that's fine, but it'll burn the relationship
- ❌ **Enterprise merchants (>₹5Cr/month)** — procurement is too slow, security reviews you can't pass yet
- ❌ Anyone who needs Relay to **replace an existing workflow on Day 1** — they need migration support you can't provide
- ❌ Merchants whose primary ask is **"AI agents that talk to my customers"** — different product. Don't let beta scope-creep into agentic territory before you've nailed trigger-action

---

## 8. Intake Conversation — 3 questions to ask every candidate

If they answer all three with specifics, let them in.

**Q1. "What's one repetitive thing your team does every day that you wish a bot did?"**
- Looking for: specificity
- ✅ "Email refund confirmations to customers, copy-paste them into Tally, and update a Sheet"
- ❌ "Automation in general" / "Make us more efficient"

**Q2. "Have you tried to build this before? With what?"**
- Looking for: prior attempts
- ✅ "We have a janky Zap that breaks every two weeks" / "We hired a dev who left"
- ❌ "We haven't really thought about it" — means they don't actually feel the pain

**Q3. "If we gave you access tomorrow, who on your team would actually build the workflow?"**
- Looking for: a named human
- ✅ "Priya, our ops manager — she set up our HubSpot automations"
- ❌ "I'll figure it out" from a non-technical founder = warning sign

---

## 9. Beta Success Threshold (Go / No-Go to public beta)

**You'll know selection was right if:**
- ✅ ≥12 of 20 merchants build ≥1 working workflow within 14 days
- ✅ ≥5 workflows run ≥50 times/month by week 6
- ✅ Exit beta with ≥10 documented use cases + ≥5 merchant testimonials

**If <8 of 20 activate** — the problem isn't the product, it's merchant selection. Re-run filters, don't ship product changes.

**Go-to-public-beta gate:**
- ≥10 ready-to-use templates published in-product (sourced from beta merchant workflows)
- ≥1 connector built per top-3 merchant request
- White-glove playbook converted to in-app guided tour + Loom library
- Self-serve activation rate target locked: ≥40% by end of public beta

---

## 10. Phased Plan (12-week roadmap)

### Phase 0 — Internal alignment (Weeks -2 to 0)
- All-hands demo + 10-min Loom
- 1-pager for Sales / CS / Support / Solution Engineering
- Internal Slack #relay-feedback
- Beta selection criteria locked (Section 4–7 above)

### Phase 1 — Private Beta (Weeks 1–6) — **WHERE WE ARE**
**Goal:** 15+ merchants run their own workflow end-to-end, unprompted, within 14 days.
- Apply the 4 filters + portfolio mix
- White-glove onboarding (CSM + SE co-builds first 3 workflows per merchant)
- Weekly 30-min calls per merchant (you personally read every workflow built)
- Shared Slack/Discord channel for beta cohort
- **Templates dependency:** Build 10 templates *during* private beta, sourced from what merchants build live

### Phase 2 — Closed Public Beta (Weeks 7–10)
**Goal:** Validate self-serve activation. 500 merchants. ≥40% build a workflow without CSM help.
- Open waitlist on cashfree.com/relay
- 10 templates published in-product
- Replace white-glove with: in-app guided tour + Loom library + community Slack
- Begin pricing experiments (show "Pro tier coming soon" — capture intent)

### Phase 3 — GA Launch (Weeks 11–12+)
**Goal:** 2,000+ merchants, north-star metric live (Successful Runs per Active Merchant per Month).
- Public PR (TechCrunch India, YourStory, Inc42, Moneycontrol)
- Reeju LinkedIn launch post
- Webinar: "Automate Your Payment Ops in 30 Minutes"
- Paid acquisition (LinkedIn CXO/ops persona, Google search "Cashfree automation")
- Partner co-marketing (Zoho, WhatsApp BSPs)
- Pricing live: free tier + Pro tier

---

## 11. Decision Rights (Decide / Input / Notify)

> Note: "DIN" in this section ≠ DIN brief in §0. This is the lightweight decide/input/notify framework for tactical decisions. The DIN brief in §0 is the gating mechanism for the launch itself.


| Decision | Decide | Input | Notify |
|---|---|---|---|
| Beta merchant selection criteria | PMM | Sales, CS, SMB head | Reeju, Mohit |
| Beta cohort composition (the 20 merchants) | PMM + CSM lead | Sales, SE | Reeju |
| Pricing model + GA tiers | Reeju + PMM | Finance, SMB, Sales | All-hands |
| Connector roadmap | Product | Sales, CS, beta merchants | PMM |
| Template library priorities | PMM | Beta merchants, CS | Product |
| Public beta gate (Go/No-Go) | PMM + Product | Reeju | All-hands |
| GA launch date | Reeju | PMM, Product, Sales | All-hands |

---

## 12. Top Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Wrong merchants in beta** (false negatives) | High | Critical | Hard-gate the 4 filters. Don't dilute for "diversity" or politics. |
| **No-template gap kills self-serve at public beta** | High | High | Block public beta until ≥10 templates exist. Templates sourced from live private beta workflows. |
| **Beta merchants build workflows then churn** | Medium | High | Stickiness sub-goal (≥30% with workflow firing 5×/week 2). CSM check-in at day 14 on stuck merchants. |
| **Razorpay copies the wedge** | Medium | Medium | Move fast on connector + trigger expansion. Lock partner co-marketing (Zoho, WhatsApp BSPs) before they catch up. |
| **Pricing model misjudged** | Medium | Medium | Late-beta WTP conversations. Anchor ₹999–1,999/month Pro tier. |
| **AI connector misuse** (LLM sends bad customer message) | Low | High | Default AI to "draft, not send." Human approval node optional but recommended in templates. |
| **Connector reliability (third-party breakage)** | Medium | High | Per-connector health dashboard. Auto-retry. Status page. |

---

## 13. Reporting Cadence

- **Weekly to Reeju + Mohit:** 5-line update (activations, top workflows built, top connector requests, blockers, next week's focus)
- **Bi-weekly all-hands:** beta progress slide (5 min)
- **Monthly:** cohort retention + 3 customer quotes + use case taxonomy update
- **Public beta gate review:** formal Go/No-Go decision with leadership at end of Week 6
