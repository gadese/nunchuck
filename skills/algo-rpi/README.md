# Algo-RPI Skillset

Algorithm Research-Plan-Implement workflow for algorithm development and optimization tasks.

## Overview

The `algo-rpi` skillset provides a structured approach to algorithm development with quantitative verification and reproducibility:

**Standard Workflow (3 phases):**
1. **Algorithm Research** — Formalize problem, explore solution space
2. **Algorithm Plan** — Create detailed plan with P0-P5 phases and quantitative targets
3. **Algorithm Implement** — Execute plan with performance gates and reproducibility enforcement

**Full Workflow with AI Expert Review (5 phases):**
1. **Algorithm Research** — Formalize problem, explore solution space
2. **Algorithm Plan** — Create detailed plan with P0-P5 phases and quantitative targets
3. **AI Expert Plan Review** — Review for theoretical soundness, numerical stability, production-readiness
4. **AI Expert Plan Reimagine** — Reimagine plan from scratch for optimal algorithm design
5. **Algorithm Implement** — Execute approved plan with performance gates and reproducibility enforcement

Each phase includes mandatory pause points for user approval, ensuring alignment and preventing wasted effort.

## When to Use

### Use Algo-RPI for:
- Algorithm development and optimization
- Machine learning model implementation
- Performance-critical numerical code
- Tasks requiring quantitative benchmarks
- Reproducibility-critical implementations
- Classical algorithms (DP, graphs, optimization)
- AI/ML solutions (supervised, deep learning, RL)
- Vision & imaging algorithms
- NLP algorithms

### Use RPI instead for:
- General software development tasks
- Feature additions or modifications
- Refactoring existing code
- Bug fixes not requiring algorithmic analysis
- Integration work without performance constraints

## Skillset Structure

```
algo-rpi/
├── SKILL.md                         # Orchestrator skill
├── README.md                        # This file
├── .pipelines/                      # Workflow definitions
│   ├── .INDEX.md                   # Pipeline index
│   ├── 00_DEFAULT.md               # Standard Algo-RPI workflow
│   ├── 01_RESEARCH_ONLY.md         # Research phase only
│   ├── 02_PLAN_ONLY.md             # Plan phase only
│   ├── 03_IMPLEMENT_ONLY.md        # Implement phase only
│   └── 04_FULL_WORKFLOW.md         # Full workflow with AI expert review
├── .shared/                         # Symlink to coding-standards/references/
├── algo-rpi-research/              # Algorithm research member skill
│   ├── SKILL.md
│   ├── README.md
│   └── references/                 # 7 reference files (00-06)
├── algo-rpi-plan/                  # Algorithm plan member skill
│   ├── SKILL.md
│   ├── README.md
│   └── references/                 # 7 reference files (00-06)
├── algo-rpi-plan-review/           # AI expert plan review member skill
│   ├── SKILL.md
│   ├── README.md
│   └── references/                 # 7 reference files (00-06)
├── algo-rpi-plan-reimagine/        # AI expert plan reimagine member skill
│   ├── SKILL.md
│   ├── README.md
│   └── references/                 # 7 reference files (00-06)
└── algo-rpi-implement/             # Algorithm implement member skill
    ├── SKILL.md
    ├── README.md
    └── references/                 # 7 reference files (00-06)
```

## Quick Start

### Standard Workflow
```
/algo-rpi

Problem: Implement real-time object detection for video stream
Constraints: <30ms latency per frame, <2GB memory, 95%+ mAP
Data: 1080p video at 30fps, 20 object classes
Hardware: NVIDIA RTX 3080 GPU
Metrics: mAP@0.5, latency, memory usage
```

### Full Workflow with AI Expert Review
```
/algo-rpi-full

Problem: Implement real-time object detection for video stream
Constraints: <30ms latency per frame, <2GB memory, 95%+ mAP
Data: 1080p video at 30fps, 20 object classes
Hardware: NVIDIA RTX 3080 GPU
Metrics: mAP@0.5, latency, memory usage
```

