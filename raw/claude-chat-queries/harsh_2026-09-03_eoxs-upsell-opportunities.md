---
thread_name: "eoxs-upsell-opportunities"
user: "harsh"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

## EOXS Customer Upsell Opportunity Analysis

### User Request
Identify existing customers who may have opportunities for upselling or cross-selling based on their current relationship, products, or usage. Explain why each customer is a potential opportunity.

Scope: EOXS features only (not AskCruz or other products)
Customers: All 8 EOXS customers
Signals: Implementation health, pain points, relationship strength, business growth — equal weight on all

Depth level: 50ft deep

---

## FULL 50FT DEEP ANALYSIS

### 1. SABRE ALLOYS ⭐ Highest Priority

**Implementation & Relationship Health**
Sabre is the flagship account and strategic priority. 200 implementation tasks across 2+ years (soft launch Apr 2024), 1,443 emails, 113 calls. Direct engagement with Rajat (weekly calls mid-2026 labeled "EOXS – Juan & Raj"). Zero distance to decision-making.

**Engagement Signals**
Recent activity is heavy and high-touch: AskCruz proposals (Aug 13, Sep 2), "Toll Processing Business Discussion & AskCruz AI Discussion" (Sep 2), "AI Transformation Proposal" (Aug 13). Claude AI access provisioned for two internal users (Sep 1). This is an active growth conversation.

**Pain Points & Gaps**
- 100+ day stall on "Fix Packing List Module Behavior" (completed Jun–Aug 2026) — packing list errors recurring, high-friction manual workarounds.
- Inventory valuation issues tied to landed cost calculations (multi-line receipts, thickness-based distribution errors).
- Manual gross profit recalculation project ongoing since Sept 2025 — they're calculating margins by hand because the system doesn't automate it.
- Processing order errors recurring (PR7560, PR7400, PR7386, PR7320, PR7148 series in Aug 2026) — weight/UOM mismatches on blanking operations.
- "Fully Billed" PO status feature requested and recently implemented (Aug 2026) — signals they want better cash-flow/payment visibility.
- Freight charges reminders, landed cost distribution, UOM mismatches across receipt/PO/SO — supply chain complexity they're managing manually.

**Growth Signals**
- Toll processing business expansion underway (Sep 2 call topic). This is a new revenue stream requiring new workflows.
- Requesting log-note counting per salesperson per day — they're tracking salesperson productivity/metrics.
- Quarter-over-quarter financial report comparison requested (Aug 2026) — planning/forecasting mode.
- Security incident (hack; legal case evidence sent Sep 2026) — trust is maintained despite breach.

**Upsell Opportunities**

1. **Advanced Reporting & Analytics Module** — They're manually calculating margins, running QoQ financial comparisons, tracking salesperson log-note volume. A BI/reporting layer (KPIs, dashboards, drill-down analysis) would eliminate manual work and unlock insights. High ROI given their operational complexity.

2. **Landed Cost Optimization & Supply Chain Visibility** — Multiple landed cost bugs tied to multi-line-item, multi-UOM receipts. A module that handles cost allocation rules (thickness-based, weight-based, line-item-based) + supplier scorecarding would address their pain and reduce data-entry errors.

3. **Toll Processing Workflow Module** — They're expanding into toll processing (new business line). Build them a module for third-party processing orders, toll pricing, co-packing workflows, material tracking. Lock in the expansion revenue.

4. **AI-Powered Inspection & Quality Assurance** — Processing order errors recurring due to weight/UOM/specification mismatches. AI-driven pre-validation on processing orders (check UOM alignment, flag weight outliers, validate spec combinations) would prevent manual rework. Position this as AskCruz-adjacent.

5. **Margin Management & Profitability Automation** — They've been manually recalculating SO margins for 11+ months. Automate SO gross-profit calculation tied to landed costs, freight, processing labor. Make margin part of the quote-to-order workflow.

**Readiness Score: 9/10** — They're actively discussing AI/AskCruz. Multiple feature requests being built. High engagement. Gap in automation and analytics is clear and painful.

