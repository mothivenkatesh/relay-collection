---
name: turbopass
description: Builds implementation-ready TurboPass verification workflow using Cashfree Secure ID V2 APIs — DL-first identity verification. SmartOCR on DL document → /driving-license (RTO), Face Liveness, Face Match vs DL photo, /pan/advance (PAN Advanced), /bank-account/sync (BAV V2). For gig workers, two-wheeler loans, vehicle insurance, delivery partner onboarding. Full request/response JSON, Relay YAML node config, decision rules, fallback paths.
triggers:
  - /turbopass
  - turbopass verification workflow
  - DL based KYC relay
  - driving license verification workflow
  - gig worker onboarding relay
  - two wheeler loan KYC
  - phone to DL workflow
tools:
  - Read/Write
---

# Skill: TurboPass — DL-First Identity Verification

## Overview
TurboPass is a Driving License-first identity verification flow. Uses SmartOCR to extract DL number from document image, verifies against RTO database via `/driving-license`, then face-matches selfie against the RTO photo. No Aadhaar OTP required. No DigiLocker consent friction.

**Key advantage:** DL covers segments with low Aadhaar mobile linkage — gig workers, rural users, vehicle owners. RTO photo provides ground truth for face match.

**Relay Status:** READY (core path). Phone→DL lookup endpoint path to confirm with engineering (not in public V2 docs).

**V2 Base URL:**
- Sandbox: `https://sandbox.cashfree.com/verification`
- Production: `https://api.cashfree.com/verification`

**Use cases:** Two-wheeler loans, gig worker onboarding, vehicle insurance KYC, delivery partner onboarding, ride-share driver KYC.

---

## Services Used (All Cashfree Secure ID V2)

| Service | Confirmed V2 Endpoint | Notes |
|---|---|---|
| SmartOCR (DL extraction) | `POST /bharat-ocr` | Extracts DL number from document image |
| India Phone To DL | `POST /driving-license/phone` | **Confirm endpoint with engineering** — not in public V2 docs |
| DL Premium (RTO verify) | `POST /driving-license` | Confirmed V2 |
| Face Liveness | `POST /face-liveness` | Confirmed V2, multipart/form-data |
| Face Match | `POST /face-match` | Confirmed V2, multipart/form-data |
| Face Dedupe | Internal endpoint | **Confirm with engineering** — not in public V2 docs |
| PAN Advanced | `POST /pan/advance` | Confirmed V2 |
| BAV Sync V2 | `POST /bank-account/sync` | Confirmed V2 |

---

## Happy Path

### Step 1 — Phone → DL Lookup (Optional Fast Path)

If the user provides only their mobile number, attempt auto-lookup of their DL number.

> **Engineering note:** `POST /driving-license/phone` path is not confirmed in public V2 docs. Confirm endpoint before building this Relay node. If unavailable, skip to Step 2 (user manually enters DL number or uploads DL image).

```yaml
# Node: phone-to-dl (optional — confirm endpoint first)
type: http
method: POST
url: "{{BASE_URL}}/driving-license/phone"
headers:
  x-client-id: "{{env.CLIENT_ID}}"
  x-client-secret: "{{env.CLIENT_SECRET}}"
  x-api-version: "2024-12-01"
  Content-Type: "application/json"
body:
  phone: "{{input.mobile}}"
output_mapping:
  dl_number: "$.dl_number"
  dl_name: "$.name"
  dl_dob: "$.dob"
conditions:
  - if: "$.status == 'SUCCESS' AND $.dl_number IS NOT NULL"
    then: dl-rto-verify
  - if: "$.status == 'NO_MATCH' OR $.status == 'ERROR'"
    then: request-dl-upload   # fallback: user uploads DL image
```

---

### Step 2 — SmartOCR: Extract DL Number from Image

If phone→DL lookup unavailable or fails, user uploads their DL card. SmartOCR extracts the DL number.

**Request (multipart/form-data):**
```
POST /bharat-ocr
x-client-id: {{CLIENT_ID}}
x-client-secret: {{CLIENT_SECRET}}
x-api-version: 2024-12-01
Content-Type: multipart/form-data

verification_id: tp_{{uuid}}
document_type: DRIVING_LICENCE
image1: <front_of_DL_binary>
image2: <back_of_DL_binary>  (if available)
```

