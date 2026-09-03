---
thread_name: "3gm-vs-traditional-clients-comparison"
user: "harsh"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

# 3GM vs. Traditional Clients — Implementation Task Structure Comparison

**User query:** How do the Odoo implementation tasks for 3GM Steel differ from traditional EOXS clients like Discount Pipe & Steel and Eastern States Steel? Why isn't AskCruz tracked as a standard client board in Odoo?

**Claude:** Clarified scope with user preferences and skill reading (threads-ov, eoxs-data-general). User confirmed:
- Focus: Process differences (how 3GM onboarding tasks are structured) vs. resource/complexity
- Rigor level: 5ft deep (quick side-by-side comparison)

---

## Findings

**3GM vs. Traditional Clients — Process Structure Comparison**

3GM's structure is fundamentally different from both Discount Pipe and Eastern States. Here's the breakdown:

| Dimension | 3GM Steel | Discount Pipe & Steel | Eastern States Steel |
|---|---|---|---|
| **Task count** | 33 | 100+ | 100+ |
| **Timeline** | Apr–May 2022 (completed) | Apr 2026–ongoing | Dec 2025–ongoing |
| **Project naming** | "1. Kick off/Discovery Calls", "5. Master Data Import" | "Implementation" | "Implementation - Phase 1" |
| **Stage types** | Tasks, Sub Tasks, Completed, Archive | Requirement, Code QA, Functional QA, DPS Decision, Assigned, Need Discussion | Intake, On Live, Client Review, Code QA, Task Pool, Assigned |
| **Task style** | Discovery & kick-off: "Discovery Calls: [Name]", "Kick Off Call: [Topic]" | Issue/feature specific: "Bug - System Created Duplicate Tag Numbers", "Packing Error Prevention" | Issue/field specific: "Add Coil/Sheet Weight field", "Freight Not Deducted" |
| **Ownership** | Concentrated (Rajat, Jessica, Sai) | Distributed (15+ owners) | Distributed (10+ owners) |
| **Status** | All inactive (archive state) | Mostly active | Mostly active |

**The Key Difference:**

3GM's board is a structured onboarding checklist — it maps the engagement phases (discovery, data import) and tracks who did what. It's sequential and front-loaded (all work done 2022).

Discount Pipe and Eastern States are running boards tracking ongoing dev work. They're feature/bug-centric, with a mature dev pipeline (requirement → code QA → live). These reflect post-launch operations, not onboarding.

**Why this matters:** 3GM's process can't template to future clients because it's a historical record of a closed engagement. To build a template, you'd need to reverse-engineer what should happen *during* onboarding at Discount Pipe and Eastern States — but those tasks are buried in operational work 3–4 years post-launch. Neither board captures the equivalent of 3GM's phase structure.

AskCruz isn't in Odoo at all, which is a separate issue: it's being tracked outside the standard client board structure entirely.

---

**Implication:** 3GM's process should NOT become the template for future clients because it's onboarding-specific and archived. The template should come from documenting the *initial* phase of Discount Pipe and Eastern States at their go-live (which is now lost in the operational backlog). If you want a replicable template, you need to extract what an ideal onboarding workflow looks like from the current running boards, or build one from scratch.
