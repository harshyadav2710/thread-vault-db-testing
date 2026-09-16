---
thread_name: "ai-engineer-5-role"
user: "isha"
type: claude-chat
created: 2026-09-15
updated: 2026-09-15
---

## Turn 1

**User:** AI Engineer 5 role and responsibilities

**Assistant:** No asset, wiki page, or employee record in the connected EOXS systems defines a role called "AI Engineer 5" (or an "AI Engineer" level/grade at all). I checked the wiki, the full asset list (no job-description/leveling document exists among the 19 assets — nothing like a role framework or career-ladder doc), and the employee directory (no one holds that title, active or inactive).

So this isn't something I can pull from EOXS data — it's either a title from outside EOXS (a different company's internal leveling, a job posting you're evaluating, a LinkedIn profile, etc.) or a role that hasn't been documented internally yet.

Tell me which of these it is:

1. You're asking about a title you saw somewhere external (a candidate's resume, a competitor's posting, a leveling framework like Google's/Meta's "AI Engineer L5") — I can look that up via web search.
2. You want to define this as a new internal EOXS role/level and need a draft job description — that's a `human-resources:org-planning` or job-description-drafting task, not a lookup.
3. Something else you had in mind.

## Turn 2

**User:** [Uploaded file: AskCruz_OfferLetter_SHUBHAM SHARMAFinal.pdf] make it : The employee will receive a monthly in-hand salary of INR 20,000. In addition, INR 5,000 per month will be allocated as a retention amount. The accumulated retention amount will be payable upon completion of one (1) year of continuous service with the company, subject to the terms and conditions of the employment agreement.

**Assistant:** [Read the uploaded offer letter PDF (AskCruz offer letter for Shubham Sharma, Product Implementation Head / Client Relationship Manager role). Extracted full text and rendered page images to capture exact layout: AskCruz logo header with blue rule, navy-blue section headers, light-blue "Parties to this Agreement" table, navy header data tables for salary breakdown, and a footer band with AskCruz address/contact info repeated on every page.

Original Clause 3 (Salary and Compensation Structure), Clause 4 (Annual Compensation and Retention Amount), and Clause 5 (Retention Clause) contained a 40% increment table (₹10,000 → ₹14,000) plus a 30%/70% retention split table (₹50,400 retention / ₹1,17,600 regular, out of ₹1,68,000 annual).

Rebuilt the full 6-page offer letter as HTML (reusing the extracted AskCruz logo and footer images from the source PDF) and rendered it to PDF with WeasyPrint, replacing Clauses 3–5 with a single new Clause 3 containing the requested wording verbatim:

"The employee will receive a monthly in-hand salary of INR 20,000. In addition, INR 5,000 per month will be allocated as a retention amount. The accumulated retention amount will be payable upon completion of one (1) year of continuous service with the company, subject to the terms and conditions of the employment agreement."

Since two clauses were removed, renumbered all subsequent clauses down by two (old 6–22 → new 4–20), and updated the two cross-references inside old Clause 15 (now Clause 13, "Resignation and Full & Final Settlement"): "termination under Clause 13" → "termination under Clause 11", and "retention amount under Clause 5" → "retention amount under Clause 3". Also corrected an apparent typo in the source PDF: "Shubahm Sharma" → "Shubham Sharma" in the Parties table (matching the greeting and file name elsewhere in the same document).

Verified by rendering all 6 pages of the output PDF to images and reviewing them: header/footer/logo/table styling matches the original, the new Clause 3 reads correctly, and Clause 13's cross-references point to the correct renumbered clauses. Delivered the file via SendUserFile as AskCruz_OfferLetter_SHUBHAM_SHARMA_Revised.pdf.]

Revised offer letter — Clause 3 replaced with the flat ₹20,000 salary + ₹5,000/month retention wording; clauses 4–20 renumbered and cross-references in Clause 13 updated accordingly.
