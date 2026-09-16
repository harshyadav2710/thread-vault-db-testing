---
thread_name: "askcruz-junior-engineer-role"
user: "harsh"
type: claude-chat
created: 2026-09-16
updated: 2026-09-16
---

# AskCruz Junior Engineer Role Definition — Sept 16, 2026

**Participants:** Rajat Jain (CEO, EOXS/AskCruz) | Claude (Advisor)

**Context:** Rajat seeking 10ft deep role definition for junior AI engineer focusing on AskCruz product features.

---

## Conversation

**User:** ai-engineer-5-role

**Claude:** Clarified need for context: Is this hiring? Yes.

**User:** AskCruz

**Claude:** Requested skills level, scope, and rigor depth.

**User:** 1. role, 2. junior, 3. product feature, 4. 10ft deep

---

## Analysis & Research

Loaded threads-ov and eoxs-data-general skill files per user preferences. Called get_index() for baseline data.

Retrieved and analyzed:
- AskCruz Self-Knowledge, Product Definition & System Architecture (asset 16, v1.2, updated Aug 25, 2026)
- AskCruz Product Feature File (asset 19, v1.1, updated Aug 25, 2026)
- User profile (Rajat Jain, CEO EOXS, targeting $250–500k ARR by Sept 2027)

**Key findings:**

**Product State:**
- V1.0 source baseline; internal pilot at EOXS + first external customer (3GM) mid-implementation
- Architecture documented: ingestion → filtering → sensitivity classification → knowledge store → synthesis → citation check → human approval → retrieval → response
- Four core pillars: Company Brain (knowledge discovery), Company Hands (practical work), Digital Workforce (standing responsibilities), Company Personalization (company-specific behavior)
- Data completeness: 94% (product-file metric)
- Current team: Jaskeerat (frontend), build-out team (backend/DB/pipelines), Ayan (credentials), Nidhi (Linear credentials)

**Market & Growth:**
- Goal: $250–500k ARR by Sept 2027 (reset from $1M ARR based on PMF unproven, single customer)
- Product-market fit: Unproven; 1 external customer (3GM)
- Rajat working full-time on AskCruz; EOXS in support-only mode (stable, Ron bottleneck)

---

## AskCruz Junior AI Engineer — Product Features Role (10ft Deep)

### Role Summary

Build and ship features expanding AskCruz's core capabilities (Company Brain, Company Hands, Digital Workforce) for 3GM deployment and follow-on customers. Focus on LLM/AI-driven feature execution where speed and learning velocity outweigh independent system architecture.

### Why This Hire Makes Sense (Verified Context)

**Product Maturity:** V1.0 with documented architecture. Not in foundational phase; in *feature expansion and early-customer iteration* phase.

**Customer Reality:** One customer (3GM) mid-implementation drives roadmap. Junior engineer learns by shipping real customer features, not reading docs.

**Team Gap:** Frontend (Jaskeerat), backend/DB/infra (build-out team) exist. **Missing:** dedicated product feature engineer. Addition unblocks feature velocity tied to customer retention and upsell.

**Growth Dependency:** $250–500k ARR target requires shipping features that 3GM validates + attract follow-on customers. Each iteration is a product/market signal. Juniors iterate faster on bounded work.

### What They'd Actually Build (Next 6 Months)

**Company Brain (Knowledge Discovery)**
- Query refinement/clarification (ask follow-up when context insufficient)
- Citation UI improvements (make sourcing transparent)
- Related-document suggestions (surface adjacent knowledge)

**Company Hands (Practical Work)**
- Quote drafting (generate drafts from pricing logic + customer history)
- Order-risk identification (flag orders approaching promise dates)
- Call summarization (structured summaries tied to accounts)

**Digital Workforce (Monitoring)**
- Standing-watch setup (define monitored conditions; alert on triggers)
- Exception detection (unusual order/inventory/margin patterns)

**Company Personalization**
- Customer vocabulary indexing (make AskCruz "speak" like the company)
- Pricing-exception handling (encode discounts, volume rules, special terms)

**First 3GM deliverables drive prioritization.** Use actual 3GM feedback.

### Role Scope & Day-to-Day