### Individual Phases
```
/algo-rpi-research
Problem: [algorithmic problem description]
Constraints: [time/space/latency/accuracy]
Data: [characteristics, volume]
Hardware: [CPU/GPU, memory limits]

/algo-rpi-plan
Research document: llm_docs/research/2026-01-15-1400-research-algo-detection.md
Targets: mAP@0.5=0.95, latency=30ms, memory=2GB

/algo-rpi-plan-review
Plan document: llm_docs/plans/2026-01-15-1415-plan-algo-detection.md

/algo-rpi-plan-reimagine
Plan document: llm_docs/plans/2026-01-15-1415-plan-algo-detection.md
Research document: llm_docs/research/2026-01-15-1400-research-algo-detection.md

/algo-rpi-implement
Plan document: llm_docs/plans/2026-01-15-1415-plan-algo-detection.md
# Or use v2 plan if reimagined:
Plan document: llm_docs/plans/2026-01-15-1415-plan-algo-detection-v2.md
```

## Workflow Phases

### Phase 1: Algorithm Research
**Skill:** `algo-rpi-research`

**Purpose:** Formalize algorithmic problem and explore solution approaches

**Key Features:**
- **Mandatory clarification protocol** for ambiguous problem statements
- Problem formalization with inputs, outputs, constraints, metrics, targets
- Codebase interface analysis
- Solution space exploration (3-5 candidate approaches)
- Trade-off analysis (complexity, quality, resource requirements)
- Validation plan with dataset splits and reproducibility

**Output:** `llm_docs/research/YYYY-MM-DD-HHMM-research-algo-<topic>.md`

**Pause Point:** Present candidate approaches, wait for user to select approach

### Phase 2: Algorithm Plan
**Skill:** `algo-rpi-plan`

**Purpose:** Create detailed implementation plan with quantitative targets

**Key Features:**
- **Mandatory approach confirmation** from research
- **Standard P0-P5 phase structure:**
  - **P0: Baseline & Harness** — Establish baseline, dataset splits, metrics, benchmark harness
  - **P1: Prototype** — Implement minimal viable algorithm, verify correctness
  - **P2: Evaluation** — Full evaluation, ablations, significance testing
  - **P3: Optimization** — Profile, vectorize, parallelize, meet performance targets
  - **P4: Robustness** — Edge cases, determinism, error handling
  - **P5: Packaging** — Documentation, examples, reproducibility artifacts
- **Quantitative targets table** with explicit metrics, latency, memory
- Reproducibility checklist (seeds, versions, dataset hash, hardware config)

**Output:** `llm_docs/plans/YYYY-MM-DD-HHMM-plan-algo-<topic>.md`

**Pause Point:** Present plan with quantitative targets, wait for approval

### Phase 3: AI Expert Plan Review (Optional)
**Skill:** `algo-rpi-plan-review`

**Purpose:** Review implementation plan as an AI/ML expert for theoretical soundness and practical implications

**Key Features:**
- **6-dimension expert review:**
  - Algorithm selection (is this the right algorithm?)
  - Theoretical soundness (convergence, complexity, statistical validity)
  - Numerical stability (precision, overflow, gradient issues)
  - Practical deployment (latency, memory, monitoring, maintenance)
  - Evaluation rigor (baselines, metrics, statistical testing)
  - Reproducibility (seeds, versions, determinism)
- **In-place plan annotation** with severity levels (CRITICAL, IMPORTANT, SUGGESTION)
- **Algorithm alternatives** suggested when genuinely beneficial
- **Quantified concerns** with specific analysis

**Output:** Modified plan with expert review annotations and recommendations

**Pause Point:** Present review summary, offer to proceed to reimagine or skip to implement

### Phase 4: AI Expert Plan Reimagine (Optional)
**Skill:** `algo-rpi-plan-reimagine`

**Purpose:** Reimagine the implementation plan from scratch for optimal algorithm design

**Key Features:**
- **Systematic algorithm space exploration** (different families, complexities, trade-offs)
- **5-dimension optimization:**
  - Algorithm efficiency (time/space complexity, vectorization, parallelization)
  - ML best practices (proper evaluation, avoiding leakage, statistical rigor)
  - Production-readiness (latency, memory, monitoring, graceful degradation)
  - Theoretical elegance (simpler solutions, principled approaches)
  - Industry standards (what would a senior ML engineer do?)
