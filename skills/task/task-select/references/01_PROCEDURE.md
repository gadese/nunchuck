# Procedure

## Step 1: Identify the task to select

Use `task list` to find the task ID:

```bash
cd skills/task/.resources/scripts
uv run task list
```

## Step 2: Select the task

```bash
uv run task select <id>
```

Example:

```bash
uv run task select add-auth
```

## Step 3: Review warnings

If warnings appear, consider:

- **Stale warning**: Has this task been dormant? Is it still relevant?
- **Hash mismatch**: Has the task drifted from its original intent?

These are prompts for skepticism. The task is still selected, but you should verify it's still valid before proceeding.

## Step 4: Verify selection

```bash
uv run task list
```

The selected task will have `*` flag.
