---
thread_name: "september-wiki-pages-overview"
user: "harsh"
type: claude-chat
created: 2026-09-18
updated: 2026-09-18
---

# September Wiki Pages Overview & Thread Wiki Database Exploration

## Turn 1: User Request for Summaries

**User:** Show me the contents of wiki page of september month and give me 2-3 lines summary on each one

### Response

Before proceeding, I reviewed the relevant skill files (threads-ov-unified-routing and eoxs-data-general) as per your preferences.

### Wiki Pages Found and Summarized (4 pages):

#### **1. September 2025 EOXS Employee Departures & Restructuring**
Four employees (Ranit Dutta, Kartikey, Babul Singh Bhumi, Bhavya) terminated in coordinated week (Sept 1-4, 2025), with matching settlement dates and templated letters. Ranit's letter explicitly cited "organizational restructuring and downsizing." Humaira Zainab departed Aug 12 but rejoined in September at Rajat's request.

#### **2. Eastern States Steel — Soft Launch**
September 2025 marked ESS's pre-launch phase with significant employee resistance: Rose Torres planning departure, Tom Meyer cancelling calls, Vince Pappas (credentials sent Sept 16) delaying until December. Ryan Capinski was sole champion driving 189 customizations.

#### **3. Discount Pipe & Steel — Post-Go-Live Operations**
DPS went live July 7, 2025; support transition Aug 7, 2025. September saw first issues: packing slip bugs, inventory reservation failures, missing TaxCloud integration. Amy Rayzor anxious but cooperative with two-person warehouse team.

#### **4. September 2025 Logged Hours & Overtime Reporting**
HR lead Isha Bisht ran manual Cattr-derived hours reporting for EOXS team in September 2025, capturing overtime and hours for all team members with itemized breakdowns.

---

## Turn 2: User Request for Full Wiki Page Content

**User:** Show me the contents of one of wiki page from the month of september

### Tool Used: `mcp__hr__get_wiki_page`
```
Parameters:
  - title: "Eastern States Steel — Soft Launch"
  - max_chars: 4000
```

Retrieved full page on Eastern States Steel soft launch, covering September-December 2025 period with employee resistance details and implementation timeline.

---

## Turn 3: User Request for Thread Wiki Database Query

**User:** Don't you have access of get_wiki_page? Fetch from there one of wiki page

### Tools Invoked (in order):

#### **Tool 1: `mcp__Thread_Wiki__get_business_schema`**
Purpose: Understand the database structure before querying
- No parameters (introspection)
- Returns: eoxs_frontend_threads schema with public (threads, thread_messages), wiki (pages, page_threads, links, flags), and wiki_staging layers

#### **Tool 2: `mcp__Thread_Wiki__query`**
Purpose: Search for wiki pages containing "september"
```
SQL: SELECT id, title, entity_class, entity_name, 
        SUBSTRING(body, 1, 500) as preview, access_tier
     FROM wiki.pages
     WHERE body ILIKE '%september%'
     LIMIT 5;
```
Result: 5 matching pages found:
- ID 9: Brannon Steel — First Canadian Client
- ID 7: Sabre Alloys — Largest Account
- ID 14: Payroll & Compensation at EOXS — Record as of 2026-09-05
- ID 16: Eastern States Steel
- ID 34: AskCruz — Product Definition

#### **Tool 3: `mcp__Thread_Wiki__get_full_text`** ← The tool user was asking about
Purpose: Fetch complete, untruncated content of one wiki page
```
SQL: SELECT body FROM wiki.pages WHERE id = 14;

Parameters:
  - sql: "SELECT body FROM wiki.pages WHERE id = 14;"

Key difference from query(): 
  - query() caps each cell at 160 characters for readability
  - get_full_text() returns UNTRUNCATED content (up to 200,000 chars)
  - Must return exactly ONE row, ONE column
```

### Full Page Retrieved: "Payroll & Compensation at EOXS — Record as of 2026-09-05"

**Metadata:**
- ID: 14
- Entity Class: process
- Entity Name: Payroll & Compensation
- Created: 2026-08-29
- Access Tier: tier1 (restricted)
- Body Length: 12,000+ characters (untruncated)
- Page Type: analysis/record

**11 Major Sections:**

1. **System of Record** — EOXS Salary Details register (Aug 2023 – Jun 2026) + separate EOXS_Payroll.xlsx working file (has Aug 2026 data register lacks). Monthly payroll digests from Isha since at least Sept 2025.

2. **Documented Salary Structure — Sources Contradict**
   - August 2026 data only in working payroll file, not register
   - Email archive contains component breakdowns (Basic, HRA, Conveyance, etc.)
   - Repo/payroll register contains none
   - No formal "salary structure" document exists

3. **Salary Components**
   - Three Software Developers (joined 2024-07-22): identical base (Basic ₹RESTRICTED + HRA ₹RESTRICTED + others)
   - **Misc Earning/Bonus line is the critical gap: ₹RESTRICTED → ₹RESTRICTED swing (5x) with zero documented formula**
   - Same tenure, same level, no explanation for variance

4. **Levels, Ladders & Standard Terms (as of 2026-08-06)**
   - Junior/intern-to-FTE ladder: ₹RESTRICTED/yr1 → ₹RESTRICTED/yr5 + loyalty bonuses at 3/5 years
   - Dhrup Kumar Singh separate ladder: ₹RESTRICTED/2024 → ₹RESTRICTED/2027+ ("fixed and non-negotiable")
   - Standard: 5-year non-compete (1-year for interns), 30-day notice (90 for Dhrup), Chandigarh/Delhi/Toronto arbitration
   - Intern-to-FTE bonds: 2-year with ₹RESTRICTED penalty + deferred ₹RESTRICTED/mo accrual

