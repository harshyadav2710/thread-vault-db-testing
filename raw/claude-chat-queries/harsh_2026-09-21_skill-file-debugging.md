---
thread_name: "skill-file-debugging"
user: "harsh"
type: claude-chat
created: 2026-09-21
updated: 2026-09-21
---

# Skill File Debugging - Tool Calling Issues

**User Question:** How to improve skill file? Is the skill file issue why correct tool calling is not happening?

**Response:** Need more information to diagnose:

1. **Skill file content** — full SKILL.md
2. **Tool calling failure** — which tools should trigger but don't?
3. **Usage scenario** — what is the user asking Claude to do?
4. **Behavior observed** — is skill ignored, loaded incorrectly, or applied wrong?

**Common causes of tool calling failures:**
- Trigger description too vague/generic
- Description doesn't match skill purpose
- Skill name conflicts with other skills
- Missing context about when to use it
- Tool dependencies not available
- Instructions too abstract

**Next step:** User will provide skill file for analysis
