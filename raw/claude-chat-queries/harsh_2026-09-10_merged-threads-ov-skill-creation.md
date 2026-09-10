---
thread_name: "merged-threads-ov-skill-creation"
user: "harsh"
type: claude-chat
created: 2026-09-10
updated: 2026-09-10
---

## User Request

Create accurate merged skill file from two ZIP files (eoxs-frontend-threads and claude-notes-vault). Final request: combine both in ONE md file but help readers know WHEN to call which system.

## Initial Analysis Phase (FLAWED)

Created single merged skill file with critical errors:
- Documented 11 non-existent tools
- Missed checkpoint tool
- Wrong signatures for save_chat_transcript
- Tried to unify incompatible systems

## Correction Phase

User caught the error and asked me to check actual tools in ZIP files.

**Audit Results:**

claude-notes-vault (github-backed):
- 5 ACTIVE tools: save_chat_transcript (thread_name, content), checkpoint, save_analysis, propose_ov2_xref, apply_ov2_xref
- Full-overwrite save contract

eoxs-frontend-threads (EOXS DB-backed):
- Main server: save_chat_transcript (thread_name, new_messages), get_thread, list_threads
- wiki_mcp: search_wiki, get_wiki_page, list_wiki_pages, get_source_thread
- db_mcp: list_tables, describe_table, get_business_schema, query
- 11 tools total
- Append-only save contract (incompatible with github)

These are TWO incompatible systems, not one.

## Solution Created

**Single unified file: `threads-ov-unified-routing.md`** (25KB)

Structure:
- **Part 0:** Decision tree / routing guide (WHEN TO USE WHICH)
  - Quick decision matrix (5 questions)
  - Detailed routing (if using GitHub vs EOXS)
  - Test cases (how to determine which system you have)
  
- **Part 1:** Threads OV (GitHub-Backed)
  - Save contract: full overwrite
  - 5 tools documented correctly
  - Mandatory auto-save: both checkpoint() AND save_chat_transcript()
  - CROSS-LINK workflow to OV2
  - Manual SYNTHESIZE on-demand
  - Examples, guardrails, quality standards

- **Part 2:** Threads OV (EOXS Database-Backed)
  - Save contract: append-only (INCOMPATIBLE with github)
  - 11 tools across 4 connectors
  - No checkpoint tool (not needed for append)
  - No cross-linking (github system's job)
  - Automated synthesis pipeline
  - SQL recipes with examples
  - Tier-based access control
  - 4-connector architecture

- **Part 3:** Comparison & Troubleshooting
  - Detailed comparison table
  - Common mistakes ("I saved to GitHub but it's not in EOXS queries")
  - Confusion detection tests
  - System-specific troubleshooting

## What User Gets Now

ONE file (`threads-ov-unified-routing.md`) that:
1. ✅ Helps them figure out which system they're using (Part 0)
2. ✅ Provides full skill documentation for BOTH systems (Part 1 & 2)
3. ✅ Explains when to use each tool in context
4. ✅ Clarifies incompatibilities (save contracts, tools, workflows)
5. ✅ Includes comparison tables throughout
6. ✅ Documents all 16 tools correctly (5 github + 11 eoxs)
7. ✅ Provides troubleshooting for common confusion points

Commissioned craft achieved:
- Only active tools (no false documentation)
- Correct signatures (both append and overwrite documented)
- Clear routing (decision tree + test cases)
- Accurate comparisons (side-by-side tables)
- Complete examples (both systems)
- SQL recipes with working templates
- Guardrails and restrictions explained
- No tools documented that don't exist

## Related Files (Kept for Reference)

- `threads-ov-github.md` (14KB) — GitHub system only
- `threads-ov-eoxs.md` (18KB) — EOXS system only
- DEPRECATED: merged-threads-ov-skill.md (removed, was incorrect)

User can either use the unified routing file OR the individual system files, depending on preference.
