---
thread_name: "jagriti-3gm-detailed-working"
user: "harsh"
type: claude-chat
created: 2026-09-09
updated: 2026-09-09
---

# Jagriti: Complete 3GM System Understanding — From Beginner to QA Tester

## Conversation History

### Turn 1: Initial Request
**User (Jagriti):** "im jagriti, give me every information about askcruz. all the workings. how is it beneficial to companies and all the details you know about it"

**Response:** Provided overview of AskCruz (startup, MCP 2.0, team structure, 3GM project)

---

### Turn 2: 3GM Technical Deep Dive
**User:** "give me more details about Specific 3GM technical details or testing scope. i want all the information and working of the 3GM. want to understand the details which are present there to run it efficiently"

**Response:** Comprehensive 7-phase breakdown with:
- OAuth authentication flow
- Email ingestion via Microsoft Graph
- 6-table database schema
- Deduplication logic
- Attachment extraction
- Sync logging
- Performance benchmarks
- Testing scenarios

**Saved to vault:** `jagriti-3gm-detailed-working.md`

---

### Turn 3: Uploaded Documents & Beginner Explanation
**User:** Uploaded 5 documentation files:
1. linear-integration.md
2. ARCHITECTURE.md
3. STATUS.md
4. outlook-ingestion.md
5. wiki-ingestion.md

**Request:** "go through this file and make me understand the content of the file like a beginner"

**Response:** Comprehensive beginner-friendly guide covering:

**File 1: ARCHITECTURE.md**
- Blueprint of how 3GM system is connected
- Three key pieces: app.py, outlook_fetcher.py, Postgres database
- Two processes run independently, communicate via database

**File 2: outlook-ingestion.md**
- 5-step OAuth connection flow
- Email sync every 60 seconds
- Deduplication strategy (one email, multiple mailboxes)
- Attachment text extraction (PDF, Excel, images)
- 6 database tables explained with examples

**File 3: STATUS.md**
- Current system status (as of Sep 7, 2026)
- What's working: Email sync, knowledge pipeline, first live page
- What's not yet: Real mailboxes, Linear operational, scheduling
- Current metrics: 19 emails, 1 live page, 21MB database

**File 4: wiki-ingestion.md**
- 5-phase knowledge generation pipeline:
  1. DETECT - Find new emails
  2. DRAFT - AI writes summaries
  3. CONSOLIDATE - Merge duplicates
  4. REVIEW - Independent fact-check
  5. PROMOTE - Make live
- Safety model: AI can't touch public wiki or database
- Real example: "Brannon Steel" page (drafted, rejected for unsupported claim, fixed, approved, published)

**File 5: linear-integration.md**
- Two-lane Linear board:
  1. Pending Drafts - Content review
  2. System Health - Operational alerts
- Webhook integration for two-way communication
- Rejected pages can be fixed via comments
- System failures trigger alerts, auto-resolve when fixed

**Complete data flow diagram** showing all 5 phases integrated

**Saved to vault:** Updated transcript with complete beginner's guide

---

### Turn 4: Creating Understanding Document
**User:** "make a docs file based on the understanding of the documents i have provided you. it should not be very long. it should only represent about my understanding"

**Response:** Created concise documentation file capturing Jagriti's QA perspective:

## **3gm-understanding.md Contents:**

### Summary Section
- One-line system description: "Takes emails from Outlook, stores in database, turns them into wiki pages"

### Three Main Parts
1. **Email Collection** - How Outlook connects, 60-second syncing, dedup, attachment extraction
2. **Knowledge Generation** - 5-phase pipeline (detect → draft → consolidate → review → promote)
3. **Linear Board** - Two lanes for rejected pages and system health

### Current Status
- ✅ Works: Email sync, pipeline, fact-checking, first live page
- ❌ Not yet: Real mailboxes, Linear board operational, scheduling
- Numbers: 19 emails, 1 page, 0 production mailboxes

### Database Reference Table
- outlook_accounts, outlook_messages, outlook_attachments, outlook_message_sightings, outlook_folder_sync_state

### QA Testing Checklist
- Email sync testing (timing, dedup, attachment extraction, recovery)
- Wiki pipeline testing (detect, draft, review, consolidate, promote)
- Linear integration testing (rejected pages, fix comments, auto-promotion, alerts)
- Data integrity testing (orphaned records, duplicates, sighting validity, cursor accuracy)

### Key Gotchas
- Access tokens expire every hour
- Delta cursors are baked (field changes need cursor reset)
- Deletions don't reflect (archive by design)
- Dedup race conditions possible
- Graph API timing risks

### Quick Status Checks
- SQL queries to verify email count, attachment extraction, sync health, rejected pages

### Health Indicators
- Email count growing
- Attachments getting text extracted
- No sync errors for 24+ hours
- Pages being drafted and promoted
- No orphaned records

### Questions Jagriti Needs Answered
- When will real mailboxes be connected?
- What's exact failure threshold for sync alerts?
- How often to verify dedup manually?
- Rollback plan if bad page goes live?
- How to simulate attachment extraction failures?

---

## Key Learning Points Extracted

1. **System Purpose**: Archive and synthesize email data into searchable knowledge
2. **Core Workflow**: Connect → Sync → Detect → Draft → Review → Promote
3. **Safety First**: AI cannot touch production wiki, only database operations
4. **Two-Way Integration**: Linear board is control surface for rejected pages + system health
5. **Current State**: Fully built and tested with test data, awaiting production mailbox connection

---

## Files Created for Jagriti

1. **3gm-understanding.md** - Concise QA perspective document (1-page reference)
2. **Vault transcript** - Complete conversation history with all explanations

---

**Status:** Complete. Jagriti now has:
- ✅ Understanding of all 5 system components
- ✅ Knowledge of email sync mechanics
- ✅ Grasp of wiki pipeline (5 phases)
- ✅ Linear board integration knowledge
- ✅ QA testing checklist
- ✅ Concise reference document for daily work
