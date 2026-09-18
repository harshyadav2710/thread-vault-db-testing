---
thread_name: "september-wiki-pages-overview"
user: "harsh"
type: claude-chat
created: 2026-09-18
updated: 2026-09-18
---

# September Wiki Pages Overview

## Turn 1: User Request for Summaries

**User:** Show me the contents of wiki page of september month and give me 2-3 lines summary on each one

### Response

Before proceeding, I reviewed the relevant skill files (threads-ov-unified-routing and eoxs-data-general) as per your preferences. I determined I'm using the **Threads OV (GitHub-backed) system** based on available tools.

### Wiki Pages Found and Summarized

#### **1. September 2025 EOXS Employee Departures & Restructuring**
**Type:** Analysis | **Created:** Aug 13, 2026 | **Tags:** HR, Restructuring, Confidential

**Summary:**
Four employees (Ranit Dutta, Kartikey, Babul Singh Bhumi, Bhavya) were terminated in a single coordinated week (Sept 1-4, 2025), all with matching settlement dates (Sept 7) and templated letters. Ranit Dutta's letter explicitly cited "organizational restructuring and downsizing"; the others gave no stated reason but align with the same pattern, suggesting a coordinated headcount reduction rather than individual exits. Separately, Humaira Zainab departed Aug 12 but rejoined in September at Rajat's request, with back-pay arrangements for her August salary.

#### **2. Eastern States Steel — Soft Launch**
**Type:** Source | **Created:** June 21, 2026 | **Tags:** Soft-launch, Adoption, ERP Resistance

**Summary:**
September 2025 marked ESS's pre-launch phase, characterized by significant employee resistance: Rose Torres planning to leave, one employee refusing EOXS work, Tom Meyer cancelling training calls, and VP Sales Vince Pappas (credentials sent Sept 16) delaying engagement until December. President Ryan Capinski was the sole champion, personally driving 189 customizations. Rajat acknowledged EOXS's threshold (minimum 10 employees for viability) was violated, creating disproportionate implementation burden on the client side.

#### **3. Discount Pipe & Steel — Post-Go-Live Operations**
**Type:** Source | **Created:** June 21, 2026 | **Updated:** Aug 3, 2026 | **Tags:** Post-launch, Support Transition, Infrastructure

**Summary:**
DPS went live July 7, 2025; transition to ticket-based support occurred Aug 7, 2025. September 2025 saw the client's first wave of reported issues: packing slips generating incorrectly, inventory reservation failures, missing TaxCloud integration, and incomplete AirCall/barcode-scanner setup. Amy Rayzor described the mood as anxious ("life raft floating away"), with a two-person warehouse team operating a system still under active development. Packing slip bugs would persist as the most critical operational pain point through May 2026.

#### **4. September 2025 Logged Hours & Overtime Reporting**
**Type:** Analysis (referenced in search but full page retrieval failed)

**Summary from search snippet:**
In September 2025, HR lead Isha Bisht ran a manual, Cattr-derived logged-hours reporting cycle for the EOXS team, capturing overtime and hours for Dhrup, Harneet, Ron, Arpan, Rohit, Sakshi, Sheenam, and others with itemized breakdowns per employee.

---

## Turn 2: User Request for Full Wiki Page Content

**User:** Show me the contents of one of wiki page from the month of september

### Response: September 2025 EOXS Employee Departures & Restructuring (Full Content)

[Full page content provided - detailed termination records for Ranit Dutta, Kartikey, Babul Singh Bhumi, Bhavya, and Humaira Zainab's departure/rejoin cycle]

---

## Turn 3: User Request for Wiki Page + Tool Invocation Details

**User:** Fetch another wiki page and show me the tool you invokes?

### Tool Invocation Details

**Tool Used:** `mcp__hr__get_wiki_page`

**Parameters:**
```
{
  "title": "Eastern States Steel — Soft Launch",
  "max_chars": 4000
}
```

### Response Metadata

| Field | Value |
|-------|-------|
| **ID** | 1042 |
| **Page Type** | source |
| **Created** | 2026-06-21 |
| **Updated** | 2026-07-09 |
| **Access Tier** | tier2 |
| **Body Length** | 31,141 characters |
| **Truncated** | Yes (offset: 0, next_offset: 4000) |
| **Source File** | wiki/sources/eastern-states-steel/Eastern States Steel — Soft Launch.md |

### Wiki Page Content: Eastern States Steel — Soft Launch

**Tags:** eastern-states-steel, cluster, soft-launch, adoption

#### Summary

The September–December 2025 period covers Eastern States Steel's full soft-launch arc: pre-launch preparation, a November 2025 go-live, and a demanding post-launch stabilization phase marked by significant employee resistance and an unusually high customization burden. Ryan Capinski (President) was the sole internal champion throughout, personally driving 189 customizations while the rest of the ESS team either refused to engage or engaged only minimally. Rajat Jain (EOXS President) acknowledged in December 2025 that EOXS does not normally onboard companies with fewer than 10 employees precisely because the implementation workload on the client side is disproportionate.

#### Employee Resistance (September 2025)

In **September 2025**, Ryan disclosed that:
- Admin **Rose Torres** was planning to leave the company
- At least one unnamed employee had already "refused to do any additional work in EOXS," viewing it as outside their job responsibilities
- **Tom Meyer** (Production & Logistics Coordinator) was slow to engage — cancelling training calls in September, going silent in October/November
- **Vince Pappas** (VP Sales) was added to the system in September (credentials sent **September 16**) but accepted the soft-launch invite only on **December 11**

#### Implementation Timeline (September Forward)

- **Sept 2–16, 2025:** Credentials issued; initial resistance documented
- **Nov 10–15, 2025:** Intensive implementation sprint (daily zoom calls)
- **Nov 21, 2025:** Large data push of 89 additional warehouse locations
- **Nov 27, 2025:** Comprehensive live update (23 bug fixes & feature changes)
- **Dec 1, 2025:** Ryan sent detailed critique; Rajat waived cage-workflow fee
- **Dec 19–20, 2025:** Go-Live Authorization circulated
- **Dec 22, 2025:** Full active use began; high-volume support requests

#### Key Friction Points

- **Data entry dependency:** ESS staff routing all requests through EOXS instead of operating independently
- **Customization burden:** Ryan explicitly wanted team to set up customers, vendors, warehouses, products themselves
- **Assembly/cage workflow:** Still pending as of Dec 31, 2025
- **Formal go-live target:** January 5, 2026

**Outbound Links:** [[Ryan Capinski]], [[Rose Torres]], [[Tom Meyer]], [[Vince Pappas]], [[Rajat Jain]], [[Eastern States Steel — Post-Launch Operations]]

**Note:** Page is truncated; 31,141 total characters. Next chunk starts at offset 4000.
