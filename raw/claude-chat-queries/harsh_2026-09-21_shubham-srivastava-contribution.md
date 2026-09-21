---
thread_name: "shubham-srivastava-contribution"
user: "harsh"
type: claude-chat
created: 2026-09-21
updated: 2026-09-21
---

# EOXS Internals: Shubham Srivastava Contribution + Karpathy's Wiki Project

**Session Date:** 2026-09-21  
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
- **Shubham Srivastava (self-assigned)** ← focus
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

### Assignment Summary
- **Ayan Dutta:** 16 tasks (72.7% of project)
- **Jaskeerat Singh:** 3 tasks (13.6%)
- **Priyanshu Sinha:** 1 task (4.5%)
- **Unassigned:** 2 tasks (9.1%)

---

## Database Queries Executed
**Connector:** `mcp__Read-only__query` (AskCruz Odoo 13)

1. **Find Shubham Srivastava:** `SELECT * FROM hr_employee WHERE name = 'Shubham Srivastava'`
2. **Query Daily Snippets tasks:** `SELECT * FROM project_task WHERE project_id = 5 AND stage IN ('Ai Interns', 'Product Interns')`
3. **Identify Ai/Product Interns project:** `SELECT * FROM project_project WHERE name ILIKE '%karpathy%'` → No match
4. **List all projects:** `SELECT * FROM project_project` → Found "Ai/Product Interns" (ID 16)
5. **Query Ai/Product Interns tasks:** `SELECT * FROM project_task WHERE project_id = 16`