**Response:**
```json
{
  "verification_id": "tp_abc123",
  "reference_id": 12345,
  "document_type": "DRIVING_LICENCE",
  "verification_status": "SUCCESS",
  "extracted_data": {
    "name": "RAJESH KUMAR",
    "dob": "1990-01-15",
    "dl_number": "MH0120231234567",
    "address": {
      "full_address": "123, MG Road, Andheri West, Mumbai, Maharashtra 400053"
    },
    "issue_date": "2020-06-15",
    "validity": "2040-06-14"
  },
  "quality_checks": {
    "blur": false, "glare": false, "partial": false,
    "black_and_white": false, "face_present": true, "qr_present": false
  },
  "forgery_checks": {
    "screenshot": false, "alteration": false,
    "photo_imposition": false, "ai_generated": false
  }
}
```

```yaml
# Node: smartocr-dl
type: http
method: POST
url: "{{BASE_URL}}/bharat-ocr"
headers:
  x-client-id: "{{env.CLIENT_ID}}"
  x-client-secret: "{{env.CLIENT_SECRET}}"
  x-api-version: "2024-12-01"
  Content-Type: "multipart/form-data"
body:
  verification_id: "tp_{{generate_uuid()}}"
  document_type: "DRIVING_LICENCE"   # MUST be explicit — no auto-classification
  image1: "{{input.dl_front_image}}"
output_mapping:
  dl_number: "$.extracted_data.dl_number"
  dl_name: "$.extracted_data.name"
  dl_dob: "$.extracted_data.dob"
  dl_photo: "$.extracted_data.photo"   # if present
conditions:
  - if: "any forgery_check == true"
    then: REJECT
    reason: "dl_forgery_detected"   # no retry
  - if: "$.quality_checks.blur == true OR $.quality_checks.partial == true"
    then: re-prompt
    message: "{{quality_failure_reason}}"   # tell user exactly what failed
  - if: "$.extracted_data.dl_number IS NULL"
    then: request-manual-dl-entry
  - if: "$.verification_status == 'SUCCESS'"
    then: dl-rto-verify
```

---

### Step 3 — DL Premium: RTO Verification

Verify DL number against the RTO (Regional Transport Office) national database. Returns authoritative photo, vehicle classes, validity.

**Request (JSON):**
```json
POST /driving-license
x-client-id: {{CLIENT_ID}}
x-client-secret: {{CLIENT_SECRET}}
x-api-version: 2024-12-01
Content-Type: application/json

{
  "verification_id": "tp_{{uuid}}",
  "dl_number": "MH0120231234567",
  "dob": "1990-01-15"
}
```

**Response:**
```json
{
  "verification_id": "tp_abc123",
  "reference_id": 67890,
  "dl_number": "MH0120231234567",
  "dob": "1990-01-15",
  "status": "VALID",
  "details_of_driving_licence": {
    "name": "RAJESH KUMAR",
    "photo": "{{base64_rto_photo}}",
    "address": "123, MG Road, Andheri West, Mumbai, Maharashtra 400053",
    "issuance_date": "2020-06-15",
    "cov_details": [
      {"cov": "MCWOG", "issue_date": "2020-06-15", "validity": "2040-06-14"},
      {"cov": "LMV", "issue_date": "2021-01-10", "validity": "2041-01-09"}
    ]
  },
  "dl_validity": {
    "non_transport": "2040-06-14",
    "transport": null,
    "hazardous": null,
    "hill": null
  },
  "badge_details": []
}
```

