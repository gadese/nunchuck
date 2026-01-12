# Instructions

## Initialize

1. Read all reference files listed in `metadata.references` in order before taking action.

## Policies

### Always

1. Run the CLI script to create tasks — do not manually create task files.
2. Use kebab-case for task IDs (e.g., `add-login-page`, `fix-header-bug`).
3. Set `--select` flag to auto-activate the task after creation.

### Never

1. Never manually write task files — always use `task create`.
2. Never use spaces or special characters in task IDs.
3. Never skip the `--kind` and `--risk` flags — they are required for proper categorization.
