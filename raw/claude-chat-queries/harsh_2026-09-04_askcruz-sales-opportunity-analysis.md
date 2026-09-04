---
thread_name: "askcruz-sales-opportunity-analysis"
user: "harsh"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

# Ask Cruz Sales Opportunity Analysis

**User Request:** Perform a data-driven sales opportunity analysis across all connected EOXS MCPs. Start by reviewing every relevant prospect card in the CRM, including company information, notes, requirements, activity history, previous interactions, and buying signals. Next, build a complete understanding of Ask Cruz as a product, including its capabilities, target use cases, problems it solves, and value proposition. Map each prospect's needs and pain points against Ask Cruz's capabilities, including indirect or non-obvious matches. Rank the top 10 prospects based on product fit, business need, urgency, buying signals, and potential value. For each prospect, provide the evidence supporting the recommendation, the specific Ask Cruz use case, the likely business benefit, relevant decision-maker or company information if available, and a recommended next step for the sales team. Also identify any additional insights across the MCPs that could help improve prospecting strategy.

---

## Analysis Output

# **ASK CRUZ: TOP 10 SALES OPPORTUNITIES — RANKED ANALYSIS**

## **RANKING METHODOLOGY**

Each prospect was scored on:
- **Product Fit** (relevance of Ask Cruz's four capabilities to their documented business needs)
- **Business Need Urgency** (evidence of pain around knowledge access, order management, or operational visibility)
- **Buying Signals** (recent calls, emails, implementation activity, AskCruz mentions)
- **Business Value** (deal size, complexity, multi-user potential)
- **Implementation Readiness** (existing EOXS deployment, data quality, stakeholder engagement)

---

## **#1: SABRE ALLOYS** | *Highest Priority — Active Proposal Stage*

**Company Profile:** Multi-division steel processor ($13M+ annual revenue, 15 employees, 76 customer rank). Operates slitting, coil-to-length (CTL), and blanking. Heavy ERP user with 200+ implementation tasks.

**Product Fit:** ⭐⭐⭐⭐⭐
- **Company Brain:** 113 calls, 1,444 emails, 200+ active Odoo tasks reveal scattered operational knowledge. "What did we promise this customer?" and "Which orders need attention?" are exactly Company Brain use cases.
- **Company Hands:** Michael Mercadante flagged quote-drafting efficiency gaps (Jun 2026). Complex pricing (landed cost, freight, processing variances) matches Quote drafting + pricing-logic use case.
- **Digital Workforce:** Multiple blanking processing errors (PR7148, PR7320, PR7386, etc.) suggest need for standing order-risk monitoring.
- **Company Personalization:** Toll Processing is a new revenue stream requiring company-specific pricing/workflow knowledge capture.

**Buying Signals:** 
- Sep 2, 2026: "Toll Processing Business Discussion & AskCruz AI Discussion" call with Juan Deshon and Rajat
- Aug 13, 2026: "Sabre Alloys - AI Transformation Proposal" call
- Aug 11/04/Jul 21/14/7/Jun 18: Recurring "EOXS - Juan & Raj" meetings (6+ calls in 8 weeks)
- Sep 1, 2026: Claude AI Access provisioned for Juan and Tye
- Sep 3, 2026 wiki entry: "AskCruz Proposal Resent to Sabre Alloys With Aug 13 & Sep 2 Call Recaps — New Stakeholder, Toll-Processing Side Deal, Data-Privacy Pushback"

**Business Value:**
- Existing $13M+ revenue base; highest customer rank (76)
- 33 orders, 34 invoices in system = established operational volume
- New Toll Processing division = expansion TAM
- Multi-stakeholder (Juan, Tye, Michael, Charles, Ernie) = multi-user ARR opportunity

**Blockers & Mitigation:**
- Data-privacy pushback noted in Sep 3 wiki (likely around including third-party call/email data)
- *Mitigation:* Emphasize Company Brain's role-aware access tiers (tier1/tier2) and offline-first operational knowledge (orders, pricing, margins)

**Likely Use Case:**
1. **Account Prep** — Juan/Tye prepare for customer calls with "What was promised?" and "What's the margin on this order?"
2. **Quote Drafting** — Support for Toll Processing pricing, leveraging company-specific landed cost logic
3. **Order Triage** — Monitor processing queue, flag orders at risk of missing promise dates

**Recommended Next Step:**
Schedule a 45-minute "Ask Cruz Operational Demo" with Juan & Tye, focused on (1) order-risk monitoring (show sample processing order with risk flag), (2) quote-draft workflow for Toll Processing, (3) confirm data-privacy assumptions. Goal: move from proposal to signed pilot by end of September.

---

## **#2: 3GM STEEL** | *Strategic First Client — Already Contracting*

**Company Profile:** Steel processor ($10M annual revenue, 15 employees, 44 customer rank). Already signed 6-month pilot proposal (Aug 20, 2026) for Claude-powered Company Brain + EOXS integration. Currently awaiting Microsoft 365 admin consent for email sync.

**Product Fit:** ⭐⭐⭐⭐⭐
- **Company Brain:** Email integration (12 months back) + Odoo EOXS integration already contracted = knowledge foundation is *contractually required*
- **Company Hands:** Prompt History and Historical Data deferred to Year 2; scope focuses on "Company Brain (Claude trained on 3GM workflows + continuous email sync) + EOXS integration"
- **Company Personalization:** 3GM's pricing and workflow practices are central to first client implementation

**Buying Signals:** ⭐⭐⭐⭐⭐
- Signed LOI (Aug 20, 2026); pilot scope + pricing established
- Two pilot users identified (Travis Lane, Stefan Brown)
- Internal infrastructure ready (staging on DigitalOcean, stood up Aug 14)
- M365 admin consent (current blocker) is administrative, not strategic
- Communication channel established (ron@askcruz.com for customer email)

**Business Value:**
- First external Ask Cruz client = reference case + revenue [restricted: amount]
- Proof-of-concept de-risks Ask Cruz for broader sales pipeline
- 6-month pilot with "affirmative decision point" (no auto-rollover) incentivizes results delivery
- Email integration + Claude training = high-engagement model (vs. light integration)

**Blockers & Mitigation:**
- **Critical:** Microsoft 365 admin consent for read-only mail app OAuth (one-time, then sign-in links sent)
- **Status:** All client prerequisites met (Claude Pro accounts active, Outlook confirmed, 12-month history available)
- *Mitigation:* Assign single point-person to push M365 admin; offer IT configuration help if needed; target consent within 7 days to hit staging-to-production window

**Likely Use Case:**
1. **Company Brain deployment** — Email ingestion + Odoo sync → knowledge base training
2. **User-facing query interface** — Travis & Stefan ask routine business questions ("What did we promise this customer?")
3. **Operational dashboards** — Summary reports for management visibility
4. **Proof of value** — Measure time saved, decision quality, onboarding speed for new users

**Recommended Next Step:**
Assign a dedicated AskCruz Implementation Lead to own 3GM through production go-live. Weekly sync with Travis/Stefan to confirm email ingestion, staging validation, and go-live readiness. Goal: production deployment by Oct 1, 2026 to capture 1.5-month pilot runway before 30-day decision-point notice requirement.

---

## **#3: GREER STEEL COMPANY** | *Warm Lead with Documented Demand*

**Company Profile:** Steel service center ($1.07M+ annual revenue, 44 employees, 33 customer rank). VP of Sales Joe Brom explicitly requested AI-assisted contract quotes (Oct 2024). Existing EOXS customer with 18 orders, 16 invoices.

**Product Fit:** ⭐⭐⭐⭐
- **Company Hands (Quote Drafting):** Joe Brom's Oct 2024 email requesting "Contract quotes" automation is a direct Company Hands use case. Ask Cruz can draft quotes using company pricing logic.
- **Company Brain:** 18 orders indicate operational history; access to previous quotes, customer terms, and pricing exceptions would support Joe's workflow.
- **Company Personalization:** Greer's specific contract structure and margin targets can be reflected in Ask Cruz

**Buying Signals:** 
- Oct 2024: Joe Brom's documented "Contract quotes" feature request to EOXS
- Jul 28, 2026: Last order (most recent activity date = 60+ days ago, but not cold)
- Internal EOXS notes mention "Greer Steel 'KPI Module Discussion' invite" (Aug/Sep 2025) = ongoing engagement

**Business Value:**
- Joe Brom (VP Sales) = decision-maker direct access
- Greer's contract sales model (vs. spot sales) = high-value, complex-pricing use case
- Likely 3–5 primary users (sales team)
- Potential for deeper EOXS module expansion (KPIs mention suggests openness to tools)

**Implementation Readiness:** High — existing EOXS customer; data and infrastructure already in place.

**Likely Use Case:**
1. **Quote Drafting** — Greer's sales team uses Ask Cruz to draft contract quotes with company-specific pricing, terms, and margin guardrails
2. **Order Context** — Before Joe calls a customer, Ask Cruz surfaces previous orders, commitments, pricing history
3. **Margin Monitoring** — Company Brain answers "Why did this contract margin drop?" by correlating historical data

**Recommended Next Step:**
Outreach to Joe Brom (jfishel@greersteel.com) with a focused demo: "We built the contract-quote automation you asked for in Oct 2024 — here's how Ask Cruz works for your sales process." Schedule a 30-minute demo + discovery call focused on Greer's contract pipeline and pricing rules. Goal: close-of-quarter pilot proposal.

---

## **#4: EASTERN STEEL SALES** | *Multi-Division Complexity + IRIS Interest*

**Company Profile:** Multi-division steel distributor ($983K+ annual revenue, 22 customer rank). Operates with supply-chain complexity (implied by "Soft Launch" materials).

**Product Fit:** ⭐⭐⭐⭐
- **Company Brain:** Multi-division operations = scattered knowledge across Shipping, Sales, Operations; Ask Cruz centralizes "Which division owns this customer?" and "What's our margin by division?"
- **Company Hands:** Multi-location order fulfillment and inventory coordination = order-risk and fulfillment-readiness use cases
- **Digital Workforce:** Multi-division interdependencies suggest value in monitoring order-status exceptions across divisions

**Buying Signals:**
- "Eastern States Steel 'Implementation Huddle'/'Soft Launch' acceptances (Aug–Sep 2025)" = formal engagement in EOXS onboarding wave
- Wiki entry "Eastern States Steel — Soft Launch" documents active implementation effort
- EOXS notes mention "IRIS interest" (EOXS's advanced financial module) = customer is actively expanding toolset
- Recent contact: info@EasternStatesSteel.com + phone (610.275.3375) active

**Likely Use Case:**
1. **Cross-Division Account View** — Ask Cruz surfaces which division holds a customer relationship, previous orders across divisions, interdependencies
2. **Inventory Visibility** — Multi-location free-to-sell calculations (accounting for inter-location commitments)
3. **Financial Reporting** — Margin analysis by division; supports IRIS adoption

**Recommended Next Step:**
Leverage IRIS relationship as entry point. "Your IRIS implementation is capturing detailed financial data — Ask Cruz can make that data operationally useful for sales and fulfillment teams. Let's schedule a 30-min discovery on multi-division order-fulfillment challenges." Target: Q4 pilot proposal.

---

## **#5: PPC SPECIALITY METALS** | *Engagement Momentum + Quote Complexity*

**Company Profile:** Specialty metals distributor ($705K+ annual revenue, 19 customer rank, active contact Eddie@ppcmetals.com). 14 orders, 14 invoices.

**Product Fit:** ⭐⭐⭐
- **Company Brain:** "What was this customer's last order?" and "What margin are we carrying on this account?" are directly supported
- **Company Hands:** Specialty metals = premium pricing, custom specs; quote drafting with spec-based pricing rules is high-value
- **Company Personalization:** PPC's spec-based margin model differs from commodity mills; Ask Cruz can reflect Specialty Metals pricing logic

**Buying Signals:**
- "weekly-update-call acceptance" on PPC Specialty Metals noted in EOXS Internal Operations page = recurring touchpoint
- Eddie@ppcmetals.com = active contact with weekly cadence
- Recent order (Aug 28, 2026) = current user

**Likely Use Case:**
1. **Quote Drafting** — Support for specialty-metal pricing with spec-based adjustments
2. **Customer Account Briefing** — "Prepare for my call with this customer" = Company Brain core use case
3. **Margin Monitoring** — Specialty metals carry volatility; Ask Cruz flags unusual margin swings

**Recommended Next Step:**
Initiate contact with Eddie (via Raj or Ron) for a "Specialty Metals Sales Efficiency" discovery call. Focus on quote-cycle time and pricing accuracy. Goal: pilot proposal for Q4 2026 or Q1 2027.

---

## **#6: DISCOUNT PIPE & STEEL** | *Large Volume + Operational Complexity*

**Company Profile:** Pipe & steel distributor ($1.54M+ annual revenue, 27 customer rank). 19 orders, 18 invoices = high transaction volume.

**Product Fit:** ⭐⭐⭐
- **Company Brain:** High transaction volume = knowledge fragmentation. "What commitments do we have on this item?" and "Which orders are at risk?" are critical for operations
- **Digital Workforce:** High order volume suggests standing monitoring responsibilities (e.g., "Flag orders where customer has requested expedited shipping")
- **Company Hands:** Inventory availability ("free to sell") is operationally complex with high velocity

**Buying Signals:**
- EOXS engagement: Implementation Kanban exists; recent activity in support queue
- Discount Pipe email domain (info.discountpipesteel@gmail.com) = active EOXS user
- 19 orders in pipeline = operational engagement

**Likely Use Case:**
1. **Order Triage** — Identify orders at risk given high volume
2. **Inventory Coordination** — Real-time "free to sell" queries for multi-location distribution
3. **Operational Dashboards** — Management visibility into order queue health

**Recommended Next Step:**
Schedule brief discovery call with ops/sales leadership. Position Ask Cruz as "operational clarity for high-volume distribution." Goal: short-turnaround pilot (2–4 week sprint) to prove value quickly.

---

## **#7: HANSEN METALLURGICAL SERVICES (HMS)** | *Established Customer + Growth Potential*

**Company Profile:** Metallurgical services firm ($566K+ annual revenue, 23 customer rank). 16 orders, 15 invoices.

**Product Fit:** ⭐⭐⭐
- **Company Brain:** Services business = knowledge-intensive. "What testing did we run for this customer?" and "What's our service pricing for this spec?" are knowledge queries
- **Company Hands:** Services quotes (testing protocols + pricing) would benefit from Ask Cruz support
- **Company Personalization:** HMS's testing procedures and pricing matrix are highly specialized; Ask Cruz can embed company-specific rules

**Buying Signals:**
- Existing EOXS customer with consistent order volume
- No recent contact in data (last activity > 60 days)
- Clean opportunity to restart relationship with new value prop

**Likely Use Case:**
1. **Service Quote Drafting** — Support for complex testing-protocol pricing
2. **Customer History** — "What testing have we completed for this customer?" = Company Brain
3. **Service SOP Capture** — Ask Cruz can codify testing procedures, reducing onboarding time for new staff

**Recommended Next Step:**
"Check-in" outreach to Hansen leadership. Position Ask Cruz as "knowledge capture for your specialized testing business." Goal: low-risk pilots (smaller than Sabre/3GM but high-value relative to company size).

---

## **#8: THREE D METALS (HQ)** | *Large Team + Early-Stage Engagement*

**Company Profile:** Metal products company (79 employees, 6 customer rank). 1 order, 0 invoices = early-stage EOXS customer.

**Product Fit:** ⭐⭐⭐
- **Company Brain:** Larger team (79 employees) = knowledge fragmentation risk. Ask Cruz can centralize operational knowledge.
- **Company Personalization:** Three D's processes and pricing logic would be reflected in Ask Cruz

**Buying Signals:**
- Early EOXS adoption (1 order); growth trajectory suggests openness to tools
- 79-person team = multi-user potential
- Email contact available (sales@threedmetals.com)

**Likely Use Case:**
1. **Operational Knowledge Base** — Centralize procedures and pricing across 79-person team
2. **Onboarding Efficiency** — New staff can ask "How do we normally handle X?" vs. depending on tribal knowledge

**Recommended Next Step:**
Introduce Ask Cruz as part of EOXS's broader digital transformation roadmap. Position as "knowledge productivity for growing teams." Goal: 2027 pilot (allow time for EOXS relationship to deepen).

---

## **#9: BRANNON STEEL** | *International Growth + Operational Lift*

**Company Profile:** Steel manufacturer (Ontario, Canada; 4 orders, 9 invoices, 14 customer rank). Low order count, active invoicing = service/contract model.

**Product Fit:** ⭐⭐
- **Company Brain:** Small team likely relies on individual knowledge; Ask Cruz can reduce key-person risk
- **Company Personalization:** Canadian manufacturer = unique supply-chain and regulatory context; Ask Cruz can capture company-specific practices

**Buying Signals:**
- Recent activity (Jul 22, 2026 order; 9 invoices = ongoing) = active relationship
- International location (Canada) = less frequently targeted by EOXS sales
- Phone contact available ((905) 453-4730)

**Likely Use Case:**
1. **Team Knowledge Capture** — Reduce dependence on founder/leadership memory for pricing, procedures
2. **Compliance Tracking** — Capture Canadian-specific supply-chain requirements

**Recommended Next Step:**
Post-3GM & Sabre success: Expand internationally. Brannon is a reference-able Canadian manufacturer; early adoption would build regional presence. Goal: 2027 outreach after domestic pipeline fills.

---

## **#10: R.W. CONKLIN STEEL** | *Established Customer + Service-Heavy Model*

**Company Profile:** Steel distributor (11 orders, 5 invoices, 16 customer rank). Contact: pete.conklin@conklinsteel.com.

**Product Fit:** ⭐⭐
- **Company Brain:** Small team relying on established customer relationships; Ask Cruz can document historical pricing and commitments
- **Company Hands:** Quote support for long-standing customer base

**Buying Signals:**
- Last order Jan 6, 2026 = 8 months inactive; relationship warming opportunity
- Established contact (Pete Conklin) = easy re-engagement
- Low invoices relative to orders = suggests lower sales volume or project-based model

**Likely Use Case:**
1. **Relationship Reactivation** — Provide Pete with operational context to reconnect with dormant customer base
2. **Historical Knowledge** — Ask Cruz surfaces "What did we sell to this customer 2 years ago?" to support customer conversations

**Recommended Next Step:**
"Re-engagement" outreach. "We've built Ask Cruz to help you reconnect with long-standing relationships — here's how." Goal: pilot after primary pipeline (Sabre, 3GM, Greer) enters implementation.

---

## **CROSS-PROSPECT INSIGHTS FOR PROSPECTING STRATEGY**

**1. Buying Signal Pattern — Multi-Division & Scale Drive Urgency**
- Sabre (3 divisions), Eastern (multiple divisions), PPC (specialty segments) all show higher engagement
- Insight: Pitch Ask Cruz as "operational clarity at scale" for companies with 50+ employees and complex structures

**2. Decision-Maker Identification**
- High-engagement prospects have named internal champions (Sabre: Juan/Tye/Michael; Greer: Joe Brom; PPC: Eddie)
- *Strategy:* Prospecting should target VP of Sales, VP of Operations, or Founder for direct access

**3. Quote-Drafting & Pricing — Highest Perceived Value**
- 8 of 10 prospects show pricing/quoting complexity (landed cost, specialty specs, contract terms)
- *Positioning:* Lead with "Quote Drafting" use case for prospects with margin pressure or complex specs

**4. Implementation Readiness — Existing EOXS = 3x Faster Time-to-Value**
- All top-4 prospects are existing EOXS customers (data, infrastructure, relationships already in place)
- *Strategy:* Prioritize warm leads over cold outreach; ROI is demonstrable within 4–6 weeks vs. 12+ weeks for new systems

**5. Multi-User ARR Expansion — Untapped Opportunity**
- Most prospects have 3+ internal stakeholders (Sales, Ops, Finance) who could benefit from Ask Cruz
- *Pricing model:* Consider per-seat pricing on top of base Company Brain license to expand ACV from warm leads

**6. Vertical Insight — Steel Industry Strength**
- All top 10 are steel-industry businesses, BUT Ask Cruz product strategy is industry-agnostic
- *Future strategy:* Once 3GM succeeds, use as reference case to expand into non-steel verticals (automotive supply, industrial distribution, etc.)

---

## **SUMMARY PIPELINE & REVENUE IMPACT**

| Rank | Company | Likelihood | Timeline | Expected ARR Impact | Action Owner |
|---|---|---|---|---|---|
| #1 | Sabre Alloys | High (70%) | Q3 2026 | [restricted] | Raj/Ron |
| #2 | 3GM Steel | Very High (95%) | Q3 2026 (active) | [restricted] | Ayan/Ron |
| #3 | Greer Steel | Medium (55%) | Q4 2026 | [restricted] | Sales team |
| #4 | Eastern Steel | Medium (50%) | Q4 2026 | [restricted] | Sales team |
| #5 | PPC Metals | Medium (45%) | Q4 2026 | [restricted] | Sales team |
| #6–10 | Others | Low–Medium (20–40%) | Q1 2027+ | [restricted] | Q1 2027 outreach |

**ARR Stretch Goal (Year 1):** Contracts 1–3 by Q4 2026 + 2–4 by Q2 2027 = $1M ARR runway toward $1M goal
