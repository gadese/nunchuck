# Dependencies and Environment Management

## Hard Rule: No Forced Installation

> **A skill MUST NEVER install packages or system dependencies without explicit user permission.**

* `validate` may only detect and report missing dependencies
* Scripts must print:

  * what is missing
  * how to install it
  * a clear request for user action

Auto-installation is prohibited by default.

Optional opt-in flags (e.g. `--install`) are allowed **only when explicitly requested by the user**.

---

## Environment Management

If a skill uses an SDK/runtime (Python, Node, Go, etc.):

* Dependency manifests MUST live in `include/`
* `validate` must check required tooling exists
* The CLI must execute deterministically using ecosystem-standard tooling
* Environments must never be created implicitly

### Python (recommended pattern)

* `include/pyproject.toml`
* Optional `include/uv.lock`
* Prefer `uv run`
* If deps are missing, instruct the user to run `uv sync`
