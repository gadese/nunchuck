#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cmd_help() {
    cat <<'EOF'
md-split - Split a markdown file by H2 headings

Commands:
  help      Show this help message
  validate  Verify the skill is runnable (read-only)

Usage:
  md-split --in <source.md> [--out <dir>] [--prefix <NN>] [--dry-run] [--force] [--no-intro] [--manifest|--no-manifest]
  md-split help
  md-split validate

Deterministic behavior:
- Runs scripts/split.sh (or split.ps1 on Windows) to generate chunk files and .SPLIT.json
- Runs scripts/index.sh (or index.ps1 on Windows) to generate .INDEX.md
EOF
}

cmd_validate() {
    local errors=0

    if ! command -v bash &>/dev/null; then
        echo "error: bash not found" >&2
        errors=$((errors + 1))
    fi

    if [[ ! -f "$SCRIPT_DIR/split.sh" ]]; then
        echo "error: missing $SCRIPT_DIR/split.sh" >&2
        errors=$((errors + 1))
    fi

    if [[ ! -f "$SCRIPT_DIR/index.sh" ]]; then
        echo "error: missing $SCRIPT_DIR/index.sh" >&2
        errors=$((errors + 1))
    fi

    if [[ $errors -gt 0 ]]; then
        return 1
    fi

    echo "ok: md-split skill is runnable"
}

cmd_split_and_index() {
    bash "$SCRIPT_DIR/split.sh" "$@"

    local out_dir=""
    local in_file=""

    local args=("$@")
    for ((i=0; i<${#args[@]}; i++)); do
        if [[ "${args[$i]}" == "--in" ]]; then
            in_file="${args[$((i+1))]}"
        fi
        if [[ "${args[$i]}" == "--out" ]]; then
            out_dir="${args[$((i+1))]}"
        fi
    done

    if [[ -z "$out_dir" ]]; then
        if [[ -z "$in_file" ]]; then
            echo "error: --in is required" >&2
            exit 1
        fi
        local filename
        filename="$(basename "$in_file")"
        local base_name
        base_name="${filename%.*}"
        local out_dir_name
        out_dir_name="$(echo "$base_name" | tr '[:upper:]' '[:lower:]')"
        out_dir="$(dirname "$in_file")/$out_dir_name"
    fi

    bash "$SCRIPT_DIR/index.sh" --dir "$out_dir"
}

case "${1:-}" in
    help)
        cmd_help
        ;;
    validate)
        cmd_validate
        ;;
    *)
        cmd_split_and_index "$@"
        ;;
esac
