# Relay Merchant Pitch Deck — Session Notes
**Date:** 2026-05-21
**Outputs:** `relay_merchant_pitch_2026_05_21.html` · `Cashfree_Relay_Pitch_2026_05_21.pptx`

---

## What this deck is
Merchant-facing pitch deck for Cashfree Relay (Early Beta). Goal: generate demo calls via AMs sharing directly with merchants. 12 slides. Not AM-facing — no internal language.

## Design system
Sarvam buildathon style: Google Sans, `--green:#00B488`, no pills/dots, `.step` border-left blocks, `.pbox/.prow` property tables, `.eyebrow` with green line, `.insight` with `=>` prefix, `.tag` at 2px border-radius, dark divider slides.

## Slide structure
| # | Slide |
|---|-------|
| 00 | Title — "For years, software helped you see the problem." |
| 01 | Dark divider — "Walk us through your Monday morning." |
| 02 | The Morning — Reddit quotes, 3 time-stamped ops steps |
| 03 | Cost Table — 5 manual tasks with ₹ cost (no competitor names) |
| 04 | Dark divider — "Not another dashboard. A team that does the work." |
| 05 | What Relay Is — 3 cards: event/schedule trigger, no developer, data stays |
| 06 | Connectors — Cashfree (trigger) + 7 act-via + Gemini/OpenAI (AI inside agent) |
| 07 | Five AI Agents — COD Confirmation, Failed Payment Recovery, Abandoned Cart, Settlement Recon, High-Value Alert |
| 08 | COD Before/After — step-by-step contrast with RTO stats |
| 09 | What Relay Does — 4-row property table |
| 10 | Get Started — 3 steps + pricing/data/access pbox |
| · · | Closing — "Which problem do you want to stop doing by hand?" |

## Key decisions made this session
- **"AI Agent" not "Agent"** — all product noun references use "AI Agent"
- **"Early Beta" not "Preview Beta"** — explicit throughout
- **No competitor names** — Zapier, n8n, Interakt, AiSensy removed; table rebuilt around merchant's own costs
- **Trigger types** — both event-triggered (Payments, Refunds, Disputes) AND schedule-based; "Not on a schedule" language removed
- **No mobile app reference** — removed "You open your phone. The AI agents already ran."
- **No Razorpay attribution** — removed "Dushyant Panda · Razorpay FTX26" attribution
- **Contact:** mothi.venkatesh@cashfree.com (not relay@cashfree.com)
- **No em dashes in prose** — replaced throughout (verbatim merchant quotes preserved)

## Connectors live in product (as of 2026-05-21)
| Category | Integration | Actions |
|----------|-------------|---------|
| Trigger | Cashfree Payments | 11 |
| Trigger | Schedule | — |
| Act | WhatsApp Business | 2 |
| Act | Google Sheets | 1 |
| Act | Slack | 4 |
| Act | Gmail | 2 |
| Act | Google Calendar | 2 |
| Act | Calendly | 1 |
| Act | HTTP | 1 |
| AI | Google Gemini | 6 |
| AI | OpenAI | 9 |

## PPTX notes
- Generated via `relay_pitch_to_pptx.py` using python-pptx 1.0.2
- Slide size: 10 × 5.625 inches (Google Slides 16:9)
- Font: Calibri (swap to Google Sans in Google Slides after import)
- To open as Google Slides: Drive → Upload → Right-click → Open with Google Slides
