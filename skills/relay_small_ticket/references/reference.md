# Reference: Small Ticket Lending Template — Full Specs

## BAV Status Codes

| account_status_code | Meaning | Action |
|---|---|---|
| `ACCOUNT_IS_VALID` | Active account | PASS |
| `INVALID_ACCOUNT_FAIL` | Account doesn't exist | REJECT |
| `ACCOUNT_BLOCKED` | Account suspended | REJECT |
| `INVALID_IFSC_FAIL` | IFSC code invalid | Ask for correction, retry |
| `NRE_ACCOUNT_FAIL` | Non-resident external account | REJECT (unsupported) |
| `fraud_account` | Flagged as fraudulent | HARD REJECT + flag |
| `npci_unavailable` | NPCI system down | Retry after 5 min |
| `failed_at_bank` | Bank-side failure | Retry once |
| `connection_timeout` | Timeout | Retry once |
| `source_bank_declined` | Bank rejected | Retry via different gateway |
| `bene_bank_declined` | Beneficiary bank declined | REJECT |
| `imps_mode_fail` | IMPS unavailable | Internal: route to UPI fallback |
| `benficiary_bank_offline` | Destination bank offline | Retry after 5 min |

> **Internal note (not for merchant disclosure):** When `name_at_bank = null`, system retries via UPI gateway internally. Do not disclose UPI validation to merchants. `cfbankid = -1` = cached response (same-day). `cfbankid = 0` = fresh validation.

**Banks NOT supported:**
- Deutsche Bank
- Paytm Payments Bank

**IMPS limitation:** IMPS verifies only first 5 characters of IFSC (bank identifier, not branch).

---

## BAV Name Match Scoring — Full Examples

| name_1 | name_2 | Result | Score |
|---|---|---|---|
| Rohan Mathew Thomas | Rohan Mathew Thomas | DIRECT_MATCH | 100.00 |
| Rohan Mathew Thomas | Rohan Thomas | GOOD_PARTIAL_MATCH | 85.00 |
| Rohan Mathew Thomas | Roshan Thomas | MODERATE_PARTIAL_MATCH | 61.00 |
| Rohan Mathew Thomas | Rohan Mathew K | POOR_PARTIAL_MATCH | 55.00 |
| Rohan Mathew Thomas | Rajeev | NO_MATCH | 14.00 |

---

## PAN Status Values

| pan_status | Meaning | Action |
|---|---|---|
| `VALID` | Active, tax-filing individual/entity | Proceed |
| `INVALID` | Does not exist | Hard reject |
| `DELETED` | Removed from ITD database | Hard reject |
| `DEACTIVATED` | Suspended (non-linkage with Aadhaar) | Hard reject |

**PAN type by 4th character:**

| Character | Type | Category |
|---|---|---|
| P | Individual | Individual |
| C | Company | Business |
| F | Firm | Business |
| T | Trust | Business |

**Aadhaar Seeding Status:**

| Value | Meaning |
|---|---|
| Y | Linked — bypass eligible |
| R | Reverse — seeded but not confirmed |
| NA | Not linked — amber flag |

---

## Mobile360 — Full Response Schema

```json
{
  "status": "SUCCESS",
  "verification_id": "...",
  "personal_details": {
    "name": "RAJESH KUMAR",
    "gender": "MALE",
    "dob": "1990-01-15",
    "age": 35,
    "occupation": "Salaried",
    "income": "500000"
  },
  "pan_details": {
    "pan_number": "ABCDE1234F",
    "registered_name": "RAJESH KUMAR",
    "aadhaar_linked": true,
    "masked_aadhaar": "XXXXXXXX1234"
  },
  "credit_score": 720,
  "employment_details": {
    "uan": "101234567890",
    "member_id": "MH/12345/67890",
    "employer_name": "ABC Technologies Pvt Ltd",
    "establishment_id": "MHBAN0012345",
    "joining_date": "2020-04-01",
    "exit_date": null,
    "employer_confidence_score": 85
  },
  "risk_intelligence": {
    "risk_level": "LOW",
    "risk_reason": null,
    "description": "No adverse signals detected"
  },
  "mobile_number_intelligence": {
    "valid": true,
    "subscriber_status": "active",
    "prepaid_postpaid": "postpaid",
    "current_operator": "Reliance Jio",
    "porting_status": "ported"
  },
  "banking_details": {
    "bank_account": "XXXXXXXX1234",
    "ifsc": "HDFC0XXXXX",
    "branch_address": "..."
  },
  "addresses": [
    {
      "full_address": "...",
      "city": "Mumbai",
      "state": "Maharashtra",
      "pincode": "400001",
      "linkage_source": "PAN"
    }
  ],
  "phone_numbers": [...],
  "emails": [...]
}
```

