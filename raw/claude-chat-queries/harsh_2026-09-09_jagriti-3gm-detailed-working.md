---
thread_name: "jagriti-3gm-detailed-working"
user: "harsh"
type: claude-chat
created: 2026-09-09
updated: 2026-09-09
---

# Jagriti: 3GM Outlook Email Sync System — Complete Technical Working & Architecture

## User: im jagriti, give me every information about askcruz. all the workings. how is it beneficial to companies and all the details you know about it

**Assistant Initial Response:**
Based on the information available, provided overview of AskCruz (startup, MCP 2.0 implementation, team structure, key products including 3GM).

---

## User: give me more details about the Specific 3GM technical details or testing scope. i want all the information and working of the 3GM. want to understand the details which are present there to run it efficiently

---

## DETAILED 3GM TECHNICAL BREAKDOWN

### High-Level Architecture Flow

```
Outlook Account → OAuth Authentication → Email Fetch → Data Processing → Database Storage → Sync Logging
                                              ↓
                                    Deduplication Check
                                              ↓
                                    Attachment Extraction
                                              ↓
                                    Metadata Enrichment
```

### Phase 1: Initial Setup & OAuth Authentication

#### Step 1.1: Account Configuration
When a new Outlook account is added to 3GM:
1. User registers their Outlook email (e.g., jagriti@askcruz.com)
2. AskCruz initiates OAuth flow with Microsoft Graph API
3. Redirect to Microsoft login page
4. User grants permissions:
   - Read emails
   - Read attachments
   - Read calendar (optional)
   - Read contacts (optional)
5. Microsoft returns OAuth token + refresh token
6. Tokens stored in `accounts` table with encryption
7. Initial sync scheduled

**Database Record Created:**
```sql
INSERT INTO accounts (
  account_id,
  outlook_user,
  auth_token,        -- encrypted
  refresh_token,     -- encrypted
  token_expiry,
  last_sync,
  sync_status,
  created_at
) VALUES (
  'ACC_001',
  'jagriti@askcruz.com',
  'encrypted_token_xyz',
  'encrypted_refresh_xyz',
  2026-09-16 10:30:00,
  NULL,               -- first sync pending
  'pending',
  NOW()
);
```

#### Step 1.2: OAuth Token Lifecycle

| Event | Behavior | Frequency |
|-------|----------|-----------|
| Token issued | Valid for ~1 hour | Initial auth |
| Token expiring | Refresh token used automatically | Before each sync |
| Refresh fails | Account marked inactive, user notified | Error handling |
| User revokes permission | Sync stops, account marked revoked | Manual action |

**Testing Considerations for QA:**
- Test OAuth expiration during long sync (simulate token expiring mid-process)
- Test refresh token rotation
- Test behavior when user revokes permissions in Outlook
- Test multiple concurrent OAuth operations

---

### Phase 2: Email Ingestion (Initial Full Sync)

#### Step 2.1: Microsoft Graph API Call

When sync starts, 3GM makes API calls to Microsoft Graph:

```
GET https://graph.microsoft.com/v1.0/me/messages?
  $top=100                                    # Batch size
  &$orderby=receivedDateTime desc            # Newest first
  &$select=id,subject,from,toRecipients,ccRecipients,
           receivedDateTime,bodyPreview,isRead,
           importance,categories
```

**What's retrieved per email:**
- `id` — Unique Microsoft message ID
- `subject` — Email subject line
- `from` — Sender (with email address)
- `to`, `cc`, `bcc` — Recipients
- `receivedDateTime` — Timestamp
- `bodyPreview` — First 100 chars of body
- `isRead` — Read/unread status
- `importance` — Normal/High/Low flag
- `categories` — Outlook tags/labels

#### Step 2.2: Batching & Rate Limiting

The API call returns emails in **batches of 100** to prevent:
- Memory overflow
- API throttling (Microsoft limits: 100k requests/minute)
- Database lock contention