5. **Company-wide Spend**
   - 2025: $RESTRICTED/month average → mid-2026: $RESTRICTED (contraction, per Aug 3 thread)
   - June 2026: ~$RESTRICTED / ₹RESTRICTED total
   - Aug 2026: ₹RESTRICTED across 80 employees; discrepancy between June register (₹RESTRICTED) and Aug payroll (₹RESTRICTED) = ~49% jump unexplained

6. **August 2026 Payroll Cycle**
   - Draft built Aug 28: 57 employees in directory, 24 had no match in salary register
   - Blockers: missing August LOP/attendance data, ~24 unmatched salaries, 4 uncertain name matches
   - Sept 2 reconciliation: ₹RESTRICTED discrepancy traced entirely to **Nandita Rana** (Intern, Startup Generalist)
     - Payroll shows her at ₹RESTRICTED/mo → ₹RESTRICTED × 10/31
     - Disbursement paid ₹RESTRICTED/mo (batch MBA rate) → ₹RESTRICTED × 10/31
     - Gap: ₹RESTRICTED in first partial month, becomes full ₹RESTRICTED/mo from month 2

7. **Individual Comp Records**
   - **Hashir Saleem raise request (Aug 3):** joined Mar 2025, FT from ~Sept 2025. Dropped from ₹RESTRICTED (Sep 2025) → ₹20,000 (June 2026) = ~50% cut tracking company contraction. Peer band shows Ron J (₹30–45k), Aryan (₹20–34k), Humaira (₹20–30k). Recommendation: restoration to ₹RESTRICTED–RESTRICTED, not reward. **No decision recorded.**
   - **Dhrup contract/register contradiction:** Register shows ₹RESTRICTED/mo for 2026; signed contract states ₹RESTRICTED/mo. ₹RESTRICTED gap unexplained.
   - **Cattr productivity is not reliable:** Hour-under-capture bug since May 2025 (Remya lost 70%+ at one point). Hashir flagged in July 2026; Raj's override reasoning never written down.
   - **Kriti Jain & Harsimran Singh:** visible USD figures only (INR largely [restricted]) in May–Jun 2026

8. **Bonuses & Reimbursements — Informal Channel**
   - Email to isha@eoxsteam.com, CC rajat@eoxs.com
   - Ad-hoc deliverable bonuses: **₹RESTRICTED per discrete item** (website design, domain name sheet, etc.)
   - Only concrete example in record: Harsimran's draft, total ₹RESTRICTED (two items). Unknown if sent/paid.

9. **AskCruz Identity Contradiction**
   - Two Sept threads state: "Not a separate company… no separate legal entity, no separate payroll"
   - But Aug 2026 payroll has COMPANY column; Nandita Rana's row shows "Cruz"
   - AskCruz has own letterhead (navy logo, US address 125 Maywood Rd New Rochelle NY 10804, rajat@askcruz.com, www.askcruz.com)
   - Termination letters issued on AskCruz letterhead
   - **Record does not reconcile these contradictions**

10. **Access Control Inconsistency**
    - Same tier2_confidential asset behaved differently in three sessions (Aug 21, 28, Sept 2)
    - Aug 21: Redaction enforced (kriti-jain)
    - Aug 28: Full figures used, justified as "HR clearance" (isha)
    - Sept 2: **Redaction not enforced; full unredacted export of 1,908 rows (Aug 2023–Jun 2026) created** (jaee-moharir)
    - **No recorded authorization for the unredacted export**

11. **Data Quality Caveats**
    - Name variants unmerged (Amir Lari, Furqan Sarfaraz, Gaurav Singh, KUNAL GARG, Parshant, Sakshi)
    - Malformed cells (blank USD with only INR, etc.)
    - Internal count gaps: "~300 employee-month entries" vs "1,908 rows exported"
    - Transcript-saving skipped in at least two sessions
    - User preference references missing skill `raj-eoxs-vault` (only `eoxs-data-general` exists)

**17 Tribal Knowledge Points Extracted** (e.g., Misc Earning/Bonus is undocumented 5x variance, Cattr scores unreliable, restoration vs reward frame, bonus channel is email, two payroll files with only one current, interns/VAs invisible to register, batch proration formula × days/31)

**13 Open Items as of 2026-09-05:**
- Nandita Rana rate correction (₹RESTRICTED vs ₹RESTRICTED) → unresolved arrears
- Unredacted payroll export authorization never confirmed
- Hashir Saleem's raise — no decision
- Raj's July 2026 Cattr override reasoning — undocumented
- Documented rule for Misc Earning/Bonus — missing
- Dhrup register vs contract gap (₹RESTRICTED discrepancy)
- August LOP/attendance data, 24 unmatched salaries, 4 uncertain names
- Comp for Ayan Dutta, Humaira, Isha Bisht; MBA completion-bonus terms
- Formal salary/promotion structure — missing
- AskCruz letterhead brand asset verification needed

---

## Key Tool Differences Demonstrated

| Tool | Use Case | Character Limit | SQL Requirement |
|---|---|---|---|
| **mcp__hr__get_wiki_page** | Fetch wiki page by title | 1500 default (pageable) | No |
| **mcp__Thread_Wiki__query** | Search/browse wiki with WHERE clauses | 160 per cell | Yes (full SELECT) |
| **mcp__Thread_Wiki__get_full_text** | Get untruncated single field | 200,000 | Yes (exactly 1 row, 1 col) |

The **get_full_text** tool is the Thread Wiki database equivalent of "gimme the whole thing untruncated," used when query()'s 160-char preview is insufficient.