**Fill rates by field:**

| Field Group | Fill Rate | Notes |
|---|---|---|
| personal_details | ~76% | Good reliability |
| pan_details | ~70% | Good reliability |
| addresses | ~70% | PAN-linked address most reliable |
| credit_score | ~70% | Miss ~30% — have Bureau fallback plan |
| employment_details | ~50% | High miss — never depend solely on this |
| banking_details | ~30% | Very unreliable — use BAV instead |

**What Mobile360 does NOT provide (common misconceptions):**
- Digital or behavioural footprint
- Ecommerce addresses
- Vehicle RC / challans / toll data
- Mule account analytics (separate product)
- Skip tracing / nominee tracing
- Derived underwriting scores (RE must build their own model)

---

## DigiLocker Status Values

| Status | Meaning | Action |
|---|---|---|
| `PENDING` | URL generated, user hasn't started | Wait / timeout |
| `AUTHENTICATED` | User completed DigiLocker flow | Proceed to extract documents |
| `EXPIRED` | 10-minute URL expired | Regenerate URL (max 1 retry, then Path B) |
| `CONSENT_DENIED` | User denied DigiLocker consent | Route to SmartOCR path |

---

## SmartOCR — Aadhaar Fields Extracted

```json
{
  "verification_id": "...",
  "reference_id": 12345,
  "document_type": "AADHAAR",
  "extracted_data": {
    "name": "RAJESH KUMAR",
    "dob": "1990-01-15",
    "gender": "MALE",
    "aadhaar_number": "XXXX XXXX 1234",
    "address": {
      "house": "123",
      "street": "MG Road",
      "locality": "Andheri West",
      "city": "Mumbai",
      "district": "Mumbai",
      "state": "Maharashtra",
      "pincode": "400053"
    },
    "care_of": "S/O Suresh Kumar"
  },
  "quality_checks": {
    "blur": false,
    "glare": false,
    "partial": false,
    "black_and_white": false,
    "face_present": true,
    "qr_present": true
  },
  "forgery_checks": {
    "screenshot": false,
    "alteration": false,
    "photo_imposition": false,
    "ai_generated": false
  },
  "verification_status": "SUCCESS"
}
```

---

## Face Liveness — Full Response

```json
{
  "reference_id": 9876,
  "verification_id": "...",
  "status": "SUCCESS",
  "liveness": true,
  "liveness_score": 0.94,
  "gender": {"value": "Male", "confidence": 92},
  "age_range": {"min": 28, "max": 34},
  "eye_wear": {"value": false, "confidence": 88},
  "face_occluded": {"value": false, "confidence": 96},
  "quality": {
    "blur": false,
    "bright": true,
    "exposure": "NEUTRAL"
  },
  "pose": {
    "alignment": "CENTRE",
    "head_turned": false
  },
  "eyes_open": {"value": true, "confidence": 98}
}
```

**Status values:**

| Status | Meaning | Action |
|---|---|---|
| `SUCCESS` | Live face detected | Proceed to Face Match |
| `REAL_FACE_NOT_DETECTED` | Spoof attempt or photo | Re-capture (max 3x) |
| `MULTIPLE_FACES_DETECTED` | More than one face | Re-prompt |
| `FACE_NOT_DETECTED` | No face in image | Re-prompt |

---

## Face Match — Full Response

```json
{
  "status": "SUCCESS",
  "ref_id": 5432,
  "verification_id": "...",
  "face_match_result": "YES",
  "face_match_score": 0.87
}
```

**Status values:**

| Status | face_match_result | Action |
|---|---|---|
| `SUCCESS` | YES | Biometric match confirmed |
| `SUCCESS` | NO | HARD REJECT — biometric mismatch |
| `MULTIPLE_FACE_DETECTED` | NO | HARD REJECT — multiple faces in image |

**Threshold guidance:**
- Default: 0.75 (configurable via `threshold` param, range: 0 < x < 1)
- Conservative (high-value products): 0.80
- Permissive (thin-file segments): 0.70 (increases fraud risk)

---

## Error Codes — All APIs

