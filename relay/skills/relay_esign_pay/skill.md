---
name: relay-esign-pay
description: Cashfree workflow for Aadhaar eSign before payment — collect legally valid digital signatures on documents before releasing payment link. Sequential multi-signer support, 15-day expiry timer, reminder ladder. Generates working Node.js integration code, compact Relay workflow spec, IT Act compliance brief. SEBI IA, insurance, lending, RERA use cases.
triggers:
  - /relay-esign-pay
  - esign before payment
  - digital signature workflow
  - aadhaar esign relay
  - signed agreement before payment
  - investment advisor consent
tools:
  - Read/Write
---

# Aadhaar eSign + Pay

> Sign document → release payment link · Multi-signer sequential flow · Up to 2 signers · 15-day expiry window · IT Act Section 3A — legally valid as wet ink · SEBI IA / Insurance / Lending / RERA

---

## Regulatory mandate

| Obligation | Regulation | Threshold / Deadline |
|---|---|---|
| Electronic signature validity | IT Act 2000 — Section 3A (Electronic Signature) | Aadhaar-based eSign is legally equivalent to wet-ink signature |
| Aadhaar authentication | Aadhaar (Targeted Delivery) Act 2016 — Section 8 · UIDAI Auth regulations | OTP-based Aadhaar authentication only — no biometric capture |
| Investment advisor client agreement | SEBI IA Regulations 2013 — Regulation 19(1) | Mandatory signed agreement before any advisory fee |
| Signed document retention | SEBI IA Regulations 2013 — Regulation 19(3) | 5 years from relationship end |
| RERA agreement | Real Estate (Regulation and Development) Act 2016 — Section 13 | Signed agreement mandatory before accepting > 10% of consideration |
| Consent capture | DPDP Act 2023 — Section 6 | Before any Aadhaar data is accessed |
| Audit trail — OTP log | Aadhaar authentication log | Must be retained — cannot be deleted |

---

## What your customer experiences

1. Receives a signing link via SMS + Email + WhatsApp
2. Opens the link, reviews the document
3. Authenticates with Aadhaar OTP (no app install, no device dependency)
4. Signs — legally equivalent to wet ink under IT Act Section 3A
5. Signer 2 (if required) gets notified automatically once Signer 1 completes
6. All signers done → payment link released to the primary payer

---

## Use cases

| Sector | Document | Signers | Payment unlocked |
|---|---|---|---|
| SEBI Investment Advisor | Client agreement (IA Reg. mandatory) | 2 (client + IA) | Advisory fee |
| Insurance | Proposal form | 1 (policyholder) | First premium |
| Lending | Loan agreement | 1–3 (borrower + guarantors) | Disbursement |
| Real estate (RERA) | Sale agreement | 2 (buyer + seller) | Token payment |
| Rental | Rental deed | 2 (landlord + tenant) | First month rent |

---

## Quickstart — 15 minutes to live

### Environment variables

```env
CASHFREE_CLIENT_ID=
CASHFREE_CLIENT_SECRET=
CASHFREE_BASE_URL=https://sandbox.cashfree.com/verification
CASHFREE_WEBHOOK_SECRET=
BASE_URL=http://localhost:3000
RELAY_WORKFLOW_ID=
```

---

### Step 1 — Import workflow into Relay

```json
{
  "name": "esign_then_pay",
  "description": "Aadhaar eSign on document → release payment link on completion",
  "trigger": "api",
  "inputs": ["order_id", "amount", "document_url", "signers"],
  "nodes": [
    { "id": "doc-upload",    "type": "api",   "call": "POST /esignature/document",
      "content_type": "multipart/form-data", "in": { "document_url": "{{document_url}}" } },
    { "id": "esign-create",  "type": "api",   "call": "POST /esignature",
      "in": {
        "document_id":         "{{doc_id}}",
        "auth_type":           "AADHAAR",
        "expiry_in_days":      15,
        "notification_types":  ["SMS", "EMAIL", "WHATSAPP"],
        "signers":             "{{signers}}"
      }
    },
    { "id": "notify-s1",     "type": "notify", "to": "{{signers[0]}}", "channels": ["sms","email","whatsapp"] },
    { "id": "wait-s1",       "type": "wait",   "event": "esign.signer_completed", "filter": "signer_1",
      "reminders": [{ "days": 7, "msg": "7 days left to sign" }, { "days": 13, "msg": "Sign by tomorrow" }],
      "on_timeout": "esign-regen"
    },
    { "id": "notify-s2",     "type": "notify", "to": "{{signers[1]}}", "channels": ["sms","email","whatsapp"],
      "skip_if": "signers.length == 1"
    },
    { "id": "wait-s2",       "type": "wait",   "event": "esign.signer_completed", "filter": "signer_2",
      "on_timeout": "esign-regen", "skip_if": "signers.length == 1"
    },
    { "id": "esign-regen",   "type": "api",    "call": "POST /esignature",
      "note": "Must use a new verification_id — never reuse expired one",
      "max_retries": 1, "on_final_timeout": "CLOSE"
    },
    { "id": "pay-link",      "type": "api",    "call": "POST /pg/links",
      "in": { "amount": "{{amount}}", "meta": { "esign_verification_id": "{{esign_id}}", "esign_status": "COMPLETED" } }
    }
  ]
}
```

