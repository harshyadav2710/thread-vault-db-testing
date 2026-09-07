---
thread_name: "mcp-multiaccountconnection"
user: "harsh"
type: claude-chat
created: 2026-09-07
updated: 2026-09-07
---

## Render MCP Setup - Claude Desktop Configuration

**User Question:** What to do next after Render MCP deployment, connecting to Claude Desktop

**Context:**
- MCP server successfully deployed to Render
- Static bearer token auth (no OAuth)
- MCP Link: https://<your-service-name>.onrender.com/mcp
- Bearer Token: 8091c1c795108b61d60e3d9f28d6ae89763a088407caf52f91b6a6daabb6c8977

**Solution Provided - Add to Claude Desktop:**

### Steps:

**1. Open Claude Desktop Settings**
- Click ⚙️ Settings icon (bottom left)
- Navigate to Developer or Connectors
- Look for "Local MCP servers" or "MCP servers"

**2. Add Remote Server**
Click + button to add new MCP server with:
- **Name:** askcruz-email-harvester (or custom name)
- **Type/Transport:** Remote Server or HTTP/SSE
- **URL:** https://<your-service-name>.onrender.com/mcp (get actual URL from Render dashboard)
- **Authentication Type:** Bearer Token
- **Bearer Token:** 8091c1c795108b61d60e3d9f28d6ae89763a088407caf52f91b6a6daabb6c8977

**3. Save & Restart**
- Click Save/Connect
- Restart Claude Desktop
- MCP tools should now appear in conversations

### Notes:
- Do NOT use claude_desktop_config.json for remote servers — use the UI
- Config file is only for local MCP servers (stdio-based)
- Remote servers (HTTP/SSE) must be added through Settings UI
- If UI differs, look for "Add custom MCP server" or "Add remote MCP" options
