---
description: Reference file for Procedure.
index:
  - Close
  - Verify
---

# Procedure

This file is kept for continuity. Prefer `05_PROCEDURE.md`.

## Close

```bash
scripts/run.sh <id> --reason completed
```

or:

```bash
scripts/run.sh <id> --reason abandoned
```

## Verify

```bash
../task-list/scripts/run.sh --state closed
```
