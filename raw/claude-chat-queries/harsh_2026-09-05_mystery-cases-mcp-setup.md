---
thread_name: "mystery-cases-mcp-setup"
user: "harsh"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

# Mystery Cases MCP Server Setup

## User Query
The user has created a raw file in Obsidian containing information about mystery and murder cases. They:
1. Used Claude Code in VS Code to ingest the data into a wiki
2. Made a GitHub repo and connected it to Claude Code in VS Code
3. Now wants to create an MCP (Model Context Protocol) link to connect to Claude so they can search through the documents and get answers

## Assistant Response: Steps to Create an MCP Link

### 1. Choose or Build an MCP Server
**Option A: Use a pre-built MCP server (faster)**
- GitHub MCP (if available) - some MCP implementations support searching GitHub repos directly
- File-based MCP - if docs are in markdown/text format

**Option B: Build a custom MCP server (more flexible)**
- Create a Node.js or Python MCP server that:
  - Reads from GitHub repo (via git clone or GitHub API)
  - Indexes case files
  - Implements tools for searching/querying (e.g., `search_cases`, `get_case_details`)
  - Handles semantic search across case descriptions

### 2. If Building Custom - Structure
```
mystery-cases-mcp/
├── src/
│   └── server.ts (or server.py)
├── package.json (or requirements.txt)
├── .env (GitHub token)
└── README.md
```

**Minimal MCP server example (TypeScript/Node):**
- Use `@modelcontextprotocol/sdk` library
- Implement `list_resources` tool showing case files
- Implement `search_cases` tool to query data
- Implement `get_case` tool to retrieve full case details

### 3. Connect to Claude
**In Claude.ai:**
- Settings → Developer → MCP Servers
- Add MCP server URL (if deployed) or local SSE endpoint
- Test connection

**In Claude Code (VS Code):**
- Configure `.claude/claude.json` with MCP server details
- MCP server becomes available for tool use

### 4. GitHub Integration Details
- Store credentials: Add `GITHUB_TOKEN` to `.env`
- Fetch on demand: Server fetches files when queried, OR
- Pre-index: Clone repo into server, rebuild index periodically

### 5. Testing Before Full Integration
```bash
npm install (or pip install)
npm start (or python server.py)
# Then test tools with simple Claude conversation
```

## Follow-up Questions Asked
To provide more specific MCP server code examples, assistant requested clarification on:
- File format of case files (markdown, JSON, plain text)
- Search type needed (keyword vs semantic)
- Repository update frequency (static vs frequently updated)
