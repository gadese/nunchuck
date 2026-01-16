# Step 2: Control Rot (The Default Anti-Entropy Moves)

## Prefer generated truth over handwritten truth

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

### Never hide environment mutation

* Scripts MUST NOT install packages, dependencies, or tooling implicitly.
* Validation may detect and report missing dependencies, but must not modify state.
* Installation steps must be explicit, copy-pasteable, and user-initiated.

Auto-installation is a major source of hidden drift in agent-driven systems.
Prefer loud failure with clear instructions over “helpful” mutation.
