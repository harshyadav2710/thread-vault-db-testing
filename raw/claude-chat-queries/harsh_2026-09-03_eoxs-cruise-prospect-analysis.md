---
thread_name: "eoxs_cruise_prospect_analysis"
user: "harsh"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

# EOXS Cruise Product — Top 10 Prospect Analysis Request

## User Request
Go through team EOXS MCP. In the CRM module, find prospect cards with company information and notes. Analyze all logs to understand which prospects have criteria for the product. Then understand the Cruise product (company second brain), and identify the top 10 prospects best suited to sell this product. Find relevant information from all available MCPs.

## Context & Clarifications Provided
1. **Product**: Cruise is the company's second brain product
2. **Prospect Evaluation Criteria**: Company size, pain points, budget, existing solutions they use
3. **Ranking Factors**: Revenue/deal size, pipeline stage, timeline to close, engagement level
4. **Data Approach**: Pull data as-is, no transformation needed
5. **Include**: Deal history, communication logs, fit assessment focus

## Skills Reviewed
- eoxs-data-general: Navigation guide for EOXS-db (synthesized second brain) and eoxs-teams (raw SQL for CRM/pipeline/prospect data)
- threads-ov: Mandatory transcript saving for every response

## Current Status
Attempted to load EOXS connector tools through tool_search, but the actual tools from EOXS-TEAMS-MCP and EOXS-DATA-GENERAL are not loading in this session, despite being listed as connected MCP servers.

## Next Steps Required
Need to either:
1. Use Anthropic API in an artifact to call EOXS tools directly (via MCP server integration)
2. Search Threads OV for existing analyses/syntheses on prospects and Cruise product
3. Confirm correct method to access EOXS connectors in this session
