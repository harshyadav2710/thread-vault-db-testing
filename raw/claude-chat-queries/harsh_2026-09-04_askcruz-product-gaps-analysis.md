---
thread_name: "askcruz-product-gaps-analysis"
user: "harsh"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

# Ask Cruz Product Improvement Analysis — Prospect Needs vs. Capabilities Gap

## Context & Methodology

**Date:** September 4, 2026  
**Analysis Scope:** 100+ EOXS prospects (Odoo pipeline) + Ask Cruz capabilities (memory + wiki) + 3GM Steel case study (first confirmed customer)  
**Skills Applied:** threads-ov, eoxs-data-general (Odoo + email/calls layers)

---

## Data Gathered

### Ask Cruz Current State (from /areas/askcruz.md memory + wiki)

**Core Capabilities:**
- Email ingestion (Gmail, Zoho)
- Call/meeting transcripts (Fireflies, Fathom)
- Client/implementation data (Odoo)
- Employee information
- Internal documents/knowledge
- Cross-source queries
- Three-tier access control (tier1/tier2_confidential/tier2)
- 6-hour synthesis cycle (raw → filtered → classified → published)
- Data completeness: 94% (as of Aug 25, 2026)

**Known Issues & Blockers:**
- Thread Vault DB: 30% save failure rate (data loss)
- Write capability: new (Aug 14 deployment), under-tested at scale
- Ingestion gaps: legacy file-based system migration incomplete
- Latency issue: Task #152 unresolved, no root cause (Claude response latency)
- Voice capability: Task #94 flagged, 11.8 days idle (AskCruz Voice Call-In)
- Project board management: Task #156 high-priority, zero activity

**First Customer Implementation:**
- **3GM Steel:** Signed Aug 20, 2026; pilot scope (2 users: Travis Lane, Stefan Brown)
- **Immediate Blocker:** Awaiting Microsoft 365 admin consent for Outlook OAuth
- **Contract:** 6-month initial pilot, affirmative decision point at 6-month mark
- **Scope:** Company Brain (Claude trained on 3GM workflows + email sync) + EOXS integration
- **Strategy:** Claude (not AskCruz) as client-facing front-end (more secure, better feature coverage)

---

## Prospect Pipeline Analysis (via Eoxs-Teams Odoo query)

**Total Opportunities:** 100+ (ranked by create_date; earliest 2024-10-17, most recent 2026-08-24)

**Stage Distribution (sample):**
- **Leads:** 20+ (Sheffield Steel, Jindal Tubular, Chemcoaters, etc.)
- **Discovery Call (Done):** 10+ (American Consolidated, Sabel Steel, etc.)
- **Client Proposal:** 8+ (Midwest Tool Steels, Primrose, Texas Pipe Works, etc.)
- **Intent:** 8+ (Hascall Steel, Pegasus Steel, Great South Metals, etc.)
- **Actions Pending:** 8+ (Leeco Steel, HarbisonWalker, Spencer Lysek, etc.)
- **Unsure:** 20+ (Eaton Steel, DEL Metals, Alaskan Copper, etc.)
- **Parked:** 4+ (Curtis Steel, Eric Letz, Tim Heston)
- **LOST:** 6+ (Kurland Steel, Merit Brass, Duluth Steel, etc.)
- **WON:** 4+ (Brannon Steel, PPC Speciality Metals, Discount Pipe & Steel, RW Conklin Steel)