```yaml
# Node: dl-rto-verify
type: http
method: POST
url: "{{BASE_URL}}/driving-license"
headers:
  x-client-id: "{{env.CLIENT_ID}}"
  x-client-secret: "{{env.CLIENT_SECRET}}"
  x-api-version: "2024-12-01"
  Content-Type: "application/json"
body:
  verification_id: "{{generate_uuid('tp_')}}"
  dl_number: "{{dl_number}}"
  dob: "{{input.dob}}"
output_mapping:
  dl_status: "$.status"
  dl_rto_name: "$.details_of_driving_licence.name"
  dl_rto_photo: "$.details_of_driving_licence.photo"
  dl_validity_nt: "$.dl_validity.non_transport"
  vehicle_classes: "$.details_of_driving_licence.cov_details"
conditions:
  - if: "$.status == 'INVALID'"
    then: REJECT
    reason: "dl_not_found_in_rto"
  - if: "is_expired($.dl_validity.non_transport)"
    then: REJECT
    reason: "dl_expired"
  - if: "$.details_of_driving_licence.photo IS NULL"
    then: ADD_FLAG
    flag: "dl_rto_photo_unavailable"
    weight: "+2 AMBER"
    then: face-liveness   # proceed without RTO photo — face match will use SmartOCR photo
  - if: "$.status == 'VALID'"
    then: name-cross-validate
```

**Name cross-validation (OCR name vs. RTO name):**
```yaml
# Node: name-cross-validate
type: http
method: POST
url: "{{BASE_URL}}/name-match"
headers:
  x-client-id: "{{env.CLIENT_ID}}"
  x-client-secret: "{{env.CLIENT_SECRET}}"
  x-api-version: "2024-12-01"
  Content-Type: "application/json"
body:
  name_1: "{{dl_name}}"   # from SmartOCR
  name_2: "{{dl_rto_name}}"   # from RTO
output_mapping:
  cross_match_score: "$.score"
  cross_match_result: "$.result"
conditions:
  - if: "$.result == 'NO_MATCH'"
    then: REJECT
    reason: "ocr_rto_name_mismatch"
  - if: "$.result == 'POOR_PARTIAL_MATCH'"
    then: ADD_FLAG
    flag: "ocr_rto_name_poor"
    weight: "+1 AMBER"
  - else:
    then: face-liveness
```

---

### Step 4 — Face Liveness

**Request (multipart/form-data):**
```
POST /face-liveness
x-client-id: {{CLIENT_ID}}
x-client-secret: {{CLIENT_SECRET}}
x-api-version: 2024-12-01
Content-Type: multipart/form-data

verification_id: tp_{{uuid}}
image: <selfie_binary>
```

**Response:**
```json
{
  "reference_id": 9876,
  "verification_id": "tp_abc123",
  "status": "SUCCESS",
  "liveness": true,
  "liveness_score": 0.94,
  "gender": {"value": "Male", "confidence": 92},
  "age_range": {"min": 28, "max": 34},
  "eye_wear": {"value": false, "confidence": 88},
  "face_occluded": {"value": false, "confidence": 96},
  "quality": {"blur": false, "bright": true, "exposure": "NEUTRAL"},
  "pose": {"alignment": "CENTRE", "head_turned": false},
  "eyes_open": {"value": true, "confidence": 98}
}
```

```yaml
# Node: face-liveness
type: http
method: POST
url: "{{BASE_URL}}/face-liveness"
headers:
  x-client-id: "{{env.CLIENT_ID}}"
  x-client-secret: "{{env.CLIENT_SECRET}}"
  x-api-version: "2024-12-01"
  Content-Type: "multipart/form-data"
body:
  verification_id: "{{generate_uuid('tp_')}}"
  image: "{{input.selfie_image}}"   # binary file, JPEG/JPG/PNG
output_mapping:
  liveness: "$.liveness"
  liveness_score: "$.liveness_score"
  liveness_status: "$.status"
conditions:
  - if: "$.liveness == true AND $.status == 'SUCCESS'"
    then: face-match-vs-dl
  - if: "$.status == 'REAL_FACE_NOT_DETECTED'"
    then: recapture   # max 3 attempts
  - if: "$.status == 'MULTIPLE_FACES_DETECTED'"
    then: re-prompt
    message: "Multiple faces detected. Please take a selfie alone."
  - if: "$.status == 'FACE_NOT_DETECTED'"
    then: re-prompt
    message: "No face detected. Please ensure your face is visible."
```

---

### Step 5 — Face Match: Selfie vs. DL Photo (RTO or OCR)

Uses RTO photo from `/driving-license` response. Falls back to SmartOCR-extracted photo if RTO photo unavailable.

