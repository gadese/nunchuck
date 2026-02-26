# Extract-Conclusions Skill

Extracts structured conclusions from technical notebooks and summary markdown files, producing comprehensive conclusion documents for downstream consumption.

## Overview

The `extract-conclusions` skill reads technical notebooks (Jupyter `.ipynb`), summary markdown files, and related experimental artifacts, then produces a structured conclusion document. It operates from the perspective of a senior AI/ML expert with deep experience in industrial applications — combining theoretical rigor with practical engineering judgment to evaluate what was explored, why, what data was used, what the results and metrics were, and what the conclusions are.

**Key Features:**
- Expert-level ML/AI analysis of experimental work
- Structured extraction covering motivation, data, methodology, results, and conclusions
- Metrics-first reporting with quantitative rigor
- Evaluation of experimental soundness (baselines, ablations, statistical adequacy)
- Actionable conclusion synthesis grounded in evidence

## When to Use

### Use Extract-Conclusions:
- Technical notebooks need their findings extracted and organized
- Experiment results are scattered across notebooks and need consolidation
- A research phase has completed and conclusions need to be documented
- Multiple experimental runs need to be compared and synthesized
- Downstream skills (planning, data-storytelling) need a structured source of truth

### Do Not Use Extract-Conclusions:
- Need to run or modify experiments → use appropriate development tools
- Need non-technical communication → use `data-storytelling` downstream
- Need codebase documentation → use `rpi-research`
- Need algorithm design → use `algo-rpi-research` or `brainstorm`

## Quick Start

```
/extract-conclusions

Source: notebooks/experiment_01.ipynb
```

Or with multiple sources:

```
/extract-conclusions

Sources:
- notebooks/experiment_01.ipynb
- notebooks/experiment_02.ipynb
- docs/summary.md
Focus: Compare anomaly detection approaches
```

The skill will:
1. **Ingest** — Read source notebooks/documents and project context
2. **Extract** — Identify experiments, data, methodology, metrics, and findings
3. **Evaluate** — Assess rigor: baselines, statistical testing, ablations, metric alignment
4. **Synthesize** — Produce structured conclusion document with quantitative evidence
5. **Deliver** — Write output, present summary, update Memory Bank

## Output Format

Each session produces a conclusion document at:
`llm_docs/conclusions/YYYY-MM-DD-HHMM-conclusions-<topic>.md`

The document follows a structured format:
1. **Executive Summary** — Top-level takeaway in 2-3 sentences
2. **Problem Statement** — What was being investigated and why
3. **Data & Environment** — Datasets, splits, hardware, frameworks
4. **Experiments Conducted** — Each experiment with methodology, metrics, results
5. **Comparative Analysis** — Cross-experiment comparison when applicable
6. **Evaluation Rigor** — Assessment of baselines, statistical testing, ablations
7. **Conclusions** — Evidence-backed conclusions with confidence levels and practical implications
8. **Practical Implications & Next Steps** — What the conclusions mean for decisions, and recommended actions
9. **Limitations & Open Questions** — Known gaps and caveats that must be preserved downstream
10. **Key Technical Terms** — Glossary of domain-specific terms used in the document
11. **References** — Source file paths with descriptions

## Relationship to Other Skills

The `extract-conclusions` skill is the **primary upstream producer** for `data-storytelling`. Its output is explicitly structured to provide everything data-storytelling needs:

- **Core findings ranked by importance** → data-storytelling ranks by audience relevance
- **Concrete metrics with exact numbers** → data-storytelling uses these directly
- **Practical implications** → data-storytelling maps to "What This Means"
- **Recommended next steps** → data-storytelling preserves and simplifies
- **Limitations and caveats** → data-storytelling must preserve these
- **Key technical terms glossary** → data-storytelling uses for jargon translation

Typical flow:

```
Notebooks/Summaries → /extract-conclusions → /data-storytelling → Stakeholder narrative
```

Also useful upstream of `rpi-plan` / `algo-rpi-plan` when conclusions drive the next planning cycle.

## Skill Structure

```
extract-conclusions/
├── SKILL.md                    # Skill manifest
├── README.md                   # This file
└── references/
    ├── 00_ROUTER.md           # Routing logic (single default route)
    ├── 01_SUMMARY.md          # Skill identity and expert role
    ├── 02_TRIGGERS.md         # When to invoke
    ├── 03_ALWAYS.md           # Mandatory behaviors
    ├── 04_NEVER.md            # Prohibited behaviors
    ├── 05_PROCEDURE.md        # Extraction and synthesis pipeline
    └── 06_FAILURES.md         # Error handling and recovery
```

## See Also

- `data-storytelling/` — Transforms conclusion documents for non-technical audiences
- `rpi/rpi-research/` — Codebase research (produces technical documentation)
- `algo-rpi/algo-rpi-research/` — Algorithm research and evaluation
- `brainstorm/` — Interactive solution brainstorming
