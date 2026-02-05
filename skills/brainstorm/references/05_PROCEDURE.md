---
description: Multi-round narrowing funnel from problem understanding to ranked candidate shortlist.
index:
  - Step 1 — CLARIFY
  - Step 2 — DIVERGE
  - Steps 3-N — NARROW (Iterative)
  - Step N+1 — CONVERGE
  - Step N+2 — DOCUMENT
  - Output Document Template
---

# Procedure — Brainstorm Narrowing Funnel

## Step 1 — CLARIFY

**Objective:** Understand the problem, constraints, and prior work before exploring solutions.

**Duration:** 1 round.

1. Read Memory Bank files:
   - `llm_docs/memory/activeContext.md`
   - `llm_docs/memory/systemPatterns.md`
   - `llm_docs/memory/techContext.md`
   - If any file is missing (fresh project), skip gracefully and note the gap
2. Read any user-specified files or context
3. Ask 2-3 focused questions covering:
   - What is the core problem and what does success look like?
   - What are the hard constraints? (compute, latency, data availability, accuracy floor)
   - What has been tried or considered already?
4. Prefer multiple choice when feasible (reduces cognitive load)
5. Wait for answers before proceeding

**Early exit:** If the user provides a detailed problem spec with constraints, skip directly to Step 2.

---

## Step 2 — DIVERGE

**Objective:** Map the solution landscape broadly before narrowing.

**Duration:** 1 round.

1. **Web search** (mandatory): Survey the current solution landscape for the problem domain. Purpose: map the territory, not deep-dive
2. **Context7** (optional): Check relevant library docs if the domain suggests specific frameworks
3. **Novel problem detection:** If web search reveals no direct solutions in the literature:
   - Decompose the problem into core sub-problems
   - Search for each sub-problem independently across adjacent industries and domains
   - Search for partially overlapping problems that solve a subset of the requirements
   - Frame options as adaptations or combinations: "No off-the-shelf solution exists, but here are approaches from adjacent domains that can be adapted or composed"
4. Present 4-6 broad solution families using **unordered bullet points** (not numbered — avoids anchoring)
5. Mix options:
   - 2-3 established approaches
   - 1-2 emerging techniques
   - 1 unconventional or surprising option
   - For novel problems: 2-3 cross-domain adaptations, 1-2 composite approaches, 1 first-principles design
6. Challenge framing: "Before we narrow — are we solving the right problem? Is [restated problem] actually what you need?"
7. Ask user which direction(s) interest them

---

## Steps 3-N — NARROW (Iterative)

**Objective:** Progressively refine from broad directions to specific algorithm/architecture candidates.

**Duration:** Repeating rounds, cap at 5.

Each narrowing round follows this template:

1. User picks a direction or asks questions
2. Research the sub-space:
   - **Context7** for specific library documentation (e.g., PyTorch geometric, Open3D)
   - **Web search** for recent papers and benchmarks in the narrowed domain
   - For novel problems: research how similar sub-problems are solved in other industries. Look for transferable techniques, composable building blocks, and adaptation patterns
3. Present 3-5 refined options within the chosen direction, each with a one-line trade-off. For novel problems, options may include hybrid/composite approaches — explicitly note which parts are proven and which require novel integration
4. Challenge (calibrated to user signals):
   - **If user fixates early:** Strong challenge — "You've committed quickly. Have you considered [alternative]? What makes you confident [chosen] is better than [alternative] for your constraints?"
   - **If user dismisses without reasoning:** Probe — "You ruled out [option]. What's the specific concern? It actually has [advantage] that might matter for [constraint]."
   - **If user is genuinely exploring:** Light facilitation — "Interesting direction. One thing to consider: [trade-off]. Does that change your thinking?"
5. Propose next narrowing question to drive toward specificity

**Exit conditions** (any of):

- Options have reached algorithm/architecture specificity (e.g., "PointNet++ vs Point Transformer" not "deep learning vs traditional ML")
- User signals readiness to converge ("I think I know what I want")
- Round 5 reached → present best candidates so far, ask user to converge or explicitly request more rounds

**Adaptive depth:** If the problem is well-scoped (user provided detailed constraints, domain is narrow), propose early convergence after round 2.

---

## Step N+1 — CONVERGE

**Objective:** Finalize the ranked shortlist with grounded, recent information.

**Duration:** 1 round.

1. **Web search** (mandatory): Final recency check on the top 2-3 candidates. Purpose: recent developments, known issues, production adoption
2. Present top 2-3 candidates, each with:
   - Description and rationale
   - Key trade-offs (complexity, data needs, computational cost, maturity, community support)
   - Suitability for user's specific constraints
   - Recent developments (from web search)
   - Key libraries and frameworks
   - Risks and unknowns
3. Ask: "Are you satisfied with this shortlist, or would you like to explore any candidate further?"

---

## Step N+2 — DOCUMENT

**Objective:** Produce the formal brainstorm output document and update Memory Bank.

**Duration:** 1 round.

1. Check for existing file at target path. If collision exists, append `-2`, `-3`, etc.
2. Write formal brainstorm document to `llm_docs/research/`
3. Filename: `YYYY-MM-DD-HHMM-research-brainstorm-<kebab-topic>.md`
4. Use the Output Document Template below
5. Update Memory Bank: add brainstorm findings to `llm_docs/memory/activeContext.md`
6. Present document location and suggest next steps (e.g., "proceed to `/algo-rpi-research` with Rank 1")

---

## Output Document Template

```markdown
# Brainstorm — [Topic]

**Date**: YYYY-MM-DD
**Tags**: [domain tags]

## 1. Problem Understanding
- Restated problem after clarification
- Key constraints and requirements
- Data characteristics and environment

## 2. Exploration Path
- Summary of the narrowing journey (which directions explored, which pruned)
- Key decision points and rationale at each level
- Alternatives eliminated with brief rationale (why pruned)

## 3. Candidate Approaches (Ranked)

### Rank 1: [Approach Name]
- **Description:** What it is
- **Why it fits:** Alignment with user's constraints
- **Trade-offs:** Complexity, data needs, maturity
- **Key libraries/frameworks:** Specific tools
- **Risks:** Known failure modes or gaps
- **Recent developments:** Relevant papers/releases

### Rank 2: [Approach Name]
- (same structure)

### Rank 3: [Approach Name]
- (same structure)

## 4. Next Steps
- Recommended path forward (e.g., "proceed to algo-rpi-research with Rank 1")
- Open questions that may affect the final choice
- Suggested experiments or investigations
- What additional information would help decide between candidates
```
