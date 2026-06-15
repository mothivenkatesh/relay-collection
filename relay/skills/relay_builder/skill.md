---
name: relay-kyc-journey
description: Cashfree KYC Journey Builder — RBI-licence-aware intake skill that identifies merchant use case, routes to the correct regulated workflow, and generates working integration code + compliance brief. Covers PA domestic, PA-CB cross-border, PPI wallet, SEBI/FEMA wealthtech, and Banking KYC paths. MCP-ready — when Relay connects Secure ID APIs, creates and publishes the workflow live during the conversation.
triggers:
  - /relay-kyc-journey
  - /relay-builder
  - build kyc
  - kyc setup
  - start KYC integration
  - what KYC do I need
tools:
  - Read/Write
---

# Cashfree KYC Journey Builder

> Describe what you're building. I'll identify the correct RBI licence path, pick the right workflow, generate working integration code, and give you a compliance brief — in one shot.

---

## Hard rules — enforced on every skill invocation

**1. Only Cashfree Secure ID APIs in workflow nodes.**
Every `"call"` in a workflow JSON node must map to a documented Secure ID endpoint. If a required step has no Secure ID equivalent, do NOT generate the workflow node for it. Surface it as ❌ Not included in the What's covered table and describe what the user must build outside Relay.

**Secure ID API reference (complete list):**
`POST /mobile360/otp/send` · `POST /mobile360/otp/verify` · `POST /pan` · `POST /digilocker` · `POST /bharat-ocr` · `POST /face-liveness` · `POST /face-match` · `POST /name-match` · `POST /bank-account/sync` · `POST /gstin` · `POST /vkyc` · `POST /esignature`

**2. Never name or hardcode third-party vendors.**
External steps (CPV scheduling, antecedent/background checks, KRA lookup, AD Bank) stay as env var placeholders only: `{{CPV_SCHEDULING_URL}}`, `{{ANTECEDENT_CHECK_API_URL}}`, `{{KRA_URL}}`. Even if the user names their vendor ("we use X"), keep the workflow JSON vendor-agnostic. Never put a real third-party URL in a `"call"` field.

---

## RBI Licence Context

Cashfree holds three RBI licences. Each licence has distinct KYC obligations. Confirm which licence applies before picking a skill.

| Licence | Reference | What it covers | Key KYC obligation |
|---|---|---|---|
| **Payment Aggregator (PA)** | RBI/DPSS/2025-26/141 (Sep 15, 2025) | Domestic merchant onboarding + customer payments | CKYCR-first for all merchants; tiered CDD by turnover |
| **PA – Cross Border (PA-CB)** | RBI FEMA/CB-PA circular | Imports: foreign merchant acquiring; Exports: Indian exporter settlements | Buyer DD at ₹2.5L+; EDPMS/IDPMS flagging; ₹25L/txn cap |
| **Prepaid Payment Instrument (PPI)** | RBI/2017-18/153 (PPI Master Circular) | Wallet / stored-value products | Small PPI (OTP, ₹10K) → Full KYC PPI (OVD+PAN, ₹2L) upgrade path |

> **Enterprise mandate:** FIU-IND registration is mandatory for all three licence types before processing the first transaction. STR due within 7 working days of suspicion; CTR by the 15th of the succeeding month for transactions >₹10L.

---

## Quick pick

