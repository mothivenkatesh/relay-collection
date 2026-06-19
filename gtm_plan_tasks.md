# Cashfree Relay — GTM Plan with Tasks & Sub-tasks

**Owner key:** Mothi = PMM lead | Samir = Design | TBD = owner not yet assigned
**Date created:** 2026-05-06
**Anchoring thesis:** Cashfree Relay is the Payments MCP. Position underneath the agent layer.

---

## Phase 0 — Pre-Launch Foundation (T-30 to T-0, before Wave 1)

### 0.1 Strategic alignment
| Task | Sub-tasks | Owner | Dependency |
|---|---|---|---|
| Lock Payments MCP positioning with leadership | Walk Reeju + Mayank through Section 5; get sign-off on hero copy in Section 17; document objections | Mothi | TBD (Reeju calendar) |
| Align Eng on MCP commitment timeline | Confirm 6–8 week production-grade MCP path with OAuth + HITL; surface slip risks weekly | Mothi | TBD (Vinesh, Subramanian) |
| Lock template library source-of-truth | Re-read `08-template-library-spec.md`; freeze "live vs roadmap" labels for all surfaces | Mothi | — |
| Confirm Bolna build-partner deliverables | Quantified outcome by LD-7, founder quote by LD-5, blog co-byline by LD+10 | Mothi | TBD (Govardhan, Bolna) |

### 0.2 DIN approval gate (binding path)
| Task | Sub-tasks | Owner | Dependency |
|---|---|---|---|
| File DIN-RELAY-2026-Q2-001 | Compile 9 mandatory artifacts; route for 5 eSignatures (Reeju, Mayank, Ram, Mohit, Sales lead); track 8–10 day cycle | Mothi | TBD (DIN secretariat) |
| Prep PR questionnaire | Update `06-pr-questionnaire-completed.md`; circulate for legal/compliance review | Mothi | TBD (Legal) |
| Compliance signoff on HITL claims | Walk Compliance through audit-by-default + 90-day retention claim; document objections | Mothi | TBD (Compliance) |

### 0.3 Beta merchant pipeline (Wave 1)
| Task | Sub-tasks | Owner | Dependency |
|---|---|---|---|
| Build 4-filter beta selection criteria | Define ICP (5–50 person merchants, founder/owner-operator); document hard-gate rules | Mothi | — |
| Source 100 beta merchants | Pull from Cashfree CRM by criteria; validate fit; assign white-glove onboarding owner | Mothi | TBD (Sales, Mohit) |
| Draft 4-email cohort recruitment sequence | Refresh `05-launch-emails.md` to Payments MCP voice; A/B test subject lines | Mothi | — |

---

## Phase 1 — Wave 1: Quiet Public Preview (May 2026)

### 1.1 Surface readiness
| Task | Sub-tasks | Owner | Dependency |
|---|---|---|---|
| Ship landing page v3 (Payments MCP frame) | Update hero copy from `cashfree-relay-landing-v2.html`; add architecture closer; new pricing strip | Mothi | Samir (visual refresh, italic-serif treatment) |
| Build "How it works" diagram | Show 4 surfaces (Skills + MCP + builder + templates) feeding 1 engine on 1 SoR | Mothi | Samir (diagram design) |
| MCP install flow page | One-command install snippets for Claude Code, Cursor, ChatGPT directories | Mothi | TBD (Eng — install scripts) |
| Skills CLI quickstart page | Copy + screenshots of `npx @cashfreepayments/agent-skills add skills` flow | Mothi | Samir (screenshot polish) |
| Pricing page | Free/Starter/Growth/Outcome/Enterprise tiers from Section 10; preview pricing banner | Mothi | Samir (pricing table layout) |

### 1.2 Content (launch-day blogs)
| Task | Sub-tasks | Owner | Dependency |
|---|---|---|---|
| Blog 1: "Introducing Cashfree Relay: the Payments MCP for India" | 1,200–1,500 words, Reeju voice; route through Reeju for edits | Mothi | TBD (Reeju review) |
| Blog 2: "How Cashfree Relay Works" | 1,500–1,800 words; Vinesh + Eng co-byline; technical architecture deep-dive | Mothi | TBD (Vinesh) |
| Blog 3: "Relay Payment Guardrails" | 1,000–1,200 words; HITL trust play; Compliance review | Mothi | TBD (Compliance) |
| Blog hero images for all 3 | Concept + brief; brand-locked Cashfree treatment | Mothi | Samir |

