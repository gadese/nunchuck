# Quickstart Guide

## What are Agent Skills?

Agent Skills are structured instructions that help AI agents perform specific tasks more effectively. Each skill provides:

- **Clear guidance** on when and how to use the skill
- **Step-by-step procedures** for executing tasks
- **Reference materials** for detailed information
- **Scripts** for automation when applicable

## Repository Structure

```
skills/
├── README.md                          # Main documentation entry point
├── INDEX.md                           # Auto-generated skill index
├── LICENSE                            # Repository license
├── SPEC.md                            # Formal specification for skills
├── docs/                              # Documentation directory
│   ├── 01_QUICKSTART.md              # This file
│   ├── 02_SKILLS.md                  # Individual skills reference
│   ├── 03_SKILLSETS.md               # Skillsets concept and usage
│   ├── 04_SCHEMAS.md                 # Schema documentation
│   └── 05_CONTRIBUTING.md            # Contribution guidelines
├── adapter/                           # Adapter skills for IDE/tools
│   ├── SKILL.md                      # Adapter skillset orchestrator
│   ├── cursor/                       # Cursor IDE adapter
│   └── windsurf/                     # Windsurf IDE adapter
├── index/                             # Skill indexing and discovery
├── plan/                              # Planning and execution skillset
│   ├── SKILL.md                      # Plan skillset orchestrator
│   ├── .resources/                   # Shared skillset resources
│   ├── create/                       # Plan creation skill
│   ├── exec/                         # Plan execution skill
│   └── status/                       # Plan status tracking skill
└── refactor/                          # Code refactoring skillset
    ├── SKILL.md                      # Refactor skillset orchestrator
    ├── .resources/                   # Shared skillset resources
    └── [member skills]/              # Individual refactor skills
```

## Using Skills

### Finding Skills

1. Browse the [Skills Index](../INDEX.md) for a hierarchical view
2. Check the [Skills Reference](./02_SKILLS.md) for detailed descriptions
3. Search by keywords in the INDEX.md keyword index

### Activating a Skill

Skills are activated by referencing their `SKILL.md` file. The frontmatter contains:
- `name`: Unique identifier
- `description`: Purpose and usage triggers
- `metadata`: Additional properties including references, scripts, and keywords

For detailed instructions, read the reference files in the skill's `references/` directory.

### Running Scripts

Many skills include executable scripts for automation:

**macOS / Linux / WSL:**
```bash
./path/to/skill/scripts/script-name.sh
```

**Windows (PowerShell):**
```powershell
.\path\to\skill\scripts\script-name.ps1
```

## Key Concepts

### Individual Skills

Standalone skills that perform specific tasks. Examples:
- `index`: Generate skill index
- `plan-create`: Create execution plans
- `refactor-dictionaries`: Audit dictionary usage

### Skillsets

Orchestrator skills that coordinate multiple related skills. Examples:
- `plan`: Coordinates plan creation and execution
- `refactor`: Coordinates code quality audits
- `adapter`: Coordinates IDE adapter generation

See [Skillsets Documentation](./03_SKILLSETS.md) for more details.

### Windows Support

Recent updates include PowerShell (`.ps1`) scripts alongside Bash (`.sh`) scripts for cross-platform support:
- `adapter`, `index`, and `plan` skills include `.ps1` scripts
- Scripts maintain feature parity across platforms

## Quick Actions

### Generate Skill Index

```bash
# macOS / Linux / WSL
./index/scripts/index.sh

# Windows (PowerShell)
.\index\scripts\index.ps1
```

### Create a Plan

```bash
# macOS / Linux / WSL
# Follow instructions in plan/create/references/

# Windows (PowerShell)
# Follow instructions in plan/create/references/
```

### Check Plan Status

```bash
# macOS / Linux / WSL
./plan/status/scripts/status.sh

# Windows (PowerShell)
.\plan\status\scripts\status.ps1
```

### Generate IDE Adapters

```bash
# macOS / Linux / WSL
./adapter/windsurf/scripts/generate.sh
./adapter/cursor/scripts/generate.sh

# Windows (PowerShell)
.\adapter\windsurf\scripts\generate.ps1
.\adapter\cursor\scripts\generate.ps1
```

## Next Steps

- Read the [Skills Reference](./02_SKILLS.md) to explore available skills
- Learn about [Skillsets](./03_SKILLSETS.md) for coordinating multiple skills
- Review [Schema Documentation](./04_SCHEMAS.md) to understand skill structure
- Check [Contributing Guidelines](./05_CONTRIBUTING.md) to add your own skills
