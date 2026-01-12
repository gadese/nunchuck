# Procedure

## Step 1: Verify First

```bash
../.shared/scripts/skill.sh verify
```

Fix any issues before proceeding.

## Step 2: Determine Version

Get explicit version from user (e.g., "1.2.0").

## Step 3: Cut Release

```bash
../.shared/scripts/skill.sh release 1.2.0
```

Optionally specify date:

```bash
../.shared/scripts/skill.sh release 1.2.0 --date 2024-01-15
```

## Step 4: Verify Again

```bash
../.shared/scripts/skill.sh verify
```

## Step 5: Commit

Suggest committing the release.
