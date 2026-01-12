# Failures

## Changelog already exists

- Stop and ask whether to overwrite.
- If confirmed, rerun with `--force`.

## `uv` missing / CLI not runnable

- Instruct the user to install `uv`.
- Rerun `../.shared/scripts/skill.sh validate`.

## Remote URL not detected

- Proceed with the template and instruct the user to update the link reference.
