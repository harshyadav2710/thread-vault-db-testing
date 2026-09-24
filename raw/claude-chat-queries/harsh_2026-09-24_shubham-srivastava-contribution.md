---
thread_name: "shubham-srivastava-contribution"
user: "harsh"
type: claude-chat
created: 2026-09-24
updated: 2026-09-24
---

# EOXS Internals: Shubham Srivastava + Yash Sharma Task Investigation

**Session Date:** 2026-09-21 to 2026-09-24  
**Queried by:** Dhanshree Ratneria (AI Interns, AskCruz)

---

## Part 1: Shubham Srivastava Profile & Daily Snippets Project

### Employee Profile (AskCruz Odoo 13)
| Field | Value |
|---|---|
| Employee ID | 45 |
| User ID | 154 |
| Name | Shubham Srivastava |
| Job Title | AI Intern |
| Department | Product |

### Daily Snippets Project Assignment
| Attribute | Value |
|---|---|
| Task ID | 344 |
| Project | Daily Snippets |
| Stage | Ai Interns |
| Assigned To | Self |
| Status | In Progress |
| Priority | 0 (Normal) |
| Created | 2026-08-25 18:04:45 |
| Deadline | Not set |
| Planned Hours | None |
| Effective Hours | 0.0 |

### Daily Snippets — AI Interns Stage (14 total)
- Radhesh Tinani (unassigned)
- **Shubham Srivastava (self-assigned)**
- Vaibhav Tez Shakya (self-assigned)
- Abhishek Maurya (unassigned)
- Utkarsh Sharma (self-assigned)
- Mohan Dwivedi (unassigned)
- Tanvi Kumari (self-assigned)
- Lakshit Singh (unassigned)
- Jatin Rao (unassigned)
- Himanshu Kumar (unassigned)
- Yash Sharma (self-assigned)
- Dhanshree Ratneria (self-assigned)
- Dhruv Maheshwari (unassigned)
- Harsh Yadav AI (assigned to Harsh Yadav)

### Daily Snippets — Product Interns Stage (5 total)
- Himanshu Vashisth (unassigned)
- Harsh Yadav (assigned to Jaskeerat Singh)
- Jagriti (assigned to Nidhi Rana)
- Aditya Yadav (assigned to Nidhi Rana)
- Priyanshu Sinha (assigned to Ayan Dutta)

---

## Part 2: Karpathy's Wiki Project Details

**Project Name:** Ai/Product Interns (Project ID: 16)  
**Total Tasks:** 22

### Primary Karpathy's Wiki Tasks
| Task ID | Task Name | Assigned To |
|---------|-----------|-------------|
| 320 | Karpathy's wiki | Ayan Dutta |
| 426 | Karpathy's wiki/Second Brain | Ayan Dutta |

### All Tasks in Ai/Product Interns Project
| Task ID | Task Name | Assigned To |
|---------|-----------|-------------|
| 581 | Higgsfield open ai research | Ayan Dutta |
| 579 | testing the mcp | (unassigned) |
| 572 | Create Cross-Team Project Instructions | Jaskeerat Singh |
| 571 | Identify Scalable Alternatives to Claude | Priyanshu Sinha |
| 558 | Improving Skills.md priority over memory in claude | Jaskeerat Singh |
| 551 | Attachment data population through automation db | Ayan Dutta |
| 543 | Thread saving | Jaskeerat Singh |
| 540 | Test task | (unassigned) |
| 527 | MCP Write Function | Ayan Dutta |
| 502 | O-Auth connection | Ayan Dutta |
| 486 | Second brain automation | Ayan Dutta |
| 427 | OAuth Credentials | Ayan Dutta |
| 424 | Threads-wiki-local | Jaskeerat Singh |
| 365 | SOP, Product & Market Fit File Review & Error Identification | Ayan Dutta |
| 359 | Postgres Structure/MCP | Ayan Dutta |
| 358 | Access Rights on MCP | Ayan Dutta |
| 323 | Onboarding | Ayan Dutta |
| 263 | SOP File Generation | Ayan Dutta |
| 221 | AskCruz Claude Feedback | Ayan Dutta |
| 194 | Product/Pitch Deck | Ayan Dutta |

### Assignment Summary (Ai/Product Interns)
- **Ayan Dutta:** 16 tasks (72.7% of project)
- **Jaskeerat Singh:** 3 tasks (13.6%)
- **Priyanshu Sinha:** 1 task (4.5%)
- **Unassigned:** 2 tasks (9.1%)

---

## Part 3: Yash Sharma Profile & Task Completion

### Employee Profile (AskCruz Odoo 13)
| Field | Value |
|---|---|
| Employee ID | 55 |
| User ID | 155 |
| Name | Yash Sharma |
| Job Title | AI Intern |
| Department | Product |

### Daily Snippets Project Assignment
| Attribute | Value |
|---|---|
| Task ID | 330 |
| Task Name | Yash Sharma |
| Project | Daily Snippets |
| Stage | Ai Interns (Stage ID: 423) |
| Assigned To | Self |
| Status | **In Progress** (NOT Completed) |
| Kanban State | normal |
| Development State | developing |
| Progress | 0% |
| Created | 2026-08-25 17:53:59 |
| Last Updated | 2026-09-14 19:34:30 |
| Date Assigned | 2026-08-25 20:24:33 |
| Last Stage Update | 2026-08-26 21:39:09 |
| Planned Hours | None |
| Effective Hours | 0.0 |
| Date Deadline | Not set |

### Task Completion Summary for Yash Sharma
- **Total Tasks Assigned:** 1
- **Completed Tasks:** 0
- **In Progress Tasks:** 1 (Task 330)
- **Completion Rate:** 0%
- **Total Hours Logged:** 0.0 hours

---

## Comparison: Shubham vs Yash
| Aspect | Shubham Srivastava | Yash Sharma |
|--------|-------------------|------------|
| Employee ID | 45 | 55 |
| User ID | 154 | 155 |
| Department | Product | Product |
| Job Title | AI Intern | AI Intern |
| Total Tasks | 1 | 1 |
| Completed Tasks | 0 | 0 |
| In Progress Tasks | 1 | 1 |
| Effective Hours | 0.0 | 0.0 |
| Created | 2026-08-25 18:04:45 | 2026-08-25 17:53:59 |
| Last Updated | (not checked) | 2026-09-14 19:34:30 |
| Progress | (not checked) | 0% |

---

## Database Queries Executed
**Connector:** `mcp__Read-only__query` (AskCruz Odoo 13)

1. Shubham Srivastava employee lookup
2. Shubham's task assignments
3. Daily Snippets project (ID 5) all tasks by stage
4. Ai/Product Interns project (ID 16) all tasks
5. Yash Sharma employee lookup: `SELECT * FROM hr_employee WHERE name = 'Yash Sharma'`
6. Yash's task assignments: `SELECT * FROM project_task WHERE user_id = 155`
7. Yash's full task detail: `SELECT * FROM project_task WHERE user_id = 155`
8. Daily Snippets stages breakdown: `SELECT DISTINCT pt.stage_id, COUNT(pt.id) as task_count FROM project_task WHERE project_id = 5 GROUP BY pt.stage_id`
