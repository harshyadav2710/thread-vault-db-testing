---
thread_name: "shubham-srivastava-contribution"
user: "harsh"
type: claude-chat
created: 2026-09-21
updated: 2026-09-21
---

# EOXS Internals: Shubham Srivastava Contribution Investigation
**Session Date:** 2026-09-21  
**Queried by:** Dhanshree Ratneria (AI Interns, AskCruz)

---

## Initial Query: Shubham Srivastava Profile & Contributions

### Employee Profile (AskCruz Odoo 13)
| Field | Value |
|---|---|
| Employee ID | 45 |
| User ID | 154 |
| Name | Shubham Srivastava |
| Job Title | AI Intern |
| Department | Product |

### Project Assignment (Daily Snippets)
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

## Database Query Details
**Connector Used:** `mcp__Read-only__query` (AskCruz Odoo 13)  
**Queries Executed:**
1. `SELECT * FROM hr_employee WHERE name ILIKE '%shubham%'` → Found employee_id 45
2. `SELECT * FROM hr_employee WHERE name = 'Shubham Srivastava'` → user_id 154, dept: Product
3. `SELECT * FROM project_task WHERE user_id = 154` → 1 task (344, Daily Snippets)
4. `SELECT * FROM project_task WHERE project_id = Daily Snippets AND stage IN ('Ai Interns', 'Product Interns')` → 19 rows

---

## Follow-up: Wiki Search for "Karpathy"
**Status:** No matching wiki page found.

User requested: "Ai/Product Interns inside this Karpathy's wiki try now"  
**Result:** Internal wiki search for "Karpathy" returned empty. Title or reference unclear.

**Next step:** Awaiting clarification on what "Karpathy's wiki" refers to.
