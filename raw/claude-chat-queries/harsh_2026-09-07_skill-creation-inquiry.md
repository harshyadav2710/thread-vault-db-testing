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

## Skill Proposal: "clarify-and-plan"

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

### Example: Team Workflow Reorganization

**User Prompt**: "I want to reorganize my team's workflow"

**Phase 1 Questions**:
- What specifically feels broken? (Communication? Task tracking?)
- How many people on the team?
- When does this need to happen?
- What's the main pain point?

**Phase 2 Follow-ups** (after answers):
- Reflection: "So you have 8 people, 3 different tools, losing 2 hours/day?"
- Follow-ups: "Which tools must stay? What's your timeline? Who has final say?"

**Phase 3 Output**:
- Goal: Consolidate 3 tools to 1, reduce context switching from 2h to 30min/day
- Success: 100% adoption in 2 weeks, zero data loss
- Phases: Discovery (Week 1) → Setup (Week 2-3) → Training (Week 4) → Optimization (Week 5+)
- Immediate actions: Meet team, create comparison spreadsheet, demo tools, get approval

### Example: Writing Technical Guide

**User Prompt**: "Need to write technical guide for engineering team about new API"

**Phase 1 Questions**:
- Internal or public docs?
- Audience: junior or senior devs?
- How long? Quick reference or comprehensive?
- Deadline?
- Style guide to follow?

**Phase 2 Follow-ups**:
- Include setup/installation steps?
- Code examples? Which languages?
- Cover error handling and edge cases?
- Use existing documentation standards?

**Phase 3 Output**:
- Structure with Table of Contents
- Sections breakdown with specifics
- Code example specifications
- Timeline for each section
- Tools needed (diagrams, screenshots, API playground)
- Review and editing plan
- Ready-to-write outline

### Comparison: Regular Claude vs. This Skill

| Aspect | Regular Claude | This Skill |
|--------|----------------|-----------|
| Approach | Assumes understanding; jumps to output | Validates understanding first |
| Questions | May ask a few | Systematically asks until clarity |
| Output | Immediate | After full understanding |
| Structure | Consistent 3-phase framework |
| Confidence | You may get wrong plan | Plan based on deep understanding |

### When to Use This Skill

✅ Best for:
- Complex projects with unknowns
- Team initiatives needing buy-in
- Personal goals needing structure
- Major decisions/pivots
- Building something new with unclear scope

❌ Overkill for:
- Simple straightforward tasks
- Urgent situations needing immediate action
- Fully clear requirements

### Key Benefits
1. Prevents misunderstandings
2. Saves time (clarify upfront = faster execution)
3. Better plans (complete information, not assumptions)
4. Stakeholder alignment (agreement before starting)
5. Reduced rework (get it right first time)
6. Actionable output (execute immediately)

## User Follow-up
User wants to add more points to the skill file. Awaiting their input on what sections or guidelines to add.
