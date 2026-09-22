---
thread_name: "email-etl-airflow-dag"
user: "harsh"
type: claude-chat
created: 2026-09-22
updated: 2026-09-22
---

# Email Ingestion Tracking — How to Determine Ingested vs. Non-Ingested

**Thread:** email-etl-airflow-dag  
**User:** Rajat Jain (CEO, EOXS)  
**Date:** 2026-09-22  
**Question:** When you fetch 50 emails from Gmail/Zoho, how do you know which ones are "ingested" (processed) vs. "not ingested" (pending)?

---

## The Core Problem

Previous response provided a DAG but left the critical question unanswered:

```
Fetch 50 emails from Gmail API
↓
Store in DB
↓
Now what?
  - Which 50 are "ingested"? (processed into business system)
  - Which ones are "non-ingested"? (still pending)
  - How do we KNOW the difference?
```

Answer: **You need a tracking mechanism.** The `ingested` Boolean flag isn't automatic — it requires explicit business logic.

---

## Three Core Patterns Explained

### Pattern 1: Ingestion Tracking Table (Recommended for EOXS)

**Concept:** Create separate table that links raw emails to processed records.

**Tables:**
```
emails_raw (what we fetched)
├── message_id (PK)
├── from_address
├── to_address
├── subject
├── content
└── created_at

email_ingestion_tracking (how we processed it)
├── id (PK)
├── message_id (FK → emails_raw)
├── ingestion_type ('customer', 'order', 'support_ticket')
├── extracted_data (JSON of what was extracted)
├── target_table ('customers', 'orders', 'tickets')
├── target_record_id (FK to actual ingested record in business DB)
├── status ('success', 'failed', 'pending', 'skipped')
├── error_message (if failed)
├── ingested_at
└── attempted_at
```

**Flow:**
1. Fetch 50 emails → store in emails_raw
2. Process each email:
   - Try to extract data (e.g., customer info from email content)
   - Validate extracted data
   - Insert into business table (e.g., customers table)
   - Create row in email_ingestion_tracking with status='success'
   - If error → create row with status='failed' + error_message
3. Query time:
   ```sql
   SELECT * FROM email_ingestion_tracking WHERE status='success'
   -- Returns: 45 successfully ingested
   
   SELECT * FROM email_ingestion_tracking 
   WHERE status IN ('failed', 'pending')
   -- Returns: 5 not ingested (need retry or investigation)
   ```

**Advantages:**
- Audit trail (know what was extracted, where it went)
- Error tracking (why failed, what needs retry)
- Idempotent (can reprocess without duplicates)
- Flexible (supports multiple extraction types)

**Code Example:**
```python
# After processing email:
ingestion_record = EmailIngestion(
    message_id='msg_123',
    ingestion_type='customer',  # This email had customer data
    extracted_data={'name': 'John', 'email': 'john@example.com'},
    target_table='customers',  # Inserted into customers table
    target_record_id='cust_456',  # This customer ID
    status='success',  # Successfully processed
    ingested_at=datetime.utcnow(),
)
session.add(ingestion_record)
session.commit()
```

---

### Pattern 2: Status Flag in Raw Table

**Concept:** Simple Boolean or status field in emails_raw table.

**Table:**
```
emails_raw
├── message_id
├── ...
├── status ('pending', 'ingested', 'failed', 'skipped')
└── processed_at
```

**Flow:**
1. Fetch → store with status='pending'
2. Separate process updates status:
   - If successfully ingested → status='ingested'
   - If error → status='failed'
3. Query:
   ```sql
   SELECT COUNT(*) FROM emails_raw WHERE status='ingested'
   -- Returns: 45 ingested
   
   SELECT COUNT(*) FROM emails_raw WHERE status='pending'
   -- Returns: 3 still waiting to be processed
   ```

**Advantages:**
- Simple (one table, no joins)
- Fast queries
- Minimal schema

