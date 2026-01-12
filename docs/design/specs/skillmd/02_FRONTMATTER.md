# Frontmatter Fields

This document defines the canonical `SKILL.md` YAML frontmatter fields

## Canonical top-level fields

### `name`

- Type: `string`
- Purpose: Canonical identifier for the skill

### `description`

- Type: `string`
- Purpose: Human-readable summary of what the skill does

## Metadata Sub-fields

`metadata` is the primary nunchuck extension point. It is intentionally user-defined, but in this repository it has a strict canonical shape.

### `metadata.author`

- Type: `string`
- Purpose: Skill author/maintainer

### `metadata.references`

- Type: `string[]`
- Purpose: Ordered list of Markdown reference files that contain the skill’s instructions and supporting material. Paths are relative to the skill directory.

### `metadata.scripts`

- Type: `string[]`
- Purpose: List of script entrypoints used by the skill (typically shell + PowerShell variants). Paths are relative to the skill directory.

### `metadata.assets`

- Type: `string[]`
- Purpose: List of static supporting files shipped with the skill (examples, fixtures, etc.). Paths are relative to the skill directory.

### `metadata.artifacts`

- Type: `string[]`
- Purpose: List of expected/generated outputs (may be empty). This is reserved for workflow output conventions.

### `metadata.keywords`

- Type: `string[]`
- Purpose: Search/discovery keywords.
