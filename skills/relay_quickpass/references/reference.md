# Reference: TurboPass — Full API Specs

## Confirmed Cashfree Secure ID V2 Endpoints

**Base URL:** `https://api.cashfree.com/verification`
**Sandbox:** `https://sandbox.cashfree.com/verification`

### Auth Headers (required on all calls)
```
x-client-id: <CLIENT_ID>
x-client-secret: <CLIENT_SECRET>
x-api-version: 2024-12-01
```

---

## SmartOCR — DL Fields Extracted

```json
{
  "document_type": "DRIVING_LICENCE",
  "verification_status": "SUCCESS",
  "extracted_data": {
    "name": "RAJESH KUMAR",
    "dob": "1990-01-15",
    "dl_number": "MH0120231234567",
    "address": { "full_address": "..." },
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

**document_type must be explicit:** `"DRIVING_LICENCE"` — SmartOCR has no auto-classification. Wrong or missing value → 400 error.

---

## Driving License (RTO) — Full Response

```json
{
  "verification_id": "tp_abc123",
  "reference_id": 67890,
  "dl_number": "MH0120231234567",
  "dob": "1990-01-15",
  "status": "VALID",
  "details_of_driving_licence": {
    "name": "RAJESH KUMAR",
    "photo": "{{base64_encoded_rto_photo}}",
    "address": "123, MG Road, Mumbai",
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
  }
}
```

**Vehicle Class Codes:**
| Code | Description |
|---|---|
| MCWOG | Motorcycle Without Gear (scooter, moped) |
| MCG | Motorcycle With Gear |
| LMV | Light Motor Vehicle (car, SUV) |
| TRANS | Transport vehicle |
| HMV | Heavy Motor Vehicle |
| HTV | Heavy Transport Vehicle |

**Status values:**
| Status | Action |
|---|---|
| `VALID` | Proceed |
| `INVALID` | Reject — DL not in RTO database |

---

## Name Match — Full Reference

```json
POST /name-match
{
  "name_1": "RAJESH KUMAR",
  "name_2": "Rajesh K"
}

Response:
{
  "score": 0.77,
  "result": "MODERATE_PARTIAL_MATCH"
}
```

Name match result reference:
| Result | Score Range | TurboPass Action |
|---|---|---|
| DIRECT_MATCH | 1.00 | Proceed |
| GOOD_PARTIAL_MATCH | 0.85–0.99 | Proceed |
| MODERATE_PARTIAL_MATCH | 0.60–0.84 | +1 AMBER |
| POOR_PARTIAL_MATCH | 0.34–0.59 | REJECT (DL context) |
| NO_MATCH | 0.00–0.33 | REJECT |

---

## Face Liveness — Status Values

| Status | Meaning | Action |
|---|---|---|
| `SUCCESS` | Live face detected | Proceed to Face Match |
| `REAL_FACE_NOT_DETECTED` | Spoof or photo | Re-capture (max 3×) |
| `MULTIPLE_FACES_DETECTED` | >1 face | Re-prompt |
| `FACE_NOT_DETECTED` | No face | Re-prompt |

---

## Face Match — Status Values

| Status | face_match_result | Action |
|---|---|---|
| `SUCCESS` | YES | Biometric match — proceed |
| `SUCCESS` | NO | REJECT — biometric mismatch |
| `MULTIPLE_FACE_DETECTED` | NO | REJECT — multiple faces |

**Score thresholds:**
| Threshold | Use Case |
|---|---|
| 0.80 | Conservative — vehicle insurance, high-value |
| 0.75 | Standard (default) |
| 0.70 | Permissive — thin-file, rural (higher fraud risk) |

---

## PAN Advanced (`/pan/advance`) — Full Response

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
    "pincode": "400001",
    "country": "India"
  }
}
```

**PAN type (4th character):**
| Char | Type |
|---|---|
| P | Individual |
| C | Company |
| F | Firm |
| T | Trust |

---

## BAV Sync V2 — Status Codes

| account_status_code | Meaning | Action |
|---|---|---|
| `ACCOUNT_IS_VALID` | Active account | PASS |
| `INVALID_ACCOUNT_FAIL` | Account doesn't exist | REJECT |
| `ACCOUNT_BLOCKED` | Account suspended | REJECT |
| `INVALID_IFSC_FAIL` | IFSC code invalid | Ask for correction, retry |
| `NRE_ACCOUNT_FAIL` | Non-resident external | REJECT |
| `fraud_account` | Flagged fraudulent | REJECT + FLAG |
| `npci_unavailable` | NPCI down | Retry after 5 min |
| `connection_timeout` | Timeout | Retry once |
| `benficiary_bank_offline` | Bank offline | Retry after 5 min |

**Rate limit:** Max 15 calls per account per 24 hours. 25th attempt → `FRAUD_ACCOUNT` flag.

---

## Error Codes — All V2 APIs

| HTTP | Code | Meaning | Action |
|---|---|---|---|
| 400 | `pan_missing` | PAN not provided | Add pan field |
| 400 | `verification_id_already_exists` | Duplicate ID | Generate new UUID |
| 400 | `otp_expired` | OTP expired | Re-send OTP |
| 401 | `authentication_failed` | Invalid credentials | Check CLIENT_ID/SECRET |
| 403 | `ip_validation_failed` | IP not whitelisted | Whitelist server IP |
| 422 | `insufficient_balance` | Wallet low | Recharge account |
| 429 | `too_many_requests_per_operation` | Rate limited | Backoff + retry |
| 500 | `verification_failed` | Source unavailable | Retry with backoff |

---

## Amber Flag Weight Table

| Flag | Weight | Triggered By |
|---|---|---|
| `ocr_rto_name_poor` | +1 AMBER | OCR name ≠ RTO name (POOR match) |
| `dl_rto_photo_unavailable` | +2 AMBER | RTO returned no photo |
| `borderline_face_match` | +2 AMBER | Face score 0.70–0.75 |
| `aadhaar_not_linked` | +1 AMBER | PAN Advanced: aadhaar_linked = false |
| `pan_dl_name_moderate` | +1 AMBER | PAN name ≠ DL name (MODERATE) |
| `bav_name_moderate` | +1 AMBER | BAV name MODERATE match |

**Decision:** 0 AMBER → APPROVE | 1-2 AMBER → MANUAL REVIEW | 3+ AMBER → REJECT

---

## Endpoints to Confirm with Engineering (Not in Public V2 Docs)

| Service | Expected Path | Status |
|---|---|---|
| Phone → DL lookup | `POST /driving-license/phone` | Confirm with engineering |
| Face Dedupe Search | Internal path | Confirm with engineering |
| Face Analyzer | Embedded in `/face-liveness` response | Use liveness quality fields instead |
| AML/PEP Basic | Internal path | Use internal API |