**Disadvantages:**
- No error tracking (why failed?)
- No audit trail (what was extracted?)
- No visibility into what was done with email

---

### Pattern 3: Match Against Existing Data (Duplicate Detection)

**Concept:** Check if email content already exists in warehouse → if yes, it's ingested; if no, it's new.

**Flow:**
1. Fetch 50 emails
2. For each email:
   - Extract key identifiers (sender, subject, date)
   - Check if already exists in warehouse (by matching those keys)
   - If found → mark `is_ingested=True` (already processed)
   - If not found → mark `is_ingested=False` (new, never processed)
3. Query:
   ```sql
   SELECT 
       CASE WHEN is_ingested THEN 'Ingested' ELSE 'New' END,
       COUNT(*)
   FROM emails_raw
   GROUP BY is_ingested;
   ```

**Advantages:**
- No separate processing needed
- Immediate knowledge of ingestion status
- Detects duplicates

**Disadvantages:**
- Only works if warehouse already has the data
- Doesn't track partial/failed ingestions
- Doesn't know what was extracted or why

---

## Recommended Pattern for EOXS: Hybrid Approach

Combine **Pattern 1 + Pattern 3**:

```python
def ingest_emails_with_tracking(**context):
    """
    Complete ingestion with full tracking.
    """
    emails = fetch_from_gmail()  # 50 emails
    session = get_db_session()
    
    ingestion_counts = {
        'success': 0,
        'failed': 0,
        'skipped': 0,
        'not_attempted': 0,
    }
    
    for email in emails:
        # Store raw email
        raw_email = EmailRaw(
            message_id=email['message_id'],
            from_address=email['from'],
            subject=email['subject'],
            content=email['content'],
            created_at=datetime.utcnow(),
        )
        session.add(raw_email)
        session.flush()
        
        # Try to ingest
        try:
            # Step 1: Validate
            if not email['content'].strip():
                raise ValueError("Empty email content")
            
            # Step 2: Extract
            extracted = extract_customer_from_email(email['content'])
            
            # Step 3: Check if already ingested (duplicate detection)
            existing_customer = session.query(Customer).filter_by(
                email=extracted['email']
            ).first()
            
            if existing_customer:
                # Already ingested → just track it
                ingestion = EmailIngestion(
                    message_id=email['message_id'],
                    ingestion_type='customer',
                    extracted_data=extracted,
                    target_table='customers',
                    target_record_id=str(existing_customer.id),
                    status='success',  # Was already ingested before
                    ingested_at=datetime.utcnow(),
                )
            else:
                # New → ingest it
                customer = Customer(**extracted)
                session.add(customer)
                session.flush()
                
                ingestion = EmailIngestion(
                    message_id=email['message_id'],
                    ingestion_type='customer',
                    extracted_data=extracted,
                    target_table='customers',
                    target_record_id=str(customer.id),
                    status='success',
                    ingested_at=datetime.utcnow(),
                )
            
            session.add(ingestion)
            ingestion_counts['success'] += 1
            
        except ValueError as e:
            # Data invalid → skip, don't retry
            ingestion = EmailIngestion(
                message_id=email['message_id'],
                status='skipped',
                error_message=str(e),
                attempted_at=datetime.utcnow(),
            )
            session.add(ingestion)
            ingestion_counts['skipped'] += 1
            
        except Exception as e:
            # Unexpected error → failed, should retry
            ingestion = EmailIngestion(
                message_id=email['message_id'],
                status='failed',
                error_message=str(e),
                attempted_at=datetime.utcnow(),
            )
            session.add(ingestion)
            ingestion_counts['failed'] += 1
    
    session.commit()
    
    # Log summary
    logging.info(f"Ingestion complete: {ingestion_counts}")
    return ingestion_counts
```

---

## Report Query (What Goes in CSV Email)

