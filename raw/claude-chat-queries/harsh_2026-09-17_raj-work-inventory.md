---
thread_name: "raj-work-inventory"
user: "harsh"
type: claude-chat
created: 2026-09-17
updated: 2026-09-17
---

# Raj's Work Inventory & EOXS Skills Update

## Initial Query
User asked: "Can you just list out the exact titles of all the work done by raj in his claude account we currently have in the system? I want to see a full inventory of what topics are documented."

## Issues Identified

1. **Wrong MCP Used**: I initially called `Internal-team`'s `search_wiki()` instead of `Thread-wiki`'s tools
   - This caused confusion because both MCPs have tools with the same names but search different data sources
   - Internal-team searches EOXS company docs (HR, ops, policies)
   - Thread-wiki searches Claude conversation threads and transcripts

2. **Clarification Request**: User asked which MCP provided the response
   - Response came from: **MCP: Internal-team**, Tool: `mcp__Internal-team__search_wiki`
   - But this was the WRONG choice for a thread-shaped question

## Root Cause Analysis

The `threads-ov-unified-routing` skill file clearly states (Part 0, lines 74-81):
> **Rule:** If the question is about a conversation, a chat thread, "what did we discuss," or **"what did [user] work on in Claude"** — route to **Thread Wiki**, never to Eoxs-Data-General.

User's question: "list out the exact titles of all the work done by raj in his claude account" is 100% a thread-shaped question that should route to Thread Wiki, not Internal-team.

## Solution: Updated `eoxs-data-internal-team/SKILL.md`

Added three critical sections to prevent this confusion:

### **1. New Warning Section at Top (Lines 6-27)**
```markdown
# ⚠️ CRITICAL: Tool Name Collision With Thread Wiki

This connector exposes search_wiki() and get_wiki_page() tools with identical 
names to Thread Wiki's tools — BUT THEY SEARCH DIFFERENT DATA SOURCES.

Tool Name          | This Connector (Internal-Team)           | ≠ Thread Wiki
search_wiki()      | Searches EOXS company docs              | Searches Claude conversation threads
get_wiki_page()    | Returns company documentation pages     | Returns synthesized thread summaries

## ❌ DO NOT USE THIS CONNECTOR FOR:
- "What did [user] work on in Claude?" → Use Thread Wiki (list_threads() / get_thread())
- "List all conversations by Raj" → Use Thread Wiki (list_threads(user="raj"))
- "What Claude threads mention [topic]?" → Use Thread Wiki
- "Show me all saved transcripts by [user]" → Use Thread Wiki
- Any question about "Claude conversations," "chat threads," or "saved transcripts"
```

### **2. Stop Sign in Section 1 (Line 59)**
```markdown
🛑 THREAD QUESTION? STOP. See the warning above. If the user is asking about 
Claude conversations, chat threads, or "what did [user] do in Claude," route to 
Thread Wiki, not here. This connector's search_wiki() will return company docs, not threads.
```

### **3. Explicit Capability Denial in Section 3 (Lines 166-171)**
```markdown
- NO THREAD / CONVERSATION LOOKUP CAPABILITY — cannot list Claude transcripts, 
  search user threads, or find saved chat conversations. Use Thread Wiki for any 
  "what did [user] do in Claude" question.

If asked to list a user's Claude conversations or threads, say plainly: 
"That requires Thread Wiki, not this connector. I need to search the thread archive instead."
```

## Files Created

1. **Updated skill file**: `/mnt/skills/plugins/eoxs-data-internal-team/SKILL.md`
   - Modified with three new warning/routing sections

2. **Downloadable copy**: `/mnt/user-data/outputs/eoxs-data-internal-team-UPDATED.md`
   - Complete updated file available for download

## Key Learning

The tool name collision (`search_wiki()` exists in both Internal-team and Thread-wiki) creates a silent failure mode where the wrong connector returns plausible-looking but incorrect data (company wiki page instead of thread summary) with no error.

Solution: Explicit, visible routing guardrails at the top of the skill file that flag thread-shaped questions immediately before any tool calls are made.

## Next Steps for Implementation

1. Use this updated skill file in production
2. Whenever a user asks "what did [user] do in Claude", the file now immediately flags it
3. Route to Thread Wiki's `list_threads()` / `get_thread()` instead
4. This prevents the wrong MCP from silently returning wrong-source answers
