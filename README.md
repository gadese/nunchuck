# Nunchuck

A rigorously structured collection of agent skills designed to reduce drift, enforce determinism, and make agentic work auditable. Built on the [Open Agent-Skill Specification](https://github.com/JordanGunn/agent-skill-spec) and extended with internal specifications that define canonical structures, execution patterns, and epistemic guardrails.

---

## Documentation

- **[Quickstart Guide](./docs/QUICKSTART.md)** — Getting started
- **[Skills Reference](./docs/SKILLS.md)** — Browse all available skills
- **[Skillsets](./docs/SKILLSETS.md)** — Orchestrator skills that coordinate member skills
- **[Contributing](./CONTRIBUTING.md)** — Add your own skills

---

## Design Philosophy

This repository treats language as inherently ambiguous and builds systems that succeed *despite* that ambiguity. Three principles guide all skill design:

- **Determinism First, Subjectivity Last** — Subjective reasoning must never compensate for missing deterministic outputs. If evidence is incomplete, return to earlier execution phases rather than explaining around gaps.

- **Artifacts as Completion Signals** — Success is mechanically verifiable. Skills declare what they produce; validation checks existence. Missing artifacts redirect execution to producing steps.

- **Professional Skepticism** — Agents interpret, clarify, and challenge rather than blindly comply. User input is valuable but not authoritative truth. Responsibility for correctness cannot be outsourced.

These principles are formalized in the [Design Documentation](./docs/design/.INDEX.md), which includes epistemic tenets, interaction tenets, and a determinism framework.

---

## Specification Compliance

### Open Agent-Skill Spec

All skills conform to the [Open Agent-Skill Specification](https://github.com/JordanGunn/agent-skill-spec), ensuring portability across agent platforms. Each `SKILL.md` contains frontmatter-only definitions with explicit metadata for references, scripts, and keywords.

### Internal Specifications

Beyond the open spec, this repository enforces internal specifications that define:

- **[SKILL.md Structure](./docs/design/specs/skillmd/.INDEX.md)** — Frontmatter schema, body constraints, validation rules
- **[References Structure](./docs/design/specs/references/.INDEX.md)** — Canonical 7-file reference set (`00_ROUTER` through `06_FAILURES`)
- **[Scripts Structure](./docs/design/specs/scripts/.INDEX.md)** — Cross-platform script requirements and naming
- **[Skillset Structure](./docs/design/specs/skillset/.INDEX.md)** — Orchestrator schema, pipelines, shared resources

These specifications ensure consistency across all skills and enable tooling to validate compliance.

---

## Skills

All skills live in the `skills/` directory. Browse them directly or use the reference documentation:

- **[Skills Reference](./docs/SKILLS.md)** — Complete list of skillsets and member skills with descriptions and keywords
- **[Skillsets Documentation](./docs/SKILLSETS.md)** — How orchestrator skills coordinate members, schema details, and usage patterns

### Available Skillsets

**Research-Plan-Implement (RPI):**
- `/rpi` — Generic software development workflow
- `/rpi-research` — Codebase research and documentation
- `/rpi-plan` — Technical planning
- `/rpi-plan-review` — Expert review of implementation plans
- `/rpi-plan-reimagine` — Reimagine plans from scratch for optimization
- `/rpi-implement` — Plan execution
- `/rpi-full` — Full workflow with expert review and reimagine phases

**Algorithm RPI:**
- `/algo-rpi` — Algorithm development workflow
- `/algo-rpi-research` — Algorithm problem research
- `/algo-rpi-plan` — Algorithm planning with P0-P5 phases
- `/algo-rpi-plan-review` — AI/ML expert review of algorithm plans
- `/algo-rpi-plan-reimagine` — AI/ML expert reimagination for optimal design
- `/algo-rpi-implement` — Algorithm implementation with metrics
- `/algo-rpi-full` — Full workflow with AI expert review and optimization

**Standalone Skills:**
- `/brainstorm` — Interactive algorithm/AI solution brainstorming
- `/code-review` — Code quality review (scoped to modified files)
- `/commit-message` — Generate conventional commit messages
- `/memory-bank` — Manage persistent workspace context
- `/doctor` — Diagnostic protocol for complex failures

**Reference-Only:**
- `coding-standards` — Centralized code guidelines (accessed via `.shared/` in other skills)

---

## Usage

See the **[Quickstart Guide](./docs/QUICKSTART.md)** for installation, IDE integration, and first steps.

---

## Scripts

Utility scripts provide thin integration layers without duplicating skill content. Skills remain spec-compliant so they transfer cleanly when IDEs adopt agent skills natively.

### Deploy to Other Projects

Copy nunchuck skills to another project and generate workflows:

```bash
# Full deployment (copy skills + generate workflows)
bash scripts/deploy/deploy-to-project.sh /path/to/your/project

# Dry run to see what would be copied
bash scripts/deploy/deploy-to-project.sh /path/to/your/project --dry-run

# Copy skills only (generate workflows later)
bash scripts/deploy/deploy-to-project.sh /path/to/your/project --skills-only
```

This creates a `.nunchuck/` directory in your target project (gitignored) containing skills and scripts, then generates workflows that reference them.

### IDE Adapters

Generate IDE-specific configurations that reference skills without copying them:

```bash
# Windsurf: generates .windsurf/workflows/
bash scripts/adapters/windsurf/run.sh --skills-root skills --output-root .

# Cursor: generates .cursor/commands/
bash scripts/adapters/cursor/run.sh --skills-root skills --output-root .
```

Windows (PowerShell):

```powershell
.\scripts\adapters\windsurf\run.ps1 --skills-root skills --output-root .
.\scripts\adapters\cursor\run.ps1 --skills-root skills --output-root .
```

### Index Generator

Generate `.SKILLS.md` for agent discovery:

```bash
bash scripts/index/run.sh --skills-root skills
```

---

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for release history.

## License

See [LICENSE](./LICENSE) for details.
