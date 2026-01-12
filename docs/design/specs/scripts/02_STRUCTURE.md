# Canonical Directory Structure

A `nunchuck` skill SHALL adhere to the following top-level structure:

```text
scripts/
  .config.{sh,ps1}      # OPTIONAL: configurable parameters (sourced)
  skill.{sh,ps1}        # REQUIRED: CLI entrypoint
  include/              # REQUIRED: implementation root           
```

## Principles

* `scripts/` is the CLI harness
* `scripts/src/` is the implementation
* All interaction with a skill happens through the CLI entrypoint.
