# Agent Skills

A collection of structured skills for AI agents to perform specific tasks effectively and avoid common pitfalls in agentic programming.

## What's New

**Recent Updates (January 2026):**

- 🚀 **New CLI**: Simplified nunchuck CLI with flat command structure
- 📦 **Centralized Skills**: All skills installed to `~/.nunchuck/skills` for easy access
- ⚡ **uv + hatchling**: Fast Python build system with uv package manager
- ✨ **New Skillset**: `changelog` - Keep a Changelog management
- 🪟 **Windows Support**: PowerShell installers and cross-platform scripts
- 🔄 **Simplified Usage**: `nunchuck list` and `nunchuck use <skill>` commands

See [CHANGELOG.md](./CHANGELOG.md) for complete release history.

## Quick Links

- 📚 [Skills Reference](./docs/SKILLS.md) - Browse all available skills
- 🎯 [Skillsets](./docs/SKILLSETS.md) - Learn about orchestrator skills
- 📋 [INDEX.md](./INDEX.md) - Auto-generated skill index with keywords
- 📖 [Agent Skills Specification](./docs/references/AGENT_SKILLS_SPEC.md) - Official Agent Skills format
- 🚀 [nunchuck CLI](./docs/CLI.md) - Command-line tool for skill management

## Overview

This repository provides **agent skills** - structured instructions that help AI agents perform specific tasks more effectively. Each skill includes:

- **Clear guidance** on when and how to use the skill
- **Step-by-step procedures** stored in reference files
- **Executable scripts** for automation (Unix and Windows)
- **Keywords and metadata** for easy discovery

### Key Features

- **Individual Skills**: Standalone skills for specific tasks
- **Skillsets**: Orchestrator skills that coordinate multiple related skills
- **Cross-Platform**: Scripts for both Unix/macOS/Linux (`.sh`) and Windows (`.ps1`)
- **Progressive Disclosure**: Frontmatter-only `SKILL.md` files that reference detailed documentation
- **Spec Compliant**: Follows the [Agent Skills specification](./docs/references/AGENT_SKILLS_SPEC.md)

## Documentation

### Getting Started

- **[Quickstart Guide](./docs/QUICKSTART.md)** - Get up and running quickly
  - What are Agent Skills?
  - Repository structure overview
  - Using skills and running scripts
  - Quick actions and common commands

### Reference Documentation

- **[Skills Reference](./docs/SKILLS.md)** - Complete guide to individual skills
  - Adapter skills (Cursor, Windsurf)
  - Index skill (skill discovery)
  - Plan skills (create, exec, status)
  - Refactor skills (code quality audits)
  - Keyword index for quick lookup

- **[Skillsets](./docs/SKILLSETS.md)** - Understanding orchestrator skills
  - What are skillsets?
  - How skillsets work
  - Available skillsets (adapter, plan, refactor)
  - Creating new skillsets

- **[Schema Documentation](./docs/schema/SKILL.md)** - Technical reference
  - SKILL.md frontmatter schema
  - SKILLSET custom schema
  - Plan artifact frontmatter
  - Examples and validation

- **[Contributing Guidelines](./CONTRIBUTING.md)** - Add your own skills
  - Adding individual skills
  - Creating skillsets
  - Schema requirements
  - Testing and submission

## Available Skills

### Skillsets (Orchestrators)

- **[changelog](./skills/changelog/SKILL.md)** - Keep a Changelog management
- **[doctor](./skills/doctor/SKILL.md)** - Diagnostic protocol for debugging
- **[md](./skills/md/SKILL.md)** - Markdown chunking workflows
- **[plan](./skills/plan/SKILL.md)** - Coordinate planning, execution, and status tracking
- **[prompt](./skills/prompt/SKILL.md)** - Prompt forging + deliberate execution
- **[task](./skills/task/SKILL.md)** - Task lifecycle management

### Member Skills

Each skillset contains member skills that can be used individually or together:

| Skillset | Members |
|----------|---------|
| changelog | `changelog-init`, `changelog-update`, `changelog-release`, `changelog-verify` |
| md | `md-split`, `md-merge`, `md-review` |
| plan | `plan-create`, `plan-exec`, `plan-status`, `plan-review` |
| prompt | `prompt-forge`, `prompt-compile`, `prompt-exec` |
| task | `task-create`, `task-list`, `task-select`, `task-close` |

See [Skills Reference](./docs/SKILLS.md) for detailed descriptions.

## Quick Start

### Install nunchuck CLI

**Unix (macOS/Linux/WSL):**

```bash
# Install with uv (recommended)
./scripts/install.sh uv

# Or use pip/pipx
./scripts/install.sh pipx
```

**Windows (PowerShell):**

```powershell
# Install with uv (recommended)
.\scripts\install.ps1 uv

# Or use pip
.\scripts\install.ps1 user
```

### Use Skills

```bash
# List all available skills
nunchuck list

# Copy a skill to your project
nunchuck use doctor

# Generate IDE adapters
nunchuck adapter --windsurf
```

See [Quickstart Guide](./docs/QUICKSTART.md) for more details.

## Understanding Skills

### Skill Structure

Each skill follows a canonical structure:

```text
skill-name/
├── SKILL.md              # Frontmatter + minimal instructions
└── references/           # Detailed documentation
    ├── 00_INDEX.md
    ├── 01_SUMMARY.md
    ├── 02_TRIGGERS.md
    ├── 03_ALWAYS.md
    ├── 04_NEVER.md
    ├── 05_PROCEDURE.md
    └── 06_FAILURES.md
```

### Skillset Structure

Skillsets coordinate multiple related skills:

```text
skillset/
├── SKILL.md              # Orchestrator with metadata.skillset
├── .pipelines/           # Execution pipelines
├── .shared/              # Shared resources
│   ├── assets/
│   ├── references/
│   └── scripts/
└── member-skill/         # Individual skills
    └── SKILL.md
```

See [Skillsets Documentation](./docs/SKILLSETS.md) to learn more.

## Contributing

We welcome contributions! See the [Contributing Guidelines](./CONTRIBUTING.md) for complete details.

## License

See [LICENSE](./LICENSE) for details.
