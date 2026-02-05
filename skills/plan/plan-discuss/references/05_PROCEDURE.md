---
description: Canonical execution path for this skill.
index:
  - Step 1: Ensure artifact exists
  - Step 2: Clarify and fill intent
  - Step 3: Mark ready (optional)
---

# Procedure

## Step 1: Ensure artifact exists

Run:

```bash
./scripts/skill.sh
```

This creates `.plan/active.yaml` if missing and prints status.

## Step 2: Clarify and fill intent

Iterate with the user until:

- Objective is specific and testable
- Success criteria are checkable
- Constraints and assumptions are explicit
- Open questions are enumerated
- A minimal subplan/task outline exists (titles only)

Update `.plan/active.yaml` accordingly.

## Step 3: Mark ready (optional)

Once there are no open questions blocking compilation:

```bash
./scripts/skill.sh --mark-ready
```

Then invoke `plan-create`.

