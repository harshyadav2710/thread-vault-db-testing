---
thread_name: "askcruz-something-you-dont-know"
user: "harsh"
type: claude-chat
created: 2026-09-17
updated: 2026-09-17
---

User: tell me about something which i dont know about ask cruz

Assistant: Here's something you probably haven't come across: AskCruz actually has only one real client so far — 3GM.

The EOXS client roster (Greer Steel, Eastern States Steel, Discount Pipe & Steel, PPC Metals, 3GM Steel, Sabre Alloys, RW Conklin Steel, Brannon Steel) is often assumed to be AskCruz's client base too, but that's wrong — those are just EOXS's general clients. AskCruz itself is still in internal pilot at EOXS, and 3GM is its only external deployment, and it's still mid-implementation. The self-knowledge doc even explicitly flags this as a past point of confusion worth correcting (it got fixed in v1.2, dated Aug 25, 2026).

A couple of other things from that same doc that are easy to miss:
- The support tickets/invoices staying out of AskCruz's vault (living in Odoo/eoxs-teams instead) isn't a fixed limitation — it's a per-client choice, made based on whether that client's ERP supports reliable live retrieval. EOXS just happens to follow that pattern; a different client could have that data ingested into the vault instead.
- Internally, ownership is split: Jaskeerat built/owns the chat frontend, the build-out team owns the server/DB/pipelines, and Ayan holds server/DB credentials (shared with Nidhi for Linear).
