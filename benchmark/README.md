# Benchmarks

This directory houses benchmark harnesses for skills in this repository.

## Strategy (High-Level)

We compare baseline agent behavior against skill-assisted behavior using repeatable prompts and measurable checks. The goal is to measure whether a skill improves speed, reduces wasted context, and increases correctness.

Core principles:

- **Paired runs**: For each task, run a baseline prompt and a skill-assisted prompt.
- **Repeatable**: Run each task multiple times (`N`) and summarize averages.
- **Deterministic checks**: Each task defines checks/tests to evaluate correctness.
- **Auditable**: Every run records environment metadata, timing, and outputs.
- **Optional isolation**: Runs can execute in per-run workdirs for clean state.

## Common Measurements

- **Time to completion** (seconds)
- **Correctness** via check/test commands
- **Token/context usage** if the CLI reports it
- **Diff size** (files/insertions/deletions) as a proxy for change scope

## Layout

Each skill can have its own harness under `benchmark/<skill>/` with:

- `tasks/` task definitions (baseline + skill prompts, checks/tests)
- `scripts/` runner and scoring utilities
- `runs/` outputs and receipts

## Usage

See each skill's benchmark README for concrete commands and environment variables.
