---
description: Canonical execution path for this skill.
index:
  - Step 1: Pre-merge Lint
  - Step 2: Merge
  - Step 3: Post-merge Lint
  - Step 4: Review
---

# Procedure

## Step 1: Pre-merge Lint

```bash
../md-review/scripts/skill.sh chunks/
```

Fix any issues before proceeding.

## Step 2: Merge

```bash
./scripts/skill.sh chunks/ --out merged.md
```

## Step 3: Post-merge Lint

```bash
../md-review/scripts/skill.sh merged.md
```

## Step 4: Review

Invoke md-review for quality assessment.
