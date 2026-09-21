---
thread_name: "harsh-yadav-contribution-lookup"
user: "harsh"
type: claude-chat
created: 2026-09-21
updated: 2026-09-21
---

# Harsh Yadav Contribution Lookup - Complete Read-Only MCP Analysis

## Query Sequence
1. Initial query: "What is the contribution of Harsh Yadav on which project did he works?"
2. Follow-up: "check in askcruz board"
3. Final: "can u try to check read only mcp try to fetch from this"

## Read-Only MCP Connector Results

### Employee Profile (from hr_employee + hr_department + hr_job)
```
Employee ID: 53
User ID: 151
Name: Harsh Yadav
Work Email: harshy@askcruz.com
Department: Product
Job Title: AI Intern
Status: Active
Joined Date: Aug 27, 2026 12:55:59
```

### Project Assignment (from project_project)
```
Project ID: 5
Project Name: Daily Snippets
Project Manager: Ayan Dutta (Implementation Head, User ID: 7)
Total Tasks in Project: 37
Project Active: Yes
Start Date: Not set
End Date: Not set
Partner: Not set
```

### Task Assignment (from project_task + project_task_type)
```
Task ID: 325
Task Name: Harsh Yadav AI
Project: Daily Snippets (ID: 5)
Stage: Ai Interns
Priority: Normal (0)
Kanban State: Normal
Created Date: Aug 25, 2026 17:48:55
Created By: Isha Bisht
Last Updated: Aug 27, 2026 18:49:46
Deadline: Not set
Parent Task: None
Progress: 0.0%
Planned Hours: Null
Effective Hours: 0.0
Total Hours Spent: 0.0
Description: (Empty - contains only HTML br tag)
```

### Subtasks (from project_task WHERE parent_id = 325)
Result: **No subtasks found**

### Training Applications (from emp_training_application)
Result: **No training applications found**

### Summary Metrics
- **Tasks Assigned:** 1
- **Tasks Created:** 0
- **Tasks Edited:** 0
- **Subtasks:** 0
- **Training Programs:** 0
- **Total Hours Logged:** 0.0

## Final Conclusion
Harsh Yadav is an **AI Intern in the Product Department** with a single active assignment on the **Daily Snippets** project (managed by Ayan Dutta). His only task is "Harsh Yadav AI" in the Ai Interns stage, which was created Aug 25, 2026 and has not yet logged any working hours.

**Data Source:** Read-Only MCP Connector (askcruz database via teams-askcruz)
**Query Date:** 2026-09-21
**Connector Type:** Universal Read-Only AskCruz Connector
