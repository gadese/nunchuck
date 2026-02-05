---
description: Use fast-context to gather task surface area before evaluating.
auto_execution_mode: 3
---

# INSTRUCTIONS

## NEVER

1. Execute the `grape` skill `scripts/` contents during invocation of this workflow.
2. Edit the `grape/` directory contents during invocaton of this workflow.

## ALWAYS

1. Use the `grape/references` to guide workflow execution intent.

## Details

1. Read the `grape/references` to understand the intent of the this workflow.
2. Execute the grape skill instructions using internal call to `functions.code_search(...)` instead of `grape/scripts/` contents.
