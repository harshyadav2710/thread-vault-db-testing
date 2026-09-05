---
thread_name: "mystery-cases-mcp-setup"
user: "harsh"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

# Building a Custom MCP Server for Mystery Cases Repository

## User Request
User wants detailed instructions on how to build their own MCP (Model Context Protocol) server to connect their GitHub-hosted mystery/murder case data to Claude.

They have:
- Obsidian file with raw case information
- Used Claude Code in VS Code to ingest data into a wiki
- Created a GitHub repository connected to Claude Code
- Now needs steps to build and configure an MCP server

## Assistant's Response: Complete MCP Server Build Guide

### Part 1: Project Setup
1. Create new directory and initialize npm project
2. Install dependencies: `@modelcontextprotocol/sdk`, `zod`
3. Install dev dependencies: `typescript`, `@types/node`, `tsx`
4. Configure `tsconfig.json` with critical settings (`"module": "Node16"` and `"moduleResolution": "Node16"`)
5. Update `package.json` with proper bin, type: "module", and scripts

### Part 2: Build the MCP Server
**Created a complete `src/index.ts` template with:**
- Server initialization using Anthropic's MCP SDK
- Three tool definitions:
  - `search_cases`: Search cases by keyword
  - `get_case_details`: Retrieve full case information
  - `list_cases`: List all available cases
- Tool handler implementations with mock data
- Request handlers for tool listing and execution
- Error handling and stdio transport setup

### Part 3: Connect to Claude Code
- Build the server: `npm run build`
- Add to Claude Code: `claude mcp add mystery-cases-mcp node dist/index.js --scope project`
- Verify connection: `claude mcp list`
- Test by asking Claude to search cases

### Part 4: Integrate Real Data from GitHub
Provided enhanced `loadCasesFromGitHub()` function using:
- Octokit library for GitHub API access
- Reads markdown files from GitHub repository
- Uses `GITHUB_TOKEN` environment variable for authentication
- Installation: `npm install @octokit/rest`

### Part 5: Optional Deployment
- For remote access: Use SSE (Server-Sent Events) transport
- Deploy to services like Railway, Heroku, or Fly.io

### Additional Resources
- File structure template
- Troubleshooting table with common issues and solutions
- Referenced official MCP SDK documentation and community tutorials from:
  - DEV Community guides (10-20 minute tutorials)
  - TypeScript SDK repository
  - Snyk and other developer guides
  - HuggingFace MCP Course Unit 3
