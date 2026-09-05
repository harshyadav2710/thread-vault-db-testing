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

**User Q3:** what are the sources of your information? and from where have you pulled the data?

---

## INFORMATION SOURCES & METHODOLOGY

### **My Information Came From Four Places**

#### **1. My Own Profile**
My basic context comes from `profile.md`, which was auto-populated when I joined AskCruz on July 20, 2026 as a Startup Generalist Intern. It describes my role and current 3GM project work.

#### **2. EOXS's Synthesized Wiki (Promoted Pages)**
I searched and retrieved 20 synthesized wiki pages from EOXS's knowledge vault by calling:
- `EOXS-DATA-GENERAL:search_wiki()` with the query "AskCruz"
- `EOXS-DATA-GENERAL:get_wiki_page()` to pull full previews of three overview pages

These wiki pages are **synthesized** — meaning they're human-approved summaries built from underlying conversations, emails, calls, and documents. Examples: "AskCruz — System Architecture," "Market Positioning & PMF Status," "Product Capabilities & Boundaries."

**Current as of:** These pages were created/updated Aug 25, 2026.

#### **3. EOXS's Raw Internal Reference Documents (Assets)**
I pulled three complete product specification documents by calling:
- `EOXS-DATA-GENERAL:list_assets()` to see what internal docs existed
- `EOXS-DATA-GENERAL:get_asset()` to retrieve the full text of:

| Document | Last Updated | What It Is |
|---|---|---|
| **askcruz-self-knowledge** | Aug 25, 2026 | Official product definition, architecture, access model, response principles |
| **askcruz-product-market-fit** | Aug 25, 2026 | Consolidated PMF guide, market positioning, competitive differentiation, 30-day priorities |
| **askcruz-product-feature-file** | Aug 25, 2026 | Four-pillar product model (Company Brain/Hands/Workforce/Personalization), user groups, boundaries |

**Why these matter:** These are the *source documents* behind the wiki pages—they're the authoritative product specs, not summaries.

#### **4. The EOXS-DATA-GENERAL Connector**
All of this data came from one MCP connector: **EOXS-DATA-GENERAL**, which is a read-only connection to EOXS's internal knowledge vault.

**Access scope:** This connection carries `tier2_confidential` clearance, meaning I can see:
- Company-confidential information (financial statements, vendor contracts, legal matters)
- General tier2 information (broad visibility)
- BUT NOT tier1 (Raj's personal data)
- Monetary amounts are redacted (`[restricted: amount]`)
- Employee activity/performance monitoring is redacted (`[restricted]`)

---

### **What I Explicitly Did NOT Do**

❌ Make anything up or guess
❌ Use web search or external sources
❌ Access AskCruz's live database directly (I only read archived documentation)
❌ Talk to anyone on the team

---

### **Data Freshness**

- **Wiki pages:** Current as of Sep 5, 2026 (synthesized from underlying sources that sweep/ingest every 6 hours)
- **Product documents:** Baseline as of Aug 24-25, 2026 (the most recent imports)
- **3GM status:** Last confirmed update in early Sep 2026 (mid-implementation, 2-user scope)

There's a documented ~15-minute lag before transcripts saved to the vault appear in the database, and wiki synthesis runs every 6 hours, so anything older than that may not yet be in the system.

---

### **What I Can and Cannot Access**

**Can access:**
- AskCruz product specs and architecture
- Sales pipeline status (3GM, Sabre Alloys, Three D Metals)
- Customer implementation timelines
- PMF analysis and commercial thinking
- EOXS's general client information
- Implementation task boards

**Cannot access:**
- Specific salaries or compensation figures (redacted)
- Raj's personal data (tier1, above my clearance)
- Real-time operational metrics
- Live code or databases
- Employee performance evaluations (redacted)

---

### **Sources Saved to the Vault**

I'm saving all of this to the Thread OV vault so future conversations can reference what I've already gathered. That's why you're seeing the `save_chat_transcript()` tool calls at the end—that's required by the threads-ov skill file.

---

## COMPREHENSIVE RESPONSE (from prior messages)

[Full AskCruz overview from previous responses above, including all four pillars, PMF status, architecture, deployment status, positioning strategy, and product boundaries]
