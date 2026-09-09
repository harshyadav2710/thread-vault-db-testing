---
thread_name: "jagriti-3gm-detailed-working"
user: "harsh"
type: claude-chat
created: 2026-09-09
updated: 2026-09-09
---

# Jagriti: 3GM Outlook Email Sync System — Complete Beginner-Friendly Explanation

## User: "go through this file and make me understand the content of the file like a beginner"

**Uploaded Files:**
1. linear-integration.md
2. ARCHITECTURE.md
3. STATUS.md
4. outlook-ingestion.md
5. wiki-ingestion.md

---

## COMPREHENSIVE BEGINNER'S GUIDE TO 3GM SYSTEM

### **File 1: ARCHITECTURE.md — The Blueprint**

**What it does:** Shows how the entire 3GM system is connected.

**Simple diagram:**
```
Browser → Nginx + Flask Server → Database
          (your connection)    (stores emails)
                ↓
    outlook_fetcher.py (gets new emails every 60s)
```

**Three key pieces:**
1. **app.py** - Handles when you connect your Outlook account
2. **outlook_fetcher.py** - Continuously checks for new emails
3. **Postgres Database** - Stores everything (accounts, emails, attachments)

---

### **File 2: outlook-ingestion.md — How Emails Get Collected**

**The 5-Step Connection Process (OAuth):**

**Step 1: Generate Invite Link**
```bash
python -m ingestion.oauth_outlook invite 3gm_travis_outlook "Travis"
→ Creates a link that expires in 48 hours
```

**Step 2: Click Link → `/oauth/outlook/connect`**
- Link validation (is it real? expired?)
- Redirect to Microsoft's login page

**Step 3: Sign into Microsoft**
- Standard Microsoft login screen
- Click "Yes" to allow email reading
- App NEVER sees your password—only Microsoft knows it

**Step 4: Microsoft Sends Back Authorization Code → `/oauth/outlook/callback`**
- Code exchanged for two tokens:
  - **Access Token**: Read emails now (expires in ~1 hour)
  - **Refresh Token**: Get new access token later (lasts much longer)

**Step 5: Account Saved + Auto Sync Starts**
- Account info stored in database
- System immediately syncs existing emails
- User sees: "Travis's Outlook is connected"

**Why PKCE is Important:**
- Creates a verifiable connection between Steps 1 and 4
- Makes OAuth safe even over public networks
- Microsoft verifies the connection before giving tokens

---

### **The Email Sync Process (Every 60 Seconds)**

**Step-by-step:**

1. **Check Token Freshness**
   ```
   if (access_token age > 1 hour):
       use refresh_token to get new access_token
   ```

2. **Ask Microsoft for New Emails**
   ```
   Microsoft Graph API Call:
   "Give me all emails in Inbox since last check"
   
   Response includes:
   - Email ID (unique identifier)
   - Subject, Sender, Recipients
   - Body content (HTML + plain text)
   - Attachment list
   
   Returns in batches of 100 (to avoid memory overload)
   ```

3. **Deduplication**
   ```
   For each email received:
   - Check: Have we seen this email ID before?
   - If NO → Save to database
   - If YES → Skip message, but record this mailbox saw it
   
   Why? If CC'd to both Travis and Stefan:
   - First mailbox syncs it → saved
   - Second mailbox syncs same email → only record they saw it too
   - Result: One email record, two "sightings"
   ```

4. **Extract Attachment Text**
   ```
   For each attachment:
   - PDF → OCR to read text
   - Excel → Extract cell data
   - Images → OCR to read text
   - Save original file + extracted text
   ```

5. **Update Sync Timestamp**
   ```
   Save: "Last synced Inbox at 2:45 PM today"
   Next sync will only ask for emails after 2:45 PM
   ```

**The 6 Database Tables:**

| Table | Purpose | Example |
|-------|---------|---------|
| `outlook_accounts` | Connected mailboxes | Travis's account, token, sync time |
| `outlook_messages` | Actual emails (deduplicated) | "Q3 Report" email |
| `outlook_attachments` | Files from emails | Q3_Report.pdf (2.8 MB) |
| `outlook_message_sightings` | Which mailbox saw which email | "Travis saw this in Inbox" |
| `outlook_folder_sync_state` | Sync cursor per folder | "Inbox synced to Sept 7, 2pm" |
| `outlook_connect_tokens` | Temporary invite links | Link valid 2026-09-10, expires 2026-09-12 |

---

### **File 3: STATUS.md — What's Actually Running**

**Current System State (as of 2026-09-07):**

✅ **WORKING:**
- Email collection from Outlook
- Knowledge base pipeline (detect → draft → review → promote)
- Real wiki page created ("Brannon Steel")
- System monitoring built (but not fully connected)

❌ **NOT YET:**
- Real mailboxes connected (only test accounts used)
- Linear system fully operational
- Full automated scheduling running

