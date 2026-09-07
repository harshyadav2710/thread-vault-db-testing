---
thread_name: "render-github-connection"
user: "harsh"
type: claude-chat
created: 2026-09-07
updated: 2026-09-07
---

## Render Deployment Setup

**User Question:** How to connect a repo to Render (screenshot showed New Blueprint interface with GitHub option)

**Answer Provided:**

### Connection Steps

1. **Authorize with GitHub** (if not already done)
   - Click "Configure account" in the GitHub section
   - Authorize Render to access your GitHub repos

2. **Select Your Repository**
   - Once authenticated, search for or select **`jagriti-14/askcruz-email-harvester`** in the "Connect a repository" search box
   - Click **Connect** on the repository listing

3. **Create the Blueprint Instance**
   - After connecting, you'll configure the blueprint settings
   - Set your environment variables (if needed for OAuth, database URLs, API keys)
   - Choose the branch to deploy from (usually `main`)
   - Set any runtime settings

4. **Deploy**
   - Click "Create Blueprint Instance" to deploy
   - Render will trigger an auto-deployment whenever you push to that branch

### For 3GM Outlook Testing Specifically

Since you're testing OAuth and email deduplication, make sure your Render environment has:
- Outlook OAuth credentials configured as environment variables
- Database connection strings if needed for the 6-table schema
- Any API keys or tokens required

If you get stuck on environment variable setup or OAuth configuration, let me know—Render's documentation on secrets and environment vars is solid, but the OAuth flow with Outlook can have some gotchas.
