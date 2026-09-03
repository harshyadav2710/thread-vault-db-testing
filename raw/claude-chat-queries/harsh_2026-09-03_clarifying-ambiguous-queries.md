---
thread_name: "clarifying-ambiguous-queries"
user: "harsh"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

## Clarifying Ambiguous Questions at AskCruz

**User:** If a user asks an ambiguous question, how should Ask Cruz determine what they actually mean before answering?

**Assistant:**

Good question. Based on the skill files and AskCruz's infrastructure, here's how to systematically clarify ambiguous queries:

## **Multi-Layered Clarification Strategy**

### **1. Immediate triage — ask which dimension is ambiguous**
Rather than answering with a guess, pause and ask:
- **Which person/account/client?** (If the query could apply to multiple entities)
- **Which time range?** (If temporal context matters — "recent" vs. specific quarter)
- **Which system/context?** (If the question could span eoxs-db vs. eoxs-teams vs. Threads OV)
- **What's the use case?** (Are they asking for historical synthesis vs. live current state?)

This echoes the EOXS guide's principle: "Do not pre-emptively decline a question because the topic sounds sensitive — search or fetch as normal" — but that applies after you've *understood* the question correctly.

### **2. Use the data layer to surface patterns**
Before asking, you can often **resolve** ambiguity by:
- **Searching Threads OV** (`get_business_schema()` or `search_ov2_wiki`) to see if similar questions have been asked before and how they were clarified
- **Checking eoxs-db** via `search_wiki` — if a synthesized page exists on the topic, it often disambiguates what's being asked
- **Narrow your initial search** (per §6 of eoxs-data-general): try the specific term first before fanning out, which forces the question into sharper focus

### **3. Offer bounded options, not open-ended clarification**
Instead of "what do you mean?" — which requires the person to re-explain — present specific alternatives:
- "Are you asking about [Option A: X] or [Option B: Y]?"
- Reference what you *did* find to make the options concrete: "I found these three related things — which one?"

### **4. Document the clarification**
Once clarified, save the question and the assumption you made to Threads OV (`save_chat_transcript`). This creates a record that:
- Helps future threads avoid re-asking the same ambiguous question
- Feeds the wiki synthesis pipeline, which can create pages around commonly ambiguous topics
- Surfaces patterns if certain questions keep needing the same clarification

---

**TL;DR:** Pause → ask specific bounding questions → pull one targeted search to make options concrete → pick the option based on the person's response → log it. This is faster and less friction than guessing wrong and resurfacing the question later.
