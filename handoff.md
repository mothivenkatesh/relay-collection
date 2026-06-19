# Cashfree Relay Skills — Developer Handoff Note

**Date:** May 2026
**Author:** Mothi Venkatesh, Developer Ecosystem, Cashfree
**Scope:** 13 Relay workflow templates + 1 TurboPass skill + 1 master builder/router

---

## What These Are

Production-ready Relay workflow templates for Cashfree Secure ID V2 APIs. Each skill is a `.md` file that functions as a Claude skill — when invoked, it generates complete Relay YAML workflow configs + API integration code (Node.js/Python) for a specific KYC/onboarding use case.

Intended users: Cashfree merchants and internal sales engineers who want to go from "I need KYC" to a running integration without starting from scratch.

---

## What It Took to Build

### 1. API Verification Pass
Every API endpoint, content-type, field name, and response schema was verified against live Cashfree V2 documentation before being included in any skill. Key corrections made during this process:

| What was wrong | What's correct |
|---|---|
| `/smart-ocr` | `/bharat-ocr` |
| Face APIs using JSON + base64 | `multipart/form-data` with raw binary |
| Face match fields `selfie`/`face_reference` | `first_image` / `second_image` |
| Mobile360 marked as internal | Confirmed public: `/mobile360/otp/send` + `/mobile360/otp/verify` |
| eSign path `/esign/v3/request` | `/esignature` (create) + `/esignature/document` (upload) |
| VKYC add-user path `/vrs/v2/video-kyc/add-user` | `POST /user` |
| Hardcoded `https://api.cashfree.com/verification/` | `{{BASE_URL}}/` template variable |
| `DRIVING_LICENSE` | `DRIVING_LICENCE` (British spelling, per API docs) |
| Missing `x-api-version: 2024-12-01` header | Required for `aadhaar_seeding_status` in PAN response |

### 2. Voice of Customer — Two Input Sources

**Source A: Internal call notes** (Kotak, IDFC First, SBM, Dhani, Standard Chartered, RBL, 50Fin, Vivriti Capital, ESAF SFB, Spandana Sphoorty, Motilal Oswal, ~25 other accounts)

Key findings translated into workflow nodes:
- **Name format reversal** (50Fin): Aadhaar returns "SURNAME FIRSTNAME", PAN returns "FIRSTNAME SURNAME" — added token-sort retry before flagging name mismatch
- **30% PAN input drop-off** (Motilal Oswal): Mobile360 returns `pan_details.pan_number` at 70% fill rate — added pre-fill node to skip manual PAN entry
- **40-45% VKYC completion rate** (Standard Chartered, RBL): Primary cause is 24hr link expiry with no nudge — added 4hr pre-expiry nudge + rescheduling node
- **Jandhan account detection** (Spandana Sphoorty): MFI disbursements fail on Jandhan accounts — added BAV flag
- **t+1/t+7/t+30 monitoring tiers** (HDFC Bank panel): Don't wait for t+30 to run first check — added tiered model in continuous monitoring
- **Multilingual VKYC** (Vivriti Capital): Rural customers drop off when agent doesn't speak their language — added `preferred_language` in VKYC meta
- **Age >65 routing** (50Fin): Elderly customers struggle with unassisted VKYC — added `assisted_preferred: true` flag
- **Signature capture** (ESAF SFB): Needed for cheque book issuance — added optional VKYC annotation node

**Source B: HyperVerge WealthTech Onboarding Excellence Report (37 pages)**

Key findings that drove two entirely new skills:
- Selfie drop-off at **29.2%** is the #1 abandonment point in wealthtech — drove the selfie recovery orchestrator in `relay-wealthtech-broker`
- PAN form drop-off at **17.22%** — confirmed Mobile360 pre-fill as the fix
- SEBI VKYC requirements differ from RBI (trained officer, geolocation, tamper-proof storage)
- KRA (NSDL/CDSL) lookup-first path eliminates re-onboarding for existing investors
- Nomination is a standalone step (2024 SEBI: handwritten → electronic)
- NRI accounts require passport as primary ID, overseas address proof, FATCA/CRS, PIS permission

### 3. Battletest Pass

A systematic review of all 11 original skills for:
- Wrong API paths/formats
- Missing hard-reject conditions (fraud_account BAV, forgery detected)
- Missing retry/recapture logic (face liveness ×3 pattern)
- Missing DigiLocker expiry → regen → SmartOCR fallback chains
- Stale internal endpoint warnings that were no longer accurate
- Rate limit violations (BAV: 15 calls/account/24hr — added dedup guards)

---

## Architecture Decisions

**`{{BASE_URL}}` pattern everywhere** — Never hardcode `https://api.cashfree.com/verification`. All skills use `{{BASE_URL}}` so merchants can point at sandbox vs. production without editing YAML.

**Amber flag accumulator** — The risk decision model is consistent across all banking skills: 0 AMBER = approve straight-through, 1-2 AMBER = VKYC or manual review, 3+ AMBER = EDD/reject. Every flag has an explicit weight.

**Hard reject vs. soft flag** — Clear separation: PAN INVALID/DELETED, forgery detected, fraud_account BAV, face match NO → always hard reject with no retry. Everything else → accumulate AMBER and let the aggregator decide.

