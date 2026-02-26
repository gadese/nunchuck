---
description: Step-by-step extraction and synthesis pipeline for the extract-conclusions skill.
index:
  - Step 1 — INGEST
  - Step 2 — EXTRACT
  - Step 3 — EVALUATE
  - Step 4 — SYNTHESIZE
  - Step 5 — DELIVER
  - Output Document Template
---

# Procedure — Conclusion Extraction Pipeline

## Step 1 — INGEST

**Objective:** Read and fully understand the source material and project context.

**Duration:** 1 round.

1. Read Memory Bank files if they exist:
   - `llm_docs/memory/activeContext.md`
   - `llm_docs/memory/techContext.md`
   - If missing, skip gracefully and note the gap
2. Read the source files provided by the user:
   - For Jupyter notebooks (`.ipynb`): read all cells, noting markdown narrative and code outputs
   - For markdown summaries: read the full document
   - For Python scripts (`.py`): read and identify experiment logic, parameters, metrics computation
   - For data files (CSV, JSON, YAML): inspect structure, schema, sample rows, and summary statistics
   - For log outputs or config files: extract relevant parameters, results, and environment details
   - For any other format: read and note the structure
3. If no source is provided, ask: "Which notebooks or documents should I extract conclusions from? Please provide file paths."
4. If multiple files are provided, identify their relationships (sequential experiments, parallel comparisons, etc.)

**Early exit:** If the user provides clear file paths and context, proceed directly to Step 2.

---

## Step 2 — EXTRACT

**Objective:** Systematically extract all experimental information from each source.

**Duration:** 1-2 rounds depending on source count.

For each source document, extract:

1. **Problem statement and motivation**
   - What question or problem was being investigated?
   - Why was this investigation undertaken? What drove the need?
   - What were the hypotheses or expected outcomes?

2. **Data description**
   - What datasets were used? (name, source, size, characteristics)
   - How was data split? (train/val/test ratios, stratification, cross-validation)
   - What preprocessing or feature engineering was applied?
   - Any data quality issues noted?

3. **Methodology and experiments**
   - What algorithms, models, or approaches were tried?
   - What hyperparameters were used or tuned?
   - What was the experimental setup? (hardware, frameworks, seeds, repetitions)
   - What baselines were established?

4. **Results and metrics**
   - What metrics were reported? (exact values with units)
   - What were the comparative results across approaches?
   - What visualizations or plots were produced? (describe, do not reproduce)
   - What statistical tests were applied, if any?

5. **Author conclusions**
   - What did the notebook author conclude?
   - What recommendations or next steps did they suggest?
   - What limitations did they acknowledge?

6. **Technical vocabulary**
   - Collect every domain-specific term, acronym, and metric name encountered
   - Note its meaning and context — this feeds the downstream glossary for `data-storytelling`

Track each extraction with its source reference: `path/to/file` cell [N] or section [name].

---

## Step 3 — EVALUATE

**Objective:** Assess the rigor and soundness of the experimental work.

**Duration:** 1 round.

Apply expert judgment across these dimensions:

1. **Algorithm selection**
   - Is the chosen approach appropriate for the problem constraints?
   - Were reasonable alternatives considered?
   - Are trade-offs (accuracy vs speed vs memory) well-reasoned?

2. **Evaluation rigor**
   - Are baselines appropriate and sufficient?
   - Are metrics aligned with the actual objective?
   - Is statistical testing adequate for the claims made?
   - Are ablations meaningful (if present)?
   - Is the test set truly held out?

3. **Reproducibility**
   - Are random seeds fixed?
   - Are environment details documented?
   - Could the experiments be reproduced from the information given?

4. **Evidence strength**
   - How confident can we be in the conclusions given the evidence?
   - Rate each major conclusion: **Strong** (robust evidence), **Moderate** (reasonable but gaps exist), **Weak** (insufficient evidence)

Be constructive: note strengths as well as gaps. Assume competence and look for genuine issues, not nitpicks.

---

## Step 4 — SYNTHESIZE

**Objective:** Produce the structured conclusion document.

**Duration:** 1 round.

1. Write the executive summary (2-3 sentences capturing the top-level takeaway)
2. Write the problem statement grounded in the source motivation
3. Document data and environment from extracted details
4. For each experiment: methodology, metrics (exact values), key result, source reference
5. If multiple experiments: produce comparative analysis with a summary table
6. Include the rigor evaluation from Step 3
7. Write conclusions with confidence levels, grounded strictly in reported results
8. Rank each conclusion by importance: **Primary** (drives decisions), **Supporting** (provides context), **Background** (technically interesting but not decision-critical)
9. Write practical implications: what the conclusions mean for real-world decisions and actions
10. Write recommended next steps grounded in the conclusions
11. Document limitations and open questions (caveats that must be preserved downstream)
12. Compile the key technical terms glossary from Step 2 vocabulary collection
13. Compile all source references

---

## Step 5 — DELIVER

**Objective:** Write the output file and hand off.

**Duration:** 1 round.

1. Check for existing file at target path; if collision, append `-2`, `-3`, etc.
2. Write the conclusion document to `llm_docs/conclusions/YYYY-MM-DD-HHMM-conclusions-<kebab-topic>.md`
3. Update Memory Bank if it exists: add key conclusions to `llm_docs/memory/activeContext.md`
4. Present a brief summary in chat:
   - Top 2-3 conclusions with confidence levels
   - Key metrics highlighted
   - Document location
5. Ask if the user wants to adjust scope, depth, or focus

---

## Output Document Template

```markdown
# Conclusions — [Topic]

**Executive Summary:** [2-3 sentences.] | **Sources:** [file paths] | **Date:** YYYY-MM-DD

## 1. Problem Statement
What was investigated, why, and what hypotheses were stated.

## 2. Data & Environment
Datasets (name, source, size), splits, preprocessing, hardware/frameworks/seeds.

## 3. Experiments Conducted
Per experiment: approach, hyperparameters, metrics (table), key finding, source ref.

## 4. Comparative Analysis
Cross-experiment comparison table (when multiple experiments exist).

## 5. Evaluation Rigor
Baselines, metric alignment, statistical adequacy, reproducibility.

## 6. Conclusions
Per conclusion: evidence-backed statement with confidence (Strong/Moderate/Weak) and importance rank (Primary/Supporting/Background).

## 7. Practical Implications & Next Steps
What the conclusions mean for decisions. Recommended actions grounded in evidence.

## 8. Limitations & Open Questions
Known limitations with source refs. Caveats that must be preserved downstream.

## 9. Key Technical Terms
Glossary: every domain-specific term, acronym, and metric with definition and context.

## 10. References
`path/to/file` cell [N] or section [name] — brief description per entry.
```
