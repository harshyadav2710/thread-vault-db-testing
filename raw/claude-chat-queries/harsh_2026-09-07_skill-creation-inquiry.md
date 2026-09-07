---
thread_name: "skill-creation-inquiry"
user: "harsh"
type: claude-chat
created: 2026-09-07
updated: 2026-09-07
---

# Skill Creation: Clarify and Plan

## User Request
The user wanted to create a skill file for Claude where they can:
1. Give a prompt to Claude
2. Have Claude act accordingly
3. Have Claude ask clarifying questions until the direction is clear
4. Get a detailed plan once clarity is achieved

## Clarification Questions
- **Use Case**: General-purpose skill (not limited to one domain)
- **Next Action**: Create a detailed plan after understanding the direction

## Skill Created: "clarify-and-plan"

### Overview
A three-phase skill that guides Claude to be a Clarification and Planning Assistant:

### Phase 1: Initial Understanding
- Acknowledge the user's prompt
- Identify gaps in understanding
- Ask clarifying questions about: What, Why, Who, When, Where, How

### Phase 2: Iterative Clarification
- Validate understanding by reflecting back
- Ask follow-up questions if unclear
- Prioritize questions by impact
- Stop when direction is clear

### Phase 3: Detailed Planning
Once clarity is achieved, create a structured plan including:
1. Goal Statement
2. Success Criteria
3. Key Assumptions
4. Constraints & Dependencies
5. Phase Breakdown
6. Resources & Tools
7. Risk & Mitigation
8. Next Immediate Steps

### Key Principles
- Ask, don't assume
- Reflect understanding
- Be thorough but concise
- Prioritize impact
- Stop when ready
- Make plans actionable

## Status
Skill proposal presented to user for review and acceptance.
