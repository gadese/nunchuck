---
description: Canonical execution path for this skill.
index:
  - Step 1: Ensure intent exists and is ready
  - Step 2: Compile active plan
  - Step 3: Validate deterministically
---

# Procedure

## Step 1: Ensure intent exists and is ready

Use `plan-discuss` until `.plan/active.yaml` is `status: ready`.

## Step 2: Compile active plan

```bash
./scripts/skill.sh
```

This creates/overwrites `.plan/active/` from `.plan/active.yaml` and bakes in a deterministic surface scan result for auditability.

## Step 3: Validate deterministically

`plan-create` must produce schema-valid plan files. If compilation fails, fix `.plan/active.yaml` (or schemas) and re-run.