---

### Step 2 — Backend (Node.js)

```javascript
// server.js
import express from 'express';
import crypto  from 'crypto';

const app = express();
app.use(express.json({ verify: (req, _, buf) => { req.rawBody = buf; } }));

const {
  CASHFREE_CLIENT_ID, CASHFREE_CLIENT_SECRET,
  CASHFREE_WEBHOOK_SECRET, RELAY_WORKFLOW_ID, BASE_URL,
} = process.env;

// ─── Start eSign flow ─────────────────────────────────────────────────────────
app.post('/api/esign/start', async (req, res) => {
  const { orderId, amount, documentUrl, signers } = req.body;
  // signers: [{ name, mobile, email, signPage, signX, signY }, ...]
  // signX/Y: PDF coordinates (A4 = 595×842 pt, origin bottom-left)
  // Example bottom-right of page 4: signPage=4, signX=350, signY=100, width=150, height=60

  const r = await fetch(
    `https://api.cashfree.com/relay/v1/workflows/${RELAY_WORKFLOW_ID}/runs`,
    {
      method: 'POST',
      headers: {
        'x-client-id':     CASHFREE_CLIENT_ID,
        'x-client-secret': CASHFREE_CLIENT_SECRET,
        'Content-Type':    'application/json',
      },
      body: JSON.stringify({
        customer_id:   orderId,
        redirect_url:  `${BASE_URL}/esign/done`,
        webhook_url:   `${BASE_URL}/api/esign/webhook`,
        metadata: { order_id: orderId, amount, document_url: documentUrl, signers },
      }),
    }
  );

  const { run_id } = await r.json();
  // Cashfree notifies each signer via SMS/Email/WhatsApp — no redirect URL needed
  res.json({ runId: run_id, message: 'Signing links sent to signers' });
});

// ─── Webhook ──────────────────────────────────────────────────────────────────
app.post('/api/esign/webhook', (req, res) => {
  const sig = req.headers['x-cashfree-signature'];
  const expected = crypto
    .createHmac('sha256', CASHFREE_WEBHOOK_SECRET)
    .update(req.rawBody).digest('base64');
  if (sig !== expected) return res.status(401).send('Bad signature');

  const { event, customer_id, identifier, status, signed_document_url } = req.body;

  switch (event) {
    case 'SIGNER_COMPLETED':
      // One signer done — Relay notifies next signer automatically
      console.log(`Signer ${identifier} completed for order ${customer_id}`);
      break;

    case 'ESIGN_COMPLETED':
      // ✅ All signers done — payment link has been released by Relay
      // Store signed_document_url — 5-year retention required (SEBI/lending compliance)
      storeSignedDocument(customer_id, signed_document_url);
      notifyPaymentLinkSent(customer_id);
      break;

    case 'ESIGN_EXPIRED':
      // ⏰ Link expired — Relay regens once automatically, then closes
      console.log(`eSign expired for order ${customer_id} — Relay handling regen`);
      break;

    case 'ESIGN_DECLINED':
      // ❌ Signer declined
      markDeclined(customer_id, identifier);
      break;
  }

  res.json({ received: true });
});

async function storeSignedDocument(orderId, url) { /* save to S3/DB — keep 5 years */ }
async function notifyPaymentLinkSent(orderId)     { /* tell customer their payment link is ready */ }
async function markDeclined(orderId, signer)      { /* notify merchant, update order status */ }

