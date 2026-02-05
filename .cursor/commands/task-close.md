# task-close

Close a task by setting state to closed, recording close_reason and closed_at. Recomputes intent hash and clears `.tasks/.active` if it pointed to this task.

This command delegates to the agent skill at `skills/task/task-close/`.

## Skill Root

- **Path:** `skills/`

## Skill Location

- **Path:** `skills/task/task-close/`
- **Manifest:** `skills/task/task-close/SKILL.md`

