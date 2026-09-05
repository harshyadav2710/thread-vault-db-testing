---
thread_name: "askcruz-overview"
user: "harsh"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

## Jagriti's Question: How Does Daily Activity Summary Work?

**User:** Jagriti Chowdhury (QA, HR MCP testing)

**Question:** "How will the daily activity summary works?"

---

## WHAT IS IT?

Daily activity summary is an automation that:
1. Every day at 5 PM, runs automatically
2. Reads your Slack messages (from channels you posted in)
3. Reads your GitHub commits (from that day)
4. Sends both to Claude AI to summarize
5. Claude writes a summary (e.g., "Tested Okta provisioning, found 2 bugs, deployed fix")
6. Summary automatically posts to your Odoo daily task
7. You see it at 5 PM without doing anything

---

## HOW IT WORKS (TECHNICAL FLOW)

```
5:00 PM Trigger
  ↓
Read Slack messages from channels you participated in
Read GitHub commits you made today
  ↓
Send to Claude API with prompt: "Summarize this QA work"
  ↓
Claude generates summary (e.g., "Tested leave management, found half-day bug, deployed fix")
  ↓
Post summary to Odoo task automatically
  ↓
Done (Jagriti sees it in her Odoo task at 5 PM)
```

---

## EXAMPLE FOR JAGRITI (HR MCP QA)

### Slack messages captured:
```
"Testing Okta provisioning - found bug in group sync"
"Leave management edge case: incorrect half-day calculation"
"Fixed bug, pushed to staging"
"QA approved for 2 of 5 test suites"
```

### GitHub commits captured:
```
[09:30] Fix: Okta group sync issue #234
[14:15] Refactor: Leave calculation logic
[16:45] Test: Add edge case coverage for half-days
```

### Summary Claude generates:
```
Daily QA Summary — Jagriti Chowdhury — Sep 5, 2026

Okta Provisioning:
- Tested full workflow, found bug in group sync
- Bug fixed and deployed to staging
- Status: Ready for re-testing

Leave Management:
- Edge case found: half-day calculation incorrect
- Root cause: Decimal rounding in business logic
- Fix deployed, new test coverage added
- Status: Awaiting re-test

Blockers: None
```

---

## HOW TO BUILD IT (THREE OPTIONS)

### Option 1: Zapier (30 minutes)
- Create Zap: Daily trigger at 5 PM
- Step 1: Read Slack messages (Slack API)
- Step 2: Read GitHub commits (GitHub API)
- Step 3: Call Claude API to summarize
- Step 4: Post to Odoo task
- Cost: $50-100/month
- Timeline: 30 min

### Option 2: Python Script (2-3 days)
- Write script that runs daily at 5 PM
- Script reads Slack → GitHub → calls Claude → posts to Odoo
- Cost: ~$0.50/month (Claude API only)
- Timeline: 2-3 days

### Option 3: Claude Cowork (1 week)
- Build recurring workflow in Cowork
- Cowork runs the automation, posts results
- Cost: Included in Cowork subscription
- Timeline: 1 week

---

## BENEFIT FOR JAGRITI

### Before (Manual):
```
5:00 PM: Check Slack for your messages (5 min)
5:10 PM: Check GitHub for your commits (5 min)
5:20 PM: Type summary in Odoo (10 min)
Total: 20 min/day × 250 working days = 83 hours/year
```

### After (Automated):
```
5:00 PM: Automation runs
5:01 PM: Summary posted to Odoo
You read it (2 min) to verify it's accurate
Total: 2 min/day × 250 days = 8 hours/year
Saved: 75 hours/year
```

---

## WHAT YOU NEED TO MAKE IT WORK

✅ Slack access (you have)
✅ GitHub access (if on team repo)
❓ Claude API key (ask Ayan)
❓ Odoo API access (ask Ayan)
✅ Daily task in Odoo (create "Daily QA Summary" recurring task)

---

## NEXT STEPS FOR JAGRITI

**This week:**
1. Ask Ayan for Claude API key + Odoo API access
2. Try Zapier version (30 min proof-of-concept)
3. Test it (post manually to Slack, watch summary generate)

**Next week:**
1. If it works, migrate to Python version (cheaper long-term)
2. Run it daily
3. Show Ron the output (he'll see your work automatically documented)

---

## KEY INSIGHT

This automation is **especially valuable for QA** because:
- Daily record of all bugs found + fixes tested
- Automatic handoff documentation
- Management visibility into your work
- No manual writing required
- Progress tracked automatically

It's like having a personal scribe who documents your day for you.
