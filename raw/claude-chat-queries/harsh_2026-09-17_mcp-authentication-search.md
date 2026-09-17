---
thread_name: "mcp-authentication-search"
user: "harsh"
type: claude-chat
created: 2026-09-17
updated: 2026-09-17
---

# MCP Authentication Knowledge Base Search

**Date:** Friday, September 18, 2026  
**User:** Rajat Jain (CEO, EOXS)

---

## User Request

> Search my knowledge base for the concept "MCP authentication" and summarize the relevant information, including its source references.

---

## Search Process

1. **Initial Setup:** Read threads-ov unified routing skill and eoxs-data-general skill per user preferences
2. **Knowledge Base Query:** Searched for "MCP authentication" using available tools
3. **Source Identified:** Found relevant information in local memory file `/areas/wiki-llm.md`
4. **OAuth Token Configuration Issue:** Attempted to access OV2 GitHub wiki but OV2_GITHUB_TOKEN not configured

---

## Summary: MCP Authentication in Your Knowledge Base

### **Project: Wiki LLM — Tiered MCP System**

**Source:** `/areas/wiki-llm.md` (updated Sept 5, 2026)

**Overview:**  
You're building an internal knowledge LLM system with 3 separate MCP servers (one per access tier) to support personalized data access for EOXS internal users, customers, and partners.

### **Current Authentication Architecture**

| Aspect | Status |
|--------|--------|
| **Current State** | Zero authentication (all MCP URLs publicly accessible) |
| **Implementation Target** | Per-server OAuth with Bearer token validation |
| **Architecture** | Decentralized: each MCP server validates tokens independently |
| **Token Lifespan** | Long-lived tokens issued via shareable one-time links |
| **Token Scope** | Each token tied to specific tier + user for personalized access |

### **OAuth Implementation Details**

- **Initial approach:** GitHub OAuth for `personal-wiki-tier1.onrender.com`
- **Current approach:** Google OAuth (switched from GitHub)
- **Google OAuth Config:**
  - Client ID: `576411310302-vqbr1lvu5pn3i4o6ohg8nv24hrasnnhs.apps.googleusercontent.com`
  - Credentials stored in `GOOGLE_CREDENTIALS_JSON` environment variable
  - Callback endpoint: `/oauth/github/callback` (GitHub approach, not yet implemented for Google)
  
- **Known Issue:** Redirect URI mismatch — Google app config specifies localhost, but server runs on `https://personal-wiki-tier1.onrender.com`

### **Access Scope**

- **3 users** within EOXS have access to the system
- **External sharing** via individual shareable links for customers, partners, and integrators

### **Key Implementation Gap**

The Google OAuth redirect URI needs to be updated in your Google Cloud config to match your Render deployment domain.

---

## Additional Context

The wiki-llm system is part of your broader infrastructure to support:
- Tiered access control for EOXS internal knowledge
- Customer and partner integration via individual tokens
- Personalized data filtering per tier and user

**Status as of Sept 6, 2026:** Actively debugging OAuth configuration issues with Google implementation.