---

### 2. DISCOUNT PIPE & STEEL ⭐ High Priority

**Implementation & Relationship Health**
Mature go-live (Jan 2025 implied by email density), but high-friction operations. 231 implementation tasks, 642 emails, 63 calls. Multiple third-party partners involved (Alt Digital AI consultants Tina Valdez, Jamie Vernon). Ron J is primary escalation contact. Heavy operational load on support.

**Engagement Signals**
Aug 18 check-in titled "ROI Concerns & Push Toward Client-Side Delegation" — explicit signal they're frustrated with cost-of-operations and want to shoulder more themselves. Aircall & Stripe integration tasks stalled for months (escalated Jun 2026). High velocity of bugs and feature requests but slower resolution.

**Pain Points & Gaps**
- Recurring packing-list bugs (quantity discrepancies, tag mapping errors, weight mismatches) causing operational blocks. Multiple tasks spanning Mar–Aug 2026.
- Inventory reservation conflicts and double-selling risks (multiple recent failures). Reservation logic changes in Aug 2026 broke auction-sale pricing workarounds.
- CRM contact merge failures (silent failure, manual merge required).
- Control-tag accuracy issues across sales orders, transfers, packing lists.
- Reporting filter persistence not working as expected (Aug 2026 — marked done, then contradicted).
- External integrations stalled (Aircall video, Stripe video — "unanswered for over a month").
- Refunds/returns capability gap identified.
- Bank reconciliation billing dispute (Aug 2026).

**Growth Signals**
- New warehouse added (Jul 2026 email: "New Warehouse").
- Inventory expansion and complexity (tag-based operations on auction sales, blanking lines).
- Discussion of operations blockers escalation (Aug 2026) — they're pushing for external load-check tool and MCP connector write-access (they want to build integrations themselves).
- Multiple user seat requests and access-rights changes (new users, new roles).

**Upsell Opportunities**

1. **Advanced Inventory & Warehouse Management Module** — They're managing multiple warehouses, tag-based operations, auction tagging, and control-tag accuracy is a known blocker. A module with multi-location support, bulk tag operations, lot tracking, auto-reservation rules would reduce manual workarounds and errors.

2. **Quality Assurance & Packing Validation Module** — Packing-list bugs are systemic and high-cost. A pre-shipment validation layer (verify weight/piece count, flag tag mismatches, confirm address accuracy) would catch errors before they ship and reduce returns/disputes.

3. **Refunds & Returns Management Module** — Identified as a capability gap. Build them a returns workflow (receipt, inspection, credit/rework decision, inventory reintegration).

4. **Integration Platform / MCP Connector Toolkit** — They explicitly requested write-access to build their own integrations. Offer them a low-code integration builder (Zapier-style) or native MCP connector templates for their priority integrations (external load-check, internal systems). Position as "delegation automation" — lets them build without EOXS dev.

5. **Reporting & Business Intelligence Suite** — Multiple reporting requests (filter persistence, cash reporting, margin/gross-profit menu options). A BI layer + self-service dashboard builder would unlock insights without custom dev.

6. **Bank Reconciliation & Cash Management Module** — Bank reconciliation billing dispute is live. Reconciliation is a core pain point. Offer a dedicated cash-reconciliation module with auto-matching and exception handling.

**Readiness Score: 7/10** — They're operationally mature but frustrated. Multiple feature requests, but integration stalls signal bandwidth/roadmap conflict with EOXS. "ROI concerns" comment suggests price sensitivity; position upsells as efficiency/automation plays, not complexity adds.

---

### 3. EASTERN STATES STEEL ⭐ High Priority

**Implementation & Relationship Health**
Live implementation (soft launch Dec 2025), 225 implementation tasks, 82 calls. Active engagement during soft-launch period (Dec 2025–early 2026) with multiple sales module "Soft Launch" calls. Recent activity (Aug 2026) shows ongoing requests and support.

