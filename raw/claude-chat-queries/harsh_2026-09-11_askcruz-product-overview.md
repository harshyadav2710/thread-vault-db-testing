---
thread_name: "askcruz-product-overview"
user: "harsh"
type: claude-chat
created: 2026-09-11
updated: 2026-09-11
---

# AskCruz Product Overview Thread

**User:** give me all the information you know about askcruz. what are its competitors and why askcruz is different from other products. how is it designed. what are its functioning and how is it beneficial to other companies. what are the information about the company which are stored here and how the information's are being fetched. collect the proper information from the mcp and provide me with the necessary answers.

**Assistant:**

## AskCruz — Full Overview

**What it is:** AskCruz is an AI-powered company knowledge platform and conversational assistant, built and operated by EOXS (Entrepreneurial Overhead Elimination Services). It turns a company's scattered information — email, calls, implementation/onboarding records, documents, business conversations — into a searchable, structured "second brain" that employees query in plain language.

It's currently in production as EOXS's internal pilot, and is mid-implementation with its **first (and so far only) external client, 3GM** — a steel-industry company, though AskCruz itself is explicitly **industry-agnostic**: its addressable market is any business with fragmented data, not any one vertical.

### The core problem it solves
Companies usually don't lack information — they lack a unified way to find and use it. Knowledge sits scattered across inboxes, spreadsheets, call recordings, project boards, and people's memories. AskCruz's thesis: **scattered information → organized knowledge → searchable evidence → conversational answer.**

### How it's designed (architecture)
A pipeline, not just a chatbot front end:

**Source systems → Ingestion → Filtering → Sensitivity classification → Central knowledge store → Knowledge generation → Citation check → Human approval → Retrieval → Response**

- **Sources:** Gmail (3 accounts), a shared Zoho support inbox, Fireflies and Fathom call transcripts, and client Odoo/implementation boards. Whether tickets/invoices are pulled live from a client's ERP or ingested into the vault is a per-client configuration choice, not fixed.
- **Ingestion:** event-driven hooks, scheduled sweeps, and source-specific fetchers/sync jobs.
- **Sensitivity classification:** every piece of info is tagged General / Company-Confidential / Raj-Personal, mapping to product access tiers `tier2` / `tier2_confidential` / `tier1`. Uncertain cases default to the more restrictive tier.
- **Knowledge generation:** raw source material is synthesized into readable knowledge pages with citations, checked, and **requires human approval** before publishing. This synthesis cycle runs every 6 hours.
- **Retrieval:** at query time, access/sensitivity boundaries are enforced again (two layers: database-level access control + an independent AI response-level security check) — a user's wording is never treated as authorization.

### What it functionally does — four pillars
1. **Company Brain** — shared working knowledge (who does what, past commitments, pricing exceptions, customer history, company vocabulary).
2. **Company Hands** — practical work: drafting quotes, flagging at-risk orders, summarizing calls, preparing account context.
3. **Digital Workforce** — standing responsibilities: watching an order queue, following an exception, reporting when a condition needs attention.
4. **Company Personalization** — reflects one specific company's vocabulary, pricing logic, tolerances, and customer expectations rather than generic industry assumptions.

### Benefit to companies
- One conversational entry point instead of manually searching five systems.
- Faster onboarding for new employees (less dependence on one person's memory).
- Evidence-oriented answers with citations, flagged uncertainty/conflicts rather than confident guessing.
- Role-aware access so sensitive data (financials, employee monitoring data) stays restricted.
- Grows incrementally as more sources are connected — not an all-or-nothing rollout.

### Competitors / differentiation
The internal documentation doesn't name specific competitor products — instead it positions AskCruz against two *categories*:
- **Generic AI** (e.g., a general chatbot) — broad knowledge, but no access to a company's internal context.
- **Traditional search tools** — can locate a record, but the employee still has to open it, read it, and reconstruct context by hand.

AskCruz's stated differentiator: *"Search finds information. AskCruz is designed to make organizational knowledge usable."* — i.e., it's a full pipeline (ingest → structure → verify → converse), not just a search index or a raw LLM wrapper. Other claimed differentiators: industry-agnostic positioning, multi-source synthesis, sensitivity-aware access control, citation-backed generation, and mandatory human approval before anything is published as knowledge.

Note: the documents are explicit that broad product-market fit is *not yet proven* — retention, ROI, pricing, and repeatable acquisition are still open questions with only one external client (3GM) so far.

### Where this information comes from, and how it's fetched
This all came from **curated internal reference documents** stored in the EOXS second-brain database (accessed via the `EOXS-DATA-GENERAL` connector, per the `eoxs-data-general` skill), specifically the "Assets" table:
- *AskCruz — Self-Knowledge, Product Definition & System Architecture*
- *AskCruz — Product–Market Fit & Product Knowledge Guide (Consolidated)*
- *AskCruz — Product Feature File*

I called `get_index()` for scope, `list_assets()` to find the relevant docs, then `get_asset(slug)` to pull each document's full raw text (not the summarized wiki version, since exact wording mattered here). All three are `tier2`-cleared documents, so nothing was redacted in this pull.
