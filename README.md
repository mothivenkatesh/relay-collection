# relay-collection

Consolidated snapshot of the three `relay`-named repositories, combined into one **private** repo on 2026-06-16. Each source repo lives in its own subfolder.

This is a **files-only snapshot** — the current contents of each source repo at consolidation time, with a fresh git history. Upstream commit history was not carried over.

## Contents

| Subfolder | Source repo | Visibility | What's inside |
|---|---|---|---|
| [`relay/`](relay/) | `mothivenkatesh/relay` | private | Main Relay working repo — landing page (`relay/docs/index.html`), Razorpay Agent Studio competitor teardown, 20+ `relay_*` agent skill specs, research data, decks |
| [`relay-gtm/`](relay-gtm/) | `mothivenkatesh/relay-gtm` | private | Cashfree Relay GTM material — "GTM v2 (phased to GFF 2026)", `RELAY_GTM_v1.md`, research |
| [`cashfree-relay-preview/`](cashfree-relay-preview/) | `mothivenkatesh/cashfree-relay-preview` | public | Relay preview landing page ("Best Payments MCP for India's AI-Native Businesses") |

## Notes

- The three source repos remain **intact and unchanged**. This collection is additive.
- To refresh a subfolder, re-pull from its source repo and copy the files in.