**Engagement Signals**
Aug 6, 2026 "Brainstorming" call — exploratory, open-ended. Recent new-user onboarding (Sam Stroman, Aug 2026) signals team growth. Two new warehouse requests filed (Nucor – Decatur AL, Obsidian Metal Processing – New Madison OH, both Aug 27). System slowdown reported Aug 21 — platform scaling concern.

**Pain Points & Gaps**
- Inventory valuation investigation stalled pending full physical inventory (Apr–Sep 2026) — a blocker holding up financial close.
- Multiple weight/dimension display and mapping errors (incorrect width on printed tags, wrong weight on BOL, incorrect actual weight).
- Control-tag accuracy issues (allocation field, packing sync, merge conflicts).
- Processing errors and landed-cost blocking issues.
- CRM auto-creation disabled (they turned it off) — they don't want auto-contact creation.
- Sales order workflow complexity (multiple filter requests, field visibility, delivery address management).
- System performance concerns (slowdown reported, new warehouses may worsen).

**Growth Signals**
- Team expansion (new employee Sam Stroman being onboarded).
- Multi-warehouse expansion underway (two new warehouse locations being added Aug 27).
- Inventory valuation investigation suggests they're doing a formal audit/reconciliation (financial close prep).
- Brainstorming call suggests exploration of new features/use cases.

**Upsell Opportunities**

1. **Multi-Location Warehouse Management & Logistics Module** — They're adding two new warehouse locations. A dedicated module for warehouse configuration, shipping-from-location rules, inter-warehouse transfers, and carrier integration would support the expansion and reduce manual coordination.

2. **Inventory Valuation & Physical Inventory Reconciliation Module** — Valuation investigation stalled for 5 months. Provide a guided physical inventory workflow (cycle-counting, tag generation, variance investigation, accounting integration). Unlock their financial close process.

3. **Performance Optimization & System Scaling Services** — System slowdown reported. Offer performance tuning, database optimization, or a "scale-ready" infrastructure review as they add users/warehouses.

4. **Advanced Reporting & Financial Consolidation** — Multiple reporting requests (P&L period filters, balance sheet sign display, multi-location consolidation). Offer a BI layer with multi-location roll-up reporting.

5. **Workflow Automation & Sales Order Configuration** — Multiple sales order field-visibility requests, delivery address filtering, menu customization. Offer a low-code workflow builder that lets them hide/show fields, set defaults, and trigger actions without dev work.

6. **Logistics & Bill-of-Lading Module** — BOL weight-mapping errors and Zdesigner printer issues suggest they need better control over shipping docs. Offer a logistics module with carrier integration, BOL generation, and label printing orchestration.

**Readiness Score: 7.5/10** — They're operationally mature with active growth (team, locations). Pain points are clear (valuation, performance, logistics). Brainstorming call signals openness to expansion.

---

### 4. BRANNON STEEL ⭐ Medium-High Priority

**Implementation & Relationship Health**
In-flight implementation, no Odoo base URL yet (likely still in sandbox or pre-launch). 29 calls since early 2026 (weekly huddles Mar–Aug 2026). Zero implementation tasks recorded (suggests tasks managed elsewhere or not yet populated). Ron J owns the implementation huddles. High-cadence engagement.

**Engagement Signals**
Weekly "Implementation Huddle || Brannon Steel" calls every Tuesday from Feb-Aug 2026 (at minimum 10+ calls). MTR AI project is the focus (Material Test Report AI functionality). Multiple cancellations/reschedules Jan–Feb 2026 suggest early-stage friction, but cadence stabilized by Mar.

**Pain Points & Gaps**
- MTR AI implementation is active but cadence/status unclear from call titles alone. Wiki pages reference "Algoma Join Report (Live) & Pre-Purchase MTR–Spec Verification (Proposed)" — suggests some pieces live but feature set incomplete.
- MTR Inventory Module escalation vs. ticket status conflict documented.
- Samples workflow (task thread active).
- They're in heavy implementation mode; likely dozens of small asks accumulating.