**Request (multipart/form-data):**
```
POST /face-match
x-client-id: {{CLIENT_ID}}
x-client-secret: {{CLIENT_SECRET}}
x-api-version: 2024-12-01
Content-Type: multipart/form-data

verification_id: tp_{{uuid}}
first_image: <selfie_binary>
second_image: <dl_rto_photo_binary>   (or SmartOCR photo if RTO unavailable)
threshold: 0.75
```

**Response:**
```json
{
  "status": "SUCCESS",
  "ref_id": 5432,
  "verification_id": "tp_abc123",
  "face_match_result": "YES",
  "face_match_score": 0.87
}
```

```yaml
# Node: face-match-vs-dl
type: http
method: POST
url: "{{BASE_URL}}/face-match"
headers:
  x-client-id: "{{env.CLIENT_ID}}"
  x-client-secret: "{{env.CLIENT_SECRET}}"
  x-api-version: "2024-12-01"
  Content-Type: "multipart/form-data"
body:
  verification_id: "{{generate_uuid('tp_')}}"
  first_image: "{{input.selfie_image}}"
  second_image: "{{dl_rto_photo OR dl_ocr_photo}}"
  threshold: "{{env.FACE_MATCH_THRESHOLD | default: 0.75}}"
output_mapping:
  face_match_result: "$.face_match_result"
  face_match_score: "$.face_match_score"
conditions:
  - if: "$.face_match_result == 'YES' AND $.face_match_score >= 0.75"
    then: pan-advance
  - if: "$.face_match_result == 'NO'"
    then: REJECT
    reason: "face_mismatch_vs_dl"
  - if: "$.status == 'MULTIPLE_FACE_DETECTED'"
    then: REJECT
    reason: "multiple_faces_in_dl_photo"
  - if: "$.face_match_score >= 0.70 AND $.face_match_score < 0.75"
    then: ADD_FLAG
    flag: "borderline_face_match"
    weight: "+2 AMBER"
    then: pan-advance
```

**Threshold guidance:**
| Threshold | Use Case |
|---|---|
| 0.75 (default) | Standard gig worker / loan onboarding |
| 0.80 | Conservative — vehicle insurance, high-value |
| 0.70 | Permissive — thin file, rural segments (higher fraud risk) |

---

### Step 6 — PAN Advanced (`/pan/advance`)

Returns richer data than standard `/pan`: gender, DOB, masked Aadhaar, masked email, masked mobile, address from ITD.

**Request (JSON):**
```json
POST /pan/advance
x-client-id: {{CLIENT_ID}}
x-client-secret: {{CLIENT_SECRET}}
x-api-version: 2024-12-01
Content-Type: application/json

{
  "pan": "ABCDE1234F",
  "verification_id": "tp_{{uuid}}",
  "name": "RAJESH KUMAR"
}
```

**Response:**
```json
{
  "status": "SUCCESS",
  "reference_id": 11111,
  "verification_id": "tp_abc123",
  "pan": "ABCDE1234F",
  "registered_name": "RAJESH KUMAR",
  "name_pan_card": "RAJESH KUMAR",
  "first_name": "RAJESH",
  "last_name": "KUMAR",
  "type": "Individual",
  "gender": "MALE",
  "date_of_birth": "1990-01-15",
  "masked_aadhaar_number": "XXXXXXXX1234",
  "aadhaar_linked": true,
  "email": "r****h@gmail.com",
  "mobile_number": "98****3210",
  "address": {
    "full_address": "123, MG Road, Mumbai 400001",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pincode": "400001"
  }
}
```

