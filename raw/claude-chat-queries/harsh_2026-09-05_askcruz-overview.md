---
thread_name: "askcruz-overview"
user: "harsh"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

## How to Build Reusable MCP Servers — Beginner Explanation

**User Question:** "How can we build reusable MCP servers? Make me understand like I'm a beginner. Don't make me understand step by step. Just tell me in short: how to build, how it can be helpful, what things I need, is it already built, what challenges?"

---

## WHAT IS AN MCP SERVER? (30-Second Version)

Think of an MCP server as a **"translator plug"** for Claude.

Just like a USB adapter lets different devices talk to each other, an MCP server lets Claude talk to Outlook, Odoo, Postgres, or any system without Claude knowing the specific details.

**Real example:**
- Claude needs to deduplicate 50K emails from 3GM's Outlook
- Claude doesn't natively speak "Outlook API"
- An MCP server translates: Claude asks → MCP server calls Outlook → Gets emails → Deduplicates → Returns result to Claude
- Claude doesn't need to learn Outlook; the MCP server is the translator

---

## HOW DO YOU BUILD ONE? (Short Version, No Step-by-Steps)

You write code that tells Claude:
```
"When you need to deduplicate emails, call my email_dedup function"
"When you need task info, call my fetch_tasks function"  
"When you need to verify the database schema, call my validate_schema function"
```

That's it. You're defining: **"Here are the functions Claude can call, what they do, what data they need."**

**The building blocks you need:**
1. **Python SDK or TypeScript SDK** (Anthropic provides these)
2. **Your business logic** (code that talks to Outlook, deduplicates, validates)
3. **Function definitions** (telling Claude what each function does)
4. **Authentication** (OAuth for Outlook, DB credentials for Postgres, etc.)

**Code length:** ~200 lines for a basic MCP server. Most of it is boilerplate the SDK handles.

---

## HOW IS IT HELPFUL FOR ASKCRUZ?

**Current pain point:**
- 3GM needs email integration → You write OAuth + dedup logic (2-3 weeks)
- Sabre Alloys needs email integration → You write the same OAuth + dedup logic again (2-3 weeks)
- Three D Metals needs it → Same work again (2-3 weeks)
- Legal services prospect → Same work again (2-3 weeks)
- Total: 8-12 weeks for 4 clients doing the identical task

**With a reusable MCP server:**
- Build the email_dedup MCP once (2-3 weeks)
- Use for 3GM: Point it at 3GM's Outlook, set credentials (1 day)
- Use for Sabre: Point it at Sabre's Outlook, set credentials (1 day)
- Use for Three D: Same MCP, new credentials (1 day)
- Use for legal services: Same MCP, new credentials (1 day)
- Total: 2-3 weeks + 4 days = same as before BUT you only do the hard work once

**Real time saved:** Instead of rebuilding the core logic 4 times, you build it once and reuse it.

**Money saved:** Processing 3GM's 50K emails with prompt caching + one MCP: $20. Processing 4 clients' emails: ~$100 total (instead of building 4 separate integrations that cost $400+ in setup time).

---

## IS IT ALREADY BUILT?

**Partial answer: Yes, but not for your specific use case.**

**Pre-built MCP servers from Anthropic:**
- Google Drive (read files)
- Slack (send messages, read channels)
- GitHub (read repos, commits)
- Git (local git operations)
- Postgres (query databases)
- Puppeteer (browse websites)
- Linear (read/write tasks)
- Notion (read/write docs)

**What's NOT built:** There is no pre-built Outlook email deduplication MCP that AskCruz needs. You'll have to write that.

