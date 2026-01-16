#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INCLUDE_DIR="$SCRIPT_DIR/include"

if [[ -f "$SCRIPT_DIR/.config.sh" ]]; then
    source "$SCRIPT_DIR/.config.sh"
fi

cmd_help() {
    cat <<'EOF'
prompt-compile - Compile .prompt/active.yaml into .prompt/PROMPT.md

Commands:
  help      Show this help message
  validate  Verify the skill is runnable (read-only)

Usage:
  prompt-compile [--force] [--dry-run]
  prompt-compile help
  prompt-compile validate

Deterministic behavior:
- Verifies active artifact exists
- Validates artifact (unless --force)
- Writes .prompt/PROMPT.md (unless --dry-run)
- Preserves active artifact
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

    if [[ ! -f "$INCLUDE_DIR/prompt_compile_cli.py" ]]; then
        echo "error: missing $INCLUDE_DIR/prompt_compile_cli.py" >&2
        errors=$((errors + 1))
    fi

    if [[ $errors -gt 0 ]]; then
        return 1
    fi

    echo "ok: prompt-compile skill is runnable"
}

cmd_run() {
    PYTHONPATH="$INCLUDE_DIR" uv run python "$INCLUDE_DIR/prompt_compile_cli.py" "$@"
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
