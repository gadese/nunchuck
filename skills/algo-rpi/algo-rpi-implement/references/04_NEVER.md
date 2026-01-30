# Never

## Prohibitions

**YOU MUST NOT:**

- **Redesign the algorithm or question the selected approach from the plan** — The algorithm choice was decided in planning; execute what's specified

- **Implement features or optimizations not specified in the current phase** — Stick to the phase deliverables; no scope creep

- **Skip verification steps or benchmarking between phases** — Every phase must be verified before proceeding

- **Proceed past a major mismatch without user confirmation** — If plan assumptions don't match reality, STOP and present options

- **Modify files outside the scope defined in the plan** — Only change files specified in the plan or necessary for the algorithm

- **Compromise reproducibility** — Never skip seeds, deterministic ops, or version pinning

- **Report vague performance claims** — Every performance claim must be backed by measurement with explicit numbers

- **Assume correctness without verification** — Always run tests, measure metrics, compare to baseline

- **Optimize prematurely** — Complete P2 evaluation before P3 optimization; don't optimize before establishing baseline performance

- **Skip quantitative measurements** — Every phase must report metrics in table format

- **Proceed with failing tests** — Fix all test failures before moving to next phase

- **Leave plan checkboxes unmarked** — Update plan document as work completes

- **Use non-deterministic operations without documentation** — If non-deterministic ops are necessary, document their impact

- **Skip reproducibility verification** — Must verify identical results across runs with same seed
