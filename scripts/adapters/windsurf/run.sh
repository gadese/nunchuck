#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/adapters/windsurf/run.sh [--skills-root <dir>] [--output-root <dir>]

Generates Windsurf workflows into:
  <output-root>/.windsurf/workflows/

Defaults:
  --skills-root  skills
  --output-root  .
EOF
}

SKILLS_ROOT="skills"
OUTPUT_ROOT="."

while [[ $# -gt 0 ]]; do
  case "$1" in
    --skills-root)
      SKILLS_ROOT="$2"
      shift 2
      ;;
    --output-root)
      OUTPUT_ROOT="$2"
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

if [[ ! -d "$SKILLS_ROOT" ]]; then
  echo "Skills root not found: $SKILLS_ROOT" >&2
  exit 1
fi

SKILLS_ROOT_ABS="$(python3 -c 'import os,sys; print(os.path.realpath(sys.argv[1]))' "$SKILLS_ROOT")"
OUT_DIR="$OUTPUT_ROOT/.windsurf/workflows"
mkdir -p "$OUT_DIR"

# Ensure output reflects the current skill set (remove stale generated workflows).
# Only remove files that look like generator output and whose basename is not a current skill.
declare -A _EXPECTED=()
while IFS= read -r -d '' _sf; do
  _EXPECTED["$(basename "$(dirname "$_sf")")"]=1
done < <(find "$SKILLS_ROOT" -type f -name "SKILL.md" -print0)

while IFS= read -r -d '' _wf; do
  _base="$(basename "$_wf" .md)"
  if [[ -n "${_EXPECTED[$_base]:-}" ]]; then
    continue
  fi
  if grep -q "This workflow delegates to the agent skill at" "$_wf"; then
    rm -f "$_wf"
  fi
done < <(find "$OUT_DIR" -maxdepth 1 -type f -name "*.md" -print0)

extract_description() {
  awk '
  BEGIN { in_fm=0; in_desc=0; desc="" }
  /^---[[:space:]]*$/ {
    if (!in_fm) { in_fm=1; next }
    else { exit }
  }
  in_fm {
    if (in_desc) {
      if ($0 ~ /^[^[:space:]][^:]*:[[:space:]]*/) {
        in_desc=0
      } else {
        sub(/^[[:space:]]+/, "", $0)
        if (desc != "") desc = desc " "
        desc = desc $0
        next
      }
    }

    if ($0 ~ /^description:[[:space:]]*/) {
      val = $0
      sub(/^description:[[:space:]]*/, "", val)
      if (val == ">" || val == "|") {
        in_desc=1
        next
      }
      gsub(/^"|"$/, "", val)
      print val
      exit
    }
  }
  END {
    if (desc != "") print desc
  }
  ' "$1"
}

sanitize_yaml_string() {
  python3 -c 'import json,sys; print(json.dumps(sys.stdin.read().strip()))'
}

count=0
while IFS= read -r -d '' skill_file; do
  skill_dir="$(dirname "$skill_file")"
  name="$(basename "$skill_dir")"

<<<<<<< HEAD
  # Skip coding-standards (reference-only, not invoked directly)
  if [[ "$name" == "coding-standards" ]]; then
    continue
  fi

  rel_dir="$skill_dir"
  rel_dir="${rel_dir#"$SKILLS_ROOT"/}"
=======
  skill_dir_abs="$(python3 -c 'import os,sys; print(os.path.realpath(sys.argv[1]))' "$skill_dir")"

  rel_dir="$skill_dir_abs"
  rel_dir="${rel_dir#"$SKILLS_ROOT_ABS"/}"
>>>>>>> master

  desc_raw="$(extract_description "$skill_file" | tr '\n' ' ' | sed -e 's/[[:space:]]\+/ /g' -e 's/^ //g' -e 's/ $//g')"
  desc_yaml="$(printf '%s' "$desc_raw" | sanitize_yaml_string)"

  workflow_file="$OUT_DIR/$name.md"

  {
    echo "---"
    echo "description: $desc_yaml"
    echo "auto_execution_mode: 1"
    echo "---"
    echo
    echo "# $name"
    echo
    echo "This workflow delegates to the agent skill at \`$skill_dir_abs/\`."
    echo
    echo "## Skill Root"
    echo
    echo "- **Path:** \`$SKILLS_ROOT_ABS/\`"
    echo
    echo "## Skill Location"
    echo
    echo "- **Path:** \`$skill_dir_abs/\`"
    echo "- **Manifest:** \`$skill_dir_abs/SKILL.md\`"
    echo
  } > "$workflow_file"

  count=$((count + 1))
done < <(find "$SKILLS_ROOT" -type f -name "SKILL.md" -print0)

echo "Generated $count workflow(s) in $OUT_DIR"
