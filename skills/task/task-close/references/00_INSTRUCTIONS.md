# Instructions

## Initialize

1. Read all reference files listed in `metadata.references` in order before taking action.

## Policies

### Always

1. Use the CLI script to close tasks — do not manually edit task files.
2. Provide a close reason: `completed` or `abandoned`.
3. Close tasks when they are done, not when they are "mostly done".

### Never

1. Never close a task without a reason.
2. Never use `completed` if acceptance criteria are not met — use `abandoned`.
3. Never leave stale tasks open indefinitely — close them as `abandoned` if no longer pursuing.
