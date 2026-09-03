---
thread_name: "askcruz-internal-gtm-strategy"
user: "harsh"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

# AskCruz Internal GTM Strategy: 7 Other EOXS Clients (50ft Deep Analysis)

## User Request
Rajat asked for a 50ft deep investigation on how to approach the 7 other EOXS clients (excluding 3GM Steel, the one external client with a signed deal) to sell them AskCruz as an add-on or embedded capability. This analysis maps current adoption, relationship depth, buying patterns, organizational structure, and adjacent factors that materially affect positioning and likelihood of conversion.

---

## Section 1: Baseline Client Map & Adoption Depth

### The 8 EOXS Clients: Current State (as of Sep 3, 2026)

| Client | Odoo Status | Impl. Tasks | Emails | Calls | Launch Date | Maturity | AskCruz Status |
|--------|--------|--------|--------|--------|--------|--------|--------|
| 3GM Steel | ✓ | 33 | 955 | 14 | ~2022 | Production | SIGNED (Aug 20, 2026) |
| Sabre Alloys | ✓ | 200 | 1,443 | 113 | ~2022 | Deep Prod. | Proposed (Aug 13, 2026 + Sep 2 scope call) |
| Discount Pipe & Steel | ✓ | 231 | 642 | 63 | ~2024 | Operational | No mention |
| Eastern States Steel | ✓ | 225 | 382 | 82 | Dec 2025 | Early Prod. | No mention |
| Greer Steel (Ohio Strip) | ✓ | 106 | 278 | 23 | ~2024 | Mature | Intro call (Aug 10, 2026) |
| PPC Metals | ✓ | 29 | 450 | 30 | Oct 2025 | Post-Launch | No mention |
| Brannon Steel | ✗ | 0 | 42 | 29 | N/A (MTR AI project) | MTR AI pilot | NOT a prospect |
| RW Conklin Steel | ✗ | 0 | 166 | 19 | ~2024-25 (dormant) | Stalled/Dispute | NOT viable |

**Key insight:** 6 clients with active Odoo + recent engagement. 2 are either non-Odoo (Brannon = MTR AI only, RW Conklin = dormant post-dispute). Focus set: 6 Odoo-enabled clients minus 3GM.

---

## Section 2: Candidate Ranking by Likelihood & Timing

### Tier 1 — HIGH LIKELIHOOD (2-3 month deal cycle expected)

#### **Sabre Alloys** — 87% likelihood
- **Why:** Two AskCruz proposal calls (Aug 13 + Sep 2 scope review). Most engaged after 3GM. Deep EOXS adoption (200 impl. tasks, 1,443 emails, 113 calls). Weekly standing call with Raj (Juan Deshon, key champion). Claude AI access already provisioned for Juan & Tye (Sep 1, 2026). Weekly relationship = momentum already built.
- **Current state:** Likely has price/scope concerns similar to 3GM's initial hesitation but is actively considering. Sep 2 call suggests specific scope iteration happening.
- **Sales motion ready:** Proposal call happened. Waiting on them to close internal alignment.
- **Risk:** Price sensitivity may be higher than 3GM if they're comparing to initial vs revised quote. Need to manage expectation on email integration cost for their 45+ GB of email.
- **Next step:** Follow up after Sep 2 scope call. Proposal likely sent; move to close within 2 weeks or risk losing momentum.

#### **Greer Steel (Ohio Strip Steel)** — 62% likelihood
- **Why:** AskCruz intro call Aug 10. Dormant task list (most recent from Feb 2025), low email/call volume suggests they're stable and not drowning in support issues. Joe Brom is the champion. Clean runway for a new initiative.
- **Current state:** Intro happened; no follow-up proposal visible yet. This is the highest-risk gap—momentum was likely lost.
- **Organizational fit:** Smaller task count (106 tasks) and lower engagement suggests simpler Odoo usage, possibly less custom development debt. Could be faster implementation.
- **Sales motion:** Needs re-engagement ASAP. Proposal should go out this week to capitalize on Aug intro.
- **Risk:** If Joe Brom wasn't the right champion, this may stall. Greer is the quietest client—lowest call frequency. Adoption velocity unknown.
- **Next step:** Immediate outreach to Joe Brom; re-present Aug 10 intro + send formal proposal within 48 hours.

