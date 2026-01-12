#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

if ! command -v python3 >/dev/null 2>&1; then
  echo "Error: python3 not found" >&2
  exit 2
fi

export PYTHONPATH="$ROOT_DIR/src"

python3 -m nunchuck validate "$ROOT_DIR"
