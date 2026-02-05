#!/usr/bin/env bash
set -euo pipefail

TASK_FILE="${1:-}"
if [[ -z "$TASK_FILE" ]]; then
  echo "usage: run_grape.sh <task-file>" >&2
  exit 2
fi

CODEX_CMD="${CODEX_CMD:-}"
if [[ -z "$CODEX_CMD" ]]; then
  echo "error: CODEX_CMD is not set (e.g., 'codex exec')" >&2
  exit 2
fi

CODEX_ARGS="${CODEX_ARGS:-}"

N="${N:-5}"
WARMUP="${WARMUP:-1}"
TIMEOUT_SEC="${TIMEOUT_SEC:-}"
WORKDIR="${WORKDIR:-}"
WORKDIR_MODE="${WORKDIR_MODE:-}"
WORKDIR_SOURCE="${WORKDIR_SOURCE:-}"
TASK_ID="$(basename "$TASK_FILE" | sed 's/\.[^.]*$//')"

MODE="grape"
if [[ -n "$WORKDIR" ]] && [[ ! -d "$WORKDIR" ]]; then
  echo "error: WORKDIR does not exist: $WORKDIR" >&2
  exit 2
fi

if [[ -n "$WORKDIR_MODE" ]] && [[ "$WORKDIR_MODE" != "copy" ]]; then
  echo "error: WORKDIR_MODE must be empty or 'copy'" >&2
  exit 2
fi

SOURCE_DIR=""
if [[ -n "$WORKDIR_SOURCE" ]]; then
  if [[ ! -d "$WORKDIR_SOURCE" ]]; then
    echo "error: WORKDIR_SOURCE does not exist: $WORKDIR_SOURCE" >&2
    exit 2
  fi
  SOURCE_DIR="$WORKDIR_SOURCE"
else
  if command -v git >/dev/null 2>&1 && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    SOURCE_DIR="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
  else
    SOURCE_DIR="$(pwd)"
  fi
fi

run_in_workdir() {
  if [[ -n "$WORKDIR_EFFECTIVE" ]]; then
    (cd "$WORKDIR_EFFECTIVE" && "$@")
  else
    "$@"
  fi
}
TASK_HASH=""
if command -v sha256sum >/dev/null 2>&1; then
  TASK_HASH="$(sha256sum "$TASK_FILE" | awk '{print $1}')"
elif command -v shasum >/dev/null 2>&1; then
  TASK_HASH="$(shasum -a 256 "$TASK_FILE" | awk '{print $1}')"
fi

HOSTNAME="$(hostname 2>/dev/null || uname -n 2>/dev/null || echo "")"
OS_NAME="$(uname -s 2>/dev/null || echo "")"
OS_RELEASE="$(uname -r 2>/dev/null || echo "")"

CMD="$CODEX_CMD $CODEX_ARGS"
USE_TIMEOUT="false"
if [[ -n "$TIMEOUT_SEC" ]] && [[ "$TIMEOUT_SEC" =~ ^[0-9]+$ ]] && [[ "$TIMEOUT_SEC" -gt 0 ]] && command -v timeout >/dev/null 2>&1; then
  USE_TIMEOUT="true"
fi

