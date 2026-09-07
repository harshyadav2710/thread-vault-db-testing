---
thread_name: "skill-creation-inquiry"
user: "harsh"
type: claude-chat
created: 2026-09-07
updated: 2026-09-07
---

# Skill Creation: Clarify and Plan - Detailed Breakdown

## User Request
Create a skill file where Claude:
1. Takes a user prompt
2. Asks clarifying questions
3. Asks until direction is clear
4. Creates a detailed plan

## Clarification Provided
- Use Case: General-purpose skill (works across all domains)
- Next Action: Create detailed plan after understanding direction

## User Feedback - Key Principle
"Do not take assumptions if you don't have knowledge on that question and also you can ask me question before you give me an answer."

## Skill Proposal: "clarify-and-plan" - Initial Version

### Overview
A 3-phase skill that guides Claude to be a Clarification and Planning Assistant.

### Phase 1: Initial Understanding
6 W's Framework: What, Why, Who, When, Where, How

### Phase 2: Iterative Clarification
Reflect, validate, follow-up, stop when clear

### Phase 3: Detailed Planning
8-part structured plan: Goal Statement, Success Criteria, Key Assumptions, Constraints & Dependencies, Phase Breakdown, Resources & Tools, Risk & Mitigation, Next Immediate Steps

## User Enhancement Request - 12 Suggested Additional Points

1. **Assumption Tracking & Validation** - List and validate assumptions before proceeding
2. **Knowledge Boundary Declaration** - Be transparent about what Claude doesn't know
3. **Question-First Approach** (Core) - Never suggest solutions before understanding context
4. **Information Source Verification** - Ask where information comes from
5. **Clarifying Hidden Assumptions** - Dig into vague terms like "quickly" or "limited budget"
6. **Confirmation at Each Step** - Confirm understanding before moving to next phase
7. **Distinguish Known vs. Unknown** - Clear lists of Known/Unknown/Assumptions
8. **Ask Before Recommending** - Ask questions instead of suggesting solutions directly
9. **Validate Competing Information** - Clarify contradictions rather than assume
10. **Context-First Mindset** - Get full background before structuring plan (Phase 0)
11. **Confirmation Checkpoints** - Validation gates before each major phase
12. **Request Clarification, Not Assumptions** - Language shift from assuming to asking

## Enhanced Core Principle
"Ask clarifying questions until direction is clear, NEVER make assumptions, NEVER recommend without context, and ALWAYS validate assumptions explicitly"

## Current Status
User indicated they want "Some specific ones" (not all 12). Asked user to specify which numbered points (1-12) they want included in the final skill file. Awaiting their selection.

Note: Model was switched to claude-sonnet-5 mid-session via /model command.
