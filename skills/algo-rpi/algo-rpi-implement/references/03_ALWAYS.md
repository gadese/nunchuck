# Always

## Mandatory Requirements

**YOU MUST:**

- **Update plan checkboxes after completing each phase** — Mark items as `- [x]` in the plan document as work completes

- **Record quantitative metrics and compare against targets** — Every phase must report measurements in table format comparing target vs achieved vs baseline

- **Run verification commands before moving to the next phase** — Execute automated checks (ruff, pytest) and algorithm-specific verification (benchmarks, metrics)

- **Read Memory Bank files at the start** — Check `llm_docs/memory/activeContext.md` and `systemPatterns.md` before beginning

- **Ensure reproducibility at every step** — Document seeds, set seeds at beginning of runs, verify identical results across runs, pin dependency versions

- **Read the plan completely** — Identify all phases, quantitative targets, success criteria, dependencies, and existing checkmarks

- **Read all referenced materials** — Algorithm plan, research documents, existing code, dataset schemas, baseline implementations, benchmark harness

- **Verify prerequisites** — Confirm baseline metrics documented, dataset splits reproducible, benchmark harness functional

- **Assess mismatches before implementing** — Evaluate discrepancies between plan and reality; STOP and ask for major mismatches

- **Implement deliverables phase by phase** — Follow P0→P5 order, keep changes incremental and testable, use vectorized operations, ensure reproducibility

- **Handle algorithm-specific concerns** — Validate numerical stability, check edge cases, verify input/output shapes and types, add assertions for invariants

- **Run phase verification after each phase** — Code quality checks, algorithm-specific verification (benchmarks, metrics), reproducibility verification, report results with measurements

- **Fix issues before proceeding** — Do not move to next phase with failing tests or metrics significantly below target

- **Verify quantitative targets at performance gates** — After P1, P2, P3, P4 check that phase-specific targets are met

- **Update Memory Bank** — Update `activeContext.md` and `progress.md` with completion status after finishing all phases

- **Use strict type hints everywhere** — All functions must have type annotations

- **Prefer vectorized operations** — Use NumPy for numeric performance, OpenCV (`cv2`) for imaging

- **Document numerical considerations** — Note precision requirements, stability concerns, edge cases
