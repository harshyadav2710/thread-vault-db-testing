---
thread_name: "askcruz-overview"
user: "harsh"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

## AskCruz Deep Dive — Complete Overview

**User Q1:** what is askcruz? give all the information you know about askcruz

**User Q2:** say more about it

---

## COMPREHENSIVE RESPONSE

### **Four Product Pillars**

AskCruz is built around four canonical capabilities:

**1. Company Brain** — The company's shared working knowledge. Enables users to ask ordinary business questions and get answers based on available company context. Examples: "Who handled this customer issue?", "What was promised to this customer?", "How do we normally handle this situation?", "Why did this customer's margin change?"

**2. Company Hands** — Practical work AskCruz performs using company knowledge. Includes drafting quotes with company pricing logic, flagging orders at risk of missing promise dates, summarizing customer calls, preparing account briefings, and identifying operational issues.

**3. Digital Workforce** — Standing responsibilities that watch and report. Rather than one-time answers, this capability monitors conditions (order queues, defined exceptions) and alerts when attention is needed.

**4. Company Personalization** — AskCruz reflects how *your specific company* actually works, not generic industry assumptions. This includes vocabulary, pricing practices, tolerances, customer expectations, and established operational patterns.

---

### **Product-Market Fit Status**

**Current thesis:** AskCruz solves a horizontal, cross-industry problem—companies that have scattered data across multiple systems need that knowledge structured and accessible from one place.

**Core problem addressed:** Fragmented business data + fragmented organizational knowledge = employees wasting time searching multiple systems or asking around.

**Strong PMF signals:**
- Working product already deployed and running internally at EOXS
- Industry-agnostic positioning backed by architecture designed to scale across any vertical
- First external customer (3GM Steel) acquired and mid-implementation

**Evidence still needed for proven PMF:**
- Customer retention and renewal rates
- Actual usage frequency and patterns
- Measurable time saved or business impact
- Willingness to pay and pricing acceptance
- Customer expansion (more users, more sources)
- Customer referrals
- Repeatable acquisition across different industries

**30-day priorities** (as documented):
1. Product refinement using real customer needs
2. Customer readiness and deployment repeatability
3. Customer acquisition while measuring what buyers value

---

### **Architecture and Data Pipeline**

The documented 10-stage pipeline:

**Source Systems → Ingestion → Filtering → Sensitivity Classification → Central Knowledge Store → Knowledge Generation → Citation Check → Human Approval → Retrieval → Response**

**Connected data sources:**
- **Gmail** (three individual accounts)
- **Zoho** (shared support inbox)
- **Fireflies** (business call transcripts)
- **Fathom** (call recordings)
- **Odoo** (client implementation/onboarding boards for configured clients)
- **Linear** (tracking and reporting)

**Ingestion mechanisms** (all automatic):
- Event-driven ingestion
- Scheduled sweeps
- Source-specific fetchers
- Synchronization jobs

**Knowledge generation:** Runs on a **6-hour synthesis cycle**—raw information is synthesized into readable knowledge pages, citations are verified, and human approval is required before publication.

**Access control:** Three-tier system:
- `tier1` = Raj-Personal (most restricted)
- `tier2_confidential` = Company-Confidential (internal-team-only sensitive information like financials, salaries, legal matters)
- `tier2` = General (broad visibility, with financial amounts and employee performance data stripped)

---

### **Current Deployment & Client Status**

**EOXS Internal Pilot:** AskCruz is fully operational and running as an internal second brain for EOXS itself.

**3GM Steel (First External Customer):**
- Deal confirmed August 2026 (2-user scope, reduced from original proposal)
- Currently mid-implementation (as of early September 2026)
- Primary buyer: CEO (customer-side)
- Use cases: sales prep, customer history, order tracking, inventory/availability checks, quote drafting with company pricing

**Important distinction:** EOXS has a broader roster of clients it serves through other services. **These are NOT AskCruz clients.** Only 3GM is confirmed as an AskCruz customer. This distinction matters for marketing and positioning.

**Sales pipeline includes:**
- Sabre Alloys (proposal sent Aug 13; follow-up call Sep 2)
- Three D Metals (prospect in development)
- Legal services exploration (distinct from steel verticals)

---

### **Positioning Strategy**

**Official positioning: Industry-agnostic horizontal platform.** AskCruz is NOT a steel-only product. That it's currently piloted at EOXS (a steel-sector operator) and that 3GM is a steel company reflects who was onboarded first, not a scope limitation.

**Canonical product definition:**
> AskCruz is an industry-agnostic AI agent that connects a company's scattered business data, structures it into usable organizational knowledge, and lets employees access that knowledge through a single conversational interface.

**Market definition:** Any industry + scattered business data + need for structured centralized access = AskCruz's addressable market.

**Competitive differentiation:**
- Horizontal vs. vertical-specific
- Multi-source knowledge layer (not single-system search)
- Conversational interface
- Access controls and sensitivity classification built-in
- Citation verification and human approval in the pipeline
- Expandable (grows as more sources connect)

---

### **Known Positioning Conflicts**

There's an **internal contradiction in source materials**: One asset frames AskCruz as steel-industry-specific; another (the market-fit guide) and the client-facing documentation all frame it as industry-agnostic. The PMF guide is the canonical positioning; the steel-only framing is outdated or needs revision.

---

### **My Role (3GM Project)**

I'm currently testing the **3GM project** — specifically the **Outlook email sync system** (3GM stands for the project, not the company).

**What I'm testing:**
- OAuth authentication flow
- Email deduplication (ensuring duplicate emails are handled correctly)
- Attachment text extraction
- Database verification across a 6-table schema

This is part of onboarding 3GM's email data into AskCruz's ingestion pipeline so their email knowledge becomes available through the product.

**My team:**
- Priyanshu Sinha — Frontend (teams.askcruz.com)
- Jagriti Chowdhury — QA, HR MCP testing
- Isha Bisht — HR Executive (onboarding, offboarding, leave)
- Danish & Harsimran — Other interns

---

### **Product Boundaries (What AskCruz Is NOT)**

- Not a replacement for an ERP system
- Not unrestricted database access
- Not real-time (ingestion/synthesis have update cycles)
- Not autonomous decision-maker (human review required for important decisions)
- Not limited to steel or any single industry
- Not 100% complete on every company's data (only ingests what's connected)
- Not guaranteed accurate (answers depend on source quality and freshness)

---

**Sources:** Complete AskCruz product documents (self-knowledge, market-fit guide, product feature file, client-facing understanding, system architecture) imported Aug 25, 2026; EOXS wiki pages (synthesized, current as of Sep 5, 2026).