| I'm building… | Skill | Licence |
|---|---|---|
| **PA merchant onboarding (CKYCR-first, tiered CDD)** | `/relay-pa-merchant` | **PA** |
| **Cross-border — Indian exporter KYC (EDPMS)** | `/relay-pa-cb-export` | **PA-CB** |
| **Cross-border — foreign merchant / buyer KYC (IDPMS)** | `/relay-pa-cb-import` | **PA-CB** |
| **PPI wallet (Small → Full KYC upgrade path)** | `/relay-ppi-wallet` | **PPI** |
| BNPL / quick loans / gig credit (<₹60K) | `/relay-small-ticket` | Banking/NBFC |
| Bank / NBFC / savings account onboarding | `/relay-standard-cdd` | Banking |
| Existing customer — re-KYC / periodic refresh | `/relay-existing-customer` | Banking/NBFC |
| Low-friction second product for known customer | `/relay-low-risk-cdd` | Banking/NBFC |
| Gold loan / high-value secured lending | `/relay-gold-verify-pay` | Banking/NBFC |
| Collect eSign before payment | `/relay-esign-pay` | Any |
| Demat / trading / MF account (SEBI) | `/relay-wealthtech-broker` | SEBI |
| NRI investor account (SEBI/FEMA) | `/relay-nri-wealthtech` | SEBI/FEMA |
| Gig worker / two-wheeler loan (DL-first, no Aadhaar) | `/relay-quickpass` | Banking/NBFC |
| Mule / fraud detection at onboarding | `/relay-mule-prevention` | Any |
| GIFT City / IFSCA regulated account | `/relay-gift-city` | IFSCA |
| Post-activation AML / transaction monitoring | `/relay-continuous-monitoring` | Any |
| High-risk / Enhanced Due Diligence | `/relay-edd` | Any |

---

## Not sure? Answer 5 questions.

**1. Which RBI licence path applies?**
PA domestic · PA-CB cross-border · PPI wallet · SEBI wealthtech · Banking/NBFC · IFSCA

**2. What sector?**
Lending · Banking · Wealthtech · Insurance · D2C/BNPL · B2B SaaS · Merchant onboarding

**3. Average loan or transaction size?**
<₹60K · ₹60K–₹5L · >₹5L · Merchant turnover >₹40L annual

**4. New or existing customers?**
New · Existing (re-KYC or new product) · Both

**5. Any hard requirements?**
Video KYC mandatory · eSign before payment · Multilingual agents · NRI customers · SEBI-regulated · GIFT City · Cross-border · DL-only (no Aadhaar)

### Route map

| Licence | Sector | Use case | Skill |
|---|---|---|---|
| PA | Merchant | CKYCR onboarding ≤₹40L turnover | `relay-pa-merchant` (Simplified CDD) |
| PA | Merchant | CKYCR onboarding >₹40L turnover | `relay-pa-merchant` (Full CDD) |
| PA-CB | Export | Indian exporter KYC | `relay-pa-cb-export` |
| PA-CB | Import | Foreign merchant / buyer DD | `relay-pa-cb-import` |
| PPI | Wallet | Small PPI → Full KYC upgrade | `relay-ppi-wallet` |
| Banking | Lending | <₹60K BNPL | `relay-small-ticket` |
| Banking | Banking | New customer | `relay-standard-cdd` |
| Banking | Banking | Existing customer | `relay-low-risk-cdd` |
| Banking | Secured | Gold / high-value loan | `relay-gold-verify-pay` |
| Banking | Gig/2W | DL-first, no Aadhaar | `relay-quickpass` |
| SEBI | Wealthtech | Demat / MF | `relay-wealthtech-broker` |
| SEBI/FEMA | Wealthtech | NRI investor | `relay-nri-wealthtech` |
| Any | Fraud | Mule detection | `relay-mule-prevention` |
| IFSCA | GIFT City | Offshore fund | `relay-gift-city` |
| Any | EDD | PEP / sanctions / adverse media | `relay-edd` |
| Any | Monitoring | Post-activation cron + anomaly | `relay-continuous-monitoring` |
| Any | Re-KYC | Perpetual KYC refresh | `relay-existing-customer` |

---

## What every skill generates

**1. Integration code**
Working Node.js backend + React frontend + webhook handler. Set 5 env vars, paste, done.

**2. Relay workflow spec**
Compact JSON — import into Relay's visual builder today, or auto-created via MCP when Relay connects Secure ID APIs.

**3. Compliance brief**
One table: covered / needs config / your responsibility. Regulation cited per workflow — RBI Master Direction reference, FIU-IND obligations, monetary thresholds, CKYCR mandate where applicable.

