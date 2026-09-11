---
thread_name: "askcruz-messaging-final-data-integration-skill"
user: "harsh"
type: claude-chat
created: 2026-09-11
updated: 2026-09-11
---

# AskCruz Messaging Strategy + OV Vault Data Integration Skill
## September 11, 2026

### Part 1: AskCruz Messaging Strategy (3GM Beachhead)

**Final Recommendation:** Position AskCruz for 3GM-type customers (20-100 person companies, single acute pain, one decision maker, operational efficiency focus).

**Core Message:** "Connect Claude to your company data. Stop manually pulling reports. Get answers in seconds."

**What to Lead With:**
1. Problem: Manual report pulling across ERP, email, spreadsheets
2. Solution: Connect Claude to actual company data once
3. Proof: 3GM case study
4. First win: Proposal Generation (auto-generate from pricing + customer history)

**Key Insight:** 3GM and Sabre are fundamentally different customer types:
- 3GM: Operational efficiency (one person, one use case, quick ROI)
- Sabre: Strategic insight (multi-stakeholder, multi-dimensional, architecture-driven)

**Action Items:**
1. Rewrite landing page (lead with "automated reports")
2. Reprice Phase 1 (Proposal Gen) for SMB ($X/month, 3-month min)
3. Find 5 more 3GM-type customers in 8 weeks
4. Freeze Sabre-sized deals until 10+ 3GMs signed

---

### Part 2: Data Integration Configuration Issue Identified

**The Problem:** 
- I fetched data from Raj's account when asked in the Cowork chat (Askcruz explainer video script)
- I did NOT automatically fetch it here (messaging strategy chat)
- I operated in "pull-only-on-request" mode, not "auto-discovery" mode
- This meant missing actual customer usage data that would have enriched the analysis

**Root Cause:** No unified data source routing configuration. I don't automatically know "what other sources might have relevant data about this entity?"

**Solution:** Create a skill-based data integration layer that maps every entity (customer, product, person) to all sources where information about them lives, and automatically fetches from all of them.

---

### Part 3: OV Vault + AskCruz Data Integration Skill Created

**File Created:** `/mnt/skills/user/ov-askcruz-data-integration/SKILL.md`

**What This Enables:**
1. Entity detection (when 3GM is mentioned)
2. Automatic source discovery (load entity-data-sources.md)
3. Batch fetch from all sources (documents + threads + calls + wiki + emails)
4. Smart prioritization (primary sources > analysis sources)
5. Deduplication and conflict resolution
6. Universal application across all Claude instances

**Configuration Required:**
1. Create `/config/entity-data-sources.md` at OV vault root (maps customers/products to all data sources)
2. Add data_integration settings to user preferences or .claude-config.md
3. Add data integration protocol to Claude system instructions
4. Ensure Raj's documents folder is queryable/indexed
5. Verify Thread Testing MCP contains customer threads

**Why This Matters:**
- Every query about a customer gets complete picture (behavior + stated pain + analysis)
- No more "I didn't have that information" when it's in the system
- Universal application: all Claude instances connected to OV vault use same routing
- Single source of truth for data source mapping
- Automatic updates as new sources come online

---

### Key Deliverables

1. **AskCruz Messaging** (transcript saved in threads-ov)
   - Complete positioning strategy for 3GM beachhead
   - Immediate actions for landing page, pricing, sales motion

2. **Data Integration Skill** (new SKILL.md created)
   - Ready to install
   - Includes configuration template
   - Includes implementation checklist
   - Includes troubleshooting guide
   - Designed for universal adoption

### Next Steps

1. **For Messaging:** Implement the 3GM-focused positioning immediately
2. **For Data Integration:**
   - Map entity-data-sources.md with all customers/products/people
   - Identify exact locations of Raj's documents
   - Confirm which MCP contains customer threads
   - Add standing instructions to preferences
3. **Cross-Chat Consistency:** Once configured, this skill applies everywhere—no need to re-request data sources per conversation