| HTTP Status | Code | Meaning |
|---|---|---|
| 400 | `pan_missing` | PAN not provided |
| 400 | `pan_length_short` | Invalid PAN format |
| 400 | `verification_id_already_exists` | Duplicate ID — generate new UUID |
| 400 | `otp_expired` | OTP validity expired — re-send OTP |
| 400 | `otp_retry_limit_exhaust` | Too many wrong OTPs — restart flow |
| 401 | `authentication_failed` | Invalid client credentials |
| 403 | `ip_validation_failed` | Server IP not whitelisted |
| 409 | `verification_id_already_exists` | ID reuse detected |
| 422 | `insufficient_balance` | Wallet balance low — recharge account |
| 429 | `too_many_requests_per_operation` | Rate limited — back off |
| 429 | `too_many_requests_per_ip` | IP rate limited |
| 500 | `verification_failed` | Source temporarily unavailable — retry |
| 502 | `verification_failed` | Gateway error — retry with backoff |

---

## CKYC Upload (Post-Onboarding, 10-Day Mandate)

If no existing CKYC record found at onboarding:
- Upload mandate: within 10 days of onboarding
- Upload processing: 48-72 hours
- Max file size: per CERSAI spec
- Format: CERSAI-compliant ZIP

**Upload outcomes:**

| Outcome | Meaning | Action |
|---|---|---|
| SUCCESS | New CKYC ID created | Store CKYC ID, record complete |
| PROBABLE_MATCH | Potential duplicate found | Run Name Match + Face Match to resolve |
| CONFIRMED_MATCH | Existing CKYC found | Link to existing, do not create duplicate |

> **Architecture note:** CKYC upload/download/search must run on-premise (self-hosted Docker). Cannot route through Cashfree cloud. On-premise deployment is a prerequisite for CKYC nodes in Relay.

---

## Relay Node Configuration Reference

```yaml
# Node: PAN Verification
type: http
method: POST
url: "{{BASE_URL}}/pan"
headers:
  x-client-id: "{{env.CLIENT_ID}}"
  x-client-secret: "{{env.CLIENT_SECRET}}"
  x-api-version: "2024-12-01"
  Content-Type: "application/json"
body:
  pan: "{{input.pan}}"
  name: "{{input.name}}"
output_mapping:
  pan_status: "$.pan_status"
  aadhaar_seeding_status: "$.aadhaar_seeding_status"
  name_match_result: "$.name_match_result"
  name_match_score: "$.name_match_score"
  registered_name: "$.registered_name"
conditions:
  - if: "$.pan_status != 'VALID'"
    then: REJECT
    reason: "pan_invalid"
  - if: "$.aadhaar_seeding_status != 'Y'"
    then: ADD_FLAG
    flag: "aadhaar_not_linked"
  - if: "$.name_match_result == 'POOR_PARTIAL_MATCH' OR $.name_match_result == 'NO_MATCH'"
    then: REJECT
    reason: "name_mismatch"
```

```yaml
# Node: BAV Sync
type: http
method: POST
url: "{{BASE_URL}}/bank-account/sync"
headers:
  x-client-id: "{{env.CLIENT_ID}}"
  x-client-secret: "{{env.CLIENT_SECRET}}"
  x-api-version: "2024-12-01"
  Content-Type: "application/json"
body:
  bank_account: "{{input.account_number}}"
  ifsc: "{{input.ifsc}}"
  name: "{{input.name}}"
output_mapping:
  account_status: "$.account_status"
  name_match_result: "$.name_match_result"
  name_match_score: "$.name_match_score"
  name_at_bank: "$.name_at_bank"
retry:
  on: ["npci_unavailable", "connection_timeout", "benficiary_bank_offline"]
  delay: 300  # 5 minutes
  max_attempts: 1
  on_retry_fail: ROUTE_TO_ASYNC
conditions:
  - if: "$.account_status == 'INVALID' OR $.account_status == 'BLOCKED'"
    then: REJECT
  - if: "$.account_status_code == 'fraud_account'"
    then: REJECT_AND_FLAG
  - if: "$.name_match_result == 'MODERATE_PARTIAL_MATCH'"
    then: MANUAL_REVIEW
```

---

## Relay Template — Amber Flag Accumulator

```yaml
# Accumulate amber flags across all nodes
amber_flag_count: 0
amber_flags: []

# At Decision Node:
conditions:
  - if: amber_flag_count == 0
    then: APPROVE
  - if: amber_flag_count >= 1 AND amber_flag_count <= 2
    then: MANUAL_REVIEW
    queue: "credit_ops_review"
  - if: amber_flag_count >= 3
    then: REJECT
    reason: "multiple_risk_signals"
```