```yaml
# Node: pan-advance
type: http
method: POST
url: "{{BASE_URL}}/pan/advance"
headers:
  x-client-id: "{{env.CLIENT_ID}}"
  x-client-secret: "{{env.CLIENT_SECRET}}"
  x-api-version: "2024-12-01"
  Content-Type: "application/json"
body:
  pan: "{{input.pan}}"
  verification_id: "{{generate_uuid('tp_')}}"
  name: "{{input.name}}"
output_mapping:
  pan_status: "$.status"
  pan_name: "$.registered_name"
  pan_dob: "$.date_of_birth"
  pan_gender: "$.gender"
  aadhaar_linked: "$.aadhaar_linked"
conditions:
  - if: "$.status != 'SUCCESS'"
    then: REJECT
    reason: "pan_invalid"
  - if: "$.aadhaar_linked == false"
    then: ADD_FLAG
    flag: "aadhaar_not_linked"
    weight: "+1 AMBER"
  - if: "$.status == 'SUCCESS'"
    then: pan-dl-name-crosscheck

# Node: pan-dl-name-crosscheck
type: http
method: POST
url: "{{BASE_URL}}/name-match"
headers:
  x-client-id: "{{env.CLIENT_ID}}"
  x-client-secret: "{{env.CLIENT_SECRET}}"
  x-api-version: "2024-12-01"
  Content-Type: "application/json"
body:
  name_1: "{{pan_name}}"
  name_2: "{{dl_rto_name}}"
output_mapping:
  pan_dl_match: "$.result"
  pan_dl_score: "$.score"
conditions:
  - if: "$.result == 'NO_MATCH'"
    then: REJECT
    reason: "pan_dl_name_mismatch"
  - if: "$.result == 'POOR_PARTIAL_MATCH'"
    then: REJECT
    reason: "pan_dl_name_poor_match"
  - if: "$.result == 'MODERATE_PARTIAL_MATCH'"
    then: ADD_FLAG
    flag: "pan_dl_name_moderate"
    weight: "+1 AMBER"
    then: bav-sync
  - if: "$.result == 'GOOD_PARTIAL_MATCH' OR $.result == 'DIRECT_MATCH'"
    then: bav-sync
```

**PAN Advanced vs. Standard PAN (`/pan`) — what you get extra:**
| Field | `/pan` | `/pan/advance` |
|---|---|---|
| pan_status | ✓ | ✓ |
| registered_name | ✓ | ✓ |
| aadhaar_seeding_status | ✓ | — |
| aadhaar_linked (bool) | — | ✓ |
| gender | — | ✓ |
| date_of_birth | — | ✓ |
| masked_aadhaar_number | — | ✓ |
| email (masked) | — | ✓ |
| mobile (masked) | — | ✓ |
| address | — | ✓ |

---

### Step 7 — BAV Sync V2 (`/bank-account/sync`)

**Request (JSON):**
```json
POST /bank-account/sync
x-client-id: {{CLIENT_ID}}
x-client-secret: {{CLIENT_SECRET}}
x-api-version: 2024-12-01
Content-Type: application/json

{
  "bank_account": "1234567890",
  "ifsc": "HDFC0001234",
  "name": "RAJESH KUMAR",
  "phone": "9876543210"
}
```

**Response:**
```json
{
  "reference_id": 22222,
  "account_status": "VALID",
  "account_status_code": "ACCOUNT_IS_VALID",
  "name_at_bank": "RAJESH KUMAR",
  "bank_name": "HDFC Bank",
  "name_match_score": 97.0,
  "name_match_result": "DIRECT_MATCH",
  "utr": "UTR123456",
  "ifsc_details": {
    "address": "HDFC Bank, Andheri Branch, Mumbai",
    "city": "Mumbai",
    "state": "Maharashtra"
  }
}
```

```yaml
# Node: bav-sync
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
  phone: "{{input.mobile}}"
retry:
  on: ["npci_unavailable", "connection_timeout", "benficiary_bank_offline"]
  delay: 300
  max_attempts: 1
  on_retry_fail: ROUTE_TO_ASYNC
output_mapping:
  account_status: "$.account_status"
  account_status_code: "$.account_status_code"
  name_match_result: "$.name_match_result"
  name_match_score: "$.name_match_score"
conditions:
  - if: "$.account_status_code == 'fraud_account'"
    then: REJECT_AND_FLAG
    reason: "fraud_account_bav"
  - if: "$.account_status == 'INVALID'"
    then: REJECT
    reason: "bank_account_invalid"
  - if: "$.name_match_result == 'DIRECT_MATCH' OR $.name_match_result == 'GOOD_PARTIAL_MATCH'"
    then: decision-node
  - if: "$.name_match_result == 'MODERATE_PARTIAL_MATCH'"
    then: ADD_FLAG
    flag: "bav_name_moderate"
    weight: "+1 AMBER"
    then: decision-node
  - if: "$.name_match_result == 'POOR_PARTIAL_MATCH' OR $.name_match_result == 'NO_MATCH'"
    then: REJECT
    reason: "bav_name_mismatch"
```

