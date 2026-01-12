#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MIMIC_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

exec "$MIMIC_ROOT/scripts/eject.sh" "$@"
