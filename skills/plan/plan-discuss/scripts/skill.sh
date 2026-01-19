#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INCLUDE_DIR="$SCRIPT_DIR/include"

cmd_help() {
  cat <<'EOF'
plan-discuss - Shape and stabilize intent into .plan/active.yaml

Usage:
  plan-discuss [--mark-ready]
  plan-discuss help
  plan-discuss validate

Deterministic behavior:
- Ensures .plan/active.yaml exists (creates it if missing)
- Prints current artifact status and any schema errors
- Optionally marks artifact ready (requires no open questions)
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

  if [[ ! -f "$INCLUDE_DIR/plan_discuss_cli.py" ]]; then
    echo "error: missing $INCLUDE_DIR/plan_discuss_cli.py" >&2
    errors=$((errors + 1))
  fi

  if [[ $errors -gt 0 ]]; then
    return 1
  fi

  echo "ok: plan-discuss skill is runnable"
}

cmd_run() {
  uv run --project "$INCLUDE_DIR" -- python "$INCLUDE_DIR/plan_discuss_cli.py" "$@"
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

