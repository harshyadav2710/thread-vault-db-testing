---
thread_name: "3gm-askcruz-status"
user: "harsh"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

# 3GM Steel AskCruz Deal Status — Deep Investigation

## User Question
What is the status of the 3GM Steel deal in AskCruz? (Requested with 50ft depth rigor)

---

## Analysis

### Deal Structure & Contract Terms

**Signed:** August 20, 2026 (after 8 days of proposal refinement: Aug 12–20)

**Scope:** Company Brain (Claude trained on 3GM's 4-year data set + continuous email sync)
- 2 users: Travis Lane (CCO) and Stefan Brown (CFO)
- 6-month initial pilot (ends ~Feb 2027 based on typical cycles)
- Decision point 30 days before expiry: renegotiate, extend, or exit
- No automatic renewal

**Product & Front-End:** Claude (not AskCruz). Ron made the strategic call on Aug 17 that Claude has "more built-out functionality" for 3GM's day-to-day needs, while AskCruz continues development for future clients.

**Pricing Structure** (per Ron's Aug 17 corrected proposal):
- Company Brain per-user rate (specific amount redacted)
- Platform infrastructure fee (one-time, redacted)
- EOXS Integration (one-time, redacted) — covers connecting 3 email accounts + model training + workflow customization
- Email ingestion cost (per-GB; 3GM has 12-month history window, Sept 2025–present)
- Claude subscription (set up by 3GM directly with Anthropic; EOXS does not manage)

---

### Timeline: Proposal to Signature

| Date | Event |
|---|---|
| Aug 12 | Rajat calls Travis to pitch Company Brain; call recorded (Fireflies) |
| Aug 14 | Two proposals sent with conflicting pricing/unit rates |
| Aug 17 | Ron sends corrected proposal addressing Travis's 5 objections; strategic decision to use Claude as front-end |
| Aug 19 | Travis confirms 3GM moving forward at reduced scope (2 users instead of original proposal scope) |
| Aug 20 | Rajat agrees to shorten the 6-month initial term per Travis's request; deal signed |

---

### Current Blocker: Microsoft 365 Email OAuth

**Stated Issue (from memory, as of Sept 1):** 3GM's Microsoft 365 admin must grant read-only mail app OAuth consent. Without this, email sync cannot begin.

**All other prerequisites reportedly in place:**
- Claude Pro accounts active (NOT verified by email confirmation)
- Outlook confirmed as email provider
- 12-month email history window identified (Sept 2025–present)
- Staging environment on DigitalOcean stood up Aug 14 (NOT verified as current)
- Company Brain training readiness claimed but NOT confirmed

**Critical gap:** No evidence of follow-up on this blocker since Sept 1. No recent emails requesting OAuth permission from 3GM's admin, no calls checking status, no project board tracking it.

---

### Implementation Readiness — Red Flags

**No project board in Odoo.** All current 3GM tasks are from the 2022 EOXS onboarding (4 years old), marked inactive. There is zero formal tracking for the AskCruz implementation.

**No project owner assigned.** Ron is listed as point of contact (ron@askcruz.com), but there is no formal Odoo project, no task list, no sprint, no milestones.

**13-day communication silence (Aug 20–Sept 2).** After signature, no record of:
- Kickoff meeting scheduled
- OAuth request sent to 3GM's admin
- Payment confirmation or receipt
- Claude account provisioning confirmation
- EOXS integration start date

**Wiki page flagged as unverified (Aug 28).** Most recent synthesis says kickoff date and payment details were to be "finalized," but flag notes this was reconstructed from search snippets, not confirmed from full email bodies. As of Sept 3, no update since Aug 28.

**Recent emails (Sept 1–3):** All 3GM communication is routine support tickets (product variant issues). Zero AskCruz deal follow-up.

---

### Prerequisites Status — Verification Matrix

| Item | Status | Evidence |
|---|---|---|
| Deal signed | ✓ Confirmed | Aug 20 email (Rajat confirms term reduction) |
| Scope (2 users, 6mo pilot, Claude front-end) | ✓ Confirmed | Ron's Aug 17 proposal, Travis's Aug 19 confirm |
| EOXS integration scope defined | ✓ Confirmed | Ron's Aug 17 email explains integration covers 3 accounts + training |
| Staging environment stood up | ? Claimed only | Memory says Aug 14; no email verification |
| Claude Pro accounts active | ? Claimed only | Memory says active; no email confirmation from 3GM |
| Company Brain training ready | ? Claimed only | Memory says ready; no implementation task or verification |
| OAuth request sent to 3GM | ✗ Not found | No email evidence in recent communications; assumed blocker but unconfirmed as actually requested |
| Kickoff date set | ✗ Not found | Wiki says "being finalized" (unverified); no email confirmation |
| 50% kickoff payment received | ✗ Not found | Wiki says "to get finalized"; no confirmation of receipt |

---

### Key Dependencies & Risks

**Immediate (OAuth blocker):**
- If OAuth hasn't been formally requested yet, 3GM's IT/admin doesn't even know it's needed.
- If requested, no documented SLA on 3GM's approval timeline.
- No escalation plan if 3GM's admin is slow or unresponsive.
- 14+ days of silence is concerning if this is truly blocking progress.

**Secondary (implementation readiness):**
- Company Brain training readiness is stated but not tested.
- No pilot/staging test run with Travis/Stefan documented to validate before production flip.
- Ayan Dutta (AskCruz backend owner) has 31 open tasks across 5 boards; competing priorities unclear.

**Contractual (renewals & retention):**
- 6-month term ends ~Feb 2027 with 30-day decision point.
- No renewal/expansion plan documented.
- No success metrics defined to justify renewal.

**Organizational (ownership):**
- No one clearly owns the 3GM implementation day-to-day in a formal capacity.
- Ron is named in emails but has no formal project board assignment.
- No escalation path if issues arise during implementation.

---

### What Must Happen Next

1. **Confirm OAuth status immediately:** Did Ron actually send the OAuth request to 3GM's M365 admin? If not, do it today. If yes, what was the response and when do we expect approval?

2. **Set OAuth follow-up cadence:** 3–5 business day check-in calls; do not let this drift silent again.

3. **Create formal Odoo project board** for 3GM AskCruz with tasks:
   - OAuth approval (blocker)
   - Claude account provisioning
   - EOXS integration setup & model training
   - Company Brain training & validation
   - Staging UAT with Travis/Stefan
   - Production deployment & go-live

4. **Confirm kickoff date and payment receipt** in writing—no more ambiguity about whether these are "being finalized."

5. **Schedule kickoff call** with 3GM (Travis & Stefan) to walk through Company Brain setup and set expectations on response times, data freshness, integration workflow.

---

### Bottom Line

The deal is real and signed, but **implementation is in stasis.** The OAuth blocker is claimed but unverified—there's no evidence it's been formally requested or followed up on since Sept 1. You're 14 days past signature with no project board, no assigned project owner, and no visible forward momentum.

This is your first external AskCruz customer. The $1M ARR goal depends on nailing this onboarding. Right now, no one is visibly shepherding it forward.

**Critical question to resolve before proceeding:** Has Ron actually sent the OAuth request to 3GM's admin, and if so, what is the status?
