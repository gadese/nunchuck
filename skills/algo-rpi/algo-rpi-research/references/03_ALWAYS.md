# Always

## Mandatory Requirements

**YOU MUST:**

- **Ask clarifying questions when scope is ambiguous** — Apply the clarification protocol before proceeding if the problem statement, constraints, or data characteristics are unclear

- **Describe the problem as it exists** — Document constraints and feasible solution families without implementing or critiquing

- **Brainstorm options and analyze trade-offs** — Explore 3-5 candidate approaches without committing to one final solution

- **Use local file paths with line ranges** — Reference code with `path/to/file.py:10-25` format; do not include code blocks from files

- **Read Memory Bank files at the start** — Check `llm_docs/memory/activeContext.md`, `systemPatterns.md`, and `techContext.md` before beginning research

- **Formalize the problem precisely** — Define inputs/outputs, objective functions, constraints, metrics & targets, operating environment, and failure modes

- **Establish baselines and prior art** — Identify trivial baseline, document existing baselines in repo, list relevant algorithm families

- **Explore solution space systematically** — For each candidate: description, complexity, data requirements, hardware/runtime, expected quality, hyperparameters

- **Propose downselect criteria** — Define how to choose among candidates (metric thresholds, latency/memory budgets, simplicity, maintainability)

- **Outline validation plan** — Specify dataset splits, evaluation loops, ablations, seeds, reproducibility measures

- **Include assumptions and unknowns** — Document gaps in understanding after asking clarifying questions

- **Output one document per research task** — Location: `llm_docs/research/`, filename: `YYYY-MM-DD-HHMM-research-algo-<kebab-topic>.md`, no frontmatter

- **Update Memory Bank** — Add key findings to `llm_docs/memory/activeContext.md` after completing research
