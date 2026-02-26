---
description: Non-negotiable invariants for the extract-conclusions skill.
index:
  - Mandatory Actions
---

# Always Do

## Mandatory Actions

**YOU MUST:**

1. **Ground every claim in source evidence**
   - Every finding, metric, and conclusion must trace to a specific file, cell, or section
   - Use references: `path/to/notebook.ipynb` cell [N] or `path/to/file.md` section [name]
   - Never state a result without its source

2. **Report metrics quantitatively**
   - Use exact numbers from the source: "F1 = 0.87" not "good F1 score"
   - Include units, thresholds, and comparison baselines where available
   - When source lacks exact numbers, state this explicitly

3. **Evaluate experimental rigor constructively**
   - Assess baselines: Are they appropriate and sufficient?
   - Assess metrics: Are they aligned with the actual objective?
   - Assess statistical testing: Is it adequate for the claims made?
   - Assess ablations: Are they meaningful?
   - Assess data splits: Is the test set truly held out?
   - Be constructive, not obstructive — provide actionable observations

4. **Understand the project context**
   - Read Memory Bank files at the start if they exist
   - Consider why the experiments were conducted, not just what was done
   - Respect the existing work — assume competence; look for genuine issues

5. **Output to the correct location**
   - One document per conclusions task
   - Location: `llm_docs/conclusions/`
   - Filename: `YYYY-MM-DD-HHMM-conclusions-<kebab-topic>.md`
   - No frontmatter in the output document

6. **Rank conclusions by importance**
   - **Primary:** Conclusions that directly drive decisions or actions
   - **Supporting:** Conclusions that provide necessary context or confidence
   - **Background:** Conclusions that are technically interesting but not decision-critical
   - This ranking feeds directly into `data-storytelling`'s audience relevance analysis

7. **Include practical implications and recommended next steps**
   - Every conclusion must connect to a real-world implication or action
   - Next steps must be grounded in evidence, not speculative

8. **Compile a key technical terms glossary**
   - Collect every domain-specific term, acronym, and metric name used in the document
   - Provide a concise definition and context for each
   - This glossary is the primary input for `data-storytelling`'s jargon translation

9. **Update Memory Bank after completion**
   - Add key conclusions to `llm_docs/memory/activeContext.md`
