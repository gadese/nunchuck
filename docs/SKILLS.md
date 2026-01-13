# Skills Reference

Complete reference of all skills and skillsets available in nunchuck.

---

## Skillsets (Orchestrators)

Skillsets coordinate multiple related skills. See [Skillsets Documentation](./SKILLSETS.md) for details.

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

### dtx

**Path:** `skills/dtx/`

Manages an agent's working context via explicit, auditable `.dtx/` artifacts.

**Member Skills:**

- `dtx-gather` - Deterministic evidence gathering (glob + ripgrep)
- `dtx-state` - Present current admissible working set
- `dtx-forget` - Revoke a premise from the contract
- `dtx-validate` - Validate artifacts for integrity and staleness

**Keywords:** `context`, `evidence`, `contract`, `gather`, `forget`

[Read more](../skills/dtx/README.md)

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

- `plan-create` - Create execution plans
- `plan-exec` - Execute existing plans
- `plan-status` - Track plan progress
- `plan-review` - Review plan completion

**Keywords:** `plan`, `planning`, `execute`, `status`

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

- [Skillsets Documentation](./SKILLSETS.md) - Spec-compliant agent skill groups
- [Contributing Guidelines](../CONTRIBUTING.md) - Add your own skills
