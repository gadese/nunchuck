---
name: task-close
license: MIT
description: >
  Close a task by setting state to closed, recording close_reason and closed_at.
  Recomputes intent hash and clears `.tasks/.active` if it pointed to this task.
metadata:
  author: Jordan Godau
  references:
    - 00_INSTRUCTIONS.md
    - 01_PROCEDURE.md
  keywords:
    - task
    - close
    - complete
    - finish
    - done
    - abandon
---

# INSTRUCTIONS

1. Refer to `metadata.references`.
