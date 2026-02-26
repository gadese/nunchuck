---
description: Activation and deactivation signals for the extract-conclusions skill.
index:
  - When to Invoke
  - Expected Inputs
  - Response Format
  - Clarification Protocol
---

# Triggers

## When to Invoke

Invoke this skill when you need to:
- Extract conclusions from completed experimental notebooks
- Consolidate findings from multiple experiment runs or notebook files
- Document what was tried, why, with what data, and what the results were
- Produce a structured conclusion artifact for downstream planning or communication
- Evaluate the rigor of experimental work (baselines, metrics, statistical testing)

Do not invoke when:
- The task is to run or modify experiments
- The task is to write code or change the codebase
- The audience is non-technical and needs accessible narrative (use `data-storytelling`)
- The task is codebase documentation (use `rpi-research`)

## Expected Inputs

- One or more source files: Jupyter notebooks (`.ipynb`), markdown summaries, Python scripts, data files (CSV, JSON, YAML), configuration files, log outputs, or any other relevant artifacts
- Optional: Specific focus area or comparison to prioritize
- Optional: Context about the project goals or constraints

## Response Format

When invoked without parameters, respond with:

"I'm ready to extract and synthesize conclusions from your technical notebooks and documents.

Please provide the source file(s) to analyze. If your request involves multiple documents or a broad scope, I will ask clarifying questions before proceeding."

Then wait for the user's input and apply the clarification protocol.

## Clarification Protocol

**MANDATORY**: Before conducting extraction, ask clarifying questions when:
- Multiple notebooks exist and it is unclear which to analyze
- The relationship between documents is unclear
- The experimental context or project goals are ambiguous

Ask 2-3 focused questions covering:
1. **Scope**: Which notebooks/documents should be included?
2. **Focus**: Any specific experiments, metrics, or comparisons to prioritize?
3. **Context**: What is the project goal driving these experiments?

**Exception**: If the user provides specific file paths and scope is clear, proceed directly.
