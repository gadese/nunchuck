#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INCLUDE_DIR="$SCRIPT_DIR/include"

if [[ -f "$SCRIPT_DIR/.config.sh" ]]; then
    source "$SCRIPT_DIR/.config.sh"
fi

cmd_help() {
    cat <<'EOF'
prompt-forge - Shape and stabilize intent into .prompt/active.yaml

Commands:
  help      Show this help message
  validate  Verify the skill is runnable (read-only)

Usage:
  prompt-forge [--mark-ready] [--force]
  prompt-forge help
  prompt-forge validate

Deterministic behavior:
- Ensures .prompt/active.yaml exists (creates it if missing)
- Prints current artifact status
- Optionally marks artifact ready (requires no open questions unless --force, and requires a prompt)
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

    if [[ ! -f "$INCLUDE_DIR/prompt_forge_cli.py" ]]; then
        echo "error: missing $INCLUDE_DIR/prompt_forge_cli.py" >&2
        errors=$((errors + 1))
    fi

    if [[ $errors -gt 0 ]]; then
        return 1
    fi

    echo "ok: prompt-forge skill is runnable"
}

cmd_run() {
    PYTHONPATH="$INCLUDE_DIR" uv run python "$INCLUDE_DIR/prompt_forge_cli.py" "$@"
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
