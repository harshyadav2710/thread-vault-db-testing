---
thread_name: "qa-batch-verifier-skill-build"
user: "harsh"
type: claude-chat
created: 2026-09-07
updated: 2026-09-07
---

## QA Batch Verifier Skill Build

User: let me tell you properly why i want to make this skill file actually the main reason behind it is that recent days i have got many different QA tasks on my plate with different outcome need obviously so what i want is that i want a skill file where i can perform my QA's in a way where i can pull most of the data on a few goes rathe than a long prompting session which will reduce the cost me on both aspects long time consumption on one QA and reaching token limit in a small span of time so what you can do is to help me build a skill on that situation given upwards which will work on any kind of QA's i will perform and help me out to get more data on one go can you built me on and also if you have any questions by the time you are building the skill do ask ill give you the right direction you can continue walking

A: I asked three clarifying questions to scope the skill properly:
1. What kinds of systems/sources do your QA tasks usually pull data from?
2. What does a QA task's 'outcome' usually look like when you're done?
3. The core cost problem you're solving — is it mainly about how you ask (prompting), or how many separate tool calls get made?

User answered:
1. Databases (SQL), Emails/calls (eoxs-db), Mixed sources, Codebase/logs (all selected)
2. All deliverable types apply (varies per task)
3. Both equally — too many back-and-forth turns AND too many individual tool/query calls

I proposed qa-batch-verifier skill v1 focused on:
- Phase 0: Scope the whole task in one pass, ask all clarifying questions in a batch
- Phase 1: Batch pulls, parallelize independent lookups, write one comprehensive query instead of several narrow ones
- Phase 2: Track state in one working file across the QA session
- Phase 3: Report once at the end with a structured pass/fail table and discrepancy list

---

User: i need more context on that

A: I explained with examples how the skill works:
- **Without the skill:** multiple turns (Turn 1: check OAuth, Turn 2: check dedup, Turn 3: check attachments) = ~7.5k tokens, 3 turns
- **With the skill:** Scope upfront, then parallel pulls on all checks at once = ~3k tokens, 2 turns

Key benefit: one comprehensive joined query instead of five separate queries.

---

User: want it tweaked

A: I asked what specifically to adjust:
- Which phases to change (0/1/3)
- For a concrete example of a recent QA task

User answered:
- Adjust Phase 0 (scoping), Phase 1 (batching pulls), Phase 3 (reporting)
- Said "Here's a specific one" but then shifted focus

---

User: i have a task on the access right discrepancy what can we do on that?

A: I started asking specifics about the access rights task but user didn't fully answer. Then user said:

"also ill be working on different kind of tasks so let us re think on this and remake some thing more effective."

---

User: [Confirmed they want the skill rethought for ANY task type, not just access rights]

A: Asked what makes a workflow reusable:
1. A decision tree (ask what task, THEN prescribe flow) ✓ Selected
2. A modular checklist builder (you describe what, skill prescribes how) ✓ Selected
3. A flexible turn structure template ✓ Selected
4. Just give me a faster prompting pattern ✓ Selected

**Pain point:** Not batching queries (making 5 calls instead of 1 joined query) — THIS is the #1 token killer

---

A: Rebuilt qa-batch-verifier v2 with focus on:
- **Step 0:** Triage (what systems, what comparison, what scope) — 30 seconds to prevent 10 turns
- **Step 1:** Design the query before running (ONE comprehensive query with JOINs, not 5 separate calls) — THE CORE OF THE SKILL
- **Step 2:** Batch multiple sources in parallel if needed
- **Step 3:** Track findings in ONE markdown table (no re-narrating)
- **Step 4:** Report once with summary + table + discrepancies

Key example: Instead of Query 1 (users) → Query 2 (access_logs) → Query 3 (okta_sync), write ONE query with LEFT JOINs and CASE WHEN to surface all checks at once.

**Skill is now:**
- Adaptable to any task type (not locked into one pattern)
- Focused on query batching (the real token killer)
- Reusable across access rights, sync checks, schema audits, dedup, etc.

Skill proposal shown to user for review/save.