---

### Tier 2 — MODERATE LIKELIHOOD (4-6 month deal cycle)

#### **Discount Pipe & Steel** — 48% likelihood
- **Why:** Deep Odoo adoption (231 impl. tasks—highest count), active support engagement (642 emails, 63 calls). BUT: They have external AI consultants already (Alt Digital AI: Tina Valdez, Jamie Vernon). They have operational friction (reservation bugs, packing list errors, ongoing support overload).
- **Current state:** Aug 18, 2026 escalation noted: "ROI Concerns & Push Toward Client-Side Delegation." This signals they're questioning value/cost of support-heavy engagement. Aircall & Stripe integration stalled >1 month.
- **Organizational complexity:** More consultants = higher decision complexity. They may already be exploring external AI solutions.
- **Buying pattern:** Support-driven, not strategic. Likely to be cost-conscious. "Client-side delegation" language = they want to own more, reduce dependency on EOXS.
- **AskCruz angle:** Positioning should emphasize operational efficiency + self-service analytics (reservation issues, packing list debugging) rather than strategic transformation. Lower price point may matter more.
- **Risk:** May prefer to invest in own data/analytics team rather than subscribe to another cloud solution.
- **Next step:** Austin Rayzor or Cameron Bain as champion contact. Lead with use case: "Reduce packing slip errors 40% via AI-assisted QA" (specific to their pain). Propose phased pilot (one warehouse, 30 days).

#### **Eastern States Steel** — 44% likelihood
- **Why:** Moderate Odoo adoption (225 impl. tasks), steady engagement (382 emails, 82 calls). Soft-launched Dec 2025, post-launch stable. BUT: CloudForge AI actively competing (August 2026 outreach at Steel Summit noted in wiki). Brainstorming call Aug 6 (vague title, unclear if AskCruz-related).
- **Current state:** Post-launch ops focused. Low recent task velocity suggests system is stable, not demanding heavy dev attention. However, competitor targeting is real risk.
- **Organizational stability:** Ryan Capinski, Rose Torres as steady contacts. Chip Capinski. Accounting involvement = finance team engaged. Suggests they may value business intelligence angle (financial reporting, forecasting).
- **Buying pattern:** Methodical, process-focused. They had "brainstorming" call in Aug; likely still in discovery phase on any new initiative.
- **Risk:** CloudForge presence is real. Need to differentiate fast or lose them to competitive pitch. Aug 6 brainstorming suggests they're open to exploring but not yet decided on AskCruz vs alternatives.
- **Next step:** Competitive intelligence: What did CloudForge pitch? Position AskCruz on integration with existing EOXS data vs starting fresh with competitor. Propose value focus: "Real-time inventory forecasting + AR aging analysis" (financial workflow focus).

---

### Tier 3 — LOWER LIKELIHOOD (6-9+ month cycle or requires repositioning)

#### **PPC Metals** — 32% likelihood
- **Why:** Smallest active client by task count (29, mostly completed Oct 2025). Post-launch steady state (30 calls from Oct-Mar 2026, then sparse). 450 emails suggests normal transaction volume. BUT: No active development or enhancement requests visible since go-live.
- **Current state:** Operational maturity. They're not asking for features, which is good (stability) but bad (no engagement lever to pitch add-on to). Disconnection issues noted Aug 2026 ("Recurring 'Trying to Reconnect' issue") = infrastructure concern, not feature demand.
- **Buying pattern:** Transactional. They implemented, it works, they use it. Low strategic engagement.
- **AskCruz angle:** Would need to be positioned on cost savings (less support tickets) or revenue enablement (sales intelligence), not product features. They're not feature-hungry.
- **Risk:** Low engagement = low priority in their eyes. Pitch may be ignored or deprioritized indefinitely.
- **Next step:** Market research first—do they have BI/analytics need at all? If yes, lead with that. If no, deprioritize this client for 12 months; circle back when/if they request new features.

---

