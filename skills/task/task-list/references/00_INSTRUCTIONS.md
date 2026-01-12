# Instructions

## Initialize

1. Read all reference files listed in `metadata.references` in order before taking action.

## Policies

### Always

1. Use the CLI script to list tasks — do not manually parse `.tasks/` directory.
2. Pay attention to warning flags: `stale` and `hash-mismatch`.
3. Use filters (`--state`, `--stale`) to narrow results when needed.

### Never

1. Never ignore stale or hash-mismatch flags — they indicate tasks needing review.
2. Never assume a task is current without checking its flags.
