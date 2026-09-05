---
thread_name: "askcruz-overview"
user: "harsh"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

## Claude Features for AskCruz — Complete Research & MCP Explanation

**User Journey:**
1. Asked: What are the new Claude features that can help AskCruz?
2. Asked: Where did you get your information from? (source transparency)
3. Asked: How to build reusable MCP servers? (beginner-friendly explanation)
4. Said: "leave it" (end conversation)

---

## RESEARCH SUMMARY

**Information sources used:**
- EOXS wiki (20+ synthesized pages on AskCruz, team, operations, challenges)
- AskCruz product spec documents (self-knowledge, market-fit, product feature file)
- Web search on Claude features (Sep 2026)
- Web search on MCP servers (specification, challenges, 2026 state)
- EOXS task board data (Ron's open items, ownership drift, deadline gaps)
- EOXS "Study Time" session transcript (Sep 2, 2026: Claude/MCP tooling review)

**Key findings delivered:**
1. **6 specific Claude features for AskCruz:**
   - Claude Code + Gmail MCP for 3GM OAuth testing
   - Cowork for task automation & ownership drift detection
   - Reusable MCP servers for multi-client integration
   - Fable 5.1 + prompt caching for email processing cost savings
   - Interactive artifacts for live task dashboards
   - Batch API for testing at scale

2. **MCP server explanation (beginner-friendly):**
   - What it is: translator plug between Claude and external systems
   - How to build: ~200 lines of code using Anthropic SDK
   - Why helpful: build once, reuse for 3GM/Sabre/Three D/future clients
   - Already built: yes for Gmail/Drive/GitHub; NO for Outlook email dedup
   - Main challenges: silent failures, scaling problems, credential sprawl, zero audit logging, deployment complexity

---

## CONTEXT SAVED FOR FUTURE REFERENCE

**About user (Aditya Yadav):**
- Startup Generalist Intern at AskCruz (joined July 20, 2026)
- Currently testing 3GM project: Outlook email sync (OAuth, dedup, attachment extraction, schema verification)
- Shared account with: Priyanshu (frontend), Jagriti (QA testing), Isha (HR), Danish, Harsimran

**About AskCruz:**
- Industry-agnostic AI knowledge platform (NOT steel-only despite 3GM being steel company)
- 10-stage ingestion pipeline with 6-hour synthesis cycle
- First external customer: 3GM (deal confirmed Aug 2026, mid-implementation, 2-user scope)
- Sales pipeline: Sabre Alloys, Three D Metals, legal services
- Real problems: task management overhead, ownership drift, email at scale

**Key decisions:**
- MCP servers: build after 3GM launches, not before (don't block 3GM go-live)
- Claude features: prioritize Cowork (task automation) + Fable 5.1 (cost savings) for immediate impact
- Testing approach: use Claude Code + Gmail MCP for 3GM, then evaluate building reusable MCP for next client