### 1.3 Distribution & directories
| Task | Sub-tasks | Owner | Dependency |
|---|---|---|---|
| Submit to Anthropic MCP directory | Server manifest, screenshots, install flow validation | Mothi | TBD (Eng — manifest) |
| Submit to Cursor MCP registry | Listing copy, install steps | Mothi | TBD (Eng) |
| Submit to ChatGPT app directory | Listing copy, screenshots | Mothi | Samir (screenshots) |
| Submit to OpenAI Agent Builder + Google Gemini Extensions | Counter-endorsement to Anthropic-Razorpay narrative | Mothi | TBD (Govardhan — partner intros) |

### 1.4 Internal enablement
| Task | Sub-tasks | Owner | Dependency |
|---|---|---|---|
| Sales one-pager | Pillars from Section 6; objection handling; pricing cheat sheet | Mothi | Samir (one-pager design) |
| Sales pitch deck | 12 slides; Payments MCP frame; competitive section reframing Razorpay | Mothi | Samir (deck design) |
| Internal FAQ (Section 16 guardrails) | What to avoid saying; cultural framing rules; Razorpay reframe script | Mothi | — |
| Pulse + dashboard banner copy | "Public preview" framing; HITL emphasis | Mothi | TBD (Product — banner placement) |

### 1.5 Beta ops & telemetry
| Task | Sub-tasks | Owner | Dependency |
|---|---|---|---|
| Define Wave 1 success metrics | 100 merchants on ≥1 workflow; 1k MCP installs; 500 Skills installs; 3 case studies; 5 directory listings | Mothi | TBD (Gopi — dashboard access) |
| Weekly merchant feedback loop | 30-min sessions; capture template requests + pain points; feed Wave 2 priorities | Mothi | — |
| Case study pipeline | Identify 3 candidate merchants by T+30; outcome interviews; quote approvals | Mothi | TBD (Bolna + 2 others) |

---

## Phase 2 — Wave 2: Flagship GA Launch (Q3 2026)

### 2.1 Pre-conditions (T-60 to T-0)
| Task | Sub-tasks | Owner | Dependency |
|---|---|---|---|
| Track 6 specialist agents shipping | Weekly status with Eng on RTO Recovery, Refund Triage, Cart Recovery, Dispute Response, Settlement Reconciler, Subscription Recovery | Mothi | TBD (Vinesh, Subramanian) |
| Outcome pricing tier live | Walk through 5–8% recovery model; legal contracts template; Finance signoff | Mothi | TBD (Finance, Legal) |
| Production MCP w/ OAuth + HITL default | Track from MCP commitment memo | Mothi | TBD (Eng) |
| ISV partner program with 3 named launch partners | Govardhan-led; Mothi co-drafts launch-partner brief | Mothi | TBD (Govardhan) |

### 2.2 Launch-day cascade content (Section 12)
| Task | Sub-tasks | Owner | Dependency |
|---|---|---|---|
| Reeju LD-1 teaser LinkedIn post | Quiet 60-word teaser; ghost-writes for Reeju | Mothi | TBD (Reeju approval) |
| Reeju LD founder LinkedIn post | Substantive 250-word; Payments MCP narrative; ghost-writes for Reeju | Mothi | TBD (Reeju approval) |
| Ram + leadership repost copy | 3 variants for leadership reuse | Mothi | TBD (Comms team) |
| Team broadcast email + dashboard banner + in-app + Pulse | All-hands launch comms package | Mothi | Samir (banner art), TBD (Product) |
| PR embargo kit | Press release, fact sheet, exec quotes, image assets, demo video link | Mothi | Samir (image assets), TBD (PR agency) |

### 2.3 Influencer + webinar cascade (LD+1 → LD+21)
| Task | Sub-tasks | Owner | Dependency |
|---|---|---|---|
| 5–8 mid-sized influencer briefs | Identify dev/fintech voices; one drop per day LD+1 → LD+5; provide angle, not script | Mothi | — |
| Webinar 1: Live build (LD+7) | Title, abstract, registration page, demo script | Mothi | Samir (registration page), TBD (Vinesh — demo) |
| Webinar 2: Bolna in production (LD+14) | Title, abstract, Bolna co-host coordination, registration page | Mothi | TBD (Govardhan, Bolna) |
| Builder's Day virtual event (LD+21) | "Run Cashfree Anywhere"; agenda, speakers, registration, content kit | Mothi | TBD (Govardhan, Marketing) |

