# Always

## Mandatory Requirements

**YOU MUST:**

- **Confirm selected approach from research before planning** — If research presents multiple options, get explicit user confirmation on which approach to plan for

- **Reference local file paths and line ranges only** — Use `path/to/file.py:10-25` format for existing materials

- **Output a single plan file per invocation** — Location: `llm_docs/plans/`, filename: `YYYY-MM-DD-HHMM-plan-algo-<kebab-topic>.md`, no frontmatter

- **Quantify all goals** — Metric targets, latency budgets, memory constraints must be explicit numbers, not vague descriptions

- **Read Memory Bank files at the start** — Check `llm_docs/memory/activeContext.md`, `systemPatterns.md`, and `techContext.md` before planning

- **Read the research document completely** — Understand recommended approaches, rationale, trade-offs, interface requirements, dataset characteristics, and evaluation methodology

- **Read all additional inputs fully** — Never skip or partially read provided files, dataset schemas, baseline scripts, or prior implementations

- **Gather technical context** — Identify relevant source files, datasets, benchmarks, integration points, hardware/runtime assumptions

- **Verify understanding** — Cross-reference research requirements with actual materials; identify discrepancies

- **Synthesize and clarify** — Present understanding of problem definition, selected approach, integration points, hardware constraints; ask questions only if genuinely ambiguous

- **Confirm algorithm choice** — If research presents multiple viable approaches, present refined options with pros/cons and get user confirmation

- **Sketch algorithm architecture** — Define data preparation, core algorithm, postprocessing, evaluation, and packaging (textual, no code blocks)

- **Define interfaces and invariants** — Specify input/output types and shapes, preconditions, postconditions, error handling, integration boundaries

- **Present plan structure for approval** — Show P0-P5 phases with objectives; wait for structure approval before writing detailed plan

- **Use standard P0-P5 phase structure** — Baseline & Harness → Prototype → Evaluation → Optimization → Robustness → Packaging

- **Define quantitative targets table** — Include primary metric, latency, memory with target values, baseline values, and notes

- **Specify success criteria for each phase** — Include both automated checks and manual verification with measurable outcomes

- **Include reproducibility checklist** — Random seeds, dependency versions, dataset version/hash, hardware configuration

- **Document risks and mitigations** — Identify potential blockers and mitigation strategies

- **Update Memory Bank** — Add design decisions to `llm_docs/memory/activeContext.md` after completing plan
