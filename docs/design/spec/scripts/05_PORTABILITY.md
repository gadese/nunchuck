# Cross-Platform Portability

## Best practice

provide **both Unix and Windows entrypoints**:

* `skill.sh`
* `skill.ps1`

## Rules

* No WSL requirement for Windows
* Use platform-native path handling
* If unsupported, `validate` must fail fast with a clear explanation

## Tooling

### Preferred Harness Tooling

The CLI harness should prefer **portable, language-agnostic CLI tools** whenever possible:

* `git`
* `grep` / `rg`
* `sed`
* `awk`
* `jq`
* `find`
* `xargs`

Language SDKs belong in `include/`, not in the harness.