- **Comprehensive comparison** explaining v2 improvements over original
- **Creates new v2 plan** (preserves original)

**Output:** `llm_docs/plans/YYYY-MM-DD-HHMM-plan-algo-<topic>-v2.md`

**Pause Point:** Present v2 plan with comparison, get user confirmation on which plan to implement

### Phase 5: Algorithm Implement
**Skill:** `algo-rpi-implement`

**Purpose:** Execute plan with quantitative verification and reproducibility

**Key Features:**
- **Phase-by-phase execution** (P0 → P5)
- **Performance gates** at P1, P2, P3, P4 milestones
- **Quantitative measurement** in table format
- **Reproducibility enforcement** (seeds, deterministic ops, version pinning)
- Mismatch evaluation before implementation
- Progress tracking with plan checkboxes

**Output:** Code changes, benchmark results, updated plan, reproducibility artifacts

**Pause Point:** Present implementation summary with final metrics table

## When to Use Full Workflow vs Standard Workflow

### Use `/algo-rpi-full` (with AI expert review) when:
- Algorithm choice is critical and needs expert validation
- Performance targets are aggressive and need optimization
- Production deployment requires high confidence in design
- You want a second opinion on the algorithm approach
- You're willing to invest time in thorough review and optimization
- Numerical stability or theoretical soundness is critical

### Use `/algo-rpi` (standard workflow) when:
- Algorithm choice is straightforward
- Time constraints don't allow for extensive review
- The problem is well-understood and low-risk
- You're confident in the initial plan
- You need to iterate quickly

## Integration with Other Skills

### Code Review
After implementation, invoke `/code-review` to:
- Run automated quality checks
- Review against coding standards
- Focus on algorithm-specific concerns (numerical stability, vectorization, type hints)
- Fix issues and verify corrections

### Commit Message
After code review, invoke `/commit-message` to:
- Generate conventional commit message
- Analyze staged changes
- Present for user confirmation

### Doctor
During implementation, invoke `/doctor` if:
- Unexpected errors occur
- Numerical stability issues arise
- Performance debugging needed

## Memory Bank Integration

The Algo-RPI workflow integrates with Memory Bank at each phase:

**Read at start of each phase:**
- `llm_docs/memory/activeContext.md` — Current context
- `llm_docs/memory/systemPatterns.md` — Existing patterns
- `llm_docs/memory/techContext.md` — Technical context

**Update after each phase:**
- Research: Add key findings and candidate approaches to `activeContext.md`
- Plan: Add design decisions and quantitative targets to `activeContext.md`
- Implement: Update `progress.md` with completed work and final metrics

## Clarification Protocols

**Algorithm Research MUST ask clarifying questions when:**
- Problem statement is ambiguous or underspecified
- Constraints (time/space/latency/accuracy) are unclear
- Data characteristics or hardware limits are not specified

Questions cover:
1. **Objective(s):** What should the algorithm optimize?
2. **Constraints:** Time/space/latency/accuracy requirements? Hardware limits?
3. **Data:** Characteristics, volume, variability?
4. **Environment:** CPU/GPU? Batch/streaming? Determinism?
5. **Boundaries:** Privacy/fairness? Allowed libraries/frameworks?

**Algorithm Plan MUST confirm:**
- Selected approach from research (if multiple options)
- Quantitative targets (metrics, latency, memory)
- Hardware constraints
- Plan structure (P0-P5 phases)

**Exception:** If request is narrowly defined and unambiguous, proceed directly.

## Pause Points

**Mandatory pause points between ALL phases:**
- ⏸️ After Research: Present candidate approaches, wait for user to select
- ⏸️ After Plan: Present plan with quantitative targets, wait for approval
- ⏸️ After Implement: Present implementation summary with metrics, wait for approval

These pause points ensure:
- User alignment at each stage
- Opportunity to adjust direction
- Prevention of wasted implementation effort
- Clear handoff between phases

## Reproducibility Requirements

**MANDATORY at every phase:**

1. **Random Seeds:** Set and document Python, NumPy, PyTorch/TensorFlow seeds
2. **Deterministic Ops:** Use deterministic algorithms where possible, document non-deterministic ops
3. **Version Pinning:** Pin all dependency versions in requirements file
4. **Data Versioning:** Record dataset version or hash
5. **Verification:** Same seed → same results across multiple runs

