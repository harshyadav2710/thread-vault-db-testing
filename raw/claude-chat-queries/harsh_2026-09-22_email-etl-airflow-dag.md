---
thread_name: "email-etl-airflow-dag"
user: "harsh"
type: claude-chat
created: 2026-09-22
updated: 2026-09-22
---

# Email (Gmail/Zoho Mail) Ingestion ETL DAG — Connection Methods

**Thread:** email-etl-airflow-dag  
**User:** Rajat Jain (CEO, EOXS)  
**Date:** 2026-09-22  
**Query:** How to connect Gmail and Zoho Mail to Airflow DAG to fetch data, create CSV, send email with attachment showing ingested/non-ingested emails

---

## Use Case

Build an Airflow DAG that:
1. Fetches emails from Gmail and/or Zoho Mail
2. Stores email metadata + ingestion status in database
3. Queries database for ingested vs. non-ingested emails
4. Generates CSV report
5. Sends email with CSV attachment to stakeholders

---

## Connection Approaches Provided

### Approach 1: Gmail via Gmail API
- **Auth:** Google Service Account (JSON key from GCP)
- **Setup:** Google Cloud Console > Create project > Enable Gmail API > Create Service Account > Download key
- **Pros:** Official API, most reliable, rich features
- **Cons:** Requires GCP account setup

**Airflow Connection:**
- Type: Google Cloud Platform
- Extra: Service account JSON with private_key, client_email, project_id

**Code:** Full Python function provided to:
- Build Gmail API client with service account credentials
- Query Gmail API for unread messages from last 24 hours
- Extract headers: From, To, Subject, Date, snippet
- Push email list to XCom

### Approach 2: Gmail via IMAP
- **Auth:** Username + App Password (simpler alternative)
- **Pros:** Simple, no GCP required
- **Cons:** Less feature-rich, slower for large volumes

### Approach 3: Zoho Mail via API
- **Auth:** OAuth 2.0 (Client ID, Client Secret, Refresh Token)
- **Setup:** Zoho Developer Console > Create OAuth app > Generate refresh token
- **Pros:** Official API, OAuth flow handles token refresh
- **Cons:** OAuth setup slightly more complex

**Airflow Connection:**
- Type: HTTP
- Host: https://mail.zoho.com
- Extra: grant_type, client_id, client_secret, scope

**Code:** Full Python function provided to:
- Exchange refresh token for access token
- Query Zoho Mail API for messages in account
- Extract message metadata
- Push to XCom

### Approach 4: Zoho Mail via IMAP
- **Auth:** Username + App Password
- **Pros:** Simple, no Zoho developer setup
- **Cons:** Less powerful than API

---

## Complete DAG Pipeline Provided

**5-Task Pipeline:**

1. **fetch_gmail_data** (PythonOperator)
   - Uses Gmail API via service account
   - Fetches unread emails from last 24 hours
   - Returns list of email objects with: message_id, from, to, subject, date, snippet, ingested flag
   - Pushes to XCom: `emails` list

2. **fetch_zoho_mail_data** (PythonOperator)
   - Uses Zoho Mail API via OAuth
   - Fetches messages from account
   - Returns same schema as Gmail data
   - Both Gmail and Zoho run in parallel (fan-out)

3. **store_emails_in_db** (PythonOperator)
   - Reads emails from XCom
   - Uses SQLAlchemy to define Email table
   - Performs upsert: insert if new, update if exists (prevents duplicates)
   - Schema: message_id (PK), from, to, subject, date, snippet, ingested (Boolean), timestamps
   - Logs success/failures

4. **generate_report** (PythonOperator)
   - Queries database: `SELECT ingested status, COUNT(*), email subjects FROM emails WHERE created_at >= 24h AGO GROUP BY ingested`
   - Generates Pandas DataFrame
   - Saves as CSV: `/tmp/email_ingestion_report.csv`
   - Pushes path to XCom: `csv_path`

5. **send_email_with_attachment** (PythonOperator)
   - Reads CSV path from XCom
   - Constructs email message (MIMEMultipart)
   - Attaches HTML body with report metadata
   - Attaches CSV file with base64 encoding
   - Sends via SMTP (Gmail or custom SMTP server)
   - Logs delivery

**Task Dependencies:**
```
[fetch_gmail, fetch_zoho] >> store_db >> gen_report >> send_email
```
Gmail and Zoho fetch run in parallel, then merge for storage.

---

## Airflow Variables Required (Admin > Variables)

```json
// Gmail Setup (pick one auth method)
gmail_service_account: {full json with private_key, client_email, project_id}
OR
gmail_app_password: "app_specific_password_from_google_account"

// Zoho Setup (pick one auth method)
zoho_client_id: "your_client_id"
zoho_client_secret: "your_secret"
zoho_refresh_token: "your_refresh_token"
OR
zoho_app_password: "app_password_from_zoho"

// Email Delivery
smtp_server: "smtp.gmail.com"
smtp_port: "587"
smtp_user: "notification_account@gmail.com"
smtp_password: "app_password"
email_from: "noreply@eoxs.com"
email_to: "rajat@eoxs.com,team@eoxs.com"

// Database
db_connection_string: "postgresql://user:password@host:5432/etl_db"
```