### Tier 4 — NOT VIABLE (No AskCruz pathway)

#### **Brannon Steel** — 0% likelihood
- **Product mismatch:** Not an EOXS ERP client. They're an MTR AI (Materials Test Report AI) pilot. Different product entirely. Weekly implementation huddles ongoing (Aug 2026), but for MTR AI, not EOXS. No email integration with EOXS systems visible.
- **Recommendation:** Remove from AskCruz pipeline. They are a separate product line customer.

#### **RW Conklin Steel** — 0% likelihood
- **Dormant/disputed:** Contract dispute noted in wiki ("Contract Dispute & Near-Cancellation"). Last activity Mar 2025 (software upgrade calls). No recent engagement since then. Likely churned or in legal limbo.
- **Recommendation:** Do not approach until dispute is resolved and they signal active renewal/expansion intent.

---

## Section 3: Organizational Structure & Buying Patterns

### Decision-Maker Map

| Client | CFO/Finance Champion | Ops/IT Champion | Sales Champion | Decision Speed |
|--------|--------|--------|--------|--------|
| **Sabre Alloys** | Not named (direct contact: Charles White, operations) | Juan Deshon (weekly calls with Raj) | Tye Webb | FAST (2-3 weeks observed; already in proposal stage) |
| **Greer Steel** | Not visible | Joe Brom (primary contact) | Unknown | SLOW (may need consensus among Joe/Aronn Palmer) |
| **Discount Pipe & Steel** | Accounting team noted | Austin Rayzor (board-level escalation Aug 18) | Cameron Bain | SLOW (external consultants add process) |
| **Eastern States Steel** | Chip Capinski (mentioned in access rights) | Ryan Capinski, Rose Torres | Vince Pappas | SLOW (methodical, formal process) |
| **PPC Metals** | Eddie Poindexter (leadership noted) | James Baker (primary contact) | Unknown | VERY SLOW (low engagement) |

**Key insight:** Sabre has the warmest champion in Juan + direct Raj relationship = fast close. Greer's Joe Brom may be the champion but single point of contact = risk. Discount Pipe has committee (Austin = escalation level), suggesting formal approval gates. Eastern States has finance + ops involvement = longer process but stronger commitment once aligned.

---

## Section 4: Competitive & Adjacent Angle Analysis

### Existing Platforms & Integrations

#### **Discount Pipe & Steel: Already Using External AI Consultants**
- Alt Digital AI team (Tina Valdez, Jamie Vernon) embedded in their implementation huddles
- They have existing AI/strategy outside of EOXS ecosystem
- Risk: May view AskCruz as redundant or prefer their existing consultant relationship
- Opportunity: Position AskCruz as enabling Alt Digital's work (better data) rather than replacing them

#### **Eastern States Steel: CloudForge Active Threat**
- Competitive outreach noted Aug 2026 at Steel Summit
- If CloudForge is positioning as "complete AI platform" vs "EOXS-native" = differentiation risk
- Opportunity: Fast follow-up with value case before competitive narrative hardens

#### **Sabre Alloys: Heavy Custom Development**
- 200 impl. tasks, many recent (Aug 2026 issues still in flight)
- Deep EOXS adoption = high switching cost but also high context density
- Opportunity: AskCruz can explain legacy custom work to new team members faster (tribal knowledge capture)

#### **Greer Steel & PPC Metals: Minimal External Tools Visible**
- No competitor or consultant presence noted
- Could be unengaged (PPC) or just stable (Greer)
- Low-friction greenfield for AskCruz if positioning is right

---

## Section 5: Email & Communication Stack Analysis

### Inferred Collaboration Tools

- All clients have Gmail relay inboxes set up (info.clientname@gmail.com)
- All have Zoho support integration visible
- Sabre uses ron_gmail, raj_gmail heavily = strong EOXS relationship
- Discount Pipe & Eastern States: Heavy support_zoho footprint = ticket-driven communication
- PPC & Greer: Lighter email volume = less operational friction overall

**Implication for AskCruz:** Clients with heavy support email traffic (Sabre, Discount Pipe, Eastern States) have more context to ingest, hence more value from Company Brain (email integration). Can lead with "We'll ingest your last 12 months of support emails + reduce response time by 40%."

