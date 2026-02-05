# Skills Reference

Complete reference of all skills available in nunchuck.

---

## Skill Containers

Some skill directories are **containers** of multiple standalone skills (for example `skills/plan/` and `skills/prompt/`). Containers are for discovery and organization, not orchestration.

### doctor

**Path:** `skills/doctor/`

Diagnoses software failures by combining deterministic evidence gathering with agent judgment. Models failures as medical cases. Idempotent — run repeatedly until confident diagnosis.

**Keywords:** `diagnose`, `debug`, `investigate`, `evidence`, `hypothesis`, `treatment`

[Read more](../skills/doctor/README.md)

---

### grape

**Path:** `skills/grape/`

AI-enabled, deterministic codebase search. Converts vague intent into explicit, auditable grep parameters and executes a stable surface scan over disk.

**Keywords:** `search`, `grep`, `codebase`, `find`, `scan`

[Read more](../skills/grape/README.md)

---

### md

**Path:** `skills/md/`

Orchestrates markdown document workflows with deterministic operations (split, merge, lint) and agent review.

**Member Skills:**

- `md-split` - Split large markdown files into chunks
- `md-merge` - Merge markdown chunks back together
- `md-review` - Agent review of markdown content

**Keywords:** `markdown`, `split`, `merge`, `lint`, `review`

[Read more](../skills/md/README.md)

---

### plan

**Path:** `skills/plan/`

Manages bounded work units with structured plans stored in `.plan/`.

**Member Skills:**

- `plan-discuss` - Clarify and stabilize intent into `.plan/active.yaml`
- `plan-create` - Compile intent into `.plan/active/`
- `plan-exec` - Execute tasks and archive to `.plan/archive/`

**Keywords:** `plan`, `planning`, `execute`, `archive`, `intent`

[Read more](../skills/plan/README.md)

---

### prompt

**Path:** `skills/prompt/`

Separates intent formation from execution to protect humans from premature or misaligned action.

**Member Skills:**

- `prompt-forge` - Create structured prompts from intent
- `prompt-compile` - Compile YAML artifact into PROMPT.md
- `prompt-exec` - Execute compiled prompts

**Keywords:** `prompt`, `intent`, `forge`, `compile`, `execute`

[Read more](../skills/prompt/README.md)

---

### task

**Path:** `skills/task/`

Manages bounded work units with single-file tasks stored in `.tasks/`, skepticism-aware hashing, and staleness detection.

**Member Skills:**

- `task-create` - Create new tasks
- `task-list` - List available tasks
- `task-select` - Select a task to work on
- `task-close` - Close completed tasks

**Keywords:** `task`, `create`, `list`, `select`, `close`

[Read more](../skills/task/README.md)

---

### rpi

**Path:** `skills/rpi/`

Research-Plan-Implement workflow for general software development tasks.

**Member Skills:**

- `rpi-research` - Codebase research and documentation
- `rpi-plan` - Technical planning
- `rpi-plan-review` - Expert review of implementation plans
- `rpi-plan-reimagine` - Reimagine plans from scratch for optimization
- `rpi-implement` - Plan execution

**Keywords:** `research`, `plan`, `implement`, `review`, `reimagine`, `workflow`

[Read more](../skills/rpi/README.md)

---

### algo-rpi

**Path:** `skills/algo-rpi/`

Algorithm Research-Plan-Implement workflow for algorithm development and optimization tasks.

**Member Skills:**

- `algo-rpi-research` - Algorithm problem research
- `algo-rpi-plan` - Algorithm planning with P0-P5 phases
- `algo-rpi-plan-review` - AI/ML expert review of algorithm plans
- `algo-rpi-plan-reimagine` - AI/ML expert reimagination for optimal design
- `algo-rpi-implement` - Algorithm implementation with metrics

**Keywords:** `algorithm`, `research`, `plan`, `implement`, `review`, `reimagine`, `quantitative`, `reproducibility`

[Read more](../skills/algo-rpi/README.md)

---

## Standalone Skills

### brainstorm

**Path:** `skills/brainstorm/`

Interactive algorithm/AI solution brainstorming through multi-round narrowing funnel. Explores problem space via Socratic dialogue and tool-assisted research, converging to a ranked shortlist of 2-3 candidate approaches.

**Keywords:** `brainstorm`, `algorithm`, `ai`, `exploration`, `interactive`, `narrowing`

[Read more](../skills/brainstorm/README.md)

---

### code-review

**Path:** `skills/code-review/`

Systematic code review and cleanup. Reviews ONLY modified or specified files for quality, adherence to guidelines, and best practices.

**Keywords:** `code-review`, `quality`, `standards`, `cleanup`

[Read more](../skills/code-review/README.md)

---

### commit-message

**Path:** `skills/commit-message/`

Generate descriptive, conventional commit messages based on code changes.

**Keywords:** `commit`, `message`, `conventional`, `git`

[Read more](../skills/commit-message/README.md)

---

### memory-bank

**Path:** `skills/memory-bank/`

Manages workspace-specific Memory Bank files in `llm_docs/memory/`. Provides persistent cross-session context for AI agents.

**Keywords:** `memory`, `context`, `persistence`, `workspace`

[Read more](../skills/memory-bank/README.md)

---

## See Also

- [Contributing Guidelines](../CONTRIBUTING.md) - Add your own skills
