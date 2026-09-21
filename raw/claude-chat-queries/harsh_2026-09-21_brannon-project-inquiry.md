---
thread_name: "brannon-project-inquiry"
user: "harsh"
type: claude-chat
created: 2026-09-21
updated: 2026-09-21
---

# Brannon Project - Jaskeerat Singh Contribution Inquiry

**User Query:** What is Jaskeerat's contribution on the Brannon project?

## Findings

Jaskeerat Singh has contributed significantly to the **Brannon Steel MTR AI Implementation** project, primarily on QA, data validation, and system logic implementation for the MTR (Material Test Report) matching and compliance verification system.

### Key Contributions (Feb 2026 - Sept 2026):

**1. Data Validation & Inventory Alignment (Jul 10, 2026)**
- Requested latest inventory sheet from Brannon (Ranim Fallaha) to analyze data and validate current inventory against MTR records
- Identified discrepancies between uploaded MTRs and actual inventory

**2. MTR Quality & Extraction Issues (Jul 16, 2026)**
- Identified that rotated/incorrectly oriented MTR PDFs were causing extraction failures (batch numbers, heat numbers incomplete)
- Manually corrected problematic records
- Recommended proper PDF orientation before upload to prevent future extraction errors

**3. Complex Specification Logic Implementation (Jul 22-28, 2026)**
- Worked on SSAB MTR handling scenarios with multiple tested pieces vs. shipped batches
- Clarified requirements with Brannon on how to handle cases where:
  - Inventory contains a shipped batch (e.g., A69)
  - But multiple different pieces were tested (A70, A72, A73 with different mechanical properties)
- Implemented updated logic to associate shipped batches with tested piece data per ASTM standards
- Updated system to handle MTRs without batch numbers (assigned "Nil" placeholders initially)

**4. Bug Investigation & Fixes (Aug 14-31, 2026)**
- Documented and tracked issues reported by Brannon:
  - False compliance results (MTRs passing when they shouldn't)
  - Missing MTRs in chatbot responses despite being matched in Joint Inventory
  - Incorrect grade/specification matching
- Addressed and fixed underlying issues
- Validated corrections and shared updates with team

**5. Manufacturer Criteria Logic (Sep 8, 2026)**
- Explained filtering logic to Brannon: System uses only data from manufacturers who sold material to Brannon; if a manufacturer page lacks passing grades for a spec, results are filtered out (even if matched in Joint Report)
- Key insight: Clarified the distinction between Joint Report matching vs. actual result eligibility

**6. Specification Compliance Requirements (Sep 17, 2026)**
- Collaborated on fine-grain steel requirement logic (Section 6.2 criteria: Aluminum, Vanadium, or Columbium content validation)
- Addressed edge case compliance issues and documented expected behavior

### Summary Role:
Jaskeerat served as a **QA lead and requirements engineer** for the MTR matching system, bridging Brannon's business requirements (ASTM compliance, specification matching) with technical implementation, identifying extraction issues, clarifying edge-case logic, and iteratively fixing system bugs discovered during live testing.