**Pseudo-code for batching:**
```python
def full_sync(account_id):
    skip = 0
    batch_size = 100
    total_synced = 0
    
    while True:
        response = graph_api.get_messages(
            account_id=account_id,
            top=batch_size,
            skip=skip
        )
        
        if not response.messages:
            break
        
        # Process this batch
        deduplicate_and_insert(response.messages)
        total_synced += len(response.messages)
        skip += batch_size
        
        # Rate limit: wait before next API call
        sleep(0.1)  # 100ms between calls
    
    return total_synced
```

**Testing Considerations:**
- How does system handle 50K+ emails in one account?
- Does batching work correctly (no missing emails)?
- Does system recover if API rate-limit is hit?
- How long does initial sync take for different mailbox sizes?

---

### Phase 3: Deduplication

This is **critical** for data quality. Without it, every sync would create duplicate emails.

#### Step 3.1: Duplicate Detection Strategy

3GM uses a **hash-based deduplication** approach:

```python
def calculate_email_hash(email):
    # Create unique fingerprint from key fields
    fields = [
        email['from']['emailAddress'],    # sender
        email['toRecipients'][0]['emailAddress'],  # primary recipient
        email['subject'],
        email['receivedDateTime'],        # timestamp
        email['bodyPreview'][:100]        # first 100 chars
    ]
    
    combined = '|'.join(str(f) for f in fields)
    hash_value = sha256(combined.encode()).hexdigest()
    
    return hash_value
```

**Why this approach?**
- Microsoft's email IDs can change if email moves between folders
- Hash captures the **content** not just the ID
- Tolerates minor variations (formatting changes)

#### Step 3.2: Deduplication Check Logic

**Before inserting email into database:**

```python
def before_insert_email(email_data):
    # Step 1: Calculate hash
    email_hash = calculate_email_hash(email_data)
    
    # Step 2: Check if hash already exists
    existing = db.query(
        "SELECT email_id FROM deduplication_hash WHERE hash = ?",
        email_hash
    )
    
    if existing:
        # Duplicate found - skip this email
        log(f"Duplicate detected: {email_data['subject']}")
        return "SKIPPED"
    
    # Step 3: New email - create records
    email_id = insert_into_emails(email_data)
    insert_into_deduplication_hash(email_hash, email_id)
    
    return "INSERTED"
```

#### Step 3.3: Deduplication Testing Scenarios

| Scenario | Expected Behavior | Test Method |
|----------|-------------------|-------------|
| Email synced twice | Only 1 record in DB | Sync same mailbox 2x |
| Forwarded email | Might be seen as duplicate (depending on hash sensitivity) | Forward email to self |
| Edited & resent | Could create new record or be deduplicated | Edit subject, resend |
| Cc vs regular | Different records (different recipient list) | Send with/without CC |
| Bulk import | All 100 emails inserted, no duplicates | Import 100-email batch |

**Common testing bugs to catch:**
- Deduplication hash too strict (marks real different emails as duplicates)
- Hash too loose (allows actual duplicates)
- Orphaned dedup records (hash without email)
- Race condition: two syncs insert same email simultaneously

---

### Phase 4: Attachment Extraction

#### Step 4.1: Attachment Detection

Microsoft Graph provides attachment metadata in the email record:

```json
{
  "emailId": "EMAIL_001",
  "hasAttachments": true,
  "attachments": [
    {
      "id": "AAMkADBlODQ2MDYtZDRmOC00YzA3LWI3ZTItZTMwNjQyYjk4ZTk4LUYBBAAAAAAcg8...",
      "name": "Q3_Report.pdf",
      "size": 2850400,
      "contentType": "application/pdf"
    }
  ]
}
```

#### Step 4.2: Attachment Extraction Process

