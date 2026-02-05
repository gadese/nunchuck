---
description: Canonical execution path for this skill.
index:
  - Step 1: Validate and select active task
  - Step 2: Load task files
  - Step 3: Execute work
  - Step 4: Record results
  - Step 5: Archive when terminal
---

# Procedure

## Step 1: Validate and select active task

Run:

```bash
./scripts/skill.sh
```

This validates `.plan/active/`, synchronizes derived statuses, and deterministically selects the single `in_progress` task (starting the next pending task if none are in progress).

## Step 2: Load task files

Read:

- `.plan/active/plan.md`
- `.plan/active/<letter>/index.md`
- `.plan/active/<letter>/<roman>.md`

## Step 3: Execute work

- Perform each Work step.
- Verify artifacts exist.

## Step 4: Record results

- Write concrete **Output**.
- Write explicit **Handoff**.
- Set task status to `complete`.

## Step 5: Archive when terminal

When all tasks are `complete` or `deferred`, re-run `./scripts/skill.sh` to archive the plan to `.plan/archive/<id>/`.
