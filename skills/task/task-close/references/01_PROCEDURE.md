# Procedure

## Step 1: Verify task completion

Before closing, confirm:

- For `completed`: All acceptance criteria in `## Acceptance` are checked
- For `abandoned`: Decision has been made to stop pursuing this task

## Step 2: Close the task

```bash
cd skills/task/.resources/scripts
uv run task close <id> --reason <completed|abandoned>
```

Examples:

```bash
uv run task close add-auth --reason completed
uv run task close old-feature --reason abandoned
```

## Step 3: Verify closure

```bash
uv run task list --state closed
```

The task should appear with `closed` state.

## Notes

- If the closed task was active, `.tasks/.active` is automatically cleared
- The `closed_at` timestamp is set automatically
- The intent hash is recomputed to capture final state
