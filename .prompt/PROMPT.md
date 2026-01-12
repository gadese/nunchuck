# Nunchuck CLI Consolidation

## Objective

Consolidate the nunchuck CLI to be a globally-installed tool that manages agent skills with adapter generation, validation, and installation.

The CLI is for **consuming and managing skills**, not authoring.

## Constraints

- Must be globally installable (`pip install`)
- Must keep original skills safe in read-only global location
- Must support multiple IDE adapters (Windsurf, Cursor)
- Must integrate existing shell scripts into Python CLI
- Must work cross-platform (Unix + Windows)
- Standardize terminology on "skills" (deprecate "packs")

## Decisions

### Global Store

`~/.nunchuck/skills/` — created automatically on first CLI use. No explicit init command needed. The store is the read-only source of truth for projects.

### Adapter Generation

Auto-detect `.windsurf/` or `.cursor/` in target project and generate adapters automatically. Also provide explicit flags: `--windsurf`, `--cursor`.

### Terminology

Use "skills" consistently throughout. Deprecate "packs" terminology in code and documentation.

### Scope

Consumption and management only. Authoring support is out of scope for now.

## CLI Commands

### Global Skill Management

| Command | Description |
|---------|-------------|
| `nunchuck add <path>` | Add skill to global store (from local path or remote) |
| `nunchuck remove <name>` | Remove skill from global store |
| `nunchuck list [--global]` | List skills (in global store or target project) |
| `nunchuck validate <path>` | Validate skill against Agent Skills spec |

### Project Operations

| Command | Description |
|---------|-------------|
| `nunchuck use <name>` | Use skill in project (references global store + auto-generate adapters) |
| `nunchuck drop <name>` | Remove skill from project |

### Adapter Generation

| Command | Description |
|---------|-------------|
| `nunchuck adapter` | Auto-detect IDE and generate adapters |
| `nunchuck adapter --windsurf` | Generate Windsurf workflows |
| `nunchuck adapter --cursor` | Generate Cursor rules |

### Utilities

| Command | Description |
|---------|-------------|
| `nunchuck index` | Generate agent-optimized .INDEX.md for skills |

## Current State

### Existing Commands

- `list` — Discover skills in a directory
- `validate` — Validate skill against spec
- `install` — Copy skill to project's `.nunchuck/packs/`
- `uninstall` — Remove skill from project

### Separate Scripts (to migrate)

- `scripts/adapter/windsurf.sh` — Generate Windsurf workflows
- `scripts/adapter/cursor.sh` — Generate Cursor rules
- `scripts/index/index.sh` — Generate agent-optimized index

### Gaps to Address

1. Adapter generation not in CLI
2. Index generation not in CLI
3. No global skill store implementation
4. "packs" terminology needs migration to "skills"

## Migration Tasks

1. Rename internal "packs" → "skills" in code
2. Implement global store at `~/.nunchuck/skills/`
3. Migrate `scripts/adapter/windsurf.sh` logic to Python
4. Migrate `scripts/adapter/cursor.sh` logic to Python
5. Migrate `scripts/index/index.sh` logic to Python
6. Add new commands: `add`, `use`, `drop`, `adapter`, `index`
7. Update existing commands: `list`, `validate`
8. Remove deprecated: `install`, `uninstall` (replaced by `use`, `drop`)
