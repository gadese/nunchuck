#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

if ! command -v python3 >/dev/null 2>&1; then
  echo "Error: python3 not found" >&2
  exit 1
fi

TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT

export PYTHONPATH="$ROOT_DIR/src"

echo "[smoke] list packs in repo root"
python3 -m nunchuck list --root "$ROOT_DIR"

echo "[smoke] validate repo root as pack"
set +e
python3 -m nunchuck validate "$ROOT_DIR"
VALIDATE_CODE=$?
set -e
echo "[smoke] validate exit code: $VALIDATE_CODE (expected 0 when repo is spec-compliant)"

echo "[smoke] install repo pack into temp project"
python3 -m nunchuck install "$ROOT_DIR" --project "$TMPDIR"

echo "[smoke] uninstall repo pack from temp project"
python3 -m nunchuck uninstall nunchuck --project "$TMPDIR"

echo "[smoke] ok"