---

## Sandbox setup (do this once)

Get credentials from [sandbox.cashfree.com](https://sandbox.cashfree.com) → Secure ID → Developers.

```env
CASHFREE_CLIENT_ID=
CASHFREE_CLIENT_SECRET=
CASHFREE_BASE_URL=https://sandbox.cashfree.com/verification
CASHFREE_WEBHOOK_SECRET=    # set under Dashboard → Webhooks
BASE_URL=http://localhost:3000
RELAY_WORKFLOW_ID=          # get after importing workflow into Relay
```

Switch to production: change `CASHFREE_BASE_URL` to `https://api.cashfree.com/verification`. Nothing else changes.

---

## Enterprise pre-flight checklist

Before going live with any PA / PA-CB / PPI workflow:

| Requirement | Who owns it | Action |
|---|---|---|
| FIU-IND registration (goAML portal) | Compliance | Before first transaction |
| Board-approved KYC/AML policy | Board/Legal | Before onboarding first merchant or customer |
| Designated Director nomination | Board | Before FIU-IND registration |
| CKYCR upload mandate (10 business days) | Compliance/Engineering | After each KYC completion |
| STR filing system (7 working days from suspicion) | Compliance | Before go-live |
| CTR filing (>₹10L, by 15th of next month) | Compliance | Before go-live |
| 10% beneficial ownership disclosure policy | Legal | Before merchant onboarding |

---

## MCP — coming soon

Cashfree Relay already has MCP. Secure ID APIs are connecting soon.

When live, any skill invocation creates the workflow live during the conversation:

```
/relay-pa-merchant

→ Claude asks: "Simplified CDD (≤₹40L) or Full CDD? CKYCR Docker deployed?"
→ Calls Relay MCP → create_workflow(template, config)
→ Calls Relay MCP → publish_workflow(workflow_id)
→ Returns your RELAY_WORKFLOW_ID, already live
→ Outputs integration code pre-filled with that ID

Total time: under 60 seconds. No Relay UI. No import.
```

### MCP tool definitions (Relay × Secure ID)

```json
[
  {
    "name": "create_relay_workflow",
    "description": "Creates a KYC workflow in Cashfree Relay from a named template",
    "parameters": {
      "template": "pa_merchant | pa_cb_export | pa_cb_import | ppi_wallet | small_ticket | standard_cdd | low_risk_cdd | gold_verify | esign_pay | wealthtech_broker | nri_wealthtech | relay_quickpass | mule_prevention | gift_city | edd | continuous_monitoring | existing_customer",
      "name": "string",
      "config": {
        "vkyc_enabled": "boolean",
        "ckyc_docker_deployed": "boolean",
        "cdd_tier": "SIMPLIFIED | FULL",
        "preferred_languages": ["hi", "ta", "te", "kn", "ml", "bn"],
        "face_threshold": "number (default 0.75)",
        "high_value_threshold_inr": "number (default 1000000)"
      }
    },
    "returns": { "workflow_id": "string", "status": "DRAFT" }
  },
  {
    "name": "publish_workflow",
    "description": "Publishes draft workflow — makes it live and triggerable via API",
    "parameters": { "workflow_id": "string" },
    "returns": { "workflow_id": "string", "status": "LIVE", "trigger_url": "string" }
  },
  {
    "name": "get_workflow_test_url",
    "description": "Returns sandbox test URL with pre-filled test data",
    "parameters": {
      "workflow_id": "string",
      "test_mobile": "string (default: 9999999999)"
    },
    "returns": { "test_url": "string", "expires_in_minutes": 30 }
  },
  {
    "name": "get_workflow_run_status",
    "description": "Checks status of a KYC run",
    "parameters": { "run_id": "string" },
    "returns": {
      "status": "APPROVED | REJECTED | VKYC_REQUIRED | MANUAL_REVIEW | IN_PROGRESS",
      "flags": "string[]",
      "cost_inr": "number"
    }
  }
]
```
