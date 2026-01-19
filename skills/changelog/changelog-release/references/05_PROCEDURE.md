---
description: Canonical execution path for this skill.
index:
  - Step 1: Verify First
  - Step 2: Determine Version
  - Step 3: Cut Release
  - Step 4: Verify Again
  - Step 5: Commit
---

# Procedure

## Step 1: Verify First

```bash
../changelog-verify/scripts/run.sh
```

Fix any issues before proceeding.

## Step 2: Determine Version

Get explicit version from user (e.g., "1.2.0").

## Step 3: Cut Release

```bash
scripts/run.sh 1.2.0
```

Optionally specify date:

```bash
scripts/run.sh 1.2.0 --date 2024-01-15
```

## Step 4: Verify Again

```bash
../changelog-verify/scripts/run.sh
```

## Step 5: Commit

Suggest committing the release.