**The Proof It Works:**
1. Created test accounts on Outlook
2. Connected them → emails synced to database
3. System drafted a wiki page about "Brannon Steel"
4. AI reviewer found an unsupported claim (good!)
5. Claim was fixed
6. Re-review approved it
7. Page went live on wiki

**Current Numbers:**
- 19 emails stored
- 17 email conversations
- 1 live wiki page
- 21 MB database size
- 0 production mailboxes connected (only test)

**The Two Environments:**

| Aspect | Staging | Production |
|--------|---------|------------|
| Domain | 3gmstaging.askcruz.com | 3gm.askcruz.com |
| Purpose | Testing & development | Real data goes here |
| Databases | Separate | Separate |
| Data | Test emails only | Will have real emails |
| Location | Singapore (SGP1) | Singapore (SGP1) |

---

### **File 4: wiki-ingestion.md — How Emails Become Knowledge**

**The 5-Phase Pipeline:**

**PHASE 1: DETECT**
```
"What emails are new?"

Action:
- Scan all emails in database
- Calculate SHA-256 hash (fingerprint) of each
- Compare against processed emails
- Mark new ones as "unseen candidates"
```

**PHASE 2: DRAFT**
```
"Write what these emails mean"

Action:
- Take batch of unseen emails (50 at a time)
- Send to Claude AI via command: claude -p
- AI reads emails, writes summary page
- Saves to "staging area" (not live yet)
- Example: "This email thread is about a deal with Brannon Steel"

Important Restrictions:
- AI can ONLY read emails
- AI can ONLY write to staging area
- AI CANNOT write to live wiki
- AI CANNOT access database directly
```

**PHASE 3: CONSOLIDATE**
```
"Merge duplicate drafts"

Action:
- Check if two batches drafted the same topic
- Keep only one version with best quality
- Avoid duplicate wiki pages
```

**PHASE 4: REVIEW**
```
"Fact-check everything independently"

Action:
- Different AI reviews each draft
- Checks: "Is every claim backed by a real email?"
- Marks as APPROVED ✅ or REJECTED ❌

Real example from 2026-09-06:
- Draft: "The batch/heat numbers are X"
- Review: "Where in the emails is this said?"
- Finding: "NOT in any email!"
- Decision: REJECTED ❌

Process:
1. Human fixes the page (removes unsupported claim)
2. Re-review runs independently
3. Second review approves it ✅
```

**PHASE 5: PROMOTE**
```
"Make it live"

Action:
- Approved pages published to public wiki
- Anyone can read them
- All sources linked (click to see original email)
```

**Safety Model (Two Layers):**

Layer 1 - **Tool Scope:**
- Drafting AI gets: read emails, write staging area
- Drafting AI CANNOT: touch public wiki, delete anything

Layer 2 - **Promotion Control:**
- Only `promote.py` (running outside any AI) writes to public wiki
- AI processes CANNOT force promotion

Result: AI cannot secretly publish false information

---

### **File 5: linear-integration.md — Alerting & Review Board**

**Two Separate "Lanes" on One Linear Team:**

**LANE 1: Pending Drafts (Content Review Board)**

```
Linear Board = Live To-Do List

Shows: All rejected pages + their rejection reason

How it works:
1. AI rejects a draft page
2. Page appears on Linear board with reason
3. Human reads reason
4. Human comments: "page 3: fix the date, then promote"
5. System automatically:
   - Fixes the page body
   - Re-reviews it
   - Promotes if it now passes
6. Result posted as comment on Linear
```

**Real Example:**
```
Board Item: "3GM-3: Wiki -- Pending Drafts"

Page 1: "Brannon Steel"
Rejection Reason: "Unsupported inference about heat numbers"

Human Comment: "page 1: remove the heat numbers sentence, it's not in the emails"

System Response:
- ✓ Fixed the page
- ✓ Re-reviewed it (passed this time!)
- ✓ Promoted to public wiki
- ✓ Posted: "Page 1 is now live!"
```

**LANE 2: System Health (Operational Alerts)**

```
Automatic Alerts for Failures:

When this happens:
- Outlook sync fails 3+ times in a row → New Linear issue
- Wiki drafting batch fails → New Linear issue
- System recovers → Alert auto-resolves

Each alert is independent:
- Created when problem starts
- Auto-deleted when problem ends
- No manual cleanup needed

Examples:
- "outlook_sync_failure: Travis's account sync failed 3x"
- "wiki_cycle_failure: Drafting batch 2 crashed"
- "wiki_promotion_failure: Promotion to live wiki failed"
```

---

### **The Webhook Magic (How Linear Talks Back)**

