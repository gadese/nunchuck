# Reference Frontmatter

Reference frontmatter may be included to provide additional metadata about the reference.

## Principle

> **Reference frontmatter describes intent and verification —
> not behavior, not reasoning, not prose.**

If metadata cannot be validated or enforced, it does not belong here.

## Rules

1. Frontmatter is **optional**
2. If present, it must be valid `YAML`
3. Only the keys defined below are allowed
4. Frontmatter is **descriptive**, not instructional
5. Instructions live in Markdown body content

## Fields

### `executes`

- Type: `string[]`
- Purpose: List of scripts executed by the reference

### `uses`

- Type: `string[]`
- Purpose: List of assets used by the reference

### `produces`

- Type: `string[]`
- Purpose: List of artifacts produced by the reference

## Example

```md
---
executes:
  - scripts/index.sh
  - scripts/index.ps1
uses:
  - assets/schema.json
  - assets/example.md
outputs: 
  - index-md
---
...
```