**Growth Signals**
- MTR AI project represents new functionality (materials testing automation). This is a capability expansion beyond basic ERP.
- Consistent weekly engagement (huddles stayed scheduled despite some cancellations) signals committed implementation.
- 5+ key contacts engaged (David Brannon, Kevin Brannon, Manish Trivedi, Ranim Fallaha).

**Upsell Opportunities**

1. **Accelerated Implementation Services & Change Management** — They're mid-implementation with weekly huddles. Offer structured implementation acceleration (sprint-based delivery, change management, user training modules) to reduce time-to-value and unlock go-live sooner.

2. **MTR (Material Test Report) Advanced Features Module** — They're building MTR AI; offer pre-built MTR workflows, automated spec verification, certificate-of-conformance generation, lab-integration connectors. Position as "post-launch enhancements."

3. **Quality Assurance & Inspection Workflows** — MTR is quality-centric. Offer broader QA module (incoming inspection, in-process quality gates, SPC charting) that extends their MTR investment.

4. **Training & Documentation Module** — Heavy implementation phase is a good time to sell structured training (video library, knowledge base, role-based learning paths). Reduces support load post-launch.

5. **Data Migration & Inventory Startup Services** — MTR inventory module is in-flight. Offer specialized services for high-quality data migration and inventory master-data setup.

**Readiness Score: 8/10** — They're actively implementing and engaged weekly. Time-to-value concerns are real (implementation overhead). Upsells that reduce friction or accelerate launch will land well.

---

### 5. PPC METALS ⭐ Medium Priority

**Implementation & Relationship Health**
Live (Oct 2025), stable operations. 29 implementation tasks (mostly completed or in maintenance). 450 emails, 30 calls. Go-live was intense (Oct 2025 had 10+ "Go Live" calls in rapid sequence), now transitioned to maintenance mode. Last major call Mar 3, 2026 ("Sales Pricing & Open Ticket Review").

**Engagement Signals**
Low recent call volume (last call Mar 2026; now Sep 2026 — 6-month gap). Email activity is sporadic (product variants, packing slip issues, piece-count rounding bugs, disconnection issues). Suggests they're stable but occasional issues bubble up.

**Pain Points & Gaps**
- Recurring disconnection issues ("Trying to Reconnect" error, Aug 2026) — system stability/performance concern.
- Packing slip weight discrepancies (traced to manual receiving edit, Aug 2026).
- Product variant defaults wrong (Rectangle vs. Round, Aug 2026).
- Line-number issues (recent email).
- Multiple reservations on same tag conflict handling (task completed Jun–Aug).
- Cost-per-LB and inventory valuation concerns (Tag 101918, Jun–Aug 2026).
- Piece-count rounding and tab-key interference on SO lines (Mar 2026).

**Growth Signals**
- Commissioning a new salesperson (external sales team mentioned in 2024 calls).
- Ongoing product variant management and refinement.
- Packing operations expanding/changing (weight discrepancies suggest volume growth).

**Upsell Opportunities**

1. **System Stability & Performance Monitoring Module** — Recurring disconnection issues are a friction point. Offer a monitoring/alerting layer (uptime tracking, latency alerts, user session health) or dedicated support package (priority incident response).

2. **Advanced Packing & Shipping Operations Module** — Packing slip bugs are recurring. Offer a dedicated packing module with weight validation, lot reconciliation, and carrier integration.

3. **Inventory Accuracy & Quality Assurance Module** — Product variant defaults, tag cost corrections, and piece-count rounding suggest data-quality issues. Offer a QA workflow (tag audit, cost validation, variant verification) and bulk-correction tools.

4. **Processing Optimization & Labor Tracking** — They have processing operations. Offer a processing module with labor tracking, time-studies, and efficiency metrics.

5. **Preventive Support / Health Check Services** — 6-month communication gap followed by bug reports suggests reactive posture. Offer quarterly business reviews, health checks, and proactive optimization.

