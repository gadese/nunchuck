---
description: Canonical execution path for this skill.
index:
  - Step 1: Gather Context
  - Step 2: Check for Suggestions
  - Step 3: Add Entry
  - Step 4: Verify
---

# Procedure

## Step 1: Gather Context

Ask user or infer:

- What changed?
- Which category? (Added/Changed/Fixed/etc.)
- Is there a PR/issue reference?

## Step 2: Check for Suggestions

```bash
scripts/suggest.sh
```

Use as reference, but curate.

## Step 3: Add Entry

```bash
scripts/run.sh <category> "<entry text>"
```

Example:

```bash
scripts/run.sh Fixed "Resolve authentication timeout issue (#123)"
```

## Step 4: Verify

```bash
../changelog-verify/scripts/run.sh
```