**But here's the good news:**
- Gmail MCP exists (Anthropic published it)
- Email OAuth patterns are standard (don't need to build from scratch)
- Deduplication logic is straightforward to code
- The Python SDK handles 80% of the boilerplate for you

**Reality:** You're writing 20% custom code + using 80% of Anthropic's templates.

---

## CHALLENGES YOU WILL FACE

### **Challenge 1: Silent Installation Failures**
**The problem:** You build the MCP, test it locally, it works. You configure it in Claude Desktop, restart Claude Desktop... nothing happens. No error message. No connection. Just silence.

**Why it happens:** Your code prints something to stdout that breaks the JSON-RPC stream. Claude doesn't report errors for this; it just disconnects silently.

**Real stats:** April 2026 analysis of 2,181 remote MCP servers found:
- 52% were completely dead
- 39% were degraded (slow, stale data, failing silently)
- Only 9% were fully healthy

**How to fix it:** Always log to stderr, never stdout. Tail the log file while testing.

---

### **Challenge 2: Scaling Breaks Everything**
**The problem:** Your MCP works great for 3GM (one user). You try to run it for Sabre + Three D Metals simultaneously, and sessions start colliding or conflicting.

**Why it happens:** The current MCP spec (through April 2026) assumes one user per server instance. When you have multiple users/sessions, state management becomes a nightmare. Load balancers try to distribute traffic, but MCP requires sticky routing (always hitting the same server instance). This defeats the purpose of load balancing.

**The 2026 fix:** Anthropic released a 2026-07-28 spec update that makes servers "stateless," but it just landed in beta. You might have to wait or work around it.

**Real-world example:** An engineer managing 200 engineers found 14 MCP servers across the org, at least 4 were duplicates built by different teams who didn't know the other existed.

---

### **Challenge 3: Credential Sprawl**
**The problem:** 3GM uses OAuth for Outlook on tenant A. Sabre uses OAuth on tenant B. Three D Metals uses tenant C. Soon you have 5+ different credential sets floating around, and you're manually managing which credentials go where.

**Why it happens:** MCP doesn't have built-in multi-tenant authentication. You have to manually handle who connects to which Outlook account.

**Deployment reality:** 86% of MCP servers still run on developer laptops. Only 5% actually deploy to production environments. The gap between "it works on my machine" and "it works reliably for all our customers" is where most teams get stuck.

**How to fix it:** Use an MCP Gateway platform (TrueFoundry MCP Gateway, or Gram) that handles credential vaulting automatically. Or build your own credential manager.

---

### **Challenge 4: Tool Schema Consistency at Scale**
**The problem:** You write the dedup MCP with input schema: "email_list". Six months later, you need to add "exclude_attachments: true". Now your schema changed, and you have to update it everywhere.

**Why it's hard:** When you have dozens or hundreds of tools across multiple MCPs, keeping tool definitions in sync with the actual API is a constant problem. It's like maintaining API documentation; when the API changes, the docs get stale.

**Real quote from Cloudsmith engineer:** "At scale, maintaining tool definitions becomes the bottleneck, not the protocol itself."

**How to fix it:** Use OpenAPI specs to auto-generate MCP tool definitions. Then when you update the OpenAPI spec once, MCPs regenerate automatically.

---

### **Challenge 5: Zero Audit Logging**
**The problem:** Claude calls your MCP to deduplicate 50K 3GM emails. Something goes wrong. You have no logs showing what Claude asked, what your MCP returned, or where the failure occurred.

**Why it happens:** MCP doesn't define a standard way to log who did what, when, and why. You have to build logging yourself.

**Enterprise blocker:** Security teams need to answer: "What did this agent do, when, and with whose authorization?" MCP has no standard way to answer this, so every company building it has to build custom logging.

**How to fix it:** Add logging middleware to your MCP. But it's not standardized, so you're building it from scratch.

---

### **Challenge 6: Deployment Is Harder Than Building**
**The problem:** Your MCP works locally. Deploying it to production (where Claude Code, Claude Desktop, and multiple clients can reach it reliably) requires:
- Infrastructure (EC2, Docker, Kubernetes, load balancer)
- Secrets management (OAuth tokens, DB credentials)
- Cold start handling (serverless MCPs can take 5+ seconds)
- Health checks and monitoring
- Retry logic and error handling

**Why it's hard:** MCP only defines the protocol. It doesn't handle deployment, scaling, or monitoring. You have to solve that yourself or use a platform.

**Real failure mode:** An org with 200 engineers discovered 4 duplicate MCP servers because teams didn't know the others existed, there was no central registry, and no governance.

**How to fix it:** Use managed MCP platforms (Gram, Cloudsmith's platform, TrueFoundry) that handle infrastructure. Or DIY with Kubernetes + an MCP Gateway.

---

## QUICK REFERENCE: CHALLENGE SUMMARY

| Challenge | Severity | Why It Happens | Quick Fix |
|-----------|----------|---|---|
| Silent installation failures | HIGH | Stdout pollution breaks JSON-RPC | Log to stderr only |
| Scaling to multiple users | HIGH | Spec assumes one user per instance | Use 2026-07-28 spec or wait |
| Credential sprawl | MEDIUM | No multi-tenant auth in MCP | Use MCP Gateway for vaulting |
| Schema consistency | MEDIUM | Manual tool definition updates get stale | Auto-generate from OpenAPI |
| No audit logging | HIGH | MCP doesn't define logging standard | Add custom logging middleware |
| Deployment complexity | CRITICAL | "Building is easy, deploying is hard" | Use managed platform or DIY with K8s |

---

## SHOULD YOU BUILD THIS FOR ASKCRUZ?

**Yes, but timing matters:**

✅ **Build it:** After 3GM launches successfully (mid-September)
✅ **Build it:** When you're onboarding Sabre Alloys or Three D Metals (Q4 2026)
✅ **Build it:** If you expect 4+ clients using email integration

❌ **Don't build it yet:** As a blocker for 3GM launch (use Claude Code + Gmail MCP directly instead)
❌ **Don't build it:** If you only need email integration for one client
❌ **Don't build it:** If your team has zero DevOps support

**Realistic timeline:**
- Build a basic MCP server: 2-3 weeks
- Deploy to production: 4-6 weeks (most teams get stuck here)
- Get all clients stable: 2-4 weeks more

**Better approach:** Launch 3GM with Claude Code + Gmail MCP. Once you understand all the edge cases, THEN build the reusable MCP server for Sabre.

---

## BOTTOM LINE

An MCP server is just a translator between Claude and your systems. Building one is ~200 lines of code using Anthropic's SDK. The value is massive if you need it for 3+ clients (save 2-3 weeks per client). But deployment and operations are where 95% of teams get stuck.

For AskCruz: Ship 3GM first. Then build the MCP server for the next client.
