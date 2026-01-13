# Reference Frontmatter

Reference frontmatter shall be included in all references files to:

1. Provide additional metadata about the reference.
2. Enable deterministic anchor-level routing.
3. Describe the reference file content.

---

## Fields

### Required

#### `description`

A short description of the reference file purpose and intents.

#### `index`

A flat list of H2 anchors in the reference file for section-level routing.

**Constraints:**

- Only H2 headers are indexed (H3+ navigated naturally by agent)
- Entries must match actual H2 headers in the file body
- Order should reflect document structure

### Optional

#### `summary`

A short summary of the reference file purpose and intents.

**Character limit:** 256

#### `tags`

A list of tags that can be used to search for the reference file.

---

## Example

```yaml
description: Canonical execution path for the skill.
summary: Step-by-step procedure from inputs to outputs.
tags:
  - procedure
  - execution
  - steps
index:
  - Inputs
  - Steps
  - Outputs
  - Checkpoints
```
