#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
venv_dir="$script_dir/.venv"

if [[ ! -d "$venv_dir" ]]; then
  echo "Creating virtual environment..." >&2
  python3 -m venv "$venv_dir"
fi

source "$venv_dir/bin/activate"

if ! python -c "import networkx" 2>/dev/null; then
  echo "Installing dependencies..." >&2
  pip install -q -r "$script_dir/requirements.txt"
fi

cd "$script_dir"
python -m kg "$@"