**Owns:**
- End-to-end feature: spec (with product lead) → LLM prompt engineering → backend integration → testing → ship
- Collaboration with Jaskeerat (frontend), backend team (API/DB support)
- Customer-facing feature documentation (product how-to, not marketing)

**Does not own:**
- Core architecture/system design (backend team)
- Database schema or API contract changes (backend lead)
- Product strategy or customer negotiation (CEO call)

**Typical week:**
- 1–2 features in flight (1–2 week cycles)
- Code review turnaround from build-out team
- 1–2 customer questions/feedback synthesis (direct from 3GM if needed)
- Prompt/retrieval optimization (iterative)

### Required Skills

**Must have:**
- Python or JavaScript (codebase uses both)
- Familiarity with LLMs (Claude API, RAG basics, prompt engineering)
- Git + code review workflow
- Can read and modify existing code without extensive hand-holding

**Nice to have:**
- Startup/fast-iteration experience
- Vector DB exposure (Postgres/pgvector) or search/retrieval
- Customer feedback loop experience (shipping fast based on real feedback)

**Red flags:**
- Insists on perfect design before shipping
- Uncomfortable with ambiguity
- No interest in customer impact understanding

### Growth & Onboarding Timeline

**Month 1:** Codebase deep-dive, observe 3GM calls, ship 1–2 small features (bug fixes, UI polish)

**Months 2–3:** Own 2–3 customer-facing features end-to-end; start prompt/retrieval optimization

**Months 4–6:** Autonomous feature ownership (spec → ship); begin thinking about architecture implications

### Hiring Constraints & Reality Check

**Open questions for Rajat:**
1. Annual salary range? (Affects competitive positioning)
2. 6+ month runway before net-positive delivery? (Juniors need 2–3 month ramp)
3. Full-time or contract? (FT = committed learning; contract = lower cost, higher friction)

**Market reality:**
- Junior AI/ML engineers abundant; competition real
- Differentiation: Direct CEO mentorship + shipping real features into market-potential product vs. titles
- Attractiveness: "Help build company second brain" + direct customer access > "work on infrastructure"

### Success Metrics (First 6 Months)

- Shipped: 6–8 features (customer-facing, scoped, tested)
- Customer validation: 3GM uses 3+ features regularly; feedback informs next roadmap
- Code quality: PRs merged on first/second review (post-ramp); minimal production bugs
- Autonomy: By month 6, can scope/spec/ship features with minimal oversight
- Learning velocity: Understands AskCruz architecture; proposes feature optimizations

### Red Flags to Screen

- Wants to rewrite core systems immediately (startup death wish)
- No examples of shipping under ambiguity
- Expects perfect requirements/design docs upfront
- More interested in resume than customer impact

### Bottom Line

**Hire if:**
1. 3GM will renew/expand (single-customer risk real)
2. 6+ months runway for ramp
3. Direct CEO access to customer feedback (not through layers)

**Premature if:**
1. 3GM success still binary
2. Need senior to fix tech debt immediately
3. No time to mentor (they'll flounder in ambiguity)

**Rajat's call:** What's your read on 3GM's trajectory?

---

## Data Sources & Verification

- `get_index()`: baseline counts (8 clients, 824 implementation tasks, 30.8k emails, 2.4k calls visible in this session)
- `get_asset(askcruz-self-knowledge)`: product definition, architecture, access model, tier mapping
- `get_asset(askcruz-product-feature-file)`: feature pillars, use cases, boundaries, user groups
- User memory `/profile.md`: Rajat's goals, constraints, team structure
- Threads-OV and EOXS-Data-General skill files: data access patterns and transcript handling

---

## Next Steps (If Approved)

1. Refine salary/contract terms based on Rajat's constraints
2. Draft job posting emphasizing customer collaboration + shipping velocity (vs. infrastructure work)
3. Screen for ambiguity tolerance + ship-over-perfect bias
4. Define onboarding curriculum (codebase → 3GM calls → first small feature)
5. Set 30/60/90 day checkpoints (ramp expectations)

---

**Rigor Level:** 10ft deep (verified context, fact-checked against AskCruz product docs and team data, cross-checked financial/market assumptions)

**Last Updated:** September 16, 2026