**Readiness Score: 5/10** — They're stable but not actively growing. Low engagement suggests they're content with current state. Upsells should target stability/optimization, not new capabilities. Position as "risk reduction" or "efficiency" plays.

---

### 6. OHIO STRIP STEEL (GREER) — Medium Priority

**Implementation & Relationship Health**
Mature, stable customer (go-live ~2023–2024 based on task dates). 106 implementation tasks (mostly completed). 278 emails, 23 calls. Low recent activity; last meaningful call Aug 10, 2026 ("Ask Cruz: Intro Call"). No wiki pages documented (unusual — suggests older customer predating wiki system, or inactive documentation).

**Engagement Signals**
Aug 10 AskCruz intro call signals openness to new products. Multiple 2025 calls around module features (KPI Module Discussion Aug 2025, Document Module Review Aug 2025, etc.). Recent email activity is minimal (June–Aug 2026 mostly internal or admin).

**Pain Points & Gaps**
- "Region free text" request (open, Jan 2025) suggests workflow customization needs not yet met.
- "Base code" task stalled (assigned Nov 2024, no resolution noted).
- KPI module discussion (Aug 2025) but no implementation task visible — suggests interest but lower priority.

**Growth Signals**
- Company rebranding (Greer Steel → Ohio Strip Steel, Aug 2026 noted in profile).
- KPI/scoreboarding interest (discussed Aug 2025) — suggesting they want business intelligence.
- Document module interest (Aug 2025) — workflow/knowledge management expansion.
- AskCruz intro call — exploring AI/analytics.

**Upsell Opportunities**

1. **KPI Dashboard & Business Intelligence Module** — They discussed KPI module in Aug 2025 but no implementation followed. Build them a dashboard layer (sales metrics, operational KPIs, margin analysis). Align with recent AskCruz interest.

2. **Document Management & Workflow Module** — Document module interest (Aug 2025). Offer a centralized document repository, approval workflows, and version control.

3. **Advanced Sales Analytics & Forecasting** — Rebranding suggests organizational refresh. Offer sales pipeline analytics, win/loss analysis, and forecast modeling to support growth planning.

4. **Region Configuration & Sales Territory Module** — Open task on "region free text" suggests they want flexible region management. Offer a territory-management module tied to sales tracking and commission rules.

**Readiness Score: 4/10** — They're stable and mature but low-engagement. Interest in KPI/document modules is there but not urgent. Upsells should emphasize strategic value (growth planning, rebranding support). Timing: follow up post-AskCruz conversation.

---

### 7. 3GM STEEL — Medium Priority

**Implementation & Relationship Health**
Live (2022 go-live from kick-off dates), stable operations. 33 implementation tasks, 955 emails, 14 calls. Heavy email activity (most recent is product variant additions Aug 31). Travis Lane is primary contact (Sales); Jessica Worley (Accounting).

**Engagement Signals**
Aug 12, 2026 AskCruz proposal call titled "3GM - AskCruz Proposal" — Travis Lane confirmed deal at reduced scope (2-user, shorter term). This is a closed deal (already signed). Multiple recent product variant and bug-fix activities (Aug 31 product variant additions, coil search/availability bugs, invoice customer credits).

**Pain Points & Gaps**
- Coil search/availability bug on tonnage card (open since Jun–Sep 2026).
- Phantom/duplicate customer credits blocking invoice payment application (Sep 1, 2026).
- Recurring product variant catalog additions (3+ instances Aug 24–Sep 1) suggest ongoing catalog management burden.
- Access rights escalation needed (Matt Inman elevated to match Jessica Worley, Aug 2026).
- IRIS AI historical data preload (Aug 2026) — they're using AI features or preparing for them.

**Growth Signals**
- Product variant management expanding (frequent additions suggest growing SKU base or new product lines).
- Access rights expansion (new power-user onboarded).
- Bug reports show active usage of complex features (coil search, tonnage cards).
- AskCruz deal closed at reduced scope — may expand later.

**Upsell Opportunities**

