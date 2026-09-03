---
thread_name: "employee-list-query"
user: "harsh"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

## Employee List Query

User: list all the employees name that we currently have

Claude: I need to find the current employee list. Let me check what connectors and tools are available.

[Loaded threads-ov and raj-eoxs-vault skills]

I don't have access to the employee directory tool right now. The raj-eoxs-vault skill indicates there should be an eoxs-db employee directory with list_employees, search_employees, and get_employee tools, but those aren't currently available through the connectors I can reach.

The INTERNEL_TEAM_HETZNER connector I have access to covers clients, contacts, emails, calls, wiki pages, and implementation tasks — but not the employee directory.

To get the employee list, you'll need to either:
1. Provide direct access to the employee directory connector (eoxs-db)
2. Point me to where employee records are stored if they're elsewhere
3. Confirm if employee data is managed through a different system I should query

What would work best?

User: 1

Claude: Let me search for the eoxs-db employee directory connector.

[Searched for eoxs-db employee tools - not found in deferred tools]

Found it! The EOXS-Teams connector is installed and authenticated, but it's currently disabled in this chat. To access the employee directory, you need to enable it in this chat's connector settings.

[User: enabled]

Perfect! Now I can access the employee data. Let me load the EOXS-Teams tools and get your employee list.

[Loaded EOXS-Teams query and schema tools]

[Called get_business_schema - result too large, saved to file]

The EOXS-Teams database doesn't have an employee directory table. According to the raj-eoxs-vault skill, the employee directory actually lives in a different connector called eoxs-db, not EOXS-Teams.

[Checked all available connectors]

Found it! There's an HR-MCP connector that's installed and connected, but disabled in this chat. That's your employee directory. Please enable the HR-MCP connector in your connector settings to access the employee list.

User: don't use that

Claude: Understood. What would you like me to use instead to get the employee list?

The raj-eoxs-vault skill specifies eoxs-db for employee directory queries, but those tools aren't accessible through the currently enabled connectors. Should I:
1. Enable a different connector (like Raj-Vault, Internal-Team, or AskCruz)?
2. Query a different database/system?
3. Use a different approach altogether?

What's the right path for your setup?

User: 3.

Claude: What data source or method should I use? I have access to:

1. INTERNEL_TEAM_HETZNER tools — emails, calls, wiki, clients, contacts, implementation tasks, assets
2. EOXS-Teams — raw SQL against Odoo (sales, invoices, CRM, but no HR module)
3. AskCruz, Raj-Vault, Internal-Team — currently disabled connectors

Which of these has your employee data, or where should I look?

User: 1

Claude: [Searched wiki for "employees team members staff" - found scattered mentions across various pages]

[Searched wiki for "askcruz" - found AskCruz product/project information]

[Searched wiki for "team overview people" - found individual team member mentions]

Based on searching the internal wiki, I found mentions of current EOXS team members scattered across various pages, but not a single comprehensive employee roster. From what's documented, current team members include:

1. Rajat Jain (founder/CEO)
2. Isha Bisht (HR lead)
3. Disha Acharia (disha@eoxsteam.com) — employee onboarding/offboarding
4. Kasif Nawaz — attendance/productivity
5. Sheenam Rawat (sheenam@eoxsteam.com) — Head of Marketing
6. Yash Motghare — marketing
7. Sakshi — marketing
8. Aryan Bakshi — full-time (as of Oct 1, 2025; was intern)
9. Michael Mercadante — technology/process transformation
10. Ayan Dutta — AskCruz team
11. Sebastian Roa Viertel — SDR (started Aug 27, 2026)
12. Ron J — infrastructure/DevOps
13. Nishant Patel — team member
14. Ankit Thakur (contractor) — daily work logs

There's no single "all employees" page in the available wiki. For a complete current roster with titles and departments, you'd need access to the HR module directly or ask Rajat/Isha Bisht for an official headcount list.

Want me to pull more details on any of these people?