## Performance Gates

After each major phase, verify quantitative targets:

**Gate 1 (after P1):** Correctness on test cases, metrics within tolerance on small subset

**Gate 2 (after P2):** Primary metric meets target on full test set, statistically significant

**Gate 3 (after P3):** Latency and memory meet targets, no accuracy regression

**Gate 4 (after P4):** Edge cases pass, deterministic, graceful failure

If a gate fails:
1. Document gap (target vs achieved)
2. Analyze root cause
3. Present options (adjust target, additional work, accept limitation)
4. Get user decision

## Coding Standards

All Algo-RPI phases reference shared coding standards via `.shared/` symlink:

- `code-principles.md` — Core principles (DRY, SOLID, etc.)
- `code-style.md` — Style guidelines (naming, formatting, etc.)
- `ml-dl-guide.md` — ML/DL best practices
- `data-science-guide.md` — Data science guidelines

These standards are automatically applied during implementation and code review.

## Output Artifacts

### Research Document
- Location: `llm_docs/research/`
- Format: Markdown, no frontmatter
- Content: Problem formalization, candidate approaches, validation plan
- Structure: Problem statement, inputs/outputs/constraints, metrics, codebase interface analysis, baselines, candidates, risks, experiment plan

### Plan Document
- Location: `llm_docs/plans/`
- Format: Markdown, no frontmatter
- Content: Quantitative targets, P0-P5 phases, success criteria, reproducibility checklist
- Structure: Problem statement, quantitative targets table, selected approach, integration points, hardware assumptions, P0-P5 phases, risks, reproducibility checklist

### Implementation
- Location: Modified source files
- Format: Code changes following plan
- Tracking: Plan checkboxes updated, metrics table updated
- Verification: Automated checks + performance gates per phase
- Artifacts: Requirements file, seeds documented, hardware config recorded

## Quantitative Verification

Every phase reports metrics in table format:

| Metric | Target | Achieved | Baseline | Status |
|--------|--------|----------|----------|--------|
| mAP@0.5 | 0.95 | 0.96 | 0.87 | ✓ |
| Latency | 30ms | 28ms | 45ms | ✓ |
| Memory | 2GB | 1.8GB | 3.2GB | ✓ |

All performance claims must be backed by measurements.

## Tips

1. **Start with research** if problem formalization is unclear
2. **Use plan-only** if you already have research with candidate approaches
3. **Use implement-only** if you have an approved plan ready
4. **Ask clarifying questions** early to avoid rework
5. **Trust the pause points** — they prevent wasted effort
6. **Update Memory Bank** regularly for cross-session continuity
7. **Invoke code-review** after implementation for quality assurance
8. **Verify reproducibility** at every phase — it's non-negotiable

## Examples

### Example 1: Object Detection
```
/algo-rpi

Problem: Real-time object detection for video stream
Constraints: <30ms latency per frame, <2GB memory, 95%+ mAP
Data: 1080p video at 30fps, 20 object classes, indoor/outdoor scenes
Hardware: NVIDIA RTX 3080 GPU
Metrics: mAP@0.5, latency, memory usage
```

### Example 2: Optimization Algorithm
```
/algo-rpi-research
Problem: Solve vehicle routing problem with time windows
Constraints: <1 second solve time, 100+ locations, 10 vehicles
Data: Real-world delivery data, varying traffic patterns
Hardware: CPU only, 16GB RAM
Metrics: Total distance, constraint violations, solve time
```

### Example 3: ML Model
```
/algo-rpi

Problem: Text classification for customer support tickets
Constraints: 95%+ F1 score, <100ms inference, <500MB model size
Data: 50k labeled tickets, 20 categories, imbalanced classes
Hardware: CPU inference, GPU training available
Metrics: F1 score (macro), precision, recall, inference latency
```

## See Also

- `rpi/` — Generic R-P-I workflow (use for non-algorithmic tasks)
- `code-review/` — Code quality review skill
- `commit-message/` — Commit message generation skill
- `memory-bank/` — Memory Bank management skill
- `doctor/` — Failure diagnosis skill
- `coding-standards/` — Shared coding guidelines