**Industry:** Steel distribution, service centers, processors, fabricators, tube mills (industry-specific but matching Ask Cruz's current positioning as "for steel companies")

---

## Top 10 Product Improvements

Ranked by **value/effort ratio**, cross-referenced with **prospect needs** and **3GM requirements**.

### **1. Secure Multi-Tenant Email OAuth with Microsoft 365 & Google Workspace Support**

**Prospect Need:** 3GM Steel's immediate blocker — enterprise customers require SSO-compliant email authorization, not manual credential-sharing. Microsoft 365 admin consent flow is procurement standard for mid-market/enterprise.

**Current Gap:** Email ingestion requires manual OAuth per user; no enterprise-grade multi-tenant support for Outlook/Microsoft 365.

**Proposed Solution:** Build certified OAuth2 connector for Microsoft Graph (Outlook) and maintain robust Google Workspace support. Enable admin-level consent flow for IT procurement with user-level granular permissions. Support historical email sync (12+ month windows) with compliance-safe token handling.

**Business Impact:**
- Unblocks 3GM rollout (currently waiting for M365 admin approval)
- Enterprise procurement standard → enables 20+ prospect conversations to advance past feasibility stage
- Historical email sync becomes enterprise-safe (compliant, auditable, reversible)
- De-risks customer implementation (customers don't have to share password/service account)

**Affected Prospects:** 3GM Steel (immediate), Sabre Alloys, Monarch Steel, Greer Steel, and ~15 other mid-market steel companies in "Intent"/"Proposal" stages with enterprise IT policies

**Implementation Effort:** 2–3 weeks (OAuth2 app registration, scopes, token refresh, audit logging)

**Value vs. Effort:** ⭐⭐⭐⭐⭐ **CRITICAL / HIGH EFFORT** — Table-stakes for enterprise; high business impact ($1M+ pipeline unlock).

---

### **2. Native Odoo Real-Time Module Integration (Support Tickets, Sales/Invoice Data)**

**Prospect Need:** Prospects ask "Can AskCruz answer questions about open orders, pending invoices, and customer support tickets?" Currently, AskCruz cannot — it routes to separate `eoxs-teams` SQL layer. This fragmentation limits value perception.

**Current Gap:** Support tickets, sales orders, and invoices live in Odoo but are NOT part of AskCruz knowledge synthesis. Customers must learn two interfaces (AskCruz for context, Odoo for transactional data).

**Proposed Solution:** Ingest live Odoo modules (sale.order, account.move, helpdesk.ticket) into AskCruz's knowledge synthesis pipeline with real-time updates every 30–60 minutes. Enable queries like "Show me all unpaid invoices over $5k where payment is 30+ days overdue" or "Which customer has the most open support tickets?" or "What's our cash position (total AR less total AP)?"

**Business Impact:**
- Single interface for operational intelligence (eliminates context-switching)
- Enables "Company Brain" use case for finance (real-time cash position, AR aging)
- Differentiator vs. generic document search (becomes operational BI, not just retrieval)
- Support ticket context feeds into Company Brain (customer issue awareness)

**Affected Prospects:** All service centers, distributors, and processors in pipeline (Sabre Alloys, Greer Steel, Discount Pipe & Steel, Modesto Steel, Mid City Steel, etc.) — essentially 50+ of the 100+ prospects

**Implementation Effort:** 3–4 weeks (MCP connector design, schema mapping, sync scheduling, conflict resolution for edits)

**Value vs. Effort:** ⭐⭐⭐⭐ **HIGH VALUE / MODERATE-HIGH EFFORT** — Transforms product positioning from "document retrieval" to "operational AI"; strategic product lift.

---

### **3. Structured Data Export & Custom Report Generation**

**Prospect Need:** "I love the analysis, now I need to export this into a report my CFO can use" / "Can I get a weekly dashboard of key metrics?" This is a bottleneck for executive buy-in and repeat usage.

**Current Gap:** AskCruz returns conversational text responses; no exportable structured data (CSV, Excel, JSON, PDF reports). Finance buyers need boardroom-ready output.

**Proposed Solution:** Add structured output mode (JSON for programmatic use; CSV/Excel for spreadsheet workflows). Build report template builder (low-code: "Weekly cash position," "Monthly invoice aging," "Support ticket volume by product category"). One-click export-to-PowerPoint for board presentations.

**Business Impact:**
- Executives outside AskCruz loop can consume outputs (expands adoption)
- 3GM can present Company Brain outputs to board (critical for renewal)
- Creates repeat usage ("Run my weekly report" → foundation for automation upsell)
- Compliance: audit trail on reports (financial controls)

**Affected Prospects:** Finance-conscious mid-market (Travis Lane/Stefan Brown at 3GM, CFO/controller roles at Sabre Alloys, Greer Steel, Modesto Steel, ~15–20 total)

**Implementation Effort:** 1–2 weeks (output formatting, template builder, PowerPoint generation via python-pptx)

**Value vs. Effort:** ⭐⭐⭐ **MEDIUM VALUE / LOW-MODERATE EFFORT** — Moderate impact but quick to build; enables executive adoption.

---

### **4. Advanced Workflow Automation & Action Triggers**

**Prospect Need:** "If [condition], automatically send an email / create a task / update Odoo field." AskCruz is currently read-only; prospects want autonomous action.

**Current Gap:** Write capability deployed Aug 14 but new/under-tested at scale. No workflow/trigger framework to connect insights to actions.

**Proposed Solution:** Build workflow builder (low-code UI or natural-language) that connects conditions ("Invoice overdue 30+ days", "Support ticket unassigned >4 hours", "Order shipped") to actions (email customer, flag for AR, create task, update Odoo). Start with email automation, expand to Odoo writes (fields, records).

**Business Impact:**
- Prospect example: "Automatically email customers when their order ships" (reduces manual follow-up, improves NPS)
- Company Brain can take actions, not just advise (moves from "analyst" to "autonomous agent")
- Unlocks recurring revenue model (more value per user → premium tier)
- Reduces manual operational work (cash flow improvement story)

**Affected Prospects:** Operations-heavy customers (Discount Pipe & Steel, Modesto Steel, Greer Steel, Sabre Alloys, ~20+ in "Intent"/"Proposal")

**Implementation Effort:** 4–6 weeks (workflow engine design, trigger-condition parser, UI, testing, Odoo write API hardening)

**Value vs. Effort:** ⭐⭐⭐⭐ **MEDIUM-HIGH VALUE / HIGH EFFORT** — Strategic product lift; moves positioning from "analyst" to "autonomous agent."

---

### **5. Voice Call-In & Transcription-on-Demand**

**Prospect Need:** "I'm on a call with a customer about a complex order. Can I ask AskCruz right now without typing?" / "Transcribe this call and add it to the knowledge base automatically."

**Current Gap:** Task #94 ("AskCruz Voice Call-In") flagged, 11.8 days idle. No voice interface; field/warehouse workers must use keyboard.

**Proposed Solution:** Integrate Deepgram or Twilio STT for call-in (Toll-free number or VoIP API). Transcribe live calls, auto-add to knowledge base with speaker identity. Support voice queries ("Give me the last three customer emails about this topic") with voice-out responses (TTS).

**Business Impact:**
- Warehouse/field workers (order takers, logistics) can query without computers (accessibility, efficiency)
- Sales calls auto-summarized and added to Company Brain (context enrichment, call compliance)
- Competitive differentiator (accessibility feature)
- Compliance ready (CCPA, GDPR transcription logging)

**Affected Prospects:** All steel companies with field/warehouse presence (50+ prospects)

**Implementation Effort:** 2–3 weeks (STT API integration, audio processing, speaker ID, transcription cleanup)

**Value vs. Effort:** ⭐⭐⭐ **MEDIUM VALUE / MODERATE-HIGH EFFORT** — Convenience feature, not revenue driver; solid UX improvement.

---

### **6. Predictive Analytics & Anomaly Detection**

**Prospect Need:** "Alert me if something unusual is happening" — e.g., customer order patterns change, payment delays spike, support tickets cluster on a topic.

**Current Gap:** AskCruz is retrospective (answers "what happened?"). No predictive or anomaly-detection layer to answer "is something wrong?"

**Proposed Solution:** Add lightweight ML module running on ingested data (Isolation Forest for anomalies in invoice aging, simple time-series forecasting for trend breaks). Surface alerts in AskCruz dashboard: "Payment delay spike detected (avg 45→60 days)" or "Widget X support tickets up 300% this week." Daily/weekly digest email.

**Business Impact:**
- Prospects love "early warning" stories (avoid payment defaults, catch product issues early)
- Differentiator from generic ChatGPT+documents
- Upsell opportunity: "Anomaly detection module" as premium add-on
- Enables proactive customer outreach (sales/ops narrative)

**Affected Prospects:** CFO/controller buyers and operations leaders (Travis Lane, Stefan Brown at 3GM; finance leads at Sabre Alloys, Modesto Steel, ~20+ finance-focused prospects)

**Implementation Effort:** 2–3 weeks (feature engineering on historical data, model training, alert dashboard, email formatting)

**Value vs. Effort:** ⭐⭐⭐⭐ **MEDIUM VALUE / MODERATE EFFORT** — Nice-to-have, not mandatory; good ROI on implementation time.

---

### **7. Role-Based Synthesis & Personalized Knowledge Pages**

**Prospect Need:** "I want different people to see different summaries" — Sales reps need pipeline/competitor intelligence; operations needs inventory/fulfillment context; finance needs AR/AP/cash context.

**Current Gap:** AskCruz synthesizes to a single "company knowledge base." No role-specific filtering or custom knowledge pages per department.

**Proposed Solution:** Extend tier-based access control to synthesis level. Build persona templates: Sales (pipeline, competitive intel, customer history, RFQs), Ops (inventory, orders, fulfillment, logistics), Finance (AR, AP, cash flow, compliance). Auto-populate each with relevant synthesized widgets from the knowledge base.

**Business Impact:**
- Increases adoption (users see what matters to them, not overwhelming firehose)
- Reduces cognitive load (not everyone needs to know everything)
- Unlocks per-seat pricing model (more valuable to larger teams)
- Compliance: role-based filtering naturally enforces data governance

**Affected Prospects:** All multi-department buyers (3GM has sales, ops, finance; Sabre Alloys, Greer Steel, Modesto Steel, most "Intent"/"Proposal" stage prospects)

**Implementation Effort:** 2–3 weeks (persona definitions, synthesis branching, UI/UX for role-based dashboard)

**Value vs. Effort:** ⭐⭐⭐⭐ **MEDIUM VALUE / MODERATE EFFORT** — UX improvement, adoption driver; worth priority.

---

### **8. Historical Data Backfill & Archive Ingestion**

**Prospect Need:** "We have 5 years of email and calls. Can you ingest all of it, or just the last 12 months?" Currently, 3GM's window is 12 months (Sept 2025–present). Legacy data = institutional knowledge.

**Current Gap:** Ingestion gaps from legacy system migrations; historical backfill process undefined. Prospects with 5–10 year histories are untapped.

**Proposed Solution:** Build data import wizard (UI or API) for CSV/mailbox exports. Support backfill of Salesforce/HubSpot CRM histories, archived emails, Slack exports, call recordings from various sources. Parallel ingestion (don't slow down live sync). Auto-detect and merge duplicates. Rate-limit to avoid synthesis pipeline overload.

**Business Impact:**
- Unlock deeper institutional knowledge (5–10 year histories = gold for pattern discovery)
- Prospect selling point: "We ingest your entire history, not just 12 months"
- Premium offering: "Archive ingestion as a service" (one-time fee or add-on)
- Historical context enriches predictive/anomaly models

**Affected Prospects:** Mature companies with legacy data (Sabre Alloys, Greer Steel, Sabre Alloys, most "Intent"/"Proposal" stage, ~25+ of the 100+ pipeline)

**Implementation Effort:** 2–3 weeks (import wizard, deduplication/entity resolution, backfill scheduling)

**Value vs. Effort:** ⭐⭐⭐ **MEDIUM VALUE / MODERATE EFFORT** — Data breadth feature; solid ROI.

---

### **9. Knowledge Graph Visualization & Relationship Discovery**

**Prospect Need:** "Show me how our customers, products, and sales rep performance are connected" / "Which products are most profitable?" (requires connecting sales data + product margin + order history). Text queries don't scale for exploration.

**Current Gap:** AskCruz answers text queries but has no visual network/graph mode for exploring relationships and patterns.

**Proposed Solution:** Build knowledge graph visualization (node-and-edge UI, similar to LinkedIn profile graph or Neo4j explorer). Nodes: Customers → Products → Sales Reps → Orders → Revenue. Click a node to drill down into details. Export relationship maps (PNG for presentations, JSON for programmatic use).

**Business Impact:**
- "Aha!" moments (discover cross-sells, churn risk patterns, star performers)
- Impressive in demos (visual storytelling > text conversation)
- Enable "exploratory analysis" workflow (not just Q&A)
- Enables non-technical users to explore data (democratized analytics)

**Affected Prospects:** Strategic buyers looking for competitive intelligence (C-level, business development roles at mid-market; ~15–20 of 100+)

**Implementation Effort:** 3–4 weeks (knowledge graph extraction from synthesis data, graph DB or in-memory graph, UI rendering, drill-down logic)

**Value vs. Effort:** ⭐⭐⭐ **MEDIUM VALUE / MODERATE-HIGH EFFORT** — Demo wow-factor, exploratory analysis; competitive feature.

---

### **10. Continuous Conversation Persistence & Thread Memory (Thread Vault DB v2)**

**Prospect Need:** "My conversation with AskCruz got lost" / "I want to save and share my conversation with my team." Currently, 30% of saves fail.

**Current Gap:** Thread Vault (Threads OV) has 30% save failure rate; identity state lost on container restart; ephemeral disk staging; no user-accessible conversation history UI. Data loss erodes trust.

**Proposed Solution:** Implement Thread Vault DB v2 (dual-write: PostgreSQL + file/git, automatic retry queue). Add conversation browser UI in AskCruz web app. Users can save, share (with teammates), and reference past conversations. Full audit trail (who asked what, when, what answer).

**Business Impact:**
- Eliminates data loss fear (critical UX blocker; users won't rely on system that loses data)
- Enables "conversation as knowledge artifact" (share insights with team, onboard new employees)
- Compliance (audit trail for regulated industries: finance, healthcare, manufacturing)
- Reduces churn (reliability = retention)

**Affected Prospects:** ALL (affects every user; high-impact quality fix with broad impact)

**Implementation Effort:** 4–5 weeks (database schema design, dual-write logic, retry queue, UI, migration from Threads OV, testing for data loss scenarios)

**Value vs. Effort:** ⭐⭐⭐⭐⭐ **HIGH VALUE / MODERATE-HIGH EFFORT** — More a **quality fix** than a feature; critical for product trust. Must be done; ranks high in priority.

---

## Summary Table: Rankings by Value/Effort Ratio

| Rank | Feature | Value ⭐ | Effort | Business Impact | Affected Prospects |
|------|---------|--------|--------|-----------------|------------------|
| 1 | Secure Multi-Tenant OAuth (M365/Google) | ⭐⭐⭐⭐⭐ | High | Unblocks $1M+ pipeline | 3GM, Sabre, Greer, Monarch (20+) |
| 2 | Native Odoo Integration (Tickets/Invoices) | ⭐⭐⭐⭐ | High | Operational BI differentiator | All service centers (50+) |
| 3 | Structured Export & Reporting | ⭐⭐⭐ | Low | Executive adoption, repeat usage | Finance-conscious mid-market (15+) |
| 4 | Workflow Automation & Triggers | ⭐⭐⭐⭐ | High | Moves to autonomous agent | Ops-heavy (Greer, Discount, Modesto, 20+) |
| 5 | Voice Call-In & Transcription | ⭐⭐⭐ | High | Field/warehouse accessibility | All (50+) |
| 6 | Predictive Analytics & Alerts | ⭐⭐⭐⭐ | Moderate | Early-warning selling point | Finance/CFO buyers (20+) |
| 7 | Role-Based Synthesis Pages | ⭐⭐⭐⭐ | Moderate | Adoption driver, multi-department | All multi-dept buyers (30+) |
| 8 | Historical Backfill & Archive | ⭐⭐⭐ | Moderate | Deeper knowledge, premium add-on | Mature companies (25+) |
| 9 | Knowledge Graph Visualization | ⭐⭐⭐ | High | Demo wow factor, exploration | Strategic/C-level buyers (15+) |
| 10 | Thread Vault DB v2 (Persistence) | ⭐⭐⭐⭐⭐ | High | Quality fix, reliability, sharing | ALL USERS (100%) |

---

## Recommended Implementation Roadmap (90 Days)

**Phase 1 (Weeks 1–4): De-Risk & Stabilize**
- #1 OAuth (Microsoft 365 + Google) → Unblock 3GM go-live
- #10 Thread Vault DB v2 → Stabilize core product, stop data loss

**Phase 2 (Weeks 5–8): Expand Use Cases**
- #3 Structured Export/Reports → Drive multi-prospect conversions, executive adoption
- #2 Odoo Integration (Tickets/Invoices) → Operational BI differentiator

**Phase 3 (Weeks 9–12): Delight & Upsell**
- #7 Role-Based Synthesis → Increase adoption, personalization
- #6 Predictive Analytics → Upsell opportunity, early-warning narrative

**Backlog (Beyond 90 Days):**
- #5 Voice Call-In
- #4 Workflow Automation
- #8 Historical Backfill
- #9 Knowledge Graph

---

## Key Insights

1. **OAuth is a blocker:** 3GM is stuck waiting for M365 admin consent. This is not optional; enterprise procurement requires it.

2. **Operational BI is the differentiator:** Prospects don't want "search on documents"; they want real-time insights into operations (AR aging, support ticket volume, inventory). Odoo integration transforms Ask Cruz from "document retrieval" to "operational AI."

3. **Execution risk:** Write capability (deployed Aug 14) is new/under-tested. Workflows and automation require hardened write paths. Build carefully.

4. **Trust is fragile:** 30% data loss rate on conversations is a trust killer. Fix Thread Vault DB first; everything else assumes reliability.

5. **Role-based adoption:** Multi-department buyers need different views. Personalization drives adoption and per-seat pricing.

---

## Appendix: Prospect Pipeline Snapshot

**Sample of 100+ Opportunities in EOXS Odoo CRM:**
- Leads: Sheffield Steel, Jindal Tubular, Chemcoaters, Zekelman Industries
- Discovery Calls Done: American Consolidated, Sabel Steel, Anchor Steel, A & C Metals Sawing
- Client Proposal: Midwest Tool Steels, Primrose, Texas Pipe Works, KGS Steel, Metal Resource Solutions
- Intent: Hascall Steel, Pegasus Steel, Greenslade & Company, MSP Metals
- Actions Pending: Leeco Steel, HarbisonWalker, Claus Gundlach, Titanium Industries, HARBOR PIPE & STEEL
- Won: Brannon Steel, PPC Speciality Metals, Discount Pipe & Steel, RW Conklin Steel
- Lost: Kurland Steel, Merit Brass, Duluth Steel, Samee Metals, Ontario Steel

**3GM Steel (First Customer):**
- Contract: Aug 20, 2026
- Pilot: 2 users (Travis Lane, Stefan Brown)
- Blocker: M365 OAuth approval
- Strategic Feature: Claude as front-end (vs. AskCruz)

---

**End of Analysis**

Created: 2026-09-04 | Thread: askcruz-product-gaps-analysis
