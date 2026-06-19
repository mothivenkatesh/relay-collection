# Slack Log: #wf_service_discussion
**Period:** Apr 28 – May 6, 2026
**Saved by:** Mothi for reference

---

## Key Decisions & Status

### Product / UX
- **Templates as Carousel** should be the first page of Relay (not the workflow list) — Mothi's recommendation from Friday connect with Vinesh. Flagged to Ram, Mayank, Subbu.
- **Relay naming question** raised by Mothi: "Which one are we calling Cashfree Relay — the MCP or the Workflow Builder? Because actually it's the MCP that does everything." → Unresolved in thread.
- **HITL approval UI** shipped by Vinesh (Apr 30):
  - Gmail Approval UI — live
  - Slack Approval UI — live
  - Callback URL: `/wfcd/v1/hitl/callback`
  - Re-run failed execution: `wfcd/v1/executions/<EXECUTION_ID>/rerun`
  - Valid `executionCallStatus` values: `APPROVED`, `REJECTED`, `TIMED_OUT`, `WAITING`, `RUNNING` (all caps)
  - Action button text: need to change to **Approve / Reject** everywhere (Ram's ask)

### Engineering — Infra & Performance
- **Load test results (Apr 28, Vishal):**
  - Workflow 73: 5,604 success / 2 failure; 99.91% < 100ms; status update in 51 min
  - Workflow 75: 3,434 success / 0 failure; 99.91% < 100ms; status update in 17 min
  - Target: **20 TPS** (20 CF transactions/sec for merchants with configured workflows)
- **Three bottlenecks identified:**
  1. Kafka Consumer lag (~100K messages at 20 TPS) — needs consumer tuning
  2. Conductor — excess RUNNING/SCHEDULED tasks; needs thread pool + DB connection pool tuning
  3. Vault credential fetch on every action execution — needs in-memory caching layer
- **Conductor tuning vars:**
  ```
  CONDUCTOR_APP_SYSTEM_TASK_WORKER_THREAD_COUNT=100
  CONDUCTOR_HTTP_THREADCOUNT=50
  ```
- **Workflow statuses (Conductor):** `RUNNING`, `COMPLETED`, `FAILED`, `TIMED_OUT`, `TERMINATED`, `PAUSED`
- **Sbox credential bug:** Vishal pushed a fix for credential storage. Old creds won't work — create new ones.

### MCP
- **MCP tools list (Satyam):**
  ```
  list_workflows, create_workflow, get_workflow, update_workflow, delete_workflow,
  update_workflow_name, activate_schedule_workflow, pause_workflow,
  test_workflow_from_ui, list_workflow_versions, list_recent_executions,
  get_node_executions, get_executions_by_workflow, list_credentials,
  create_credential, get_credential, delete_credential, get_node_actions,
  test_action_node, get_all_nodes_auth, resolve_dynamic, resolve_dropdown,
  get_trigger_categories, get_trigger_event_example_payload
  ```
- **Satyam's suggestion:** Club multiple API calls into single tools so output is complete, not intermediate.
- **MCP to PROD:** Satyam can take mcpsvc + commonmerchantsvc + commonwebapp to prod. workflowsvc needs Vinesh/Vishal. Blocked on mvn cache issue in sbox (May 5).
- **ChatGPT MCP:** Needs ChatGPT Plus or Pro. Still in beta.
- **Claude Desktop MCP:** Blocked on org-level custom connector restriction (Saksham flagged, May 5). Mayank to help.
- **Swiggy MCP** flagged by Mothi as good reference for builder/developer positioning: `mcp.swiggy.com/builders/docs/`

### Skills
- **Skills as npm packages** — Subbu's decision:
  ```
  npx @cashfreepayments/agent-skills add skills
  ```
  Reference: `cashfreepayments-d00050e9-workflows-ai.mintlify.app/tools-ai/cashfree-agent-skills`
- **Claude Skills Jira:** CPSS-16883 assigned to Saksham
- **Gemini testing:** Subbu asked Saksham to add skills + MCP in Gemini

### Bolna / Voice Plugin
- **Bolna Active Pieces plugin** confirmed working (Ishaan, Apr 28):
  - Workflow 1: triggers the call with prompt
  - Workflow 2: webhook for call completion report
  - Slack integration tested and working
- **CPSS-16679** (Bolna plugin) — Status: Todo → Ishaan tested, Karthik deployed in QA
- **Gap:** Call Completion Report uses `cloud.activepieces.com` webhook — harder to build callback into Relay natively

### Data Fetcher Node
- **Separated from Scheduler node** (CPSS-16838 — Done by Karthik)
- **Schema (Karthik's example):**
  ```json
  {
    "id": "txnSummary",
    "name": "Transaction Summary",
    "description": "Returns aggregate transaction metrics for the past X days",
    "kind": "WINDOWED",
    "lookback": { "defaultLookback": { "value": 7, "unit": "days" } }
  }
  ```
- **Confluence schema doc:** [Data Fetcher Node Schema](https://cashfree.atlassian.net/wiki/spaces/PE/pages/2158821476/Data+Fetcher+Node+Schema+for+Schedular+node)

### Webhook / PG Events (May 5 — Major Decision)
- **Switching from CDC to webhook-events Kafka topic** from `PG-Notification-Service` to trigger Relay workflows
- **New channel type = `RELAY`** added in PG (Vinesh, May 5)
- When a merchant adds + activates a workflow for an event → auto-enable that webhook
- Webhook version default: `2025-01-01`
- **Jira stories:** CPSS-17243 (enable webhook on go-live), CPSS-17244 (disable webhook on workflow removal)
- Ram's note: won't disable merchant's webhook setting — separate notification type added implicitly

### Go-Live Blocker Epic
- Epic: [CPSS-14491](https://cashfree.atlassian.net/browse/CPSS-14491) — Relay go-live blockers
- UI/UX tickets moved to FP board
- Post go-live items moved to [CPSS-10128](https://cashfree.atlassian.net/browse/CPSS-10128)
- Unleash toggle: `relay_enabled` added in QA/sbox by Vishal

### Env URLs
| Env | URL |
|---|---|
| QA | `https://merchant.qa.cashfree.net/relay` |
| SBOX | `https://merchant-gamma.cashfree.com/relay` |

> **Note:** Google OAuth redirect URL also changed to `/relay` — update Google Console config.

### CDN
- CPSS-16903: Pieces images migrated to Cashfree CDN — done (Vishal, May 5)

---

## Mothi's Inputs / Flags in this Thread

1. **Templates as Carousel** as first page — not workflow list (shared with Vinesh, Ram, Mayank, Subbu)
2. **Swiggy MCP** as reference for builder/dev positioning
3. **Fintech API orchestration vision** — FinQub / LendAPI model; Relay as orchestration layer for payments, payouts, KYC, KYB, fraud, sanctions; win enterprise partners (Equifax, FIS, KPMG, Deloitte)
4. **Secure ID nodes in MCP + Workflow Builder** — asked about blockers (with reference screenshot)
5. **MCP + runs visibility question:** "When a merchant installs MCP in Claude Code and creates workflows just by prompting — why do they need to log into the no-code builder just to see runs? Can't MCP show agent runs in Claude itself?"
6. **Positioning doc shared:** `docs.google.com/document/d/1eouRFAHqvcMiGTZFgjP7A7Q5CQbmE-TAWTUz7TElp6M`

---

## Competitor Signals

| Competitor | Signal |
|---|---|
| **Razorpay Agent Studio** | Live product demo on LinkedIn, Apr 30 |
| **PhonePe** | Launched AI-powered integration agent — collapses PG go-live from weeks to minutes (LinkedIn, May 6) |
| **Mistral AI** | Launched "Workflows" — enterprise AI orchestration, public preview (InfoQ, May 1) |
| **Shopify** | Replaced GPT-5 with self-hosted Qwen 3; 75x LLM cost reduction, 2x quality (AIM, May ~1) |

---

## Open Threads / Action Items

| Who | What |
|---|---|
| Vishal | Kafka consumer tuning + Vault caching for 20 TPS |
| Vinesh | HITL e2e + data fetcher |
| Karthik | Refund approval plugin, Bolna plugin in node-executor |
| Satyam | MCP to PROD (blocked on mvn cache + workflowsvc) |
| Subbu/Saksham | Skills as npm pkg + Gemini testing |
| Shanth | Docs for Overview, Create Workflow, Connections, Manage Workflows |
| Prem/DL | PG webhook new topic name for `RELAY` channel type |
| Mothi | WTF forum use case suggestions (Ram's ask for Nected-like use cases) |