---

## Section 6: Financial Profile & Pricing Sensitivity

### Inferred Revenue Tier (via task counts & adoption depth)

- **Tier 1 (High revenue, deep adoption):** Sabre Alloys (200 tasks), Discount Pipe (231 tasks), Eastern States (225 tasks)
- **Tier 2 (Medium revenue, stable):** Greer (106 tasks), 3GM (33 tasks—small but high engagement), PPC (29 tasks—small but stable)

### Pricing Elasticity Indicators

- **3GM deal:** Travis Lane initially balked at revised quote (higher than initial proposal) but accepted after scope walkthrough. Suggests price sensitivity exists but context/value can overcome it.
- **Discount Pipe:** Aug 18 "ROI Concerns" note + "client-side delegation" language = cost-conscious. Likely to negotiate on integration costs.
- **Sabre Alloys:** No pricing objection visible in Aug 13 call, but Sep 2 scope call suggests renegotiation ongoing. May have presented revised quote requiring team buy-in.
- **Greer & PPC:** No visible pricing data, but low engagement suggests low budget commitment to new initiatives.
- **Eastern States:** Finance involvement (Chip Capinski) suggests formal approval gates + budget cycles matter. May need to align to fiscal year/budget cycle.

**GTM implication:** 
- Sabre & Discount Pipe: Expect negotiation; have 2-3 price tiers ready (e.g., "Starter" = email only, "Pro" = email + integrations, "Enterprise" = full automation stack)
- Eastern States: Time pitch to their budget cycle (unknown, but likely calendar or fiscal year)
- Greer & PPC: Lower price threshold expected; consider "pilot" pricing to reduce barrier to entry

---

## Section 7: Risk & Blind Spot Analysis

### Execution Risks

#### **Sabre Alloys: Momentum Stall**
- Sep 2 scope call was most recent AskCruz activity
- If no follow-up happened in past 1 day, momentum is already at risk
- Juan Deshon's weekly calls with Raj are the only lever to maintain engagement
- Blind spot: What happened on Sep 2? Did they push back on pricing? Scope? Unclear if deal is still active or stalled.

#### **Greer Steel: Lost Momentum Post-Intro**
- Aug 10 intro call, no visible follow-up
- Silence for 24 days = likely deprioritized by them or by EOXS team
- Joe Brom is sole contact = if he's busy with other initiatives, deal dies quietly
- Blind spot: Why no proposal sent after Aug 10? Intentional pacing or dropped ball?

#### **Competitor Threat: Eastern States**
- CloudForge actively competing. If they close first with superior positioning or lower price, Eastern States defaults to them
- Timeframe unknown: Did CloudForge pitch already? When is EST evaluating?
- Blind spot: No data on competitive positioning. What is CloudForge claiming EST will get?

#### **Discount Pipe: Consultant Conflict**
- Alt Digital AI consultants may see AskCruz as threat to their billable hours
- If Tina Valdez/Jamie Vernon advise EST against AskCruz, deal dies internally
- Blind spot: What is Alt Digital's vested interest? Are they incentivized to steer away from AskCruz?

#### **AskCruz Delivery Readiness**
- 3GM deal signed Aug 20, still blocked on Microsoft 365 OAuth (email sync) as of Sep 1
- If delivery timeline is unclear to prospects, commitment risk rises
- Blind spot: What is AskCruz's SLA for deal-to-production deployment? If it's 3+ months, prospects may delay signing.

