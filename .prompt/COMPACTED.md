# Nunchuck CLI Consolidation

## Objective

Consolidate nunchuck CLI into globally-installed skill management tool with adapter generation. Focus on consumption, not authoring.

## Constraints

- Global install via `pip install`
- Read-only global store at `~/.nunchuck/skills/`
- Support Windsurf + Cursor adapters
- Cross-platform (Unix + Windows)
- Use "skills" terminology (deprecate "packs")

## Decisions

### Global Store
Auto-create `~/.nunchuck/skills/` on first use. No explicit init needed.

### Adapter Generation

Auto-detect `.windsurf/` or `.cursor/` with explicit flags: `--windsurf`, `--cursor`.

### Terminology
Standardize on "skills" throughout.

### Scope
Consumption and management only.

## CLI Commands

### Global Skill Management
| Command | Description |
|---------|-------------|
| `nunchuck add <path>` | Add skill to global store |
| `nunchuck remove <name>` | Remove skill from global store |
| `nunchuck list [--global]` | List skills |
| `nunchuck validate <path>` | Validate skill |

### Project Operations
| Command | Description |
|---------|-------------|
| `nunchuck use <name>` | Use skill in project |
| `nunchuck drop <name>` | Remove skill from project |

### Adapter Generation
| Command | Description |
|---------|-------------|
| `nunchuck adapter` | Auto-detect IDE |
| `nunchuck adapter --windsurf` | Generate Windsurf workflows |
| `nunchuck adapter --cursor` | Generate Cursor rules |

### Utilities
| Command | Description |
|---------|-------------|
| `nunchuck index` | Generate .INDEX.md |

## Current State

Existing: `list`, `validate`, `install`, `uninstall`
Scripts to migrate: adapters (windsurf.sh, cursor.sh), index.sh

## Migration Tasks

1. Rename "packs" → "skills"
2. Implement global store
3. Migrate adapter scripts to Python
4. Add commands: `add`, `use`, `drop`, `adapter`, `index`
5. Update: `list`, `validate`
6. Remove: `install`, `uninstall`

---
compaction:
  target: /home/jgodau/work/personal/nunchuck/.prompt/PROMPT.md
  mode: auto
  source_hash: <sha256>
  output_hash: <sha256>

auto_decision:
  effective_mode: mixed
  confidence: high
  justification: Content is mixed - decisional sections (Decisions, Constraints) preserved with light mode, operational sections (Current State, Migration Tasks) compacted with heavy mode. Tables preserved as they contain named entities.