---

### Step 8 — Decision Node

```yaml
# Node: decision-node
type: condition
conditions:
  - if: "amber_flag_count == 0"
    then: APPROVE
  - if: "amber_flag_count >= 1 AND amber_flag_count <= 2"
    then: MANUAL_REVIEW
    queue: "kyc_ops"
    include: "{{all_flags}}"
  - if: "amber_flag_count >= 3"
    then: REJECT
    reason: "multiple_risk_signals"

# Node: audit-log (immutable)
type: http
method: POST
url: "{{env.AUDIT_LOG_URL}}/entry"
body:
  verification_id: "{{verification_id}}"
  decision: "{{decision}}"
  nodes_executed: "{{all_node_results}}"
  amber_flags: "{{amber_flags}}"
  timestamp: "{{now()}}"
immutable: true
```

---

## Workflow Diagram

```
[INPUT: Mobile + DL image (or DL number manually)]
        │
[PHONE→DL LOOKUP (optional — confirm endpoint)]
  FOUND ──→ skip Step 2
  NOT FOUND ──→ continue to OCR
        │
[SMARTOCR: document_type=DRIVING_LICENCE]
  Forgery ──→ REJECT | Quality fail ──→ re-prompt
  Extracts: dl_number, name, dob, photo
        │
[DL PREMIUM: POST /driving-license]
  INVALID ──→ REJECT | Expired ──→ REJECT
  Photo: use for face match (fallback to OCR photo)
        │
[NAME CROSS-VALIDATE: SmartOCR name vs RTO name]
  NO_MATCH ──→ REJECT | POOR ──→ +1 AMBER
        │
[FACE LIVENESS: POST /face-liveness]
  Spoof ──→ re-capture (max 3×)
        │
[FACE MATCH: POST /face-match (selfie vs DL photo)]
  NO MATCH ──→ REJECT | Borderline ──→ +2 AMBER
        │
[PAN ADVANCED: POST /pan/advance]
  INVALID ──→ REJECT | Aadhaar not linked ──→ +1 AMBER
  PAN vs DL name: POOR ──→ REJECT | MODERATE ──→ +1 AMBER
        │
[BAV SYNC: POST /bank-account/sync]
  INVALID / fraud ──→ REJECT | MODERATE name ──→ +1 AMBER
        │
[DECISION NODE]
  0 AMBER ──→ APPROVE
  1-2 AMBER ──→ MANUAL REVIEW
  3+ AMBER ──→ REJECT
```

---

## V2 API Quick Reference

| Node | Method | V2 Path | Content-Type |
|---|---|---|---|
| SmartOCR (DL extract) | POST | `/bharat-ocr` | multipart/form-data |
| Phone→DL | POST | `/driving-license/phone` | application/json (**confirm**) |
| DL Premium (RTO) | POST | `/driving-license` | application/json |
| Name Match | POST | `/name-match` | application/json |
| Face Liveness | POST | `/face-liveness` | multipart/form-data |
| Face Match | POST | `/face-match` | multipart/form-data |
| PAN Advanced | POST | `/pan/advance` | application/json |
| BAV Sync V2 | POST | `/bank-account/sync` | application/json |

---

## Use Case Matrix

| Use Case | Why TurboPass | Key DL Signal |
|---|---|---|
| Two-wheeler loan | DL = primary ID for vehicle finance | vehicle_class: MCWOG/MCG |
| Gig worker (food/logistics) | DL is standard for delivery partners | DL valid + face match |
| Vehicle insurance | DL mandatory for motor insurance KYC | DL vehicle_classes + validity |
| Ride-share driver | DL mandatory for cab aggregators | DL valid + LMV class |
| Consumer durable (thin-file) | DL holders with low Aadhaar-mobile linkage | DL + PAN advanced |

---

## Environment Variables

```yaml
env:
  CLIENT_ID: "<cashfree_client_id>"
  CLIENT_SECRET: "<cashfree_client_secret>"
  FACE_MATCH_THRESHOLD: "0.75"   # configurable: 0.70-0.85
  AUDIT_LOG_URL: "<internal_audit_log_url>"
```
