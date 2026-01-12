#!/usr/bin/env bash
#
# nunchuck.sh - Install nunchuck CLI on Unix-like systems
#
# Usage: ./install.sh [dev|user|pipx|uv]
#   dev:  Install in development mode (editable) using pip
#   user: Install for current user only using pip
#   pipx: Install using pipx (recommended)
#   uv:   Install using uv (fastest, recommended for development)
#

set -euo pipefail

# Default installation mode
MODE="${1:-uv}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Installing nunchuck CLI...${NC}"

# Check if uv is installed (for uv mode)
if [ "$MODE" = "uv" ]; then
    if ! command -v uv &> /dev/null; then
        echo -e "${YELLOW}uv not found. Installing uv...${NC}"
        curl -LsSf https://astral.sh/uv/install.sh | sh
        
        # Add uv to PATH if not already there
        if ! command -v uv &> /dev/null; then
            export PATH="$HOME/.cargo/bin:$PATH"
            echo -e "${YELLOW}Adding ~/.cargo/bin to PATH for this session${NC}"
        fi
    fi
fi

# Check if Python 3.10+ is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed${NC}"
    echo "Please install Python 3.10 or later from https://python.org"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.10"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo -e "${RED}Error: Python $REQUIRED_VERSION or later is required (found $PYTHON_VERSION)${NC}"
    exit 1
fi

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Go up one level to get to repo root (scripts -> repo root)
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Change to repo root
echo -e "${YELLOW}Changing to repository root: $REPO_ROOT${NC}"
cd "$REPO_ROOT"

# Install nunchuck
case "$MODE" in
    "uv")
        echo -e "${YELLOW}Installing with uv...${NC}"
        uv pip install -e .
        ;;
    "dev")
        echo -e "${YELLOW}Installing in development mode...${NC}"
        python3 -m pip install -e . --user || {
            echo -e "${YELLOW}Using --break-system-packages flag...${NC}"
            python3 -m pip install -e . --break-system-packages
        }
        ;;
    "user")
        echo -e "${YELLOW}Installing for current user...${NC}"
        python3 -m pip install --user . || {
            echo -e "${YELLOW}Using --break-system-packages flag...${NC}"
            python3 -m pip install . --break-system-packages
        }
        ;;
    "pipx")
        # Check if pipx is installed
        if ! command -v pipx &> /dev/null; then
            echo -e "${YELLOW}pipx not found. Installing pipx...${NC}"
            python3 -m pip install --user pipx || {
                echo -e "${YELLOW}Installing pipx with --break-system-packages...${NC}"
                python3 -m pip install pipx --break-system-packages
            }
            
            # Add pipx to PATH if not already there
            if ! command -v pipx &> /dev/null; then
                export PATH="$HOME/.local/bin:$PATH"
                echo -e "${YELLOW}Adding ~/.local/bin to PATH for this session${NC}"
            fi
        fi
        
        echo -e "${YELLOW}Installing with pipx...${NC}"
        pipx install --editable . || {
            echo -e "${RED}Failed to install with pipx. Try 'dev' mode instead.${NC}"
            exit 1
        }
        ;;
    *)
        echo -e "${RED}Error: Invalid mode '$MODE'. Use 'dev', 'user', 'pipx', or 'uv'${NC}"
        exit 1
        ;;
esac

# Verify installation
echo -e "${YELLOW}Verifying installation...${NC}"
if command -v nunchuck &> /dev/null; then
    echo -e "${GREEN}✓ nunchuck command is available${NC}"
    nunchuck --version
else
    echo -e "${YELLOW}Warning: nunchuck command not found in PATH${NC}"
    echo "You may need to add ~/.local/bin to your PATH:"
    echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo "Add this line to your ~/.bashrc or ~/.zshrc"
fi

# Copy skills to ~/.nunchuck
NUNCHUCK_DIR="${NUNCHUCK_DIR:-$HOME/.nunchuck}"
SKILLS_SRC="$REPO_ROOT/skills"

if [ -d "$SKILLS_SRC" ]; then
    echo -e "${YELLOW}Installing skills to $NUNCHUCK_DIR...${NC}"
    mkdir -p "$NUNCHUCK_DIR/skills"
    
    # Copy each skill directory
    for skill in "$SKILLS_SRC"/*/; do
        if [ -d "$skill" ]; then
            skill_name=$(basename "$skill")
            dest="$NUNCHUCK_DIR/skills/$skill_name"
            
            if [ -d "$dest" ]; then
                echo -e "  Updating $skill_name..."
                rm -rf "$dest"
            else
                echo -e "  Installing $skill_name..."
            fi
            
            cp -r "$skill" "$dest"
        fi
    done
    
    # Count installed skills
    skill_count=$(find "$NUNCHUCK_DIR/skills" -maxdepth 1 -type d | wc -l)
    skill_count=$((skill_count - 1))  # Subtract 1 for the skills directory itself
    echo -e "${GREEN}✓ Installed $skill_count skills to $NUNCHUCK_DIR${NC}"
else
    echo -e "${YELLOW}No skills directory found in repository${NC}"
fi

echo -e "${GREEN}Installation complete!${NC}"
echo ""
echo "Usage:"
echo "  nunchuck list            List available skills"
echo "  nunchuck use <skill>     Copy skill to current project"
echo "  nunchuck validate <path> Validate a skill"
echo "  nunchuck adapter         Generate IDE adapters"
echo ""
echo "Skills are installed to: $NUNCHUCK_DIR/skills"
