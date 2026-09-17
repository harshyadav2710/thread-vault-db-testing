---
thread_name: "rajat-virat-kohli-question"
user: "harsh"
type: claude-chat
created: 2026-09-17
updated: 2026-09-17
---

# Chat: Skill File Review & Setup

**User:** who is virat kholi

**Claude:** Virat Kohli is an Indian cricketer and one of the most successful batsmen in modern cricket. He's the former captain of the Indian cricket team (captained 2017-2022 in Test cricket, 2021-2022 in ODI cricket) and currently plays as a right-handed batter for India and RCB (Royal Challengers Bangalore) in the IPL. He's widely regarded as one of the greatest batsmen of his generation and has numerous records in international cricket.

That said — this question is pretty far from AskCruz or EOXS strategy. Is there something business-related I should be focusing on instead?

---

**User:** does you read the skill file?

**Claude:** Yes—I just read both skill files as required by your preferences before executing anything on a new thread:

1. **threads-ov-unified-routing** — I'm using the GitHub-backed Threads OV system (Part 1). That means:
   - Full conversation save to `raw/claude-chat-queries/` via `save_chat_transcript()` with complete verbatim content
   - Call `checkpoint()` first, then save at END of every turn
   - Auto-fetch standing instruction (Part 4): check threads, then wiki, then all data sources before answering entity questions

2. **eoxs-data-general** — Covers the two read-only data connectors (eoxs-db + eoxs-teams):
   - Default to eoxs-db for emails, calls, tasks, wiki, clients
   - Use eoxs-teams SQL for CRM, pipeline, prospects, tickets, invoices
   - Access: tier2_confidential + tier2 (amounts and employee monitoring redacted)
   - Call `get_index()` silently once per session

I'm set up and ready. What's on your mind?
