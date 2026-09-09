---
thread_name: "askcruz-overview"
user: "harsh"
type: claude-chat
created: 2026-09-09
updated: 2026-09-09
---

# AskCruz Project Overview Chat

**Date:** September 9, 2026

## User Query
Tell me about AskCruz project and save this chat.

## Response

**AskCruz** is an AI-powered company knowledge platform that EOXS is developing and commercializing. It ingests emails, calls, support tickets, and implementation data, then serves this knowledge through a conversational interface with granular access controls.

### Strategic Vision
- **1-Year Goal:** Reach $1,000,000 ARR by September 2027
- **Current Status:** Live in production as an internal EOXS pilot + first external client (3GM Steel) in mid-implementation as of August 2026

### Technical Stack

| Component | Technology | Owner |
|-----------|-----------|-------|
| **Database** | PostgreSQL 10+ (Hetzner VPS primary + DigitalOcean staging) | Ayan Dutta |
| **Backend** | Node.js / Python | Build-out team |
| **Frontend** | Cruz codebase (React/TypeScript) | Jaskeerat Singh |
| **Data Sources** | Gmail (3 accounts), Zoho support, Fireflies, Fathom calls, Odoo boards | Ingestion pipeline |
| **Version Control** | GitLab | Ayan Dutta |

**Ingestion Cycle:** 2 hours (raw) + 6 hours (synthesis: pages → human approval → publish)  
**Data Completeness:** 94% as of Aug 25, 2026

### Access Architecture

Three-tier permission model:
- **Tier 1:** Raj-Personal (Raj only, completely isolated)
- **Tier 2 Confidential:** Company-Confidential (internal team)
- **Tier 2 General:** Public use, stripped of amounts/performance metrics

Access enforced at database + AI response levels.

### Development Team Status (as of Aug 18)

| Person | Role | Status |
|--------|------|--------|
| **Ayan Dutta** | Backend/ops/infrastructure | High velocity: 31 open tasks, 22 self-stage-moves + 15 completions this week |
| **Jaskeerat Singh** | Frontend (Cruz) owner | 4 open tasks, low engagement |
| **Nidhi Rana** | Infrastructure & QA | Completed full Postgres schema audit (30+ tables), MCP refinements |

**Recent Wins:**
- Email integration automation (Aug 17)
- SOP edit function via MCP (Aug 14)
- DigitalOcean staging server live (Aug 14)

### Known Issues & Blockers

🚨 **Critical:**
- **Task #156** (Project Board Management): High-priority, zero activity this week
- **Task #94** (AskCruz Voice Call-In): 11.8 days idle
- **Task #152** (Claude response latency): On hold, no root cause documented
- **Thread Vault DB Persistence Crisis:** Only 70% save success rate; 30% of conversation saves fail/lost due to volatile identity state and best-effort model-based saves

**Medium Priority:**
- Write capability (deployed Aug 14) is new and under-tested at scale
- Ingestion gaps remain after legacy file migration
- Knowledge transfer to team incomplete (training promised end of week)

### 3GM Client Implementation – CRITICAL BLOCKER 🔴

**Status:** Actively blocked on **Microsoft 365 admin consent** for OAuth read-only mail app

| Item | Status |
|------|--------|
| **Contract** | Signed Aug 20; 6-month pilot + affirmative decision point |
| **Scope** | Company Brain (Claude trained on 3GM workflows + email sync) + EOXS integration |
| **Users** | 2 pilots (Travis Lane, Stefan Brown) |
| **Claude Accounts** | ✅ Active with 3GM |
| **Email History** | ✅ 12-month window ready (Sept 2025–present) |
| **Outlook Confirmation** | ✅ Confirmed |
| **M365 OAuth Approval** | ❌ **AWAITING** |
| **Staging Environment** | ✅ DigitalOcean live; Company Brain build ready |

**Pricing Model:**
- Per-user Company Brain rate (separate from IRIS)
- Platform infrastructure fee
- EOXS integration one-time (connection + model training; future users charged separately)
- Email integration per-GB (3GB minimum)
- Claude subscription managed by 3GM directly

**Implementation Path:**
M365 admin approval → Ron sends Outlook sign-in links → email ingestion → Company Brain training → production deployment

**Communication:** Primary contact is ron@askcruz.com (async email preferred over daily calls)

### Next Steps / Critical Path

1. **Unblock 3GM:** Get Microsoft 365 admin consent for OAuth (highest impact—production deployment ready)
2. **Resolve Task #156:** Project board management
3. **Thread Vault DB v2:** Address 70% failure rate (4–5 weeks, ~50 hours; +$7/month infrastructure cost)
4. **Close knowledge transfer loop:** Complete backend training materials
5. **Scale write capability testing:** Ensure new SOP edit feature works reliably at volume
