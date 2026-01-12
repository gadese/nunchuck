# Skills Reference

Complete reference of all skills and skillsets available in nunchuck.

> **Tip:** Use `nunchuck list` to see all installed skills, or browse [INDEX.md](../INDEX.md) for the auto-generated index.

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

---

### doctor

**Path:** `skills/doctor/`

Diagnoses software failures by combining deterministic evidence gathering with agent judgment. Models failures as medical cases.

**Keywords:** `diagnose`, `debug`, `investigate`, `evidence`, `hypothesis`, `treatment`

**References:** `00_INDEX.md` through `06_FAILURES.md`

---

### md

**Path:** `skills/md/`

Orchestrates markdown document workflows with deterministic operations (split, merge, lint) and agent review.

**Member Skills:**

- `md-split` - Split large markdown files into chunks
- `md-merge` - Merge markdown chunks back together
- `md-review` - Agent review of markdown content

**Keywords:** `markdown`, `split`, `merge`, `lint`, `review`

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

---

### prompt

**Path:** `skills/prompt/`

Separates intent formation from execution to protect humans from premature or misaligned action.

**Member Skills:**

- `prompt-forge` - Create structured prompts from intent
- `prompt-compile` - Compile YAML artifact into PROMPT.md
- `prompt-exec` - Execute compiled prompts

**Keywords:** `prompt`, `intent`, `forge`, `compile`, `execute`

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

---

## Using Skills

### Via nunchuck CLI

```bash
# List all available skills
nunchuck list

# Copy a skill to your project
nunchuck use doctor

# Generate IDE adapters
nunchuck adapter --windsurf
```

### Via IDE Integration

After running `nunchuck adapter`, use slash commands:

- **Windsurf:** `/doctor`, `/plan-create`, `/changelog-init`
- **Cursor:** Access via command palette

---

## See Also

- [Skillsets Documentation](./SKILLSETS.md) - Learn about orchestrator skills
- [Auto-generated INDEX.md](../INDEX.md) - Complete index with pipelines
- [Schema Documentation](./schema/SKILL.md) - Understand skill structure
