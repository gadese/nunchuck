---
description: Forbidden behaviors for the extract-conclusions skill.
index:
  - Prohibited Actions
---

# Never Do

## Prohibited Actions

**YOU MUST NOT:**

1. **Fabricate or extrapolate results not present in the source**
   - Report only what the notebooks and documents contain
   - Do not infer metrics that were not computed
   - Do not draw conclusions the data does not support

2. **Execute notebook code or modify source files**
   - Read and analyze only
   - Do not run cells, change code, or alter experiments

3. **Propose new experiments, algorithms, or approaches**
   - Document what was done and concluded, not what should be done next
   - Leave planning to downstream skills (`rpi-plan`, `algo-rpi-plan`)
   - Exception: the "Open Questions" section may note obvious gaps

4. **Simplify for non-technical audiences**
   - Use precise technical language appropriate for ML practitioners
   - Leave audience translation to `data-storytelling`

5. **Dismiss work without evidence-based justification**
   - Do not critique for the sake of critiquing
   - Question only when genuinely warranted, not reflexively
   - Respect the experimental choices made; flag issues only with clear reasoning

6. **Include raw code blocks from notebooks**
   - Use cell references and descriptions, not copy-pasted code
   - Reference format: `path/to/notebook.ipynb` cell [N] — description

7. **Skip source attribution**
   - Every metric, finding, and conclusion must reference its source
   - Unattributed claims are prohibited
