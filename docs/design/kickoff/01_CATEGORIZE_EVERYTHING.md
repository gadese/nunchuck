# Step 1: Categorize Everything

## Deterministic → `scripts/`

**Goal:** repeatable, testable, language/SDK-agnostic automation.

**Typical ingredients**:

* **Portable CLI tooling:** `git`, `grep`/`rg`, `sed`, `awk`, `jq`, `find`, `xargs`
* **Content addressing:** hashes (stable IDs from canonical inputs)
* **Chronology:** date-stamped artifacts, chronological ordering, time-window queries
* **Indexing:** generate indices from disk state, not memory
* **Validation:** schema checks, naming rules, invariant checks
* **Idempotence:** re-running yields the same result (or safe no-op)

**Rules of thumb**:

* Scripts should answer: *“What is the ground truth on disk?”*
* Prefer computation over interpretation.
* Prefer deterministic naming over descriptive naming when collisions matter.

---

## Static → `assets/`

**Goal:** stable, reusable materials that do not require judgment.

**Typical contents**:

* Schemas (YAML/JSON), templates, example artifacts
* Controlled vocabularies / enums
* Canonical formats (frontmatter skeletons, filename patterns)

**Rules of thumb**:

* Assets should be safe to cache mentally: they change rarely.
* If it changes frequently, it’s probably not an asset.

---

## Subjective → `references/`

**Goal:** explicit, agent-facing judgment, interpretation, and conditional behavior.

**Typical contents**:

* Agent instructions (how to read outputs, how to decide)
* Heuristics, tradeoffs, “if/then” policies
* Edge-case handling and escalation guidance
* Examples of good/bad patterns

**Rules of thumb**:

* References should answer: *“How should I think about this?”*
* Keep interpretation here; keep raw truth in scripts.

---
