# Scripts

Utility scripts for skill management and IDE integration.

## IDE Adapters

Generate IDE-specific configurations that reference skills without duplicating content. This keeps skills spec-compliant while providing native IDE integration.

### Windsurf

Generates `.windsurf/workflows/` with slash commands for each skill.

```bash
# Unix
bash scripts/adapters/windsurf/run.sh --skills-root skills --output-root .

# Windows
.\scripts\adapters\windsurf\run.ps1 --skills-root skills --output-root .
```

### Cursor

Generates `.cursor/commands/` with command palette entries for each skill.

```bash
# Unix
bash scripts/adapters/cursor/run.sh --skills-root skills --output-root .

# Windows
.\scripts\adapters\cursor\run.ps1 --skills-root skills --output-root .
```

## Design Rationale

These scripts exist as thin integration layers. Skills remain portable and spec-compliant, ready to transfer cleanly when IDEs adopt agent skills natively. The adapters generate references to skills rather than copying content, avoiding duplication and drift.
