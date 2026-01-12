# Triggers

## Invoke when

- Before cutting a release.
- As part of CI or pre-merge validation.
- User asks whether the changelog is compliant.

## Do not invoke when

- User wants to initialize a changelog (use `changelog-init`).

## Exit immediately if

- No changelog exists and the user does not want to create one.
