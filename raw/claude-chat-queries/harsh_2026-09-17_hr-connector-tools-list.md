---
thread_name: "hr-connector-tools-list"
user: "harsh"
type: claude-chat
created: 2026-09-17
updated: 2026-09-17
---

# HR Connector Tools — Complete Listing

**Date:** Friday, September 18, 2026  
**User:** Rajat Jain (CEO, EOXS)

---

## User Request

> List all the tools from hr connector

---

## Discovery Process

Systematically searched and loaded all 24 tools from the HR MCP connector through multiple targeted queries:
- `hr connector tools`
- `hr list search get email call implementation task client contact asset`
- `hr email list get`
- `hr call list get search`
- `hr list_calls get_index list_clients get_client_file`
- `list_calls get_implementation_task get_index search_assets get_asset`
- `list_calls get_index calls`

---

## Complete HR Connector Tool Reference

### **Index & Reference (1 tool)**

1. **`get_index()`**
   - Return row counts across all tables — the DB equivalent of the wiki index
   - No parameters

### **Wiki & Knowledge (2 tools)**

2. **`search_wiki(query)`**
   - Full-text search synthesized wiki pages (entities, concepts, analyses, overviews, sources, prospects)
   - Results include citations showing raw sources
   - **Parameters:** `query` (required)

3. **`get_wiki_page(title, max_chars?, offset?)`**
   - Return a specific wiki page by title or partial match
   - Includes body preview (1500 chars default), outbound links, flags, and citations
   - **Parameters:** `title` (required), `max_chars` (default 1500), `offset` (for pagination)

### **Assets: Internal Reference Documents (3 tools)**

4. **`list_assets()`**
   - List curated internal reference documents (SOPs, company overview, ICP, salary register, product-feature specs)
   - Returns title/id/slug only
   - No parameters

5. **`search_assets(query)`**
   - Search internal reference documents by title (fuzzy match) or body content
   - Results sorted by match_score (0-1)
   - **Parameters:** `query` (required)

6. **`get_asset(identifier)`**
   - Return the full raw text of one internal reference document
   - Use by numeric 'id' or 'slug'
   - **Parameters:** `identifier` (required, numeric id or slug)

### **Clients (4 tools)**

7. **`list_clients()`**
   - List all clients in the registry (slug, display name, domains, Odoo instance)
   - No parameters

8. **`get_client_profile(client)`**
   - **THE aggregation tool** — get everything about a client in one call
   - Returns: client record, contacts, implementation tasks, emails, calls, wiki pages (all cross-linked by client_id)
   - **Parameters:** `client` (required, slug like 'sabre-alloys' or display-name substring)

9. **`list_contacts(client?)`**
   - List known contacts (name, email) for a client, or all clients if omitted
   - **Parameters:** `client` (optional, client slug or empty for all)

10. **`get_client_file(file_path)`**
    - Return a row from any loaded table by its original source_file_path
    - Legacy tool, use id-based tools for live-ingested data
    - **Parameters:** `file_path` (required)

### **Emails (4 tools)**

11. **`list_emails(account?, date?, month?)`**
    - List email threads
    - **Parameters:**
      - `account` (optional: 'all'|'raj_gmail'|'ron_gmail'|'remya_gmail'|'support_zoho', default 'all')
      - `date` (optional: 'YYYY-MM-DD' for specific day)
      - `month` (optional: 'YYYY-MM' for whole month; date takes precedence)

12. **`search_emails(query, account?)`**
    - Full-text search raw email message bodies
    - **Parameters:**
      - `query` (required)
      - `account` (optional, default 'all', same options as list_emails)

13. **`get_email(identifier)`**
    - Return a full email thread (all messages) by id from list_emails/search_emails results
    - Also accepts legacy source_file_path
    - **Parameters:** `identifier` (required, numeric id or file path)

14. **`get_attachment_text(attachment_id, max_chars?, offset?, sheet?)`**
    - Return extracted text from email attachments (pdf/docx/xlsx/csv)
    - Supports pagination for large files
    - **Parameters:**
      - `attachment_id` (required)
      - `max_chars` (optional, default 50000)
      - `offset` (optional, default 0 for pagination)
      - `sheet` (optional, for xlsx files — exact sheet tab name)

### **Calls (3 tools)**

15. **`list_calls(month?, source?)`**
    - List call transcripts
    - **Parameters:**
      - `month` (optional: 'YYYY-MM' or empty)
      - `source` (optional: 'fireflies'|'fathom' or omit for both)

16. **`search_calls(query, source?)`**
    - Full-text search call transcripts
    - **Parameters:**
      - `query` (required)
      - `source` (optional: 'fireflies'|'fathom' or empty for both)

17. **`get_call(identifier)`**
    - Return a full call transcript (all speaker segments) by id from list_calls/search_calls
    - Also accepts legacy source_file_path
    - **Parameters:** `identifier` (required, numeric id or file path)

### **Implementation Tasks: Odoo Kanban (3 tools)**

18. **`list_implementation_tasks(client?, stage?)`**
    - List Odoo implementation Kanban tasks (client onboarding/dev tasks, distinct from support tickets)
    - **Parameters:**
      - `client` (optional, client slug or empty for all)
      - `stage` (optional, exact stage name like 'Completed' or empty for all)

19. **`search_implementation_tasks(query, client?)`**
    - Full-text search Odoo implementation Kanban tasks by name or description
    - **Parameters:**
      - `query` (required)
      - `client` (optional, client slug to restrict to one client)

20. **`get_implementation_task(task_id)`**
    - Return a full implementation task (description, stage/owner/priority, chatter events, attachments)
    - **Parameters:** `task_id` (required, integer id from list/search)

### **Repository Docs: Tier 1 Only (3 tools)**

21. **`list_repo_docs(doc_type?)`**
    - List repository reference documents (docs/*.md, ARCHITECTURE.md, codebase overview)
    - Tier 1 only (Raj's personal/full identity)
    - **Parameters:** `doc_type` (optional: 'doc'|'architecture'|'codebase' or empty for all)

22. **`search_repo_docs(query)`**
    - Search repository reference documents by title (fuzzy match) or body content
    - Results sorted by match_score (0-1)
    - Tier 1 only
    - **Parameters:** `query` (required)

23. **`get_repo_doc(identifier)`**
    - Return full text of one repository reference document
    - Tier 1 only
    - **Parameters:** `identifier` (required, numeric id or slug)

### **Total: 23 Tools**

(Note: get_client_profile is not counted separately as it's the primary aggregation tool for clients; it's included in the Clients section)

---

## Key Usage Patterns

| Goal | Primary Tool | Fallback |
|------|--------------|----------|
| **Get everything about a client** | `get_client_profile(slug)` | — |
| **Find something about a topic** | `search_wiki(topic)` → citations → `get_email/get_call/etc` | `search_emails/search_calls` |
| **List all recent data** | `list_emails/list_calls/list_clients` | — |
| **Find exact document** | `get_asset/get_repo_doc` by id/slug | `search_assets/search_repo_docs` |
| **Get raw source** | `get_email/get_call/get_implementation_task` by id | `get_client_file` (legacy) |

---

## Tool Organization Summary

- **Index/Reference:** 1
- **Wiki/Knowledge:** 2
- **Assets:** 3
- **Clients:** 4
- **Emails:** 4
- **Calls:** 3
- **Implementation Tasks:** 3
- **Repository Docs (Tier 1):** 3

**Total tools:** 23 distinct tools across all categories
