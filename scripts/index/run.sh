#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: ./scripts/index/run.sh [-d|--dir <output_dir>]

Writes .SKILLS.md containing a simple list of skills (name + description).

Options:
  -d, --dir <path>   Output directory for .SKILLS.md (default: working directory)
  -h, --help         Show help
EOF
}

out_dir=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -d|--dir)
      out_dir="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ -z "$out_dir" ]]; then
  out_dir="$PWD"
fi

if [[ ! -d "$out_dir" ]]; then
  echo "Output directory not found: $out_dir" >&2
  exit 2
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/../.." && pwd)"
skills_dir="$repo_root/skills"

if [[ ! -d "$skills_dir" ]]; then
  echo "Skills directory not found: $skills_dir" >&2
  exit 2
fi

out_file="$out_dir/.SKILLS.md"

tmp_entries="$(mktemp)"
trap 'rm -f "$tmp_entries"' EXIT

while IFS= read -r -d '' skill_file; do
  awk '
    BEGIN { in_fm=0; in_desc=0; name=""; desc="" }
    NR==1 && $0=="---" { in_fm=1; next }
    in_fm && $0=="---" { exit }
    in_fm {
      if ($0 ~ /^name:[[:space:]]*/) {
        sub(/^name:[[:space:]]*/, "", $0)
        name=$0
        next
      }
      if ($0 ~ /^description:[[:space:]]*(>|\|)[[:space:]]*$/) {
        in_desc=1
        desc=""
        next
      }
      if ($0 ~ /^description:[[:space:]]*/) {
        sub(/^description:[[:space:]]*/, "", $0)
        desc=$0
        in_desc=0
        next
      }
      if (in_desc) {
        if ($0 ~ /^[[:space:]]+/) {
          sub(/^[[:space:]]+/, "", $0)
          if (desc != "") desc = desc " " $0
          else desc = $0
          next
        }
        in_desc=0
      }
    }
    END {
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", name)
      gsub(/^[[:space:]]+|[[:space:]]+$/, "", desc)
      gsub(/[[:space:]]+/, " ", desc)
      if (name != "") print name "\t" desc
    }
  ' "$skill_file" >> "$tmp_entries"
done < <(find "$skills_dir" -type f -name 'SKILL.md' -print0)

{
  echo "# Skills"
  sort -t $'\t' -k1,1 "$tmp_entries" | while IFS=$'\t' read -r name desc; do
    if [[ -n "$desc" ]]; then
      printf -- '- `%s` - %s\n' "$name" "$desc"
    else
      printf -- '- `%s`\n' "$name"
    fi
  done
} > "$out_file"
