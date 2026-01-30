# Never

## Prohibitions

**YOU MUST NOT:**

- **Make code changes or diffs in this step** — This is a planning phase only; no code implementation allowed

- **Include code blocks in the plan output** — Use file path references with line ranges only; never include actual code

- **Echo secrets or config contents** — Reference their paths only

- **Leave open questions in the final plan** — Resolve all ambiguities before finalizing; the plan must be complete and actionable

- **Use vague or qualitative targets** — All goals must be quantified with explicit numbers (e.g., "95% accuracy" not "high accuracy")

- **Skip plan structure approval** — Always present P0-P5 phase outline and wait for user approval before writing detailed plan

- **Proceed without confirming approach** — If research presents multiple options, you MUST get user confirmation on which to plan for

- **Include implementation details in chat** — Planning documents only; no code blocks or implementation guidance in chat responses

- **Use external permalinks** — Only use local file paths for references

- **Skip quantitative targets table** — Every plan must include a table with metric targets, latency, memory, baseline values

- **Omit reproducibility requirements** — Every plan must include reproducibility checklist with seeds, versions, dataset hash, hardware config

- **Plan premature optimization** — P3 optimization phase comes AFTER P2 evaluation; don't optimize before establishing baseline performance
