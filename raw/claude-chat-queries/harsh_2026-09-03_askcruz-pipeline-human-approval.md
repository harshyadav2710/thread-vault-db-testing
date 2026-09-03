---
thread_name: "askcruz-pipeline-human-approval"
user: "harsh"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

# AskCruz Customer Email Pipeline — Human Sign-Off Location

## User Query

Trace the exact path of a customer email from ingestion to publication: Ingestion → Filtering → Sensitivity Classification → Central Store → Synthesis → Human Approval. Where does human sign-off occur?

## Response

Found it. Here's the exact path with human sign-off placement:

**SOURCE (Gmail/Zoho Email) → INGESTION → FILTERING → SENSITIVITY CLASSIFICATION → CENTRAL KNOWLEDGE STORE → KNOWLEDGE GENERATION → CITATION CHECK → HUMAN APPROVAL → RETRIEVAL → RESPONSE**

**Human sign-off occurs after citation check, before retrieval.** This is the gate before knowledge is considered "published" and made available through the system.

The documented flow (Section 20, Human Verification):

Raw information → AI-generated knowledge → Citation verification → **Human approval** → Published knowledge

**Key timing detail:** Knowledge generation runs on a six-hour cycle. So customer emails ingested in one cycle don't move into the published knowledge layer until that synthesis pass completes, citations are verified, and a human approves the synthesized knowledge page.

**What each stage does:**
- **Ingestion:** Event-driven, scheduled sweeps, webhooks (2-hour sweep for emails)
- **Filtering & Sensitivity Classification:** Relevance check, tier assignment (General / Company-Confidential / Raj-Personal maps to tier2 / tier2_confidential / tier1)
- **Central Store:** Metadata attached (source, sensitivity, context, timestamps)
- **Knowledge Generation:** Raw sources synthesized into readable pages, every 6 hours
- **Citation Check:** Verify each claim has supporting evidence
- **Human Approval:** Gatekeeper before publication; this is where human judgment happens
- **Retrieval & Response:** Published knowledge available to authorized users via queries

Human sign-off is structural, not optional. Nothing goes live without it.

Source: AskCruz Self-Knowledge document (asset id 16, updated 25 Aug 2026), Sections 8 and 20.
