---
thread_name: "connector-access-boundaries"
user: "harsh"
type: claude-chat
created: 2026-09-24
updated: 2026-09-24
---

# Connector Access Boundaries Analysis

## User Query
The user asked for a comprehensive breakdown of access boundaries across all MCP connectors they have connected. They want to understand:
1. How much data they can access from each connector
2. What data they cannot access or don't have permissions for
3. Information organized by connector

## Analysis Performed
1. Called checkpoint() to start conversation tracking
2. Used MCP registry to list all connected connectors
3. Analyzed each connector based on:
   - System reminder instructions for known connectors
   - Tool descriptions from deferred tool listings
   - Standard MCP access patterns

## Connectors Identified (9 Total)
1. **THREAD OV** - Chat transcripts and analysis (with mandatory auto-save)
2. **Thread Wiki** - Read-only SQL database access
3. **EOXS-TEAMS** - Database queries and metadata
4. **Intern Team** - Business/client data and communications
5. **Claude Docs** - Anthropic API documentation
6. **auth testing** - OAuth/auth testing environment
7. **HR** - Human resources data (highly restricted)
8. **Threads-OV** - Notes vault and transcript management
9. **visualize** - Visualization and widget generation

## Key Findings
- **Most connectors are READ-ONLY**: Thread Wiki, EOXS-TEAMS, Claude Docs, visualize
- **Limited Write Access**: THREAD OV, Threads-OV can create/save but not delete
- **Highest Restrictions**: HR connector (role/permission dependent)
- **Special Constraint**: THREAD OV requires mandatory save_chat_transcript() on every response

## Deliverable
Created comprehensive markdown document (`connector_access_boundaries.md`) with:
- Detailed access boundaries for each connector
- What can be accessed (✅)
- What cannot be accessed (❌)
- Key constraints and security recommendations
- Access control tier summary
