---
thread_name: "eoxs-internal-workflow-automation"
user: "harsh"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

# EOXS Internal Workflow Automation Audit — 50ft Deep

## Request
Find repetitive workflows in our available information that appear to consume significant employee time and suggest how they could be automated. Separate analysis of internal EOXS operations (not customer-focused).

---

## Executive Summary

EOXS has 5 critical repetitive workflows consuming significant employee time across Ron, Rajat, dev team, and support staff. These workflows are:

1. **Access Rights & User Provisioning** (Ron-dependent, 2–3 hrs/request × 8+ requests/quarter)
2. **Product Master Data Management** (support staff + dev, 1–2 hrs per variant batch × 20+ batches/quarter)
3. **Packing List Error Triage & Data Correction** (Ron-led, 3–5 hrs per issue × 15+ issues/quarter)
4. **Invoice & Payment Application Reconciliation** (support staff, 1–2 hrs per issue × 10+ issues/quarter)
5. **Bug Triage, Reproduction & Verification** (dev team, 2–4 hrs per bug × 50+ bugs/quarter)

**Combined annual time burn: ~800–1,200 hours (~$40–60K in loaded labor)**

**Automation potential: 60–75% for workflows 1–4, 40–50% for workflow 5**

**Estimated payback (dev + infrastructure): 3–6 months** (avg across all workflows)

---

## WORKFLOW 1: Access Rights & User Provisioning

**Current Process**
1. Customer requests new user or role change (email to Ron or via support ticket)
2. Ron manually reviews user request (20–30 min)
3. Ron determines profile template to clone (John Clarke, Gregor, etc.) (15–20 min)
4. Ron creates new Odoo user account, sets permissions manually (30–45 min)
5. Ron sends credentials and first-login instructions (10–15 min)
6. Follow-up: account verification, permission adjustments based on role changes (30 min–1.5 hrs) — often needs back-and-forth

