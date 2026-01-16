#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INCLUDE_DIR="$SCRIPT_DIR/include"

if [[ -f "$SCRIPT_DIR/.config.sh" ]]; then
    source "$SCRIPT_DIR/.config.sh"
fi

cmd_help() {
    cat <<'EOF'
task-select - Select a task as active

Commands:
  help      Show this help message
  validate  Verify the skill is runnable (read-only)

Usage:
  task-select <id>
  task-select help
  task-select validate

Writes the active task ID to .tasks/.active.
EOF
}

cmd_validate() {
    local errors=0

    if ! command -v uv &>/dev/null; then
        echo "error: uv not found. Install from https://docs.astral.sh/uv/" >&2
        errors=$((errors + 1))
    fi

    if [[ ! -f "$INCLUDE_DIR/pyproject.toml" ]]; then
        echo "error: missing $INCLUDE_DIR/pyproject.toml" >&2
        errors=$((errors + 1))
    fi

    if [[ ! -f "$INCLUDE_DIR/task_select_cli.py" ]]; then
        echo "error: missing $INCLUDE_DIR/task_select_cli.py" >&2
        errors=$((errors + 1))
    fi

    if [[ $errors -gt 0 ]]; then
        return 1
    fi

    echo "ok: task-select skill is runnable"
}

cmd_run() {
    PYTHONPATH="$INCLUDE_DIR" uv run python "$INCLUDE_DIR/task_select_cli.py" "$@"
}

case "${1:-}" in
    ""|help)
        cmd_help
        ;;
    validate)
        cmd_validate
        ;;
    *)
        cmd_run "$@"
        ;;
esac
