#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/adapters/unix/cursor.sh [--skills-root <dir>] [--output-root <dir>]

Generates Cursor commands into:
  <output-root>/.cursor/commands/

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

SKILLS_ROOT_REL="$SKILLS_ROOT"
OUT_DIR="$OUTPUT_ROOT/.cursor/commands"
mkdir -p "$OUT_DIR"

# Ensure output reflects the current skill set (remove stale commands).
find "$OUT_DIR" -maxdepth 1 -type f -name "*.md" -delete

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

count=0
while IFS= read -r -d '' skill_file; do
  skill_dir="$(dirname "$skill_file")"
  name="$(basename "$skill_dir")"

  # Skip coding-standards (reference-only, not invoked directly)
  if [[ "$name" == "coding-standards" ]]; then
    continue
  fi

  rel_dir="$skill_dir"
  rel_dir="${rel_dir#"$SKILLS_ROOT"/}"

  desc_raw="$(extract_description "$skill_file" | tr '\n' ' ' | sed -e 's/[[:space:]]\+/ /g' -e 's/^ //g' -e 's/ $//g')"

  cmd_file="$OUT_DIR/$name.md"

  {
    echo "# $name"
    echo
    echo "$desc_raw"
    echo
    echo "This command delegates to the agent skill at \`$SKILLS_ROOT_REL/$rel_dir/\`."
    echo
    echo "## Skill Root"
    echo
    echo "- **Path:** \`$SKILLS_ROOT_REL/\`"
    echo
    echo "## Skill Location"
    echo
    echo "- **Path:** \`$SKILLS_ROOT_REL/$rel_dir/\`"
    echo "- **Manifest:** \`$SKILLS_ROOT_REL/$rel_dir/SKILL.md\`"
    echo
  } > "$cmd_file"

  count=$((count + 1))
done < <(find "$SKILLS_ROOT" -type f -name "SKILL.md" -print0)

echo "Generated $count command(s) in $OUT_DIR"