```sql
SELECT 
    CASE 
        WHEN ei.status = 'success' THEN 'Ingested'
        WHEN ei.status = 'failed' THEN 'Failed (Needs Retry)'
        WHEN ei.status = 'skipped' THEN 'Skipped (Invalid Data)'
        ELSE 'Not Yet Attempted'
    END as ingestion_status,
    COUNT(DISTINCT er.message_id) as email_count,
    STRING_AGG(DISTINCT er.subject LIMIT 5, '; ') as sample_subjects
FROM emails_raw er
LEFT JOIN email_ingestion ei ON er.message_id = ei.message_id
WHERE er.created_at >= NOW() - INTERVAL '24 hours'
GROUP BY ei.status
ORDER BY 
    CASE 
        WHEN ei.status = 'success' THEN 1
        WHEN ei.status = 'failed' THEN 2
        WHEN ei.status = 'skipped' THEN 3
        ELSE 4
    END;

-- Example Output:
-- ingestion_status         | email_count | sample_subjects
-- -------------------------+-------------+----------------------------------
-- Ingested                 | 45          | "Invoice #123"; "Welcome"
-- Failed (Needs Retry)     | 2           | "Corrupted"; "Parse error"
-- Skipped (Invalid Data)   | 2           | "Empty content"; "No email"
-- Not Yet Attempted        | 1           | "Just arrived"
```

---

## CSV Content Example

```
Header:
Email Ingestion Report - 2026-09-22 09:00:00

SUMMARY:
Total Emails Fetched: 50
Successfully Ingested: 45
Failed (Needs Retry): 2
Skipped (Invalid): 2
Pending (Not Processed): 1

DETAILS:
message_id,from_address,to_address,subject,ingestion_status,extracted_type,target_table,error_message
msg_001,customer@example.com,support@eoxs.com,Order inquiry,Ingested,customer,customers,
msg_002,supplier@vendor.com,billing@eoxs.com,Invoice,Ingested,order,orders,
msg_003,noreply@system.com,notifications@eoxs.com,Bounce,Skipped,N/A,N/A,"Empty content"
msg_004,partner@company.com,sales@eoxs.com,Partnership,Failed,N/A,N/A,"Email format not recognized"
...
```

---

## The Key Difference: Why Pattern 1 Wins for EOXS

| Aspect | Pattern 1 (Tracking Table) | Pattern 2 (Status Flag) | Pattern 3 (Duplicate Check) |
|--------|---|---|---|
| **Ingestion Visibility** | Full audit trail | Just status | Only duplicate detection |
| **Error Tracking** | Why failed? Error message | No details | No error tracking |
| **Extraction Details** | What was extracted? JSON stored | No | No |
| **Idempotency** | Safe to reprocess | Yes, but less info | Yes |
| **Retry Strategy** | Can distinguish failed vs. skipped | Just retry all failures | Can't retry |
| **Compliance** | Full audit for SOX/compliance | Limited | Limited |
| **Complexity** | Higher schema | Simple | Medium |

**For EOXS:** Use Pattern 1 because:
1. You need audit trail (compliance, debugging)
2. You need to distinguish failures (which need retry?) vs. skips (invalid data)
3. You need to track what was extracted (for reconciliation)
4. You need error messages (why did it fail?)

---

## Implementation Checklist

- [ ] Create tables: emails_raw, email_ingestion_tracking, Customer
- [ ] Write fetch_emails() → store in emails_raw
- [ ] Write process_emails() → create rows in email_ingestion_tracking
- [ ] Add status tracking: success/failed/skipped/pending
- [ ] Write report query: count by status
- [ ] Generate CSV from report query
- [ ] Send CSV via email
- [ ] Test with sample data (50 emails)
- [ ] Monitor: watch ingestion_counts for anomalies

---

## Next: Want Full Updated DAG?

Should I provide:
1. Complete DAG with email_ingestion_tracking pattern?
2. Full database schema with all tables?
3. Detailed error handling + retry logic?
4. Complete report generation + email sending?

Let me know which depth you need.
