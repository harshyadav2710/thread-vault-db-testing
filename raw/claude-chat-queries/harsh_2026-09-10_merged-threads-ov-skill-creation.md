---
thread_name: "merged-threads-ov-skill-creation"
user: "harsh"
type: claude-chat
created: 2026-09-10
updated: 2026-09-10
---

## User Request

Create accurate merged skill file from two ZIP files (eoxs-frontend-threads and claude-notes-vault), covering both systems.

Requirements: Option A (two separate skills), both save_chat_transcript contracts, only active tools.

## My Initial Attempt (WRONG)

Created single merged file with critical errors:
- Documented 11 non-existent tools (commented-out in code)
- Missed checkpoint tool entirely
- Wrong signatures for save_chat_transcript (incompatible contracts)
- Wrongly unified four separate MCP connectors

## Correction Process

User caught the error and asked me to check tools in ZIP files.

**Audit findings:**

**claude-notes-vault (git-based):**
- 5 ACTIVE tools: save_chat_transcript, checkpoint, save_analysis, propose_ov2_xref, apply_ov2_xref
- 11 tools commented-out/deprecated: search_*, list_*, get_* (all read tools)
- save_chat_transcript signature: (thread_name, content) — FULL overwrite

**eoxs-frontend-threads (DB-backed):**
- Main server: save_chat_transcript (thread_name, new_messages) — APPEND ONLY, get_thread, list_threads
- wiki_mcp: search_wiki, get_wiki_page, list_wiki_pages, get_source_thread
- db_mcp: list_tables, describe_table, get_business_schema, query
- 11 tools total, 0 commented-out
- save_chat_transcript signature: (thread_name, new_messages) — APPEND ONE EXCHANGE

Key differences:
- save_chat_transcript signatures are INCOMPATIBLE
- checkpoint exists in github, not EOXS
- Cross-linking (propose/apply) exists in github, not EOXS
- Synthesis is manual (github) vs automated (EOXS)
- These are NOT one system; they're four separate connectors (main, wiki_mcp, db_mcp)

## Solution: Two Separate Skills

### Skill 1: threads-ov-github.md (450+ lines)
- Covers claude-notes-vault only
- 5 active tools documented correctly
- Mandatory auto-save: both checkpoint() AND save_chat_transcript() every turn
- Full-overwrite save contract
- CROSS-LINK workflow to OV2
- Manual SYNTHESIZE
- File-based storage
- No mention of EOXS or database

### Skill 2: threads-ov-eoxs.md (550+ lines)
- Covers eoxs-frontend-threads cluster (4 connectors)
- 11 active tools documented correctly
- Append-only save contract (different from github!)
- NO checkpoint tool
- NO cross-linking (that's github system's job)
- Automated synthesis pipeline
- Database storage + tier-based access
- SQL recipes for queries
- Comparison table showing differences from github variant

## Key Corrections Made

1. ✅ Only documented ACTIVE tools (no commented-out tools)
2. ✅ Included checkpoint (was completely missed before)
3. ✅ Documented BOTH save_chat_transcript signatures with INCOMPATIBLE warning
4. ✅ Separated into two distinct systems (not one merged skill)
5. ✅ Added 4-connector architecture diagram (eoxs system)
6. ✅ Added comparison table (github vs EOXS)
7. ✅ Removed all tools that don't actually exist
8. ✅ Added "DO NOT CONFUSE" warnings at the top of each skill
9. ✅ Commissioned craft: SQL recipes with examples, workflow steps, troubleshooting, edge cases

## Files Delivered

- `threads-ov-github.md` (accurate, 5 tools)
- `threads-ov-eoxs.md` (accurate, 11 tools)
- DEPRECATED: merged file (do not use)
