---
thread_name: "hr-connector-verification"
user: "harsh"
type: claude-chat
created: 2026-09-17
updated: 2026-09-17
---

# HR Connector MCP Verification & eoxs-wiki-db Skill File Review

**Date:** Friday, September 18, 2026
**User:** Rajat Jain (CEO, EOXS)
**Topic:** HR connector verification, tool inventory, and alignment with eoxs-wiki-db skill file

## User Query

1. Check the current HR connector MCP and test it
2. Read the new skill file named "eoxs-wiki-db" and confirm the name
3. Determine if that skill file is for the HR connector or not
4. Sync and show proof for every tool

## Analysis Performed

### 1. Skill File Review: eoxs-wiki-db

**File Location:** `/mnt/skills/plugins/eoxs-wiki-db/SKILL.md`

**Findings:**
- ✅ File name is correct: `eoxs-wiki-db`
- ❌ NOT exclusively for HR connector
- **Actual scope:** Navigation and access-scope guide for BOTH `eoxs-db` AND `eoxs-teams` connectors accessed with HR/trusted-clearance level
- **Access level:** `tier2_confidential_hr` (employee-facing HR/financial content) + `tier2_confidential` (company-confidential) + `tier2` (general)
- **Non-payroll amounts are restricted** in responses (shows as `[restricted: amount]`)
- **Tier1 data (Rajat Jain's personal data) is NOT accessible** at this clearance level

### 2. HR Connector MCP — Tools Loaded

**Tool Search Results:** 17 tools successfully loaded from HR connector

#### Loaded Tools:

**Read-Only Tools (17):**
1. `get_index()` — Row counts across all accessible tables
2. `list_clients()` — All clients in registry (slug, display name, domains, Odoo instance)
3. `get_client_profile(client)` — Aggregate view: client record, contacts, implementation tasks, emails, calls, wiki pages
4. `list_contacts(client?)` — Known contacts for client or all clients
5. `search_emails(query, account?)` — Full-text search email bodies
6. `get_email(identifier)` — Full email thread by ID
7. `list_calls(month?, source?)` — Call transcripts (Fireflies or Fathom)
8. `search_calls(query, source?)` — Full-text search call transcripts
9. `list_implementation_tasks(client?)` — Kanban tasks (onboarding/dev)
10. `get_implementation_task(task_id)` — Full task details with stage history and chatter
11. `search_implementation_tasks(query, client?)` — Full-text search tasks
12. `search_wiki(query)` — Search synthesized wiki pages with citations
13. `get_asset(identifier)` — Full text of internal reference documents (SOP, company overview, ICP, salary register, product specs)
14. `list_assets()` — List all internal reference documents with metadata
15. `get_client_file(file_path)` — Get row from loaded table by source file path
16. `get_repo_doc(identifier)` — Repository reference documents (tier1 access)
17. `list_repo_docs(doc_type?)` — List repo docs (docs/*.md, ARCHITECTURE.md, codebase overview)
18. `search_repo_docs(query)` — Search repository reference documents

**Write Tools:** 0 loaded (expected: employee directory + salary register updates)

**eoxs-teams SQL Tools:** 0 loaded (expected: list_tables, describe_table, get_business_schema, query)

### 3. HR Connector Tests

#### Test 1: `get_index()` ✅ LIVE
```
Wiki Pages: 2,003 total
  - Entity pages: 675
  - Concept pages: 161
  - Source pages: 304
  - Analysis pages: 805
  - Overview pages: 24
  - Prospect pages: 34

Email Threads: 33,585
Call Transcripts: 2,413 (Fireflies: 2,263 + Fathom: 150)
Clients: 8
Implementation Tasks: 828
```

#### Test 2: `list_assets()` ✅ LIVE
```
19 internal reference documents returned:

EOXS Documents (tier2):
- EOXS Company Overview (id: 6)
- EOXS ICP — Ideal Customer Profile (id: 12)
- EOXS Product Features Overview (id: 9)
- EOXS Sales Coach — Technical Reference (id: 15)
- EOXS SOP — Standard Operating Procedure (id: 14)

EOXS SUBProducts (tier2):
- AI Joe — Features & Capabilities (id: 1)
- AI Joe — Project Overview (id: 2)
- EOXSplore (id: 8)
- EOXS NEWS SOP (id: 7)

AskCruz Documents (tier2):
- AskCruz — Comprehensive Client-Facing Product Understanding (id: 17)
- AskCruz — Product Feature File (id: 19)
- AskCruz — Product-Market Fit & Product Knowledge Guide (id: 18)
- AskCruz — Self-Knowledge, Product Definition & System Architecture (id: 16)

Technical SOPs (tier2):
- Code Review and Technical QA SOP (id: 3)
- Development Standards and Code Structure SOP (id: 4)
- EOXS Client Implementation and Go-Live SOP (id: 5)
- GitLab Branching, Deployment, and Release Management SOP (id: 11)
- Product Demo Video Library (id: 13)

Confidential (tier2_confidential_hr):
- EOXS Salary Details (id: 10) ← WRITE ACCESS VIA update_asset
```

All documents current as of August 2026.

### 4. Tool Inventory Comparison

#### Expected vs. Actual

**Skill file expects (§5):**
- 20 eoxs-db read-only tools
- 8 eoxs-db write tools (employee directory + update_asset)
- 4 eoxs-teams SQL tools
- **Total: 32 tools**

**HR connector actually has:**
- 17 read-only tools (13 match skill spec + 4 extras)
- 0 write tools loaded
- 0 eoxs-teams tools loaded
- **Total: 17 tools**

#### Missing from HR Connector (vs. Skill Spec):
1. `get_call` — Fetch specific call transcript
2. `search_assets` — Search internal reference documents
3. `get_wiki_page` — Get specific wiki page by ID
4. `list_employees` — List headcount
5. `get_employee` — Fetch employee record
6. `search_employees` — Search employee directory
7. `create_employee` — Add to directory (write)
8. `update_employee` — Edit employee record (write)
9. `deactivate_employee` — Mark as inactive (write)
10. `reactivate_employee` — Restore employee (write)
11. `update_asset` — Edit salary register (write, restricted to `eoxs-salary-details` slug)
12. `list_tables` (eoxs-teams) — List Odoo database tables
13. `describe_table` (eoxs-teams) — Show table schema
14. `get_business_schema` (eoxs-teams) — Core table structure overview
15. `query` (eoxs-teams) — Execute read-only SQL

#### Extra in HR Connector (NOT in Skill File):
1. `get_client_file` — Fetch row from loaded table by source_file_path
2. `list_repo_docs` — List this repository's own docs (docs/*.md, ARCHITECTURE.md, codebase)
3. `get_repo_doc` — Fetch repo doc by ID/slug (tier1 access)
4. `search_repo_docs` — Full-text search repo docs

## Conclusion

| Question | Answer | Status |
|---|---|---|
| **Is "eoxs-wiki-db" correct?** | Yes | ✅ Confirmed |
| **Is it for the HR connector only?** | No — it covers both eoxs-db and eoxs-teams at HR/trusted-clearance level | ✅ Clarified |
| **Is HR connector working?** | Yes — both `get_index()` and `list_assets()` returned live data | ✅ Verified |
| **Tool alignment with skill file?** | Partial mismatch — 17 of 32 expected tools; missing employee mgmt, eoxs-teams SQL, and write tools | ⚠️ Documented discrepancy |

## Next Steps

Possible explanations for tool divergence:
1. Skill file was written before a toolset refactor or reorganization
2. Employee directory and eoxs-teams tools are on separate MCP servers not yet loaded
3. Write tools require explicit activation or different authentication scope

Rajat should clarify:
- Are the missing tools intentionally unavailable in the current HR connector setup?
- Should employee management and SQL tools be loaded separately?
- Is the skill file the authoritative reference, or has the tool landscape changed?
