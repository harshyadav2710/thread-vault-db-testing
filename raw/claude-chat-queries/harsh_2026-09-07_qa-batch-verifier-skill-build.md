---
thread_name: "qa-batch-verifier-skill-build"
user: "harsh"
type: claude-chat
created: 2026-09-07
updated: 2026-09-07
---

User: let me tell you properly why i want to make this skill file actually the main reason behind it is that recent days i have got many different QA tasks on my plate with different outcome need obviously so what i want is that i want a skill file where i can perform my QA's in a way where i can pull most of the data on a few goes rathe than a long prompting session which will reduce the cost me on both aspects long time consumption on one QA and reaching token limit in a small span of time so what you can do is to help me build a skill on that situation given upwards which will work on any kind of QA's i will perform and help me out to get more data on one go can you built me on and also if you have any questions by the time you are building the skill do ask ill give you the right direction you can continue walking

Assistant: Good — before I draft this, I want to nail down a few specifics so the skill actually matches how you work, rather than being a generic "be efficient" doc.

[Asked three clarifying questions via AskUserQuestion:
1. What kinds of systems/sources do your QA tasks usually pull data from? (so the skill knows what to batch)
2. What does a QA task's 'outcome' usually look like when you're done?
3. The core cost problem you're solving — is it mainly about how you ask (prompting), or how many separate tool calls get made?]

User answered:
1. Databases (SQL queries via MCP connectors), Emails/calls (eoxs-db), Mixed — varies task to task, Codebase/logs (all selected)
2. "each of above" (all deliverable types apply — varies per task)
3. Both equally (too many back-and-forth turns AND too many individual tool/query calls)

Assistant: [Proposed a new skill via propose_skills tool]

Skill name: qa-batch-verifier
Description: Use for any QA/verification task (DB checks, email/call sync checks, codebase/log checks, or mixed) to front-load scoping and batch data pulls into as few turns/calls as possible.

Full skill content proposed:

---
name: qa-batch-verifier
description: Use for any QA/verification task (DB checks, email/call sync checks, codebase/log checks, or mixed) to front-load scoping and batch data pulls into as few turns/calls as possible.
---

# QA Batch Verifier

Purpose: run QA tasks (schema checks, sync verification, dedup checks, attachment/extraction checks, or anything comparing expected vs actual across DB, email/calls, codebase, or logs) while minimizing turns, tool calls, and tokens. The failure mode this skill exists to prevent: discovering scope one piece at a time across many back-and-forth turns, and issuing many small individual lookups instead of a few comprehensive ones.

## 0. Before touching any tool: scope the whole task in one pass

Do not start pulling data until the full check-list for this QA task is known. If anything is ambiguous (which systems, which tables/records, what "pass" means, what time range, what counts as a discrepancy), ask ALL clarifying questions in a single batch (one AskUserQuestion call or one consolidated message) — never drip clarifying questions one at a time across turns.

Write the scope down as a checklist before running anything: every item to verify, the expected value/state for each, and which source will supply the actual value. This checklist is the spine of the whole task — every subsequent tool call should map to one or more checklist items, and nothing should be pulled that isn't on it.

If the task spans multiple systems (e.g. DB + email + logs), group checklist items by source so all the calls to one source can be issued together (see §1).

## 1. Batch the pulls, don't trickle them

- Parallelize independent lookups. If two checklist items pull from different, unrelated sources (or different unrelated records from the same source), issue those tool calls in the same turn, not sequentially across turns.
- One comprehensive query beats several narrow ones. For SQL-backed sources: call schema-discovery once (e.g. get_business_schema), then write a single query that joins/aggregates everything the checklist needs from that table set, rather than one query per checklist item. Use WHERE ... IN (...) / joins instead of looping single-row queries.
- Prefer summary/profile tools over manual assembly. If a connector offers a rollup call (e.g. a client-profile-style tool that returns records + related emails + calls + tasks cross-linked), call that once instead of chaining several narrower searches to rebuild the same picture by hand.
- Search narrow before broad, but only once. Try the specific, well-scoped query first; widen only if it comes back thin. Don't re-issue the same search reworded hoping for more.
- Cap iteration. If a source's results are paginated or capped (e.g. row limits), aggregate/filter in the query itself rather than pulling raw rows across multiple calls to count or dedupe client-side.

## 2. Track state in one place, not in your head across turns

For any QA task with more than ~5 checklist items, keep a single working file (in the working directory or scratchpad) with the checklist and, as results come back, each item's expected/actual/pass-fail/source. Update it in place rather than re-deriving or re-summarizing prior findings in every turn — this is what actually saves tokens across a long QA session, not just fewer calls per turn.

## 3. Report once, at the end, in a fixed shape

Don't trickle findings turn by turn. Deliver one consolidated report when the checklist is complete (or when you must stop and report partial coverage). Default report shape — adjust to what the task actually needs:

| Check | Expected | Actual | Source | Result |
|---|---|---|---|---|

Followed by a short discrepancy/bug list for anything that failed, each with enough reference (id, table, file, thread) that it can be re-verified without re-running the whole QA pass. Always name the source each check came from (which connector, table, file) and flag anything you couldn't verify (out of scope, access-restricted, source too thin) rather than silently omitting it.

## 4. When scope was "mixed" or unclear at the start

If the task didn't specify sources up front, do a single quick triage pass: figure out which systems are actually relevant (don't guess — check index/schema tools once each) before building the checklist in §0. Then proceed as above. Never start pulling data from a source "just in case" — every call should trace back to a checklist item.

---

The proposal was shown to the user via propose_skills for review/save — user has not yet responded to it.