1. **Product Master & Catalog Management Module** — Frequent variant additions and catalog changes are manual. Offer a product-data-quality module (bulk import, variant creation templates, hierarchy management, obsolescence workflows).

2. **Advanced Inventory & Coil Management** — Coil search/availability bugs suggest they need better coil-specific workflows. Offer a module with coil tracking, dimensional search, lot availability, and allocation rules.

3. **Invoice & Credit Management Module** — Phantom customer credits are blocking invoicing. Offer a credit-memo and invoice-adjustment module with reconciliation workflows.

4. **AI-Powered Search & Recommendations** — IRIS AI preload signals they're open to AI. Offer AI-powered smart search (find coils by dimensions/grade), demand forecasting, or pricing optimization tied to AskCruz.

5. **User Training & Enablement** — Access rights escalation suggests team growth. Offer structured training (video library, role-based learning, certification program).

**Readiness Score: 6/10** — They're operationally stable with AskCruz already closed (foothold for upsells). Pain points are clear (product data, invoice accuracy). Upsells should be bundled with AskCruz conversation or positioned as "workflow optimization" alongside AI rollout.

---

### 8. RW CONKLIN STEEL ⚠️ Re-engagement Opportunity

**Implementation & Relationship Health**
Stalled/dormant customer. No Odoo base URL (not live). Zero implementation tasks. 166 emails (last activity Jan 2025), 19 calls (last in Mar 2025). Wiki pages reference "Contract Dispute & Near-Cancellation." This customer was in implementation but paused/stalled.

**Engagement Signals**
Feb–Mar 2025 calls around "Software Upgrade" (Product Master, Processing Module, Accounting, Inventory). Last call Mar 17, 2025 "Inventory review in EOXS." No calls or emails since. Radio silence for 6+ months (now Sep 2026).

**Pain Points & Gaps**
- Contract dispute and near-cancellation history suggests pricing/scope conflict.
- Implementation stalled pre-launch (no Odoo base URL).
- Unclear what caused the halt — could be internal prioritization, budget, or dissatisfaction.

**Growth Signals**
- None visible in recent data.

**Recommendation: Re-engagement/Opportunity Assessment**
This is not an upsell opportunity yet. This is a customer-health intervention.

**Action Plan:**
1. Executive check-in (Rajat or Ron) to understand stall reason: budget constraint, internal project delay, or dissatisfaction?
2. If budget: offer scaled-down launch (minimal scope, phased go-live) to reduce upfront cost.
3. If scope/priority: offer implementation acceleration or fixed-cost launch package.
4. If dissatisfaction: conduct needs-assessment call to identify gaps and rebuild confidence.
5. Do not upsell until customer is back to active status.

**Readiness Score: 1/10** — This is a save/recovery, not a growth play.

---

## SUMMARY: Upsell Prioritization Map

| Customer | Readiness | Upsell Fit | Primary Opportunity |
|----------|-----------|-----------|---------------------|
| Sabre Alloys | 9/10 | High | Advanced Reporting + Toll Processing Module |
| Brannon Steel | 8/10 | High | Accelerated Implementation + MTR Features |
| Discount Pipe & Steel | 7/10 | High | Warehouse Mgmt + QA + Integration Platform |
| Eastern States Steel | 7.5/10 | High | Warehouse Mgmt + Inventory Valuation |
| 3GM Steel | 6/10 | Medium | Product Master + Inventory Mgmt |
| PPC Metals | 5/10 | Medium | Stability Services + Packing Module |
| Ohio Strip Steel | 4/10 | Low | KPI Dashboard (post-AskCruz) |
| RW Conklin Steel | 1/10 | Re-engagement | Needs re-assessment first |

**Immediate High-Value Actions:**
1. Close Sabre on reporting/analytics + toll-processing module (highest readiness + highest contract value).
2. Finalize Brannon implementation acceleration (unblock go-live, then upsell post-launch features).
3. Pitch Discount Pipe on warehouse + QA modules (clear pain + team openness to tooling).