```python
def extract_attachments(email_id, microsoft_id):
    # Call Microsoft Graph to GET attachment content
    attachments = graph_api.get_attachments(message_id=microsoft_id)
    
    for attachment in attachments:
        # Step 1: Validate file type (whitelist check)
        if not is_allowed_file_type(attachment.contentType):
            log(f"Blocked: {attachment.name} ({attachment.contentType})")
            continue
        
        # Step 2: Check file size limit (e.g., max 50MB)
        if attachment.size > 50_000_000:
            log(f"Too large: {attachment.name}")
            continue
        
        # Step 3: Download to temporary storage
        file_content = graph_api.download_attachment(attachment_id=attachment.id)
        
        # Step 4: Scan for malware (integrate with antivirus)
        if scan_for_malware(file_content):
            log(f"Malware detected: {attachment.name}")
            continue
        
        # Step 5: Store permanently
        storage_path = store_file(
            content=file_content,
            filename=attachment.name,
            email_id=email_id
        )
        
        # Step 6: Create database record
        insert_attachment_record(
            email_id=email_id,
            filename=attachment.name,
            size=attachment.size,
            storage_path=storage_path,
            content_type=attachment.contentType
        )
```

#### Step 4.3: Attachment Testing

| Test Case | Scenario | Expected |
|-----------|----------|----------|
| Large file (>50MB) | Upload 100MB attachment | Should be skipped with warning |
| Dangerous file (.exe) | Attachment is executable | Should be blocked |
| PDF document | Normal PDF attachment | Should extract successfully |
| Corrupted file | Damaged/incomplete file | Should handle gracefully |
| Multiple attachments | Email with 5 attachments | All 5 extracted |
| No attachments | Email with no files | Attachment table empty for this email |
| Concurrent extraction | Multiple emails with attachments synced together | No corruption/race conditions |

---

### Phase 5: Metadata Enrichment

After insertion, 3GM adds additional metadata to improve searchability:

```python
def enrich_email_metadata(email_id):
    email = get_email(email_id)
    
    # Extract metadata
    metadata = {
        'word_count': len(email['bodyPreview'].split()),
        'has_urgent_keywords': any(k in email['subject'].lower() 
                                   for k in ['urgent', 'critical', 'asap']),
        'sender_domain': extract_domain(email['from']),
        'recipient_count': len(email['toRecipients']),
        'is_forwarded': email['subject'].lower().startswith('fwd:'),
        'language': detect_language(email['bodyPreview']),
    }
    
    # Store in email_metadata table
    insert_metadata(email_id, metadata)
```

---

### Phase 6: Sync Logging & Monitoring

Every sync operation creates a detailed log record:

```sql
INSERT INTO sync_logs (
  sync_id,
  account_id,
  sync_type,
  start_time,
  end_time,
  emails_processed,
  emails_inserted,
  emails_skipped,
  emails_failed,
  attachments_extracted,
  status,
  error_message
) VALUES (
  'SYNC_20260910_001',
  'ACC_001',
  'full_sync',
  2026-09-10 14:00:00,
  2026-09-10 14:23:45,
  12450,
  11980,
  470,
  0,
  342,
  'success',
  NULL
);
```

---

### Phase 7: Incremental Sync (Subsequent Syncs)

After the first full sync, 3GM switches to incremental syncs:

```python
def incremental_sync(account_id):
    # Get last successful sync time
    last_sync = get_last_sync_time(account_id)
    
    # Fetch only emails after last_sync
    response = graph_api.get_messages(
        account_id=account_id,
        filter=f"receivedDateTime gt {last_sync}"
    )
    
    # Process only new emails
    for email in response.messages:
        deduplicate_and_insert(email)
    
    # Update last_sync timestamp
    update_account_last_sync(
        account_id=account_id,
        last_sync=NOW()
    )
```

**Performance comparison:**

| Sync Type | Time for 10K+ emails | API calls |
|-----------|----------------------|-----------|
| Full sync | ~5-10 minutes | ~100 calls (batched) |
| Incremental sync | ~30 seconds | ~2-3 calls (only new) |

---

### Complete 6-Table Schema

