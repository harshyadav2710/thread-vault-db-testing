---
thread_name: "brannon-project-overview"
user: "harsh"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

# Brannon Project Overview Conversation

## User Request 1
Tell me everything on very high level on brannon project

## Response 1

Based on the wiki and email data, here's the high-level overview of the Brannon Steel project:

**What it is:**
Brannon Steel (a steel manufacturing client) is implementing EOXS's MTR AI module—an artificial intelligence system for Materials Testing Report (MTR) data processing and inventory management. This is an implementation/deployment project, not a product development effort.

**Timeline:**
- Launched formally Feb 2026; weekly implementation huddles run Feb-Jun 2026
- Data-sourcing phase started Jan 27, 2026
- Currently in live operations as of Aug 2026

**Key people:**
- Ranim Fallaha — Brannon-side project lead (appointed Dec 22, 2025)
- Ayaan — EOXS-side project lead (appointed Feb 24, 2026)

**Core deliverable:**
MTR AI system handling:
- Materials testing report data ingestion and duplicate detection
- Inventory data formatting and QA
- Grade verification and ASTM spec matching

**Current status challenges (as of Aug 2026):**
- Data quality issues: spec-matching false negatives and material grade mismatches emerging
- Three errors reported in a single week (Aug 11, 14, 14)—indicating gaps between what the AI flagged vs. what client specs actually require
- Naming/format inconsistencies in inventory data (M1 vs. 3.1 vs. 23.1 conventions)
- Escalation/ticket tracking getting out of sync (also noted as a wider pattern affecting other clients)

**Operational cadence:**
Weekly implementation huddles + ongoing task-thread updates via the Odoo client portal (task thread with 50+ messages logged between Jan-Aug 2026).

---

## User Request 2
yes check this also

## Response 2
I need clarification—what would you like me to check? For example:

- A specific client profile or contact details for Brannon Steel?
- Implementation task list/status in the Kanban?
- Call logs or email threads about particular issues?
- MTR AI concept/system overview?
- Financial/contract details?
- Something else?

What's the next angle you want explored?

---

## User Request 3
MTR AI concepts

## Response 3

Based on the client profile and wiki data, here's what MTR AI is as a concept:

**MTR AI — Core Concept:**

MTR AI is EOXS's artificial intelligence product for **Materials Testing Report (MTR) digitization and processing**. It's designed as a standalone module that works with any ERP system (including non-EOXS systems like Microsoft Business Central, which Brannon Steel uses).

**What it does:**

1. **MTR Ingestion & Digitization** — Automates capture of mill test reports into structured data
2. **Duplicate Detection & Deduplication** — Identifies and flags duplicate MTR submissions
3. **Spec Matching & Verification** — Matches MTRs against material specifications (ASTM standards, etc.)
4. **Inventory Data Management** — Formats and validates inventory records linked to materials
5. **Pre-Purchase Verification** — (Proposed expansion) Verifies MTRs against specs *before* purchase, without requiring storage in the system

**Brannon Steel's Implementation:**

**Phase 1 (Active):** MTR AI digitization — launched Feb 2026, confirmed complete Mar 12, 2026

**Phase 2 & 3:** Under roadmap discussion

**Current Live Features:**
- Algoma Join Report enhancement (heat/batch number matching logic) — implemented, QA tested, live in production as of Aug 2026

**Pending Feature:**
- Pre-Purchase MTR–Spec Verification — quoted but awaiting client sign-off

**Key constraint:** Works with any ERP, making it a portable product rather than EOXS-ERP-specific.

Want me to pull the full concept page or drill into specific technical details?
