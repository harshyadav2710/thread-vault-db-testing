---
thread_name: "askcruz-agent-capabilities-analysis"
user: "harsh"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

# AskCruz Agent Capabilities Analysis — Chat Transcript

**Date:** September 4, 2026  
**Participants:** Claude (analyst), EOXS/AskCruz stakeholders  
**Topic:** Identifying top 10 agent-style use cases, prospect fit, required actions, and product changes to evolve AskCruz from Q&A to operational execution

---

## User Request

Review the workflows, employee challenges, business processes, and operational requirements mentioned throughout the EOXS MCPs. Analyze AskCruz's current capabilities and identify tasks where AskCruz could evolve from simply answering questions into taking useful actions or assisting employees through multi-step workflows. Identify the top 10 agent-style use cases, the prospects that could benefit from them, what actions would be required, and what product changes would be necessary to support them.

---

## Analysis Methodology

1. **Data Collection Phase:**
   - Reviewed EOXS Skills (eoxs-data-general, threads-ov) for access scoping and connector rules
   - Called get_index() to assess available data scope (1463 wiki pages, 30,498 email threads, 2201 Fireflies calls, 824 implementation tasks, 8 clients)
   - Searched EOXS wiki for workflows, operational processes, and pain points
   - Listed 150+ active implementation tasks from Odoo Kanban across 8 clients
   - Reviewed business schema (sale_order, account_move, stock_picking, res_partner, etc.) to understand data mutations required
   - Checked AskCruz architecture memory (backend/frontend, data ingestion pipeline, current capabilities, 3GM client status)