run_once() {
  local run_id="$1"
  local warmup_flag="$2"
  RUN_DIR="benchmark/grape/runs/${run_id}"
  mkdir -p "$RUN_DIR/logs"

  WORKDIR_EFFECTIVE="$WORKDIR"
  if [[ "$WORKDIR_MODE" == "copy" ]]; then
    WORKDIR_EFFECTIVE="$RUN_DIR/workdir"
    mkdir -p "$WORKDIR_EFFECTIVE"
    if command -v rsync >/dev/null 2>&1; then
      rsync -a --exclude 'benchmark/grape/runs' "$SOURCE_DIR"/ "$WORKDIR_EFFECTIVE"/ > "$RUN_DIR/logs/workdir_copy.out" 2> "$RUN_DIR/logs/workdir_copy.err"
    else
      echo "error: WORKDIR_MODE=copy requires rsync" >&2
      exit 2
    fi
  fi

  GIT_SHA=""
  GIT_DIRTY=""
  if command -v git >/dev/null 2>&1; then
    if run_in_workdir git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
      GIT_SHA="$(run_in_workdir git rev-parse HEAD 2>/dev/null || true)"
      if [[ -n "$(run_in_workdir git status --porcelain 2>/dev/null)" ]]; then
        GIT_DIRTY="true"
      else
        GIT_DIRTY="false"
      fi
    fi
  fi

  CLEAN_STATUS="skipped"
  CLEAN_SEC=0
  if benchmark/grape/scripts/extract_prompt.py "$TASK_FILE" clean >/dev/null 2>&1; then
    CLEAN_CMD="$(benchmark/grape/scripts/extract_prompt.py "$TASK_FILE" clean)"
    if [[ -n "${CLEAN_CMD//[[:space:]]/}" ]]; then
      CLEAN_STATUS="fail"
      CLEAN_START="$(date -u +%s)"
      set +e
      if [[ -n "$WORKDIR" ]]; then
        run_in_workdir bash -c "$CLEAN_CMD" > "$RUN_DIR/logs/clean.out" 2> "$RUN_DIR/logs/clean.err"
      else
        run_in_workdir bash -c "$CLEAN_CMD" > "$RUN_DIR/logs/clean.out" 2> "$RUN_DIR/logs/clean.err"
      fi
      CLEAN_CODE=$?
      set -e
      CLEAN_END="$(date -u +%s)"
      CLEAN_SEC=$((CLEAN_END - CLEAN_START))
      if [[ $CLEAN_CODE -eq 0 ]]; then
        CLEAN_STATUS="pass"
      fi
    fi
  fi

  GIT_PRE_STATUS=""
  if command -v git >/dev/null 2>&1; then
    if run_in_workdir git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
      GIT_PRE_STATUS="$(run_in_workdir git status --porcelain 2>/dev/null || true)"
      printf "%s\n" "$GIT_PRE_STATUS" > "$RUN_DIR/logs/git_status_pre.txt"
    fi
  fi

  PROMPT="$(benchmark/grape/scripts/extract_prompt.py "$TASK_FILE" grape)"

  START_TS="$(date -u +%s)"
  TASK_FILE_PATH="$TASK_FILE" TASK_ID_VAL="$TASK_ID" MODE_VAL="$MODE" RUN_ID_VAL="$run_id" START_TS_VAL="$START_TS" \
    TASK_HASH_VAL="$TASK_HASH" GIT_SHA_VAL="$GIT_SHA" GIT_DIRTY_VAL="$GIT_DIRTY" HOSTNAME_VAL="$HOSTNAME" \
    OS_NAME_VAL="$OS_NAME" OS_RELEASE_VAL="$OS_RELEASE" CODEX_CMD_VAL="$CODEX_CMD" CODEX_ARGS_VAL="${CODEX_ARGS:-}" \
    WARMUP_VAL="$warmup_flag" TIMEOUT_SEC_VAL="$TIMEOUT_SEC" WORKDIR_VAL="$WORKDIR_EFFECTIVE" \
    WORKDIR_MODE_VAL="$WORKDIR_MODE" WORKDIR_SOURCE_VAL="$SOURCE_DIR" \
    python3 - <<'PY'
import json
import os

payload = {
    "task": os.environ.get("TASK_ID_VAL", ""),
    "mode": os.environ.get("MODE_VAL", ""),
    "run_id": os.environ.get("RUN_ID_VAL", ""),
    "start_ts": int(os.environ.get("START_TS_VAL", "0") or 0),
    "task_file": os.environ.get("TASK_FILE_PATH", ""),
    "task_hash": os.environ.get("TASK_HASH_VAL", ""),
    "git_sha": os.environ.get("GIT_SHA_VAL", ""),
    "git_dirty": os.environ.get("GIT_DIRTY_VAL", ""),
    "hostname": os.environ.get("HOSTNAME_VAL", ""),
    "os_name": os.environ.get("OS_NAME_VAL", ""),
    "os_release": os.environ.get("OS_RELEASE_VAL", ""),
    "codex_cmd": os.environ.get("CODEX_CMD_VAL", ""),
    "codex_args": os.environ.get("CODEX_ARGS_VAL", ""),
    "workdir": os.environ.get("WORKDIR_VAL", ""),
    "workdir_mode": os.environ.get("WORKDIR_MODE_VAL", ""),
    "workdir_source": os.environ.get("WORKDIR_SOURCE_VAL", ""),
    "warmup": os.environ.get("WARMUP_VAL", "") == "true",
    "timeout_sec": os.environ.get("TIMEOUT_SEC_VAL", ""),
}

path = os.path.join("benchmark", "grape", "runs", os.environ.get("RUN_ID_VAL", ""), "config.json")
with open(path, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, sort_keys=True)
PY

  OUT_FILE="$RUN_DIR/logs/${MODE}.out"
  ERR_FILE="$RUN_DIR/logs/${MODE}.err"

  set +e
  if [[ "$USE_TIMEOUT" == "true" ]]; then
    printf "%s" "$PROMPT" | run_in_workdir timeout "$TIMEOUT_SEC" bash -c "$CMD" > "$OUT_FILE" 2> "$ERR_FILE"
  else
    printf "%s" "$PROMPT" | run_in_workdir bash -c "$CMD" > "$OUT_FILE" 2> "$ERR_FILE"
  fi
  STATUS=$?
  set -e

  END_TS="$(date -u +%s)"
  DURATION=$((END_TS - START_TS))

  if [[ "$warmup_flag" == "true" ]]; then
    return 0
  fi

  CHECK_STATUS="skipped"
  if benchmark/grape/scripts/extract_prompt.py "$TASK_FILE" check >/dev/null 2>&1; then
    CHECK_CMD="$(benchmark/grape/scripts/extract_prompt.py "$TASK_FILE" check)"
    if [[ -n "${CHECK_CMD//[[:space:]]/}" ]]; then
      set +e
      if [[ -n "$WORKDIR" ]]; then
        run_in_workdir bash -c "$CHECK_CMD" > "$RUN_DIR/logs/check.out" 2> "$RUN_DIR/logs/check.err"
      else
        run_in_workdir bash -c "$CHECK_CMD" > "$RUN_DIR/logs/check.out" 2> "$RUN_DIR/logs/check.err"
      fi
      CHECK_CODE=$?
      set -e
      if [[ $CHECK_CODE -eq 0 ]]; then
        CHECK_STATUS="pass"
      else
        CHECK_STATUS="fail"
      fi
    fi
  fi

  TEST_STATUS="skipped"
  if benchmark/grape/scripts/extract_prompt.py "$TASK_FILE" test >/dev/null 2>&1; then
    TEST_CMD="$(benchmark/grape/scripts/extract_prompt.py "$TASK_FILE" test)"
    if [[ -n "${TEST_CMD//[[:space:]]/}" ]]; then
      set +e
      if [[ -n "$WORKDIR" ]]; then
        run_in_workdir bash -c "$TEST_CMD" > "$RUN_DIR/logs/test.out" 2> "$RUN_DIR/logs/test.err"
      else
        run_in_workdir bash -c "$TEST_CMD" > "$RUN_DIR/logs/test.out" 2> "$RUN_DIR/logs/test.err"
      fi
      TEST_CODE=$?
      set -e
      if [[ $TEST_CODE -eq 0 ]]; then
        TEST_STATUS="pass"
      else
        TEST_STATUS="fail"
      fi
    fi
  fi

  OUT_BYTES="$(wc -c < "$OUT_FILE" | tr -d ' ')"
  ERR_BYTES="$(wc -c < "$ERR_FILE" | tr -d ' ')"

  FILES_CHANGED=0
  INSERTIONS=0
  DELETIONS=0
  if command -v git >/dev/null 2>&1; then
    if run_in_workdir git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
      run_in_workdir git diff --name-only > "$RUN_DIR/logs/git_diff_names.txt" 2>/dev/null || true
      run_in_workdir git diff --shortstat > "$RUN_DIR/logs/git_diff_shortstat.txt" 2>/dev/null || true
      run_in_workdir git diff --stat > "$RUN_DIR/logs/git_diff_stat.txt" 2>/dev/null || true
      GIT_POST_STATUS="$(run_in_workdir git status --porcelain 2>/dev/null || true)"
      printf "%s\n" "$GIT_POST_STATUS" > "$RUN_DIR/logs/git_status_post.txt"
      if [[ -s "$RUN_DIR/logs/git_diff_shortstat.txt" ]]; then
        SHORTSTAT="$(cat "$RUN_DIR/logs/git_diff_shortstat.txt")"
        if [[ "$SHORTSTAT" =~ ([0-9]+)[[:space:]]files?\ changed ]]; then
          FILES_CHANGED="${BASH_REMATCH[1]}"
        fi
        if [[ "$SHORTSTAT" =~ ([0-9]+)[[:space:]]insertions?\(\+\) ]]; then
          INSERTIONS="${BASH_REMATCH[1]}"
        fi
        if [[ "$SHORTSTAT" =~ ([0-9]+)[[:space:]]deletions?\(-\) ]]; then
          DELETIONS="${BASH_REMATCH[1]}"
        fi
      fi
    fi
  fi

  cat > "$RUN_DIR/results.json" <<JSON
{\"task\":\"$TASK_ID\",\"mode\":\"$MODE\",\"run_id\":\"$run_id\",\"status\":$STATUS,\"start_ts\":$START_TS,\"end_ts\":$END_TS,\"duration_sec\":$DURATION,\"clean_status\":\"$CLEAN_STATUS\",\"clean_duration_sec\":$CLEAN_SEC,\"check_status\":\"$CHECK_STATUS\",\"test_status\":\"$TEST_STATUS\",\"out_bytes\":$OUT_BYTES,\"err_bytes\":$ERR_BYTES,\"files_changed\":$FILES_CHANGED,\"insertions\":$INSERTIONS,\"deletions\":$DELETIONS}
JSON

}

if [[ "$WARMUP" == "1" ]]; then
  run_once "${TASK_ID}_${MODE}_warmup_$(date +%Y%m%d_%H%M%S)" "true"
fi

for i in $(seq 1 "$N"); do
  RUN_ID="${TASK_ID}_${MODE}_${i}_$(date +%Y%m%d_%H%M%S)"
  run_once "$RUN_ID" "false"
done
