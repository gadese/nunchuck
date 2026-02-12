---
description: Step-by-step transformation from technical document to accessible narrative.
index:
  - Step 1 — INGEST
  - Step 2 — ANALYZE
  - Step 3 — STRUCTURE
  - Step 4 — DRAFT
  - Step 5 — REVIEW
  - Output Document Template
---

# Procedure — Technical-to-Narrative Transformation

## Step 1 — INGEST

**Objective:** Read and fully understand the source material and project context.

**Duration:** 1 round.

1. Read Memory Bank files if they exist:
   - `llm_docs/memory/activeContext.md`
   - `llm_docs/memory/techContext.md`
   - If missing, skip gracefully and note the gap
2. Read the source technical document(s) provided by the user
3. If no document is provided, ask: "Which technical document should I transform? Please provide the file path or paste the content."
4. If audience is not specified, ask: "Who is the target audience for this narrative?"

**Early exit:** If the user provides a clear document and audience, proceed directly to Step 2.

---

## Step 2 — ANALYZE

**Objective:** Extract what matters and identify translation challenges.

**Duration:** 1 round.

1. Identify the core findings (the "so what" of the document)
2. Rank findings by audience relevance:
   - **Primary:** Findings that directly affect decisions the audience makes
   - **Supporting:** Findings that provide necessary context or confidence
   - **Background:** Findings that are technically interesting but not decision-relevant
3. Flag technical concepts that need translation (jargon, metrics, methodology)
4. Identify limitations and caveats that must be preserved
5. Note any gaps: findings that are unclear or require additional context from the user
6. If gaps exist, ask the user targeted questions before proceeding

---

## Step 3 — STRUCTURE

**Objective:** Choose narrative framework and organize information for the audience.

**Duration:** 1 round.

Select the best-fit narrative framework based on document type:

- **Finding Story:** Single key insight with supporting evidence — use when the document has one dominant conclusion
- **Comparison Story:** Side-by-side evaluation — use when the document compares approaches, tools, or options
- **Progress Story:** Timeline of improvements or changes — use when the document tracks evolution over time
- **Risk Story:** What we found, what it means, what could go wrong — use when the document surfaces risks or limitations

Organize the information:

1. Map primary findings to the narrative arc (Hook → Context → Findings → Implications → Recommendation)
2. Place supporting findings as evidence within the arc
3. Relegate background findings to an appendix section or omit if not needed
4. Plan jargon translations and analogies for flagged technical concepts

---

## Step 4 — DRAFT

**Objective:** Write the accessible narrative document.

**Duration:** 1 round.

1. Write the executive summary (one sentence capturing the key takeaway)
2. Write the narrative following the chosen framework and arc
3. Apply jargon translations — replace or explain every technical term
4. Use concrete numbers: "3x faster" not "significantly faster", "$240K saved" not "substantial savings"
5. Include a "What This Means" section connecting findings to audience concerns
6. Include a "Limitations" section preserving source caveats in accessible language
7. Include "Recommended Next Steps" grounded in the source document's conclusions
8. Add a "Technical Appendix" section with key definitions for readers who want to dig deeper

---

## Step 5 — REVIEW

**Objective:** Verify accuracy and accessibility before delivering.

**Duration:** 1 round.

1. **Accuracy check:** Compare every claim in the narrative against the source document — flag any drift
2. **Accessibility check:** Scan for remaining jargon, unexplained acronyms, or assumed knowledge
3. **Completeness check:** Verify no key finding from the source was omitted
4. **Bias check:** Confirm the narrative does not spin findings in a direction the source does not support
5. Check for existing file at target path; if collision, append `-2`, `-3`, etc.
6. Write the final narrative to `llm_docs/narratives/YYYY-MM-DD-HHMM-narrative-<kebab-topic>.md`
7. Update Memory Bank if it exists: add narrative summary to `llm_docs/memory/activeContext.md`
8. Present the document location and offer to adjust tone, depth, or emphasis

---

## Output Document Template

```markdown
# [Headline: Impact-First Title]

**Executive Summary:** [One sentence — the single most important takeaway.]
**Source:** [Source document path or title] | **Audience:** [Target audience] | **Date:** YYYY-MM-DD

## The Key Finding
[Most important result in plain language with concrete numbers.]

## Context
[Why this matters — what was investigated and why the audience should care.]

## What We Found
[Primary findings first, supporting evidence second. Plain language with numbers.]
### [Finding 1 — Most Important]
[Plain-language explanation with concrete impact.]
### [Finding 2 — Supporting]
[Connection to Finding 1.]

## What This Means
[Implications for the audience's decisions. Connects findings to business/organizational impact.]

## Limitations
[Caveats from the source in accessible language. What we don't know yet.]

## Recommended Next Steps
1. [Most important action]
2. [Second action]
3. [Third action]

## Technical Appendix
[Key definitions for readers who want more detail.]
- **[Term 1]:** [Plain-language definition]
- **[Term 2]:** [Plain-language definition]
```
