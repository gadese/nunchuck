#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/deploy/deploy-to-project.sh <target-project-dir> [options]

Copies nunchuck skills to another project and generates IDE workflows.

Arguments:
  <target-project-dir>    Path to the target project directory

Options:
  --skills-only           Copy only skills, don't generate workflows
  --workflows-only        Generate workflows only (assumes skills already copied)
  --dry-run              Show what would be copied without actually copying
  -h, --help             Show this help message

Examples:
  # Full deployment (copy skills + generate workflows)
  scripts/deploy/deploy-to-project.sh ~/projects/my-app

  # Copy skills only
  scripts/deploy/deploy-to-project.sh ~/projects/my-app --skills-only

  # Dry run to see what would be copied
  scripts/deploy/deploy-to-project.sh ~/projects/my-app --dry-run

What gets copied:
  - skills/                    All nunchuck skills
  - scripts/adapters/          IDE adapter scripts
  - scripts/index/             Index generator script
  - .gitignore entry           Adds .nunchuck/ to target's .gitignore

What gets generated in target project:
  - .windsurf/workflows/       Windsurf workflow files
  - .cursor/commands/          Cursor command files
  - .SKILLS.md                 Skills index

EOF
}

TARGET_DIR=""
SKILLS_ONLY=false
WORKFLOWS_ONLY=false
DRY_RUN=false

# Parse arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --skills-only)
      SKILLS_ONLY=true
      shift
      ;;
    --workflows-only)
      WORKFLOWS_ONLY=true
      shift
      ;;
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    -*)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
    *)
      if [[ -z "$TARGET_DIR" ]]; then
        TARGET_DIR="$1"
      else
        echo "Unexpected argument: $1" >&2
        usage >&2
        exit 2
      fi
      shift
      ;;
  esac
done

if [[ -z "$TARGET_DIR" ]]; then
  echo "Error: Target project directory required" >&2
  usage >&2
  exit 2
fi

# Resolve paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NUNCHUCK_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
TARGET_DIR="$(cd "$TARGET_DIR" 2>/dev/null && pwd || echo "$TARGET_DIR")"

if [[ ! -d "$TARGET_DIR" ]]; then
  echo "Error: Target directory does not exist: $TARGET_DIR" >&2
  exit 1
fi

echo "Nunchuck deployment"
echo "==================="
echo "Source: $NUNCHUCK_ROOT"
echo "Target: $TARGET_DIR"
echo ""

# Function to copy with dry-run support
copy_item() {
  local src="$1"
  local dst="$2"
  local item_name="$3"
  
  if [[ "$DRY_RUN" == true ]]; then
    echo "[DRY RUN] Would copy: $item_name"
    echo "  From: $src"
    echo "  To:   $dst"
  else
    echo "Copying: $item_name"
    mkdir -p "$(dirname "$dst")"
    cp -r "$src" "$dst"
  fi
}

# Function to run command with dry-run support
run_command() {
  local cmd="$1"
  local description="$2"
  
  if [[ "$DRY_RUN" == true ]]; then
    echo "[DRY RUN] Would run: $description"
    echo "  Command: $cmd"
  else
    echo "Running: $description"
    eval "$cmd"
  fi
}

# Copy skills and scripts
if [[ "$WORKFLOWS_ONLY" == false ]]; then
  echo ""
  echo "Step 1: Copying skills and scripts"
  echo "-----------------------------------"
  
  # Create .nunchuck directory in target
  NUNCHUCK_TARGET="$TARGET_DIR/.nunchuck"
  
  if [[ "$DRY_RUN" == false ]]; then
    mkdir -p "$NUNCHUCK_TARGET"
  fi
  
  # Copy skills
  copy_item "$NUNCHUCK_ROOT/skills" "$NUNCHUCK_TARGET/skills" "skills/"
  
  # Copy adapter scripts
  copy_item "$NUNCHUCK_ROOT/scripts/adapters" "$NUNCHUCK_TARGET/scripts/adapters" "scripts/adapters/"
  
  # Copy index script
  copy_item "$NUNCHUCK_ROOT/scripts/index" "$NUNCHUCK_TARGET/scripts/index" "scripts/index/"
  
  # Add .nunchuck to .gitignore if not already there
  GITIGNORE="$TARGET_DIR/.gitignore"
  if [[ -f "$GITIGNORE" ]]; then
    if ! grep -q "^\.nunchuck/" "$GITIGNORE" 2>/dev/null; then
      if [[ "$DRY_RUN" == true ]]; then
        echo "[DRY RUN] Would add .nunchuck/ to .gitignore"
      else
        echo "Adding .nunchuck/ to .gitignore"
        echo ".nunchuck/" >> "$GITIGNORE"
      fi
    else
      echo ".nunchuck/ already in .gitignore"
    fi
  else
    if [[ "$DRY_RUN" == true ]]; then
      echo "[DRY RUN] Would create .gitignore with .nunchuck/"
    else
      echo "Creating .gitignore with .nunchuck/"
      echo ".nunchuck/" > "$GITIGNORE"
    fi
  fi
  
  echo ""
  echo "✓ Skills and scripts copied to $NUNCHUCK_TARGET"
fi

# Generate workflows
if [[ "$SKILLS_ONLY" == false ]]; then
  echo ""
  echo "Step 2: Generating IDE workflows"
  echo "---------------------------------"
  
  NUNCHUCK_TARGET="$TARGET_DIR/.nunchuck"
  
  if [[ ! -d "$NUNCHUCK_TARGET/skills" ]]; then
    echo "Error: Skills not found at $NUNCHUCK_TARGET/skills" >&2
    echo "Run without --workflows-only first, or copy skills manually" >&2
    exit 1
  fi
  
  # Generate Windsurf workflows
  run_command \
    "bash '$NUNCHUCK_TARGET/scripts/adapters/windsurf/run.sh' --skills-root '$NUNCHUCK_TARGET/skills' --output-root '$TARGET_DIR'" \
    "Windsurf workflows"
  
  # Generate Cursor commands
  run_command \
    "bash '$NUNCHUCK_TARGET/scripts/adapters/cursor/run.sh' --skills-root '$NUNCHUCK_TARGET/skills' --output-root '$TARGET_DIR'" \
    "Cursor commands"
  
  # Generate skills index
  run_command \
    "bash '$NUNCHUCK_TARGET/scripts/index/run.sh' --dir '$TARGET_DIR'" \
    "Skills index (.SKILLS.md)"
  
  echo ""
  echo "✓ Workflows generated in $TARGET_DIR"
fi

# Summary
echo ""
echo "Deployment complete!"
echo "===================="

if [[ "$DRY_RUN" == true ]]; then
  echo ""
  echo "This was a dry run. No files were actually copied or modified."
  echo "Run without --dry-run to perform the actual deployment."
else
  echo ""
  echo "Files in target project:"
  echo "  .nunchuck/skills/              - Nunchuck skills"
  echo "  .nunchuck/scripts/             - Generator scripts"
  echo "  .windsurf/workflows/           - Windsurf workflows"
  echo "  .cursor/commands/              - Cursor commands"
  echo "  .SKILLS.md                     - Skills index"
  echo "  .gitignore                     - Updated to ignore .nunchuck/"
  echo ""
  echo "The .nunchuck/ directory is gitignored and won't be committed."
  echo ""
  echo "To update nunchuck skills in the future:"
  echo "  1. cd $NUNCHUCK_ROOT"
  echo "  2. git pull"
  echo "  3. scripts/deploy/deploy-to-project.sh $TARGET_DIR"
fi

echo ""
