---
description: Failure conditions and recovery strategies for the data-storytelling skill.
index:
  - No Source Document Provided
  - Source Document Is Unclear or Incomplete
  - Multiple Conflicting Sources
  - Audience Not Specified
  - Findings Resist Simplification
  - Source Contains No Clear Conclusion
  - Narrative Drifts From Source
  - Output Path Collision
  - Memory Bank Files Missing
  - Source Too Large for Single Narrative
---

# Failures — Error Handling and Recovery

## No Source Document Provided

**Symptoms:** User invokes `/data-storytelling` without providing a document or file path.

**Recovery:**
1. Ask: "Which technical document should I transform? Provide the file path or paste the content."
2. Do not proceed until a source is provided
3. If user describes findings verbally, confirm: "Should I treat what you described as the source material?"

---

## Source Document Is Unclear or Incomplete

**Symptoms:** Source has ambiguous conclusions, missing data, or unclear methodology.

**Recovery:**
1. Ask targeted questions: "The source says [X] but doesn't clarify [Y]. Can you fill in this detail?"
2. If user cannot clarify, note the ambiguity explicitly in the output
3. Do not invent explanations to fill gaps

---

## Multiple Conflicting Sources

**Symptoms:** Multiple documents reach contradictory conclusions.

**Recovery:**
1. Ask: "These documents disagree on [X]. Which conclusion should the narrative prioritize?"
2. If user wants both perspectives, present them as competing findings with evidence for each
3. Never silently resolve a contradiction by picking one side

---

## Audience Not Specified

**Symptoms:** User provides a document but does not indicate who the narrative is for.

**Recovery:**
1. Ask: "Who is the target audience? (e.g., executives, product managers, external partners)"
2. If user is unsure, default to non-technical stakeholders and note the assumption

---

## Findings Resist Simplification

**Symptoms:** A key finding cannot be reduced without losing critical meaning.

**Recovery:**
1. Use a layered approach: simple statement first, then a "dig deeper" paragraph
2. Use analogy — but flag when the analogy is imperfect
3. If no simplification works, add a "Nuance Note" explaining what the simplified version leaves out
4. Do not omit the finding — complexity is not a reason to hide information

---

## Source Contains No Clear Conclusion

**Symptoms:** The document is exploratory or inconclusive — no firm findings.

**Recovery:**
1. Reframe around what was learned: "What we explored → What we observed → What remains open"
2. Be explicit: "This investigation did not reach a definitive conclusion."
3. Do not manufacture a conclusion the source does not support

---

## Narrative Drifts From Source

**Symptoms:** During REVIEW, a claim in the narrative does not match the source.

**Recovery:**
1. Correct the narrative to match the source — no exceptions
2. If drift happened from simplification, find a better simplification that preserves accuracy

---

## Output Path Collision

**Symptoms:** A file already exists at the target output path.

**Recovery:** Append numeric suffix (`-2`, `-3`, etc.) and inform the user.

---

## Memory Bank Files Missing

**Symptoms:** No `activeContext.md` or `techContext.md` in project.

**Recovery:** Skip gracefully, note no prior context was available, proceed normally.

---

## Source Too Large for Single Narrative

**Symptoms:** Source covers many independent topics.

**Recovery:**
1. Ask: "This covers [N] distinct topics. One narrative or separate narratives?"
2. If one: focus on highest-impact findings, reference others in appendix
3. If separate: produce in priority order, one at a time