app.listen(3000);
```

---

### Step 3 — Sign position guide

```
A4 page dimensions: 595 × 842 PDF points. Origin: bottom-left corner.

Placement reference:
  Bottom of last page:  { page: N, x: 100, y: 100, width: 150, height: 60 }
  Right column:         { page: N, x: 350, y: 100, width: 150, height: 60 }
  Two signers, same page: signer 1 at x:100, signer 2 at x:350

Rules:
  - x + width must be ≤ 595
  - y + height must be ≤ 842
  - Coordinates outside page bounds → 400 error from API
  - Max expiry: 15 days (API rejects expiry_in_days > 15)
```

---

### Step 4 — Test it

```bash
# Start eSign flow (single signer)
curl -X POST http://localhost:3000/api/esign/start \
  -H "Content-Type: application/json" \
  -d '{
    "orderId": "order_001",
    "amount": 50000,
    "documentUrl": "https://yourapp.com/docs/agreement.pdf",
    "signers": [{
      "name": "RAJESH KUMAR",
      "mobile": "9876543210",
      "email": "rajesh@example.com",
      "signPage": 4,
      "signX": 100,
      "signY": 100,
      "width": 150,
      "height": 60
    }]
  }'

# Simulate ESIGN_COMPLETED webhook
curl -X POST http://localhost:3000/api/esign/webhook \
  -H "Content-Type: application/json" \
  -H "x-cashfree-signature: <sign>" \
  -d '{
    "event": "ESIGN_COMPLETED",
    "customer_id": "order_001",
    "signed_document_url": "https://secure.cashfree.com/docs/signed_abc.pdf"
  }'
```

---

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `verification_id_already_exists` | Duplicate ID sent | Always generate a fresh UUID per request |
| `sign_position_out_of_bounds` | x+width > 595 or y+height > 842 | Validate coordinates before API call |
| `expiry_exceeded_max` | expiry_in_days > 15 | Cap at 15 |
| `aadhaar_otp_expired` | Signer took too long mid-signing | Signer must start over — send new link |
| Webhook not firing | URL not reachable from Cashfree | Use ngrok in dev: `ngrok http 3000` |

---

## Enterprise governance

| Control | Cashfree platform | Your responsibility |
|---|---|---|
| **Data residency** | India-only · AWS ap-south-1 (Mumbai) · No cross-border transfer | Signed document storage must be India-hosted |
| **Encryption** | TLS 1.3 in transit · AES-256 at rest | Maintain equivalent standards in your document storage |
| **Audit trail** | Aadhaar OTP log + session recording retained 7 years | Cannot be deleted — IT Act Section 3A audit requirement |
| **Signed document retention** | Signed document URL delivered via webhook | Store `signed_document_url` for 5 years minimum (SEBI/lending compliance) |
| **DPDP rights** | Consent event stored per DPDP Act 2023 — Section 6 | Data Principal rights (access / correction / erasure) are your obligation |
| **Document integrity** | Hash of signed document provided in webhook | Verify hash on retrieval to detect tampering |
| **Expiry management** | 15-day max expiry enforced · Auto-regen once on expiry | Never reuse an expired verification_id — always generate new UUID |

---

## What's covered

| ✅ Included | ⚠️ Needs your config | ❌ Not included |
|---|---|---|
| Document upload + eSign request creation | Document template (AOF, loan agreement, etc.) | Identity verification (use relay-standard-cdd before this) |
| Sequential multi-signer flow (up to 2) | 5-year signed document storage | |
| SMS + Email + WhatsApp notifications | | |
| Day 7 + Day 13 signing reminders | | |
| Link expiry → auto-regen once | | |
| Payment link released on completion | | |
| Webhook signature verification | | |

**Regulation:** IT Act 2000 — Section 3A (eSign validity) · SEBI IA Regulations 2013 — Regulation 19 (client agreement + 5yr retention) · RERA 2016 — Section 13 · Aadhaar Act 2016 — Section 8 · DPDP Act 2023 — Section 6

**Important:** Store `signed_document_url` for minimum 5 years. Audit trail (OTP log) must not be deleted.

---

## MCP — coming soon

```
/relay-esign-pay

→ Claude: "How many signers? Document type? Amount?"
→ Calls Relay MCP → creates eSign workflow
→ Returns RELAY_WORKFLOW_ID
→ Outputs code above, pre-filled
```
