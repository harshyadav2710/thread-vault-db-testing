---
thread_name: "odoo-backlog-tasks-lookup"
user: "harsh"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

# Finding Backlog Tasks in Odoo Dashboard

## User Query
How can I find the backlog tasks present in odoo dashboard?

Scope clarified: Looking for backlog tasks across all clients.

## Context
- User is Rajat Jain, EOXS CEO
- Query is about accessing implementation/Kanban backlog tasks in Odoo
- Primary objective: Keep EOXS stable while growing AskCruz to $1M ARR

## Response Provided

### UI Path to Access:
1. Go to Project > Implementation (or Kanban board view)
2. Filter by stage = "Backlog"
3. View all unscheduled tasks

### Current Backlog Summary:
- 9 backlog tasks across all clients (visible in this session)
- All tasks currently from Sabre Alloys "Soft Launch" project
- Owners: Faraz, Ernie, Ron Jain, Dhrup, Rajat Jain
- Priority: All Normal
- Timeline: Created April-May 2024, no recent activity
- Deadlines: Most have no deadline; 2 have past-due deadlines (April 2024)

Task examples:
- Order of multiple sales order lines
- Processing > Parent tags search refinement
- SO lines view
- Error handling for DWG in Sales order
- Post-launch cleanup (frontend/backend)

### Data Source
eoxs-db via list_implementation_tasks(stage="Backlog")