---

## Airflow Connections (Optional Alternative to Variables)

| Connection ID | Type | Host | Extra |
|---|---|---|---|
| gmail_connector | Google Cloud Platform | N/A | Service account JSON |
| zoho_mail_connector | HTTP | https://mail.zoho.com | OAuth credentials |
| postgres_etl | Postgres | localhost | DB credentials |
| smtp_gmail | SMTP | smtp.gmail.com:587 | Username & app password |

---

## Implementation Complexity & Effort

| Component | Effort | Notes |
|-----------|--------|-------|
| Gmail API setup | 30 min | GCP project creation, service account, JSON key export |
| Zoho API setup | 30 min | Zoho developer console, OAuth app, refresh token generation |
| Airflow DAG code | 1-2 hours | ~200 lines for all 5 tasks (templates provided) |
| Database schema | 30 min | Create Email table with ingestion tracking |
| SMTP setup | 15 min | Gmail app password or custom SMTP server |
| Testing | 1-2 hours | Verify email fetching, DB storage, report generation, email delivery |
| **Total** | **4-5 hours** | **Full working pipeline** |

---

## Key Design Decisions

**1. Upsert Pattern in Database**
- Problem: Same email can be fetched multiple times → duplicates
- Solution: Check if message_id exists; update if found, insert if new
- Benefit: Idempotent — safe to retry without data loss

**2. XCom for Data Passing**
- Problem: Can't pass large data structures between tasks
- Solution: Store in XCom, tasks pull by key
- Limitation: XCom has size limits (~100KB); use DB for large datasets

**3. Parallel Email Fetching**
- Problem: Fetching from both Gmail and Zoho sequentially doubles time
- Solution: Fan-out to parallel tasks [fetch_gmail, fetch_zoho]
- Benefit: Reduces total DAG execution time

**4. CSV Generation from DB Query**
- Problem: Could generate from XCom data, but fragile if process fails
- Solution: Query database (source of truth), generate from DB state
- Benefit: If DAG reruns, report reflects DB state (idempotent)

**5. Email via SMTP, not Airflow SendEmailOperator**
- Airflow SendEmailOperator doesn't attach files easily
- Direct SMTP gives more control over MIME structure
- Can add CC/BCC, custom headers, etc.

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Gmail API quota** | Calls fail if >10M/day | Monitor quota usage, implement caching |
| **Duplicate emails** | DB grows with repeats | Upsert on message_id prevents duplicates |
| **Ingestion flag never set** | Report shows "Non-Ingested" for everything | Add downstream task to update `ingested=True` after processing |
| **Database connection lost** | Store fails, email not sent | Retry logic (retries=2), alert on failure |
| **SMTP auth fails** | Email not delivered | Test SMTP creds in staging; monitor delivery logs |
| **Large data volume** | DAG timeout or memory spike | Implement pagination in API calls, limit query with date range |

---

## Next Steps for Implementation

**Week 1: Setup**
1. Create GCP project & enable Gmail API (or Zoho OAuth app)
2. Generate credentials, store in Airflow Variables
3. Create Airflow Connections
4. Set up PostgreSQL database

**Week 1-2: Development**
1. Write fetch_gmail_data() function, test locally
2. Write fetch_zoho_mail_data() function, test locally
3. Write store_emails_in_db() with SQL Alchemy
4. Write generate_report() with Pandas
5. Write send_email_with_attachment()

**Week 2: Testing**
1. Deploy DAG to staging Airflow
2. Trigger first manual run
3. Verify Gmail/Zoho auth works
4. Verify emails stored in DB correctly
5. Verify CSV generated & email delivered
6. Test failure scenarios (API down, DB error)

**Week 3: Production**
1. Deploy to production
2. Set schedule: daily at 9 AM
3. Monitor first 3-5 runs
4. Set up alerting on task failures
5. Update runbook with troubleshooting

---

## Quick Reference: Gmail API vs. IMAP vs. Zoho API

| Feature | Gmail API | Gmail IMAP | Zoho API |
|---------|-----------|-----------|----------|
| **Auth Complexity** | High (GCP + service account) | Low (username + app password) | Medium (OAuth) |
| **Feature Richness** | Rich (labels, threads, drafts, etc.) | Basic (inbox, folders) | Rich (accounts, messages, attachments) |
| **Rate Limits** | 10M/day (service account) | 2500/day (user account) | 500/min (API) |
| **Setup Time** | 30 min | 5 min | 20 min |
| **Recommended For** | Production, high volume | Dev/test, low volume | Production, enterprise Zoho users |

**Recommendation for EOXS:**
- **If mostly Gmail:** Use Gmail API (most reliable, best docs)
- **If mixed users:** Use both APIs in parallel DAG
- **If IMAP acceptable:** Use IMAP for quick MVP (less setup)

---

## Code Files Available

- Main DAG: Complete with all 5 tasks + dependencies
- Utility functions: email fetching, DB storage, report generation, SMTP sending
- Configuration: All required Variables and Connections
- Troubleshooting: Common issues (auth failures, timeouts, email delivery)

**Total Lines of Code:** ~400 lines (with comments and error handling)