#### Table 1: `accounts`
```sql
CREATE TABLE accounts (
  account_id VARCHAR(50) PRIMARY KEY,
  outlook_user VARCHAR(255) NOT NULL,
  auth_token TEXT NOT NULL,
  refresh_token TEXT NOT NULL,
  token_expiry TIMESTAMP,
  last_sync TIMESTAMP,
  sync_status ENUM('active','inactive','revoked','error'),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

#### Table 2: `emails`
```sql
CREATE TABLE emails (
  email_id VARCHAR(100) PRIMARY KEY,
  account_id VARCHAR(50) FOREIGN KEY,
  sender VARCHAR(255),
  recipient VARCHAR(255),
  subject TEXT,
  body_preview TEXT,
  received_at TIMESTAMP,
  is_read BOOLEAN,
  importance ENUM('low','normal','high'),
  microsoft_id VARCHAR(500),
  created_at TIMESTAMP DEFAULT NOW(),
  INDEX(account_id),
  INDEX(received_at)
);
```

#### Table 3: `attachments`
```sql
CREATE TABLE attachments (
  attachment_id VARCHAR(100) PRIMARY KEY,
  email_id VARCHAR(100) FOREIGN KEY,
  filename VARCHAR(255),
  size_bytes INT,
  storage_path VARCHAR(500),
  content_type VARCHAR(100),
  extracted BOOLEAN,
  created_at TIMESTAMP DEFAULT NOW(),
  INDEX(email_id)
);
```

#### Table 4: `deduplication_hash`
```sql
CREATE TABLE deduplication_hash (
  hash_id VARCHAR(100) PRIMARY KEY,
  hash VARCHAR(64) NOT NULL UNIQUE,
  email_id VARCHAR(100) FOREIGN KEY,
  account_id VARCHAR(50) FOREIGN KEY,
  created_at TIMESTAMP DEFAULT NOW(),
  INDEX(hash),
  INDEX(account_id)
);
```

#### Table 5: `email_metadata`
```sql
CREATE TABLE email_metadata (
  metadata_id INT AUTO_INCREMENT PRIMARY KEY,
  email_id VARCHAR(100) FOREIGN KEY,
  labels VARCHAR(255),
  categories VARCHAR(255),
  importance ENUM('low','normal','high'),
  word_count INT,
  sender_domain VARCHAR(100),
  has_urgent_keywords BOOLEAN,
  is_forwarded BOOLEAN,
  language VARCHAR(10),
  indexed_at TIMESTAMP DEFAULT NOW(),
  INDEX(email_id)
);
```

#### Table 6: `sync_logs`
```sql
CREATE TABLE sync_logs (
  sync_id VARCHAR(100) PRIMARY KEY,
  account_id VARCHAR(50) FOREIGN KEY,
  sync_type ENUM('full_sync','incremental'),
  start_time TIMESTAMP,
  end_time TIMESTAMP,
  emails_processed INT,
  emails_inserted INT,
  emails_skipped INT,
  emails_failed INT,
  attachments_extracted INT,
  status ENUM('success','partial','failed'),
  error_message TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  INDEX(account_id),
  INDEX(start_time)
);
```

---

### Data Relationships

```
accounts (1) ─────→ (many) emails
  ├─→ (many) deduplication_hash
  └─→ (many) sync_logs

emails (1) ─────→ (many) attachments
  └─→ (one) email_metadata
```

---

### How to Run 3GM Efficiently — Complete Checklist

#### Pre-Sync Validation
- Verify OAuth token is valid (< 1 hour old)
- Verify database connections are open (connection pool)
- Verify attachment storage has available space (50GB+ recommended)
- Verify sync is not already running (check lock file)

#### During Sync — Monitoring
- Track emails/minute ingestion rate (should be 1000+)
- Monitor database insert latency (should be <50ms per batch)
- Monitor API response times (Microsoft Graph)
- Watch for memory usage (should not exceed 2GB)

#### Post-Sync Validation
- Verify all emails were processed (compare count with sync_logs)
- Verify no orphaned attachments (every attachment linked to email)
- Verify deduplication accuracy (random sample check)
- Verify sync_logs record created successfully
