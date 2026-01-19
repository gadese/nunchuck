#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INCLUDE_DIR="$SCRIPT_DIR/include"

if [[ -f "$SCRIPT_DIR/.config.sh" ]]; then
    source "$SCRIPT_DIR/.config.sh"
fi

cmd_help() {
    cat <<'EOF'
plan-create - Compile .plan/active.yaml into .plan/active/

Commands:
  help      Show this help message
  validate  Verify the skill is runnable (read-only)

Usage:
  plan-create [--force]
  plan-create help
  plan-create validate

Creates/overwrites:
  .plan/active/plan.md
  .plan/active/<letter>/index.md
  .plan/active/<letter>/<roman>.md

Precondition:
  .plan/active.yaml exists and is status: ready (use plan-discuss).
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

    if [[ ! -f "$INCLUDE_DIR/plan_create_cli.py" ]]; then
        echo "error: missing $INCLUDE_DIR/plan_create_cli.py" >&2
        errors=$((errors + 1))
    fi

    if [[ $errors -gt 0 ]]; then
        return 1
    fi

    echo "ok: plan-create skill is runnable"
}

cmd_run() {
    uv run --project "$INCLUDE_DIR" -- python "$INCLUDE_DIR/plan_create_cli.py" "$@"
}

case "${1:-}" in
    "")
        cmd_run
        ;;
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
