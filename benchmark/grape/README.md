# Grape Benchmarks

This harness compares baseline agent runs vs grape-assisted runs.

## Structure

- `tasks/`: task definitions (prompts + success checks)
- `scripts/`: run and scoring scripts
- `runs/`: per-run outputs (config, results, logs)

## Environment

Set a Codex CLI command that reads a prompt from stdin:

```bash
export CODEX_CMD='codex exec'
```

Optional:

```bash
export CODEX_ARGS=''
export N=5
export WARMUP=1
export TIMEOUT_SEC=60
export WORKDIR=''
export WORKDIR_MODE=''
export WORKDIR_SOURCE=''
```

## Running

Baseline:

```bash
./benchmark/grape/scripts/run_baseline.sh benchmark/grape/tasks/T001_ui.md
```

Grape:

```bash
./benchmark/grape/scripts/run_grape.sh benchmark/grape/tasks/T001_ui.md
```

## Publication-grade setup

For publishable comparisons, prefer isolated workdirs and explicit clean/test commands:

```bash
export WORKDIR_MODE=copy
export WORKDIR_SOURCE=''   # optional; defaults to repo root
export WARMUP=1
export TIMEOUT_SEC=60
```

Then add per-task `Clean Command` and `Test Command` entries (e.g., lint/tests) to reduce variance.

## Notes

- `CODEX_CMD` should be a full command that consumes prompt text from stdin.
- If you want deterministic behavior regardless of your `~/.codex/config.toml`, consider:
  `export CODEX_CMD='codex -a never -s workspace-write exec'`
- The scripts log stdout/stderr to `runs/<run-id>/logs/`.
- If a task includes a `Check Command`, the runner will execute it and record pass/fail.
- If a task includes a `Test Command`, the runner will execute it and record pass/fail.
- If a task includes a `Clean Command`, it runs before each attempt and is logged.
- If a task includes `Constraints`, they are appended to the prompt before running.
- Tasks in `tasks/` use BENCH markers for deterministic checks; update prompts/checks if you prefer repo-specific assertions.
- `WARMUP=1` runs one unscored warm-up per task/mode.
- `TIMEOUT_SEC` uses `timeout` if available (set to a positive integer to enable).
- `WORKDIR` runs all commands inside a specific repo copy for isolation.
- `WORKDIR_MODE=copy` creates a per-run workdir by copying `WORKDIR_SOURCE` (or repo root) into the run directory (requires `rsync`).
- Token and context usage are parsed from JSONL logs if the CLI emits them.
