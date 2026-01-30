# Algo-RPI Plan

Algorithm implementation planning for the Algo-RPI workflow.

## Purpose

This skill creates detailed, quantitative implementation plans for algorithms based on research findings. It produces actionable plans with explicit metrics, phased development (P0-P5), and reproducibility requirements.

## When to Use

Use this skill when you:
- Have completed algorithm research and need to create an implementation plan
- Have existing research documentation with candidate approaches
- Want to define quantitative targets and phased implementation
- Need to plan algorithm development with reproducibility requirements

## Key Features

- **Mandatory approach confirmation** from research before planning
- **Quantitative targets table** with explicit metrics, latency, memory
- **Standard P0-P5 phase structure** for algorithm development
- **Reproducibility checklist** with seeds, versions, dataset hash, hardware config
- **Integration points** from research codebase interface analysis
- **Success criteria** for each phase with measurable outcomes

## Output

Plan document in `llm_docs/plans/YYYY-MM-DD-HHMM-plan-algo-<kebab-topic>.md` containing:
- Problem statement with quantitative targets
- Selected approach from research
- Hardware and runtime assumptions
- P0-P5 implementation phases with success criteria
- Risks and mitigations
- Reproducibility checklist

## Invocation

```
/algo-rpi-plan

Research document: llm_docs/research/[filename].md
Problem: [algorithmic task]
Targets: [metric]=X, latency=Yms, memory=ZMB
Hardware: [CPU/GPU/TPU, memory limits]
```

## Standard P0-P5 Phases

**P0: Baseline & Harness**
- Establish baseline performance
- Create dataset splits with fixed seeds
- Build metrics computation pipeline
- Implement benchmark harness

**P1: Prototype**
- Implement minimal viable algorithm
- Verify correctness on test cases
- Check metrics on small subset
- Create unit tests

**P2: Evaluation**
- Full dataset evaluation
- Ablation studies
- Statistical significance testing
- Compare to baseline

**P3: Optimization**
- Profile and identify bottlenecks
- Vectorize and parallelize
- Meet latency and memory targets
- Verify no accuracy regression

**P4: Robustness**
- Edge case testing
- Determinism verification
- Error handling
- Adversarial input testing

**P5: Packaging**
- API documentation
- Usage examples
- Reproducibility artifacts
- Integration guide

## Clarification Protocol

**CRITICAL:** This skill MUST confirm the selected approach from research before planning.

If research presents multiple viable approaches:
1. Present refined comparison of top 2-3 options
2. Include pros/cons and complexity analysis
3. Provide recommendation with rationale
4. Wait for explicit user selection

Questions will cover:
- Which approach to implement?
- What are the quantitative targets?
- What hardware is available?
- Are there additional constraints?

## Example

```
/algo-rpi-plan

Research document: llm_docs/research/2026-01-15-1400-research-algo-object-detection.md
Problem: Real-time object detection for video stream
Targets: mAP@0.5=0.95, latency=30ms, memory=2GB
Hardware: NVIDIA RTX 3080 GPU, 16GB VRAM
```

The skill will:
1. Read research document and confirm YOLOv8 was recommended
2. Present quantitative targets table
3. Define P0-P5 phases with specific success criteria
4. Include reproducibility requirements (PyTorch version, CUDA version, seeds)
5. Document integration points from research
6. Create actionable plan ready for implementation

## Quantitative Targets

Every plan includes a targets table:

| Metric | Target | Baseline | Notes |
|--------|--------|----------|-------|
| mAP@0.5 | 0.95 | 0.87 | On test set, 20 classes |
| Latency | 30ms | 45ms | Per frame, 1080p, GPU |
| Memory | 2GB | 3.2GB | Peak GPU memory |

All targets must be explicit numbers, not vague descriptions.

## Reproducibility

Every plan includes a reproducibility checklist:
- [ ] Random seeds documented and fixed
- [ ] Dependency versions pinned (requirements.txt)
- [ ] Dataset version/hash recorded
- [ ] Hardware configuration documented

This ensures results can be reproduced exactly.

## Integration with Algo-RPI Workflow

This is the second phase of the Algo-RPI workflow:
1. **Research** (`algo-rpi-research`) → Formalize problem, explore solutions
2. **Plan** (this skill) → Select approach, create implementation plan
3. **Implement** (`algo-rpi-implement`) → Execute plan with quantitative verification

## See Also

- `algo-rpi-research/` — Algorithm research skill
- `algo-rpi-implement/` — Algorithm implementation skill
- `rpi-plan/` — General software planning (use for non-algorithmic tasks)
- `coding-standards/` — Shared coding guidelines
