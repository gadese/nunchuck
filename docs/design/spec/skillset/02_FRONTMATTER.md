# Frontmatter

This document defines the canonical `SKILL.md` YAML frontmatter used for skillsets within the `nunchuck` repository.

## Canonical top-level fields

### `name`

- Type: `string`
- Purpose: Canonical identifier for the orchestrator skill.

### `description`

- Type: `string`
- Purpose: Human-readable summary of the skillset orchestrator.

### `metadata`

- Type: `object`
- Purpose: User-defined extension point.

## Canonical `metadata.skillset` fields

Skillsets are defined under `metadata.skillset`.

### `metadata.skillset.name`

- Type: `string`
- Purpose: Skillset identifier.

### `metadata.skillset.schema_version`

- Type: `integer`
- Purpose: Skillset schema version.

### `metadata.skillset.skills`

- Type: `string[]`
- Purpose: Ordered list of member skill names.

### `metadata.skillset.shared` (optional)

- Type: `object`
- Purpose: Declares shared resources for the skillset.

#### `metadata.skillset.shared.root`

- Type: `string`
- Purpose: Directory name for shared resources. Canonical value: `.shared`.

## Notes

- Pipelines are defined in the `pipelines/` sibling directory.
- The `requires` field is not part of the canonical skillset schema in this repository.