### 2.4 Day 1–30 content
| Task | Sub-tasks | Owner | Dependency |
|---|---|---|---|
| Blog 4: "How Cashfree teams use Relay" | LD+7; eat-our-own-cooking; internal interviews | Mothi | TBD (internal users) |
| Blog 5: Bolna case study | LD+14; co-byline; quantified outcomes | Mothi | TBD (Bolna) |
| Blog 6: "One-click extension for Claude and Codex" | LD+21; distribution expansion story | Mothi | TBD (Eng — install validation) |
| Tutorial blogs (1/week) | Auto-onboard, fraud detection, live books in Sheets, payment-failure churn | Mothi | — |
| Opinion blog: "Why we built Relay differently from Razorpay Agent Studio" | LD+10; Reeju POV; ghost-writes | Mothi | TBD (Reeju approval) |
| SEO/category piece: "Why generic workflow tools don't speak payments" | Category-creation piece; Payments MCP claim | Mothi | — |

### 2.5 Wave 2 metrics & reporting
| Task | Sub-tasks | Owner | Dependency |
|---|---|---|---|
| Wave 2 success scorecard | 500 paying merchants, ~₹12–15 cr ARR, 1 outcome contract, 8 launch partners | Mothi | TBD (Gopi — data access) |
| Weekly leadership update | Reeju + Mayank + Mohit; 5-bullet format; surface slip risks | Mothi | — |
| Post-launch retro at LD+30 | Wins, slips, Wave 3 priorities; circulate to leadership | Mothi | — |

---

## Phase 3 — Risk Watch (continuous)

| Risk | Mitigation Task | Owner | Dependency |
|---|---|---|---|
| MCP server slips past launch | Weekly Eng status; pause public-facing positioning if MCP not live by T+30 | Mothi | TBD (Eng) |
| Wrong merchants in beta | Hard-gate the 4-filter selection; resist political dilution | Mothi | TBD (Sales) |
| <10 templates at public beta | Block public beta until template count ≥10; source from private beta workflows | Mothi | TBD (Eng + merchants) |
| Razorpay GAs Agent Studio with public pricing during preview | No reaction; publish a "why we differ" explainer on standby | Mothi | — |
| Anthropic announces exclusive Razorpay MCP partnership | Lock OpenAI Agent Builder + Google Gemini listings before LD | Mothi | TBD (Govardhan) |
| Beta merchants find templates too narrow | White-glove onboarding 30 days; template request log feeds Wave 2 | Mothi | — |
| Press picks up Wave 1 unprompted | Standard reply scripted: "public preview, four automations live, more shipping" | Mothi | — |
| <6 launch partners by LD-2 | Ship with 4; accept slip rather than delay | Mothi | TBD (Govardhan) |
| AI node misuse leaks PII | Default AI to draft-not-send; HITL approval; legal/DPDP signoff before LD | Mothi | TBD (Legal, Compliance) |
| Pricing model misjudged | Late-beta WTP conversations; anchor ₹999–1,999 Pro | Mothi | TBD (Finance) |

---

## Phase 4 — Cross-cutting Workstreams

### 4.1 Design dependencies (all routed through Samir)
- Landing page v3 visual refresh + italic-serif hero
- "How it works" 4-surface diagram
- MCP install flow + Skills CLI screenshots
- Pricing table layout (5 tiers)
- Sales one-pager + 12-slide pitch deck
- Blog hero images (3 launch + 5 Day 1–30)
- Dashboard banner + in-app launch art
- PR kit image assets
- Webinar + Builder's Day registration pages

### 4.2 TBD owners to confirm before T-21
- Eng lead on MCP production hardening (Vinesh / Subramanian)
- Reeju calendar block for blog reviews + LinkedIn posts
- Govardhan deliverables on 6 launch partners
- Compliance + Legal signoffs on HITL + outcome-pricing contracts
- Finance signoff on pricing tiers + outcome model
- Gopi for dashboard + telemetry access
- PR agency for embargo kit + tier-1 press
- Bolna case study + webinar coordination

---

## Single Critical Path

**DIN approval (8–10 business days) → 9 artifacts → 5 eSignatures → Wave 1 starts → 100 merchants + 3 case studies → Wave 2 GA.**

If DIN artifacts slip 3 days, launch slips a full week. Mothi tracks DIN status daily from filing.

---

## How to use this plan

1. Copy each phase block into Notion as a project; each row becomes a task.
2. Owner = Mothi by default. Dependencies flagged "Samir" route to design queue. "TBD" tasks need owner confirmation before T-21.
3. Update weekly against the success scorecard (Section 2.5) and risk watch (Phase 3).
4. Anchor every external claim against `cashfree-relay-context.md` Section 4 + `08-template-library-spec.md`.
