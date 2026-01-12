# Reference File Naming

## Pattern

All reference files SHALL be named in the form:

```text
<NN>_<NAME>.md
```

Where:

* `<NN>` is a two-digit, zero-padded ordinal (`00`, `01`, `02`, …)
* `<NAME>` is uppercase and descriptive

## Example

```text
00_INSTRUCTIONS.md
```

## Rationale

Provides an implicit signal to the agent about the order in which content should be read.

* Ordering is determined by filename, not content
