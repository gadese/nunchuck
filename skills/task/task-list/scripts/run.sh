#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INCLUDE_DIR="$SCRIPT_DIR/include"

uv run --project "$INCLUDE_DIR" -- python "$INCLUDE_DIR/task_list_cli.py" "$@"
