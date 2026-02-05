---
description: Non-negotiable invariants for this skill.
index: []
---

# Always

- Always close via the deterministic entrypoint (`scripts/run.sh <id> --reason ...`).
- Always require a close reason (`completed` or `abandoned`).
- Always ensure the task’s acceptance criteria are consistent with the reason.