2. **Pattern Recognition:**
   - Identified recurring task types across implementation backlogs (order processing, inventory management, payment reconciliation, packing workflows)
   - Cross-referenced tasks with wiki pages to extract business context (why tasks exist, who's affected, customer pain points)
   - Mapped EOXS client base (8 active: Sabre Alloys, 3GM, Discount Pipe & Steel, Eastern States Steel, Greer Steel, PPC Metals, Brannon Steel, RW Conklin Steel)

3. **Use Case Development:**
   - Created 10 candidate workflows based on:
     - Highest frequency of implementation tasks
     - Strongest customer pain signals (from calls, emails, wiki analysis)
     - Alignment with AskCruz's ability to access data + take multi-step actions
     - Revenue/efficiency impact potential
   - Validated each use case against specific prospects (matching workflow to their workflow issues)
   - Outlined specific agent actions required (parse data → validate → write → notify → follow-up)

4. **Product Roadmap:**
   - Phased approach (5 phases, 6-9 months total) from foundation (write capabilities) to advanced workflows
   - Identified infrastructure needs (DB writes, webhooks, approval workflows, audit logging, ML/NLP)
   - Mapped to AskCruz strategic goal of $1M ARR in 12 months

---

## Key Findings Summary

### Top 10 Agent Use Cases Identified

1. **Quote-to-Order Conversion & Order Creation**
   - Automates quote validation, SO creation, salesperson retention, confirmation emails
   - Prospects: Discount Pipe & Steel, Sabre Alloys, PPC Metals
   - Required: Write to sale.order, validation rules, email integration

2. **Inventory Discrepancy Detection & Resolution**
   - Automated inventory reconciliation, tag correction, notifies teams
   - Prospects: Discount Pipe & Steel, Eastern States Steel, Greer Steel
   - Required: Write to stock.move, inventory tables, barcode scanning integration

3. **Invoice Status & Payment Tracking Automation**
   - Cross-matches invoices to payments, auto-suggests reconciliation entries, ages receivables
   - Prospects: Discount Pipe & Steel, PPC Metals, Sabre Alloys (all clients)
   - Required: Write to account.move, bank transaction matching, aging queries

4. **Packing & Shipping Error Prevention**
   - Real-time packing slip validation, tag scanning, flag mismatches, route to supervisor
   - Prospects: Discount Pipe & Steel, Eastern States Steel, Brannon Steel
   - Required: Write to stock.picking, mobile interface, barcode scanning, pick-list sync

5. **Quote Pricing & Discount Calculation**
   - Auto-generates quotes with customer-specific pricing, volume breaks, landed costs
   - Prospects: Discount Pipe & Steel, PPC Metals, Sabre Alloys
   - Required: Pricelist engine, freight calculator, quote expiration workflow

6. **Lead Scoring & Sales Opportunity Routing**
   - Inbound lead parsing, ICP scoring, auto-assignment to salesperson, follow-up scheduling
   - Prospects: EOXS internal sales, future customers (CRM expansion)
   - Required: Write to CRM module, lead scoring model, email webhook parsing

7. **Implementation Task Prioritization & Status Update**
   - Synthesizes task context from emails/calls, recommends priority, suggests next micro-action
   - Prospects: EOXS implementation team, future customers with Kanban workflows
   - Required: Write to project.task, task context synthesis, scoring algorithm, daily digest

8. **Support Ticket Triage & Auto-Response**
   - Auto-categorizes tickets, detects duplicates, assigns severity, routes to team, sends ack
   - Prospects: EOXS support, future scope expansion
   - Required: Email parsing, ticket categorization (NLP), severity rules, routing logic

9. **Monthly Reporting & Variance Analysis**
   - Automated P&L, Balance Sheet, Cash Flow; variance calculations with narratives; email delivery
   - Prospects: Discount Pipe & Steel, PPC Metals, Sabre Alloys, all expanding clients
   - Required: GL report generation, templating, variance detection, scheduled delivery

10. **Onboarding Workflow Orchestration (New Clients)**
    - Creates customized onboarding checklist, distributes tasks, tracks progress, flags risks, manages milestones
    - Prospects: 3GM Steel (current), pipeline (Primrose, Texas Pipe, Flack Global)
    - Required: Workflow templating, task dependencies, team assignment, status dashboard

### Prospect-Use Case Matrix

**Discount Pipe & Steel** is the highest-impact prospect (fits 9/10 use cases) — their implementation backlog has 60+ tasks spanning quote, inventory, invoicing, packing, pricing issues.

**3GM Steel** (current customer) benefits most from onboarding orchestration + quote/order automation for Company Brain deployment.

**EOXS Internal** benefits from task prioritization, lead routing, support triage, reporting automation to free team for product/sales work.

### Product Capability Roadmap (5 Phases, 6-9 Months)

**Phase 1 (Months 1-2) — Foundation:**
- Write access to Odoo core tables (sale.order, account.move, stock.move)
- Approval workflow engine for financial writes (human-in-the-loop)
- Audit logging (WHO/WHAT/WHEN/WHY for compliance)
- Webhook handlers (inbound email, forms, 3rd-party events)

**Phase 2 (Months 2-3) — Core Workflows:**
- Use Cases 1, 2, 3, 4 live (quote conversion, inventory, invoicing, packing)
- Customer pilot with Discount Pipe & Steel
- Mobile warehouse interface (tablet-based scanning)

**Phase 3 (Months 4-5) — Intelligence:**
- Use Cases 6, 8 live (lead routing, support triage)
- NLP-based categorization + anomaly detection
- Predictive notifications

**Phase 4 (Months 5-6) — Reporting:**
- Use Case 9 live (monthly reporting automation)
- Client-customizable templates + dashboard
- Variance narrative generation

**Phase 5 (Months 6-9) — Advanced:**
- Use Case 10 (onboarding orchestration)
- Workflow builder (no-code for power users)
- Integration marketplace (QB, Klaviyo, AirCall per requests)

### Infrastructure & Capability Requirements

- **Database:** Expand write permissions, field-level access control, audit tables, cascade triggers
- **APIs:** Webhook handlers, approval workflow engine, task creation API, queue management
- **Data Pipeline:** Real-time sync, anomaly detection stream, CDC for audit
- **External:** Email APIs, calendar, payment processors, barcode scanning, SMS/Slack
- **AI/ML:** NLP categorization, anomaly detection models, recommendation engines, RAG for narratives

### Risks & Mitigation

| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| Write operations cause data corruption | Critical | Medium | Comprehensive testing + approval + audit + rollback |
| Poor agent routing decisions | High | Medium | Simulate on historical data + human-in-the-loop for high-value |
| Customer loss of visibility | Medium | High | Audit dashboard + email summaries + feedback loop |
| Scaling costs | Medium | High | Caching + batch ops + cost monitoring |
| Regulatory/compliance | High | Low | Legal review + SOC 2 + customer data governance |
| Agent context loss (multi-step) | Medium | Medium | Persistent workflow state + replay for debug |
| Integration brittleness | Medium | High | Graceful degradation + vendor monitoring + alerts |

### Success Metrics & Go/No-Go

**Phase 1:** ≥3 internal agents write to Odoo; zero data corruption in UAT  
**Phase 2:** Quote conversion + inventory reconciliation live with 2 customers; error rate <2%  
**Phase 3:** Lead scoring accuracy >80%; support auto-triage adoption >50%  
**Phase 4:** Monthly reporting automation live; customer satisfaction >4/5  
**Phase 5:** Onboarding live for 1 new customer; go-live on-time; post-launch NPS >7  

### Strategic Alignment

These 10 agent workflows support AskCruz's $1M ARR goal by:
- Faster customer time-to-value → lower implementation duration → higher NPS → faster sales
- Reduced EOXS ops burden → frees team to sell and support
- Customer stickiness → agents become essential → churn risk ↓
- Expansion opportunity → new use cases → upsell revenue
- Market differentiation → "AI that does" (not just "AI that answers")

---

## Deliverable

Full analysis document (2000+ words, complete roadmap, phased plan, risk matrix, success metrics) saved to:  
`/home/claude/askcruz-agent-use-cases-analysis.md`

This analysis is ready for stakeholder review (Product, Engineering, Customer Success) and can be used to prioritize Phase 1 scope, start Discount Pipe & Steel co-design, and build the prototype (quote conversion workflow).
