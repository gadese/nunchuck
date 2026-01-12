# CLI Contract

## Mandatory Commands

Every skill CLI **MUST** expose the following commands:

### `help`

* Lists available commands
* Describes arguments at a high level
* Intended for both humans and agents
* Must not require environment setup

### `validate`

* Verifies the skill is runnable
* Must be **read-only**
* Must not install or modify anything
* Fails fast if:

  * required files/directories are missing
  * required tooling is unavailable
  * required manifests do not exist

### `clean`

* Required **only if** the skill produces artifacts
* Deletes only generated outputs
* Must be idempotent and scoped

### Additional Commands

Skills MAY expose additional commands (e.g. `list`, `create`, `split`, `index`, `close`, etc.).

These commands are skill-specific and not governed by the canon beyond the general rules in this spec.

## Invocation Lifecycle

For any CLI command other than `help`:

1. Source `.config`
2. Execute command.
3. Exit with an appropriate status code.

## Responsibilities

* The CLI entrypoint owns:
  * argument parsing
  * dispatch
  * lifecycle orchestration
* Implementation logic lives outside the harness.
