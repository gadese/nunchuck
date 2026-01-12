# Procedure

## Step 1: List all tasks

```bash
cd skills/task/.resources/scripts
uv run task list
```

Output format:

```
<id> | <state> | <kind> | <risk> | <title> [flags]
```

## Step 2: Interpret flags

- `*` — Currently active task (selected)
- `stale:Nd since X` — Task is stale (N days since last update/review)
- `hash-mismatch` — Task content has drifted from stored intent hash

## Step 3: Filter as needed

List only open tasks:

```bash
uv run task list --state open
```

List only stale tasks:

```bash
uv run task list --stale
```

## Step 4: Act on warnings

For stale tasks:
- Review the task — is it still relevant?
- If yes, update `updated_at` or `last_reviewed_at`
- If no, close it with `--reason abandoned`

For hash-mismatch tasks:
- The task content has changed since the hash was computed
- Review the changes — is the intent still valid?
- Re-run create or manually update `intent_hash` if valid