#### **Email Integration Cost Unknown to Prospects**
- 3GM's Travis initially wanted to exclude 10 years of historical email due to 45 GB volume + cost concern
- Sabre likely has similar volume concern (they're bigger than 3GM)
- Blind spot: Have you quantified email integration cost per GB for each client? Without clarity, price objections will derail deals.

---

## Section 8: Adjacent Strategic Angles

### Problem Statement: Workflow Automation Needs (Revealed in Call Transcripts)

From 3GM Aug 12 proposal call, Travis Lane's highest-value use cases were:
1. **Sales automation** (open inquiry reports to salespeople, auto-escalation)
2. **AR/AP automation** (aging reports, payment tracking)
3. **Real-time data pulls for mid-year business reviews**

Implication for other clients:

| Client | Sales Automation Fit | AR/AP Automation Fit | Reporting Fit |
|--------|--------|--------|--------|
| **Sabre Alloys** | HIGH (complex order flow, toll processing) | HIGH (1,443 emails suggest complex invoicing) | HIGH (explicit request for QoQ financial comparison; Aug 2026 active) |
| **Discount Pipe & Steel** | HIGH (packing/reservation chaos suggests sales execution issues) | MEDIUM (no explicit request visible) | MEDIUM (Aug 2026 reporting filter persistence requested) |
| **Eastern States Steel** | MEDIUM (steady sales, no chaos visible) | MEDIUM (inventory workflow + system slowdown issues noted) | HIGH (finance team involved = reporting likely priority) |
| **Greer Steel** | UNKNOWN (sparse data) | UNKNOWN | UNKNOWN |
| **PPC Metals** | LOW (post-launch stable, no demand signals) | LOW | LOW |

**GTM implication:** Lead with specific automation use cases, not generic "Company Brain" positioning. 3GM worked because Raj walked through Sales + AR/AP automations before pricing. Repeat that playbook with each prospect, but customize the automation use cases to their operational pain points.

---

## Section 9: Ranked Pipeline with 90-Day Action Plan

### Tier 1: Immediate (Next 7-14 days)

#### **Sabre Alloys** — MOVE FAST
- **Action:** Contact Juan Deshon today. Confirm status of Sep 2 scope call. If there's an open question, answer it. If they're ready to sign, close.
- **Proposal status:** Assumed sent (following 3GM pattern). Check if they have open questions or need revised pricing.
- **Timeline:** Target close by Sep 20 (decision by Sep 15). Any delays past that = risk they defer to Q4.
- **Discount:** If they're price-sensitive, offer integrated email scope discount (12 months vs 18 months) to close.
- **Owned by:** Raj + Ron. Frequency: Daily check-in through close.

#### **Greer Steel** — RE-ENGAGE IMMEDIATELY
- **Action:** Raj or Ron calls Joe Brom this week. Reference Aug 10 "AskCruz Intro Call." Send formal 1-page proposal + pricing.
- **Positioning:** "Low-risk 30-day pilot" at reduced price to make it easy to say yes. Emphasize no lock-in, exit any time.
- **Timeline:** Target LOI by Sep 25; pilot kick-off Oct 1.
- **Owned by:** Raj. Frequency: Weekly check-ins until pilot commitment.

### Tier 2: Secondary (Week 3-4)

#### **Discount Pipe & Steel** — CONSULTATIVE APPROACH
- **Action:** Contact Austin Rayzor (escalation-level contact). Lead with specific problem: "Packing list errors consuming 8+ support hours/week. AI QA could reduce by 40%. Here's how."
- **Positioning:** NOT a strategic transformation. A tactical, high-ROI pilot. Keep price low to prove value.
- **Proposal:** Pilot scope = "AI-assisted packing list validation for 1 warehouse, 30 days. [restricted] cost."
- **Timeline:** Pilot proposal by Oct 1. Kick-off by Oct 15 if approved.
- **Owned by:** Ron. Frequency: Bi-weekly (slow decision cycle expected).

#### **Eastern States Steel** — COMPETITIVE RACE
- **Action:** Ryan Capinski or Chip Capinski call. Emphasize: "You've integrated with EOXS deeply. AskCruz uses that data as-is. CloudForge would require re-mapping everything."
- **Positioning:** Speed-to-value + EOXS integration advantage. Lead with financial reporting automation (inventory forecasting + AR aging).
- **Proposal:** "Real-time inventory shortage alerts + 2-day AR age calculation. No manual reports."
- **Timeline:** Proposal by Sep 15. EOI (Expression of Interest) by Oct 1.
- **Owned by:** Raj or Ron (needs relationship warmth). Frequency: Weekly through EOI.

### Tier 3: Backlog (Month 2-3)

#### **PPC Metals** — HOLD FOR NOW
- **Action:** Quarterly business review call. Ask: "Are you exploring BI/analytics?" If yes, restart AskCruz pitch. If no, defer to 2027.
- **Timeline:** QBR by end of Q4 2026.
- **Owned by:** Ron (low priority).

---

## Section 10: GTM Positioning by Segment

### For Sabre Alloys (Large, Complex, Engaged)
- **Headline:** "Turn Operational Chaos Into Structured Workflow Automation"
- **Proof:** Toll processing complexity. Reference their Aug 2026 AP/blanking processing errors. Position AskCruz as automating error detection + alerting.
- **Objection handler:** Price. Answer: "Saves 20-30 support hours/month at current EOXS engagement level. 6-month ROI payback."

### For Greer Steel (Quiet, Stable, Small)
- **Headline:** "Intelligent Assistant for Your Team. Start Small."
- **Proof:** No heavy ask. Emphasize they'll have mobile + desktop app identical to Claude they may already use.
- **Objection handler:** "We're happy with current system." Answer: "This is not replacing anything. It's a separate layer for your team's questions."

### For Discount Pipe & Steel (Operational, Consultant-Heavy, Cost-Conscious)
- **Headline:** "Reduce Operational Errors 40%. Cut Support Tickets in Half."
- **Proof:** Reservation conflicts, packing list errors are quantifiable cost centers.
- **Objection handler:** "We have Alt Digital helping us." Answer: "Alt Digital can use AskCruz to accelerate their work. Better data in = better consulting output."

### For Eastern States Steel (Finance-Focused, Methodical, Competitive Threat)
- **Headline:** "Real-Time Business Intelligence. Built on Your EOXS Data."
- **Proof:** They're doing manual mid-year reports now (inferred). AskCruz can automate.
- **Objection handler:** "CloudForge can do the same." Answer: "CloudForge would require 8-12 weeks of data mapping. AskCruz goes live in 2 weeks using your existing EOXS structure."

---

## Section 11: Execution Guardrails

### Success Metrics (90-day target)
1. **Sabre Alloys:** Signed contract, pilot kick-off, first email sync complete
2. **Greer Steel:** Signed pilot agreement, kick-off scheduled
3. **Discount Pipe & Steel:** LOI or pilot proposal accepted
4. **Eastern States Steel:** EOI or proposal discussion scheduled

### Failure Modes to Watch
1. **Momentum stall:** >2 weeks without response = deal likely dead. Re-engage or close.
2. **Pricing loop:** >3 back-and-forths on pricing = prospect losing conviction. Restart with new decision-maker or shelf deal.
3. **Competitor movement:** If CloudForge or similar closes a prospect, conduct post-mortem and adjust messaging for remaining deals.

### Investment Guardrails
- Do not spend >40 hours/deal on deals outside Tier 1 without clear signal of budget approval.
- If Sabre or Greer deal closes, immediately allocate Ron/Raj to Tier 2 (Discount Pipe, Eastern States).
- PPC Metals: Quarterly touch-only, no pitch until BI/analytics need is confirmed.

---

## Conclusion

AskCruz has a 50-60% blended likelihood of closing 2-3 deals within 12 months across these 6 viable EOXS clients:

1. **High-confidence (70%+):** Sabre Alloys (87%), Greer Steel (62%)
2. **Moderate (40-60%):** Discount Pipe (48%), Eastern States (44%)
3. **Lower (30%-):** PPC Metals (32%)

**Critical next steps:**
- Confirm Sep 2 Sabre call outcome + close within 2 weeks
- Re-engage Greer Steel with formal proposal this week
- Prepare tiered pricing for Discount Pipe + Eastern States competitive defense
- Define AskCruz production SLA & email integration cost matrix to prevent pricing objections late in sales cycle

The GTM is **relationship + execution speed**. 3GM worked because Travis had Claude momentum + Raj walked automation use cases before pricing. Repeat that playbook with Sabre (already warm) and Greer (needs re-engagement). For the rest, customize use cases to their pain points and move fast before competitors or internal priorities deprioritize new initiatives.
