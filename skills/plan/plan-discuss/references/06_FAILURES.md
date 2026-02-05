---
description: What to do when things go wrong.
index:
  - Artifact invalid
  - Missing dependencies
---

# Failures

## Artifact invalid

- Run `./scripts/skill.sh` to surface schema errors.
- Fix `.plan/active.yaml` until it validates.

## Missing dependencies

- Install `uv` and re-run `./scripts/skill.sh validate`.

