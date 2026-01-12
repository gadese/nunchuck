# Canonical Execution Flow

### 0. Pre-Hook (Read-Only)

**Purpose:** establish safety and scope.

Typical activities:

* verify required tools exist
* confirm repo state (clean/dirty)
* confirm required assets or configs exist
* sanity checks

Rules:

* must not mutate state
* may abort early


### 1. Deterministic Discovery

**Purpose:** define the *complete universe* of inputs.
Characteristics:
* file discovery is explicit and repeatable
* results are concrete and enumerable
* ordering is stable
Common patterns:
* globbing by extension or path
* directory enumeration
Outputs:
* file lists
* inventories
* indexes
> Agents must not “explore the filesystem” beyond this step.
---
### 2. Deterministic Narrowing
**Purpose:** reduce scope *without guessing*.
Characteristics:
* operates only on discovered inputs
* purely read-only
* produces smaller, focused subsets
Common patterns:
* grepping for content
* pattern matching
* filtering inventories
Outputs:
* candidate lists
* match sets
* filtered inventories
---
### 3. Deterministic Execution
**Purpose:** perform the actual work.
Characteristics:
* operates only on known inputs
* may mutate files
* ideally split into plan → apply (when feasible)
Common patterns:
* refactors
* generation
* transformation
---
### 4. Deterministic Validation (Hard Gate)
**Purpose:** prove the work is complete.
This step is **mandatory when artifacts are declared**.
Typical checks:
* required artifacts exist
* forbidden patterns removed
* schemas valid
* file counts / hashes match expectations
Rules:
* failure must redirect back to earlier steps
* reasoning cannot override failed validation
> A skill is not “done” if validation fails.
---
### 5. Subjective Reasoning / Interpretation
**Purpose:** interpret validated state.
Allowed activities:
* summarization
* judgment
* prioritization
* reflection
Rules:
* must not back-propagate ambiguity
* must not invalidate deterministic guarantees
---
### 6. Artifact Creation (Human-Facing)
**Purpose:** produce durable outputs.
Examples:
* plans
* reports
* summaries
* decision records
Artifacts should reference:
* inputs used
* outputs produced
* validation status
* notable decisions
---
### 7. Post-Hook / Cleanup (Optional)
**Purpose:** tidy or finalize.
Allowed:
* remove temporary files
* normalize formatting
* write final notes
Rules:
* must not destroy primary outputs
* must not invalidate validation
---
