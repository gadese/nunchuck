#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INCLUDE_DIR="$SCRIPT_DIR/include"

if [[ -f "$SCRIPT_DIR/.config.sh" ]]; then
    source "$SCRIPT_DIR/.config.sh"
fi

cmd_help() {
    cat <<'EOF'
prompt-exec - Execute the forged prompt exactly as written

Commands:
  help      Show this help message
  validate  Verify the skill is runnable (read-only)

Usage:
  prompt-exec [--dry-run]
  prompt-exec help
  prompt-exec validate

Deterministic behavior:
- Requires .prompt/active.yaml exists
- Requires artifact status is ready
- Writes receipt to .prompt/receipts/
- Deletes .prompt/active.yaml after successful execution
- Prints the prompt text to execute
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

    if [[ ! -f "$INCLUDE_DIR/prompt_exec_cli.py" ]]; then
        echo "error: missing $INCLUDE_DIR/prompt_exec_cli.py" >&2
        errors=$((errors + 1))
    fi

    if [[ $errors -gt 0 ]]; then
        return 1
    fi

    echo "ok: prompt-exec skill is runnable"
}

cmd_run() {
    PYTHONPATH="$INCLUDE_DIR" uv run python "$INCLUDE_DIR/prompt_exec_cli.py" "$@"
}

case "${1:-}" in
    help)
        cmd_help
        ;;
    validate)
        cmd_validate
        ;;
    *)
        cmd_run "$@"
        ;;
esac