```
Flow:
1. You post comment on Linear board
2. Linear sends notification to app endpoint: /webhooks/linear
3. App verifies signature (is this really from Linear?)
4. App extracts instruction: "page 3: fix date"
5. App starts background worker:
   - Calls update_staging_page_body()
   - Resets status to "draft"
   - Runs review cycle (independent AI checks fix)
   - If approved: promotes
6. Posts result back to Linear as comment

This creates TWO-WAY COMMUNICATION:
- System → Linear (rejected pages, alerts)
- Linear → System (fix instructions via comments)
```

**Security Checks:**
- HMAC-SHA256 signature verification (timing-attack resistant)
- Only acts on comments on the pending-drafts issue
- Ignores health-lane issues (read-only there)
- Page reference REQUIRED (prevents accidents)

---

## **COMPLETE DATA FLOW (ALL 5 PHASES COMBINED)**

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. CONNECTION                                                    │
├─────────────────────────────────────────────────────────────────┤
│ Person clicks invite link
│     ↓
│ OAuth handshake (verify identity)
│     ↓
│ Account saved to database
│     ↓
│ Immediate sync starts
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 2. EMAIL COLLECTION (Every 60 seconds)                          │
├─────────────────────────────────────────────────────────────────┤
│ outlook_fetcher.py wakes up
│     ↓
│ Refresh access token if needed (> 1 hour old)
│     ↓
│ Ask Microsoft Graph: "What's new since last time?"
│     ↓
│ Receive batch of 100 emails
│     ↓
│ Dedup check: "Have we seen this email ID before?"
│     ├─→ NO: Save to outlook_messages table
│     └─→ YES: Only save to outlook_message_sightings
│     ↓
│ Extract text from attachments (PDF, Excel, etc.)
│     ↓
│ Save to database
│     ↓
│ Update sync cursor: "Last synced Inbox at X time"
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 3. KNOWLEDGE GENERATION (Every 6 hours)                         │
├─────────────────────────────────────────────────────────────────┤
│ DETECT PHASE:
│   Scan all emails
│   Hash each one
│   Find new emails not yet processed
│     ↓
│ DRAFT PHASE:
│   Send batches of emails to Claude
│   Claude writes summaries as wiki pages
│   Save to wiki_staging (not live yet)
│   Cost: ~$0.81 per cycle
│     ↓
│ CONSOLIDATE PHASE:
│   Check for duplicate-title drafts
│   Merge if found
│     ↓
│ REVIEW PHASE:
│   Independent AI fact-checks each page
│   Verifies: "Is every claim backed by an email?"
│   Marks: APPROVED ✓ or REJECTED ✗
│     ↓
│ PROMOTION PHASE:
│   Approved pages → public.wiki_pages (LIVE)
│   Rejected pages → Linear board (waiting for fix)
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 4. REJECTED PAGE WORKFLOW (Via Linear)                          │
├─────────────────────────────────────────────────────────────────┤
│ Rejected page appears on Linear board
│     ↓
│ Human reads rejection reason
│     ↓
│ Human comments: "page 3: fix the date, then promote"
│     ↓
│ Linear webhook notifies app
│     ↓
│ App fixes page body
│ App re-reviews independently
│     ↓
│ If approved:
│   └─→ Auto-promote to public wiki
│ If rejected:
│   └─→ Post rejection reason as comment
│     ↓
│ Result posted back on Linear
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 5. HEALTH MONITORING (Every 15 minutes)                         │
├─────────────────────────────────────────────────────────────────┤
│ Scan for failures:
│   - Outlook sync failed 3+ times?
│   - Wiki cycle failed?
│   - Promotion failed?
│     ↓
│ If YES: Create Linear alert
│ If NO & alert exists: Auto-resolve it
│     ↓
│ Result shows on Linear health lane
└─────────────────────────────────────────────────────────────────┘
```

---

## **KEY TAKEAWAYS**

**For You (Jagriti) as QA:**

1. ✅ Understand email sync (60-second cycles, dedup, attachment extraction)
2. ✅ Understand wiki pipeline (5 phases: detect → draft → consolidate → review → promote)
3. ✅ Understand safety (AI can't touch live wiki or database)
4. ✅ Understand Linear integration (two-way communication for fixes and alerts)
5. ✅ Understand current status (working, but only test accounts, not production yet)

**What to Test:**
- Do emails sync every 60 seconds consistently?
- Are duplicates properly detected (same email to 2 mailboxes)?
- Are attachment texts extracted correctly?
- Does review catch unsupported claims?
- Can rejected pages be fixed via Linear comments?
- Do system alerts trigger on failures?
- Do alerts auto-resolve when issues are fixed?

**File Purposes (TL;DR):**
- **ARCHITECTURE.md** = How it's connected
- **outlook-ingestion.md** = How emails get in
- **STATUS.md** = What's working today
- **wiki-ingestion.md** = How emails become knowledge
- **linear-integration.md** = How problems are tracked & fixed