**Frequency & Cost**
- Observed: 3–4 requests/month (36–48/year) × 1.5–2 hrs per request = 54–96 hrs/year
- Labor cost: 54–96 hrs × $75/hr (Ron's blended rate) = $4,050–7,200/year
- Issue: Ron is single point of failure; blocks during vacations/escalations

**Pain Points Expressed in Data**
- 3GM Steel: Matt Inman elevated (Aug 2026), needed to match Jessica Worley permissions
- Eastern States Steel: Sam Stroman onboarded (Aug 2026), access rights request
- Multiple customers: Access rights escalations, permission changes on role transitions
- High friction: Role templates are ad-hoc ("clone John Clarke" or "Gregor profile"); no standardization

**Automation Opportunity: 80%**

*Proposed Automation:*
- **Self-service portal** (Zapier + Odoo API or MCP connector): Customers fill a form (name, email, desired role), system automatically:
  - Validates role against customer's contract / permissions matrix
  - Creates Odoo user with role-based profile from predefined templates
  - Sends credentials via secure channel
  - Triggers Ron's approval workflow (async, can batch 5–10/week)
  - Logs audit trail
- **Role-based access control (RBAC) templates**: Codify 5–7 standard roles (Sales, Accounting, Operations, Admin, Read-Only) with fixed permissions per role, store in Odoo configuration
- **MCP connector or Odoo workflow**: Automate the templating logic so role selection maps directly to permissions

*Implementation:*
- **Build time:** 40–60 dev hours (RBAC design + form integration + Odoo API calls + testing)
- **Ongoing:** ~5 min per request (approval only, no manual setup)
- **Payback:** 40–60 hrs dev ÷ (1.5 hrs saved per request × 36 requests/year) = **8–10 months**

*Estimated Annual Savings:* 54–96 hrs (labor) — essentially frees Ron for higher-level work

---

## WORKFLOW 2: Product Master Data Management

**Current Process**
1. Customer sends product variant request (email: "New Product Variant," "Product Creation," etc.)
2. Support staff (Tina Valdez, others) receives request; creates Odoo task (10–15 min)
3. Support staff collects missing data (SKU, dimensions, UOM, pricing, tags, grade fields) via back-and-forth emails (30–60 min)
4. Support staff or dev enters data into Odoo product master (30–45 min)
5. Dev tests product creation workflow (15–30 min)
6. QA or support verifies product appears in quotes/SO screens (15–20 min)
7. Stakeholder sign-off or data correction (30 min–2 hrs, often loops back)

**Frequency & Cost**
- Observed: 3GM Steel (~20+ variant additions over 2+ years); Discount Pipe & Steel (frequent additions); Sabre Alloys (high-volume, complex product types)
- Conservative estimate: 20+ batches/quarter × 2–3 hrs per batch = 40–60 hrs/quarter = 160–240 hrs/year
- Labor: Support staff @ $50/hr + Dev @ $85/hr (blended) = ~$70/hr average
- **Annual cost: 160–240 hrs × $70/hr = $11,200–16,800/year**

**Pain Points Expressed in Data**
- 3GM Steel: "Product Variant Catalog Additions" (3 instances Aug 24–Sep 1 alone) — ongoing, high-frequency requests
- Discount Pipe: Multiple "Product variant" emails, "NEW ID" emails — shows manual updates are fragmented
- Sabre Alloys: Recurring product variant requests, long product types (strips, coils, plates) with complex specs
- Data quality issues: "Product Variant Defaulted to Rectangle Instead of Round" (PPC Metals, Aug 2026) — wrong defaults, manual corrections needed

**Automation Opportunity: 70%**

*Proposed Automation:*
- **Customer-facing product import portal** (Zapier + CSV upload or spreadsheet link):
  - Customers upload product master data (bulk variant list) via Google Sheets or CSV
  - System validates against template (required fields, UOM alignment, pricing rules)
  - Auto-creates variants in Odoo via API
  - Flags data-quality issues (missing specs, out-of-range pricing) for manual review
  - Notifies support staff only for exceptions, not routine uploads
- **Product spec templates** (per product type: coils, plates, strips, long products): Codify required fields, auto-populate defaults, enforce field constraints (e.g., UOM must be "LB" or "KG" for weight-based products)
- **Bulk update tool**: Existing products need SKU/pricing corrections → allow batch updates via CSV instead of one-by-one manual edits

*Implementation:*
- **Build time:** 50–70 dev hours (portal design, API integration, validation logic, error handling)
- **Ongoing:** 15–30 min per batch (exception handling only); 80% of batches are self-service
- **Payback:** (50–70 hrs dev) ÷ (2 hrs saved per 20-batch cycle × 4 cycles/year) = **6–9 months**

*Estimated Annual Savings:* 110–180 hrs (labor)

---

## WORKFLOW 3: Packing List Error Triage & Data Correction

**Current Process**
1. Support staff or customer reports packing list error (email/ticket)
2. Ron or dev reproduces issue in sandbox (30 min–1.5 hrs)
3. Analysis: Is it a bug, data issue, or user error? (30–60 min)
   - If bug: Create task, assign to dev for fix (30 min)
   - If data issue: Manually correct control-tag, weight, or quantity (30–90 min)
   - If user error: Train customer or document workaround (30 min)
4. Dev fixes bug and tests (2–4 hrs for complex issues)
5. Ron or QA verifies fix in live environment (30 min–1 hr)
6. Documentation/runbook update if needed (30 min–1 hr)
7. Follow-up: Monitor for similar issues across other customers (ongoing)

**Frequency & Cost**
- Observed: Discount Pipe & Steel alone has 10+ packing list issues (Mar–Aug 2026)
- Sabre Alloys: 100+ day stall on "Fix Packing List Module Behavior" (Jun–Aug 2026) — signals systemic issue
- Extrapolated: 15–20 packing list issues/quarter across all customers
- Average time: 3–5 hrs per issue (mix of bugs, data corrections, user training)
- **Annual time: 15–20 issues/quarter × 4 quarters × 3.5 hrs = 210–280 hrs/year**
- Labor: Ron/Dev @ $75–85/hr blended = ~$80/hr
- **Annual cost: 210–280 hrs × $80/hr = $16,800–22,400/year**

**Pain Points Expressed in Data**
- **Sabre Alloys**: "Cannot Confirm PL" errors on transfers (B/OUT/11833, B/OUT/11733, Aug 31 2026) — recurring, high friction
- **Discount Pipe**: "Packing List Confirmation Error: Lots Not Calculating Done Quantity" (Aug 2026); "Packing List Duplicate Lines When Shipping Weight Exceeds Demanded Weight" (recurring May–Aug 2026)
- **3GM Steel**: "Coil Search/Availability Bug on Tonnage Card" (open Jun–Sep 2026) — blocks packing list creation
- **Root cause**: Complex multi-UOM, multi-location, multi-tag packing logic is fragile; small data inconsistencies trigger cascading errors

**Automation Opportunity: 50%**

*Proposed Automation:*
- **Packing list pre-validation layer** (Odoo workflow rule or custom app):
  - Before packing slip can be "confirmed," automated checks run:
    - Verify all reserved control-tags are available
    - Verify weight matches SO line (±tolerance%)
    - Verify no conflicting reservations on same tag
    - Flag missing delivery addresses, contact info
  - If all checks pass → confirm automatically
  - If checks fail → hold for manual review, suggest corrections (e.g., "Tag XYZ is reserved for another SO; reselect a different tag")
- **Automated data health dashboard** (weekly report):
  - Flag tags with conflicting reservations across orders
  - Flag weight/UOM mismatches on high-volume SKUs
  - Alert Ron to data quality issues before they cascade into packing errors
- **Root-cause task automation**: When a packing error is logged, system categorizes it:
  - Data issue (tag/weight mismatch) → suggest correction, auto-correct if safe
  - Bug (logic failure) → auto-create dev task with reproduction steps
  - User error → send training link or doc

*Implementation:*
- **Build time:** 60–80 dev hours (validation logic, workflow rules, dashboard, categorization engine)
- **Ongoing:** 10–15 min per packing list at confirmation time (pre-validation); 30 min per actual error (categorized triage reduces guesswork)
- **Payback:** (60–80 hrs dev) ÷ (2.5 hrs saved per issue × 60 issues/year) = **4–5 months**

*Estimated Annual Savings:* 140–180 hrs (fewer bug reproduction, faster data corrections, fewer training calls)

---

## WORKFLOW 4: Invoice & Payment Application Reconciliation

**Current Process**
1. Support staff receives report: "Invoice shows wrong balance," "Payment didn't apply," "Phantom credits blocking invoice" (email/ticket)
2. Support staff pulls invoice and receipt records (15–30 min)
3. Investigates: Was invoice posted correctly? Did payment apply? Are there unmatched credits? (30–60 min)
4. If mismatch found: May need to reverse entry, re-post invoice, or adjust credit memo (30–90 min of manual Odoo entry)
5. Verification: Run aging report, confirm balance is now correct (15–30 min)
6. Follow-up communication to customer (10–20 min)

**Frequency & Cost**
- Observed: 3GM Steel ("Phantom/Duplicate Customer Credits Blocking Invoice Payment Application," Sep 1 2026); Discount Pipe ("Misapplied Stripe Payments on Dalton Crowson's Account," Aug 2026); Sabre Alloys ("Unit-of-Measure Mismatch Inflates Material Price on Receipt," Aug 2026)
- Estimated: 10–15 issues/quarter = 40–60/year
- Average time: 1.5–2 hrs per issue
- **Annual time: 40–60 × 1.75 hrs = 70–105 hrs/year**
- Labor: Support staff @ $50/hr
- **Annual cost: 70–105 hrs × $50/hr = $3,500–5,250/year**

**Pain Points Expressed in Data**
- **Discount Pipe**: Bank reconciliation billing dispute (Aug 2026) — reconciliation issues are common
- **Sabre Alloys**: "Fully Billed" PO status feature recently implemented (Aug 2026) — signals they were manually tracking PO invoice completion
- **3GM Steel**: Invoice data discrepancies, customer credit masking issues
- Root cause: No automated matching logic; manual payment application is error-prone

**Automation Opportunity: 75%**

*Proposed Automation:*
- **Automated payment matching** (Odoo rule or custom connector):
  - When a payment arrives (Stripe, bank transfer, check), system auto-matches to open invoices based on amount, customer, date
  - If match is clear → auto-apply payment
  - If match is ambiguous (e.g., $5,000 payment could be for 2–3 invoices) → flag for manual review with suggested matches
- **Invoice aging & credit monitoring dashboard**:
  - Daily report: invoices past due, unapplied payments per customer, credit memos awaiting application
  - Alerts if a customer has negative balance (phantom credits) for >3 days
- **Automated reconciliation report** (weekly):
  - List all unmatched invoices vs. receipts for the week
  - Flag duplicate credits, reversals, adjustments
  - Support staff review flagged items only (vs. reviewing all transactions)

*Implementation:*
- **Build time:** 40–50 dev hours (payment-matching logic, dashboard, alerting)
- **Ongoing:** 5–10 min per issue (most payments auto-match; manual review only for edge cases)
- **Payback:** (40–50 hrs dev) ÷ (1.5 hrs saved per issue × 50 issues/year) = **5–7 months**

*Estimated Annual Savings:* 65–95 hrs (labor)

---

## WORKFLOW 5: Bug Triage, Reproduction & Verification

**Current Process**
1. Support staff or customer reports bug (email/Fireflies call/task)
2. Support staff creates Odoo task with bug description (15–30 min)
3. Dev or Ron reviews task; reproduces bug in sandbox (30 min–2 hrs)
4. Dev analyzes root cause; determines if it's a code bug, data issue, or expected behavior (30 min–2 hrs)
5. If bug: Dev codes fix, tests in sandbox (1–4 hrs depending on complexity)
6. Dev submits to QA; QA verifies fix (30 min–1.5 hrs)
7. Fix deployed to live; Ron or support verifies with customer (30 min–1 hr)
8. Documentation/runbook updated if needed (30 min–1 hr)

**Frequency & Cost**
- Observed: 100+ bugs visible in wiki pages for just Sabre Alloys; 50+ for Discount Pipe; 30+ for Eastern States Steel
- Estimated: 50+ bugs/quarter across all 8 customers = 200+ bugs/year
- Average time per bug (mix of simple and complex): 2.5–3.5 hrs
- **Annual time: 200 bugs × 3 hrs = 600 hrs/year**
- Labor: Dev @ $85/hr, Ron @ $75/hr (blended ~$80/hr for triage + QA overhead)
- **Annual cost: 600 hrs × $80/hr = $48,000/year**

**Pain Points Expressed in Data**
- **Sabre Alloys**: 100+ day stall on packing list bug; multiple related bugs (Cannot Confirm PL errors) spanning months
- **Discount Pipe**: Bug backlog evident in "Requirements" stage (100+ tasks waiting for developer review); bugs like "Packing List Duplicate Lines" recur across multiple contexts
- **Eastern States Steel**: Long-standing issues (Inventory Valuation Investigation stalled 5 months)
- **Root cause**: No prioritization framework; bugs are triaged reactively; similar bugs get reopened because root-cause patterns aren't tracked

**Automation Opportunity: 40–50%**

*Proposed Automation:*
- **Automated bug categorization & deduplication** (AI or rule-based):
  - When a new bug is reported, system searches existing open bugs for keyword/module matches
  - If a similar bug exists → link them and mark as duplicate (saves 30 min–1 hr per duplicate)
  - Categorize bug by type: data-quality issue, logic bug, UI/UX issue, performance, integration
  - Route to appropriate owner (data issues → Ron/support for potential quick fix; logic bugs → dev team)
- **Automated reproduction checklist**:
  - System generates a step-by-step reproduction script (if possible) based on bug description
  - Dev confirms reproduction against script (faster than re-reading free-text description)
- **Regression test suite**:
  - After each bug fix, auto-run regression tests to catch if the fix breaks related functionality
  - Reduces back-and-forth cycles
- **Bug trend dashboard**:
  - Track bugs by customer, module, owner, age
  - Alert when a bug stalls >30 days without progress
  - Identify patterns (e.g., "packing list bugs represent 20% of all bugs; all related to multi-UOM scenarios")

*Implementation:*
- **Build time:** 80–120 dev hours (categorization rules/ML, deduplication logic, test suite integration, dashboard)
- **Ongoing:** 15–30 min per bug (instead of 2.5–3.5 hrs for mixed efficiency)
- **Payback:** (80–120 hrs dev) ÷ (1.5–2 hrs saved per bug × 200 bugs/year) = **2–3 months** (high payback)

*Estimated Annual Savings:* 350–450 hrs (labor) — mostly in triage and reproduction time

---

## WORKFLOW 6 (Bonus): Report Configuration & Filter Management

**Current Process (Minimal Automation Data, High Pain Signal)**
1. Customer requests custom report or wants to persist report filters (email request)
2. Support staff investigates: Is this a standard report? Can filters be saved? (15–30 min)
3. If custom: Support staff or dev builds report/dashboard (2–8 hrs)
4. Customer tests and requests tweaks (1–3 hrs of iteration)
5. Support staff documents custom report location and usage (30 min–1 hr)

**Frequency & Cost**
- Observed: Multiple reporting requests from Discount Pipe (filter persistence, balance sheet sign display, margin/GP options), Eastern States Steel (P&L period filters, multi-location consolidation), Sabre Alloys (quarterly comparison, log-note count reports)
- Estimated: 10–15 custom report requests/year × 3–4 hrs per request = 30–60 hrs/year
- Labor: Dev @ $85/hr
- **Annual cost: 30–60 hrs × $85/hr = $2,550–5,100/year**

**Automation Opportunity: 60%**

*Proposed Automation:*
- **Self-service BI builder** (Metabase, Tableau, Looker, or native Odoo dashboard builder):
  - Customers or power-users build ad-hoc reports without dev involvement
  - Drag-and-drop interface: select fields, set filters, choose visualization
  - System auto-enforces data permissions (users can't see reports with restricted data)
- **Filter persistence** (native Odoo feature):
  - Ensure customer filter settings are saved across sessions (appears to be a bug/gap currently)
- **Pre-built report templates** (20–30 common reports):
  - Sales by customer, by product, by salesperson
  - Profit/loss, balance sheet, aging, cash flow
  - Inventory valuation, on-hand vs. reserved
  - Customers clone and customize instead of requesting dev

*Implementation:*
- **Build time:** 40–60 dev hours (BI tool integration or Odoo dashboard builder setup, permission model, template creation)
- **Ongoing:** 0 hrs (customers self-serve) or 30 min per complex template request
- **Payback:** (40–60 hrs dev) ÷ (3 hrs saved per report × 12 reports/year) = **10–15 months**

*Estimated Annual Savings:* 20–50 hrs (labor)

---

## Summary Table: Workflow Automation ROI

| Workflow | Time Burn/Year | Automation % | Dev Cost (hrs) | Annual Savings (hrs) | Payback (months) | Priority |
|----------|----------------|--------------|----------------|----------------------|------------------|----------|
| Access Rights | 54–96 hrs | 80% | 40–60 | 43–77 | 8–10 | HIGH |
| Product Master | 160–240 hrs | 70% | 50–70 | 112–168 | 3–4 | **CRITICAL** |
| Packing List Errors | 210–280 hrs | 50% | 60–80 | 105–140 | 4–5 | **CRITICAL** |
| Invoice Reconciliation | 70–105 hrs | 75% | 40–50 | 52–79 | 5–7 | HIGH |
| Bug Triage | 600 hrs | 45% | 80–120 | 270–360 | 2–3 | **CRITICAL** |
| Report Builders | 30–60 hrs | 60% | 40–60 | 18–36 | 10–15 | MEDIUM |
| **TOTALS** | **1,124–1,581 hrs** | **~60% avg** | **310–440** | **600–860 hrs** | **3–6 avg** | |

---

## Implementation Roadmap (Phased)

**Phase 1 (Months 1–2): High-Impact, Low-Risk**
- Workflow 5 (Bug Triage automation): Highest payback (2–3 months), cleanest ROI
- Workflow 3 (Packing List pre-validation): Unblocks Sabre & Discount Pipe, reduces Ron's load significantly

**Phase 2 (Months 3–4): High-Leverage**
- Workflow 2 (Product Master import portal): Addresses product-catalog sprawl, high volume
- Workflow 1 (Access Rights portal): Removes Ron bottleneck, enables scaling

**Phase 3 (Months 5–6): Quality-of-Life**
- Workflow 4 (Invoice Reconciliation automation): Stable, lower risk; good to do once higher-impact work is underway
- Workflow 6 (BI/Report builder): Medium payback; can be outsourced or phased

**Total investment:** 310–440 dev hours (~$25–37K at $80/hr blended rate)
**Total annual benefit:** 600–860 hrs saved (~$48–69K in reduced labor)
**Net payback:** 3–6 months
**Ongoing monthly benefit:** 50–72 hrs freed up per month for higher-leverage work

---

## Critical Success Factor

**Ron is the current single point of failure.** He owns access provisioning, packing-list triage, escalation handling, and customer relationship management. Automating workflows 1–3 directly unblocks Ron and lets him scale to higher-leverage work (strategy, customer expansion, implementation planning).

Recommendation: **Prioritize workflows that remove Ron bottlenecks (1, 3, 5) first.** Then tackle product-master scaling (2). This sequence also optimizes learning (automation infra is reusable across workflows).
