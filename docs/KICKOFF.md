# Planning Kickoff Framework: Deterministic, Static, Subjective

Use this as the default “getting started” method whenever designing a new skill/skillset (or any repo workflow that mixes automation + human/agent judgment).

---

## 1) Categorize Everything

### Deterministic → `scripts/`

**Goal:** repeatable, testable, language/SDK-agnostic automation.

**Typical ingredients**

* **Portable CLI tooling:** `git`, `grep`/`rg`, `sed`, `awk`, `jq`, `find`, `xargs`
* **Content addressing:** hashes (stable IDs from canonical inputs)
* **Chronology:** date-stamped artifacts, chronological ordering, time-window queries
* **Indexing:** generate indices from disk state, not memory
* **Validation:** schema checks, naming rules, invariant checks
* **Idempotence:** re-running yields the same result (or safe no-op)

**Rules of thumb**

* Scripts should answer: *“What is the ground truth on disk?”*
* Prefer computation over interpretation.
* Prefer deterministic naming over descriptive naming when collisions matter.

---

### Static → `assets/`

**Goal:** stable, reusable materials that do not require judgment.

**Typical contents**

* Schemas (YAML/JSON), templates, example artifacts
* Controlled vocabularies / enums
* Canonical formats (frontmatter skeletons, filename patterns)

**Rules of thumb**

* Assets should be safe to cache mentally: they change rarely.
* If it changes frequently, it’s probably not an asset.

---

### Subjective → `references/`

**Goal:** explicit, agent-facing judgment, interpretation, and conditional behavior.

**Typical contents**

* Agent instructions (how to read outputs, how to decide)
* Heuristics, tradeoffs, “if/then” policies
* Edge-case handling and escalation guidance
* Examples of good/bad patterns

**Rules of thumb**

* References should answer: *“How should I think about this?”*
* Keep interpretation here; keep raw truth in scripts.

---

## 2) Control Rot (The Default Anti-Entropy Moves)

### Prefer generated truth over handwritten truth

* If a fact can be computed from disk, **compute it**.
* Handwritten indexes drift; generated indexes self-heal.

### Make drift visible

* Provide a `status`/`lint`/`validate` script that fails loudly.
* Prefer CI-friendly exit codes and machine-readable output.

### Separate identity from description

* Use hashes/IDs for stable identity.
* Store human-friendly explanations as metadata fields, not filenames.

### Keep a tight taxonomy

* Maintain a controlled list of categories/tags.
* Don’t let “misc” become a landfill without review.

---

## 3) Decide What Must Be Subjective vs Deterministic

Use this checklist:

### Should be deterministic if it is…

* derivable from disk state
* a rule/invariant
* a transform (input → output)
* a query (search/filter/list)
* a formatter

### Should be subjective if it is…

* a prioritization decision
* a risk assessment
* a tradeoff between competing goods
* something requiring project context or taste

---

## 4) Standard Skeleton for New Skill/Skillset Design

1. **Define the artifact(s)** (what will exist on disk?)
2. **Define deterministic lifecycle scripts** (create/update/list/validate)
3. **Define the static schemas/templates** (assets)
4. **Write reference guidance** (how agents interpret and act)
5. **Add rot controls** (validation + index regeneration)
6. **Add chronology + stable IDs** (hashes, dates, ordering)

---

## 5) “Kickoff Questions” (Use Every Time)

* What **must** be true, always? (invariants → scripts)
* What can be **computed** instead of documented? (generate it)
* Where will drift happen? (add validate/status)
* What needs stable identity? (hashes/IDs)
* What needs human judgment? (references)
* What must remain stable across versions? (assets)

---

## 6) Minimal Folder Convention

```
<skill-or-skillset>/
  SKILL.md
  scripts/
    *.sh
    *.ps1
  assets/
    schemas/
    templates/
  references/
    00_INSTRUCTIONS.md
    01_INTENT.md
    02_PRECONDITIONS.md
    03_SCRIPTS.md
    04_PROCEDURE.md
    05_EDGE_CASES.md
```

---

## 7) Working Definition

**Deterministic** = what can be rerun and proven.

**Static** = what should change rarely and be reused.

**Subjective** = what requires judgment and must be made explicit.
