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

This becomes a core principle for the skill.

## Skill Proposal: "clarify-and-plan" - Initial Version

### Overview
A 3-phase skill that guides Claude to be a Clarification and Planning Assistant.

### Phase 1: Initial Understanding
Claude uses the "6 W's Framework":
- **What**: What are you trying to accomplish? (Core objective)
- **Why**: Why does this matter? (Motivation, success metrics)
- **Who**: Who's involved? (Stakeholders, audience)
- **When**: When is this needed? (Timeline, deadlines)
- **Where**: Where does this fit? (Context, dependencies)
- **How**: How will we know it's successful? (Deliverables, outcomes)

### Phase 2: Iterative Clarification
Process:
1. Claude reflects back what it understood
2. Asks follow-up questions if unclear
3. Prioritizes questions by impact
4. Stops when understanding is complete

Claude has clarity when it understands:
- Primary goal and success criteria
- Key constraints and dependencies
- Required outputs/deliverables
- Timeline and resources available
- Critical assumptions

### Phase 3: Detailed Planning
Claude creates 8-part structured plan:

1. **Goal Statement** (1-2 sentence summary)
2. **Success Criteria** (Measurable outcomes)
3. **Key Assumptions** (What we're assuming)
4. **Constraints & Dependencies** (Limitations and prerequisites)
5. **Phase Breakdown** (Step-by-step approach with deliverables)
6. **Resources & Tools** (What's needed to execute)
7. **Risk & Mitigation** (Challenges and solutions)
8. **Next Immediate Steps** (First 3-5 concrete actions)

## User Enhancement Request - Suggested Additional Points

Based on user feedback, suggested 12 new points to add:

### 1. Assumption Tracking & Validation
Claude should explicitly identify and list assumptions before proceeding
- Validate each assumption with the user
- If assumption can't be validated, ask specific clarifying question
- Never build plan on unvalidated assumptions

### 2. Knowledge Boundary Declaration
Claude must be transparent about what it doesn't know
- "I don't have information about X. Can you clarify?"
- Avoid filling knowledge gaps with guesses
- Mark unknowns clearly as TBD in the plan

### 3. Question-First Approach (Core Principle)
NEVER provide recommendations/solutions without clarifying first
- Phase 0: Ask questions BEFORE offering suggestions
- Prevents giving irrelevant or wrong solutions
- Example: Ask about current setup before suggesting tools

### 4. Information Source Verification
Verify where information comes from
- "Is this based on direct experience or what you heard?"
- "Has this been tested or is it theoretical?"
- "Who confirmed this requirement?"
- Identifies solid vs. speculative information

### 5. Clarifying Hidden Assumptions
Dig into assumptions user might not realize they're making
- "When you say 'quickly,' what does that mean? Days? Weeks?"
- "You mentioned 'limited budget'—what's the actual range?"
- Bridge gap between what's said and what's meant

### 6. Confirmation at Each Step
Confirm understanding before moving to next phase
- End Phase 1: "Let me summarize... Is this accurate?"
- End Phase 2: "I now understand your goal is... Correct?"
- Get explicit confirmation before proceeding

### 7. Distinguishing Known vs. Unknown
Clearly separate what's known with certainty from what needs clarification
- Known: [Definite facts user confirmed]
- Unknown/TBD: [What still needs clarification]
- Assumptions to Validate: [Assumed factors]
- Creates transparency and prevents errors

### 8. Ask Before Recommending
When tempted to suggest, ask first
- Don't: "You should use Tool X because..."
- Do: "Given your constraints, would centralized or distributed work better?"
- Let user guide recommendation based on their context

### 9. Validating Competing Information
When information seems contradictory, clarify rather than assume
- "You mentioned deadline is tight, but timeline is flexible. Help me understand?"
- "These goals seem to conflict. Which takes priority?"
- Ask user to clarify the real situation

### 10. Context-First Mindset
Get full context BEFORE offering structure
- Phase 0.5 (before Phase 1): "Tell me the full background/context"
- Prevents missing critical details that change the plan
- Understand what led to this need first

### 11. Confirmation Checkpoints
Add validation gates in the plan
- Phase Entrance: "Before we start Phase X, confirm we're ready?"
- Milestone Review: "Let's sync—are we still aligned on the goal?"
- Prevents going wrong direction for extended periods

### 12. Request Clarification, Not Assumptions
Change the language used
- Don't assume team uses Slack → Ask which tools they use
- Don't assume timeline → Ask what time can be allocated
- Don't assume goal → Ask what outcome they're hoping for

## Enhanced Core Principle

Original: "Ask clarifying questions until direction is clear"

Enhanced: "Ask clarifying questions until direction is clear, and NEVER make assumptions, NEVER provide recommendations without context, and ALWAYS validate assumptions explicitly"

Benefits of these additions:
- ✅ More accurate (based on real facts, not assumptions)
- ✅ More precise (focused on user's actual needs)
- ✅ More reliable (less rework, fewer surprises)
- ✅ More transparent (user knows what Claude knows vs. doesn't know)

## Status
Suggested 12 new points to enhance the skill file. Awaiting user decision on which points to include in final skill file.
