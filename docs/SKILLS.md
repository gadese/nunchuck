# Skills Reference

Complete reference of all skills available in nunchuck.

---

## Skill Containers

Some skill directories are **containers** of multiple standalone skills (for example `skills/plan/` and `skills/prompt/`). Containers are for discovery and organization, not orchestration.

### changelog

**Path:** `skills/changelog/`

Manages Keep a Changelog format files with deterministic operations, chrono-aware guardrails, and git integration.

**Member Skills:**

- `changelog-init` - Initialize a new changelog from template
- `changelog-update` - Add entries to [Unreleased] section
- `changelog-release` - Cut a release by versioning [Unreleased]
- `changelog-verify` - Verify changelog format compliance

**Keywords:** `changelog`, `keepachangelog`, `release`, `versioning`

[Read more](../skills/changelog/README.md)

---

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

## See Also

- [Contributing Guidelines](../CONTRIBUTING.md) - Add your own skills