**CKYC is on-prem only** — Not a cloud API. Every skill that references CKYC has a `{{env.CKYC_DOCKER_DEPLOYED}}` guard and a documented fallback.

**Relay-partial labeling** — Every skill has a `Relay Status: READY / PARTIAL / BLOCKED` header. PARTIAL means some nodes require external systems (AML engine, device intel, PIS API) that aren't Cashfree APIs. This is explicitly documented so merchants know what they're building vs. what they're integrating.

---

## Skill Inventory

| Skill | Status | Regulatory Basis | Key APIs Used |
|---|---|---|---|
| `relay-builder` | READY | — | Routes to all others |
| `relay-low-risk-cdd` | PARTIAL | RBI risk-based CDD | Mobile360, PAN, BAV, DigiLocker |
| `relay-standard-cdd` | READY | RBI KYC Master 2016 | All core APIs + VKYC |
| `relay-small-ticket` | READY | RBI DLG Guidelines | Mobile360, PAN, BAV, bharat-ocr |
| `relay-gold-verify-pay` | READY | RBI PMLA | PAN, bharat-ocr, face-liveness, BAV |
| `relay-esign-pay` | READY | IT Act 2000 | esignature, PAN, BAV |
| `relay-edd` | PARTIAL | RBI KYC / PMLA | External case mgmt + AML APIs |
| `relay-mule-prevention` | PARTIAL | RBI AML circular | Mobile360, BAV, device intel (external) |
| `relay-gift-city` | PARTIAL | IFSCA KYC Direction 2022 | All core + VKYC (GPS gap TBC) |
| `relay-existing-customer` | BLOCKED | RBI 2yr/8yr/10yr mandate | CKYC (on-prem), PAN, BAV, biometric |
| `relay-continuous-monitoring` | PARTIAL | RBI KYC Master 2023 | PAN, BAV, cron triggers |
| `relay-wealthtech-broker` | PARTIAL | SEBI KYC Master 2023 | All core + KRA (external) + VKYC |
| `relay-nri-wealthtech` | PARTIAL | SEBI/FEMA/RBI PIS | Passport, bharat-ocr, BAV, VKYC, esignature |
| `turbopass` | READY | — | PAN, DL, bharat-ocr, face-liveness, Mobile360 |

---

## What Still Needs Work

1. **Live sandbox test** — Test script at `/tmp/cashfree_sandbox_test.py` is ready. Needs `CLIENT_ID` and `CLIENT_SECRET` from sandbox.cashfree.com → Secure ID → Developers. Run against: `/pan`, `/name-match`, `/bank-account/sync`, `/bharat-ocr`, `/face-liveness`, `/driving-license`.

2. **GPS geo-tagging in GIFT City VKYC** — Not confirmed whether GPS metadata comes in VKYC webhook or needs a separate API call. Needs confirmation from Cashfree engineering.

3. **KRA lookup integration** — `relay-wealthtech-broker` has the node spec but KRA (NSDL/CDSL/CAMS) is a separate integration. Each KRA has its own API — not a Cashfree endpoint.

4. **PIS permission API** — `relay-nri-wealthtech` needs a designated bank API (HDFC Securities, ICICI Direct, Axis) for NRI equity trading. Per-bank integration required.

5. **CKYC Docker deployment** — Any skill with CKYC requires on-prem Docker. Cashfree provides the Docker image; merchant provides the host. Documented in `relay-existing-customer`.

6. **`cashfree customer call notes.md` — second half unread** — The file was 63K tokens and only the first half was processed. The remaining accounts (HDFC ERGO expanded, additional bank panels) may contain additional alternate flows worth adding.

---

## File Structure

```
Cashfree-Relay-Skills/
├── HANDOFF.md                        ← this file
├── relay-merchant-use-cases.md       ← brief merchant-facing notes for all 9 Relay use cases
├── relay-builder/skill.md            ← master router (start here)
├── relay-low-risk-cdd/skill.md
├── relay-standard-cdd/skill.md
├── relay-small-ticket/skill.md
├── relay-gold-verify-pay/skill.md
├── relay-esign-pay/skill.md
├── relay-edd/skill.md
├── relay-mule-prevention/skill.md
├── relay-gift-city/skill.md
├── relay-existing-customer/skill.md
├── relay-continuous-monitoring/skill.md
├── relay-wealthtech-broker/skill.md
├── relay-nri-wealthtech/skill.md
└── turbopass/
    ├── skill.md
    └── references/REFERENCE.md
```

---

## How to Use

**As Claude skills:** All 14 folders live in `~/.claude/skills/`. Claude picks them up automatically. Trigger by invoking `/relay-builder` or any specific skill name.

**As standalone templates:** Each `skill.md` is a self-contained document. A developer can read any skill directly and extract the Relay YAML nodes, API request/response examples, and decision logic without needing Claude.

**To add a new skill:** Follow the structure of any existing skill — frontmatter with `name/description/triggers/tools`, then `## Overview`, `## Happy Path`, node YAML specs, `## Node Specifications` table, `## Workflow Diagram`. Register the new skill in `relay-builder/skill.md` intent detection table.
