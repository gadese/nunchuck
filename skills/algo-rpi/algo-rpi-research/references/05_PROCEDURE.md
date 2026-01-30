# Procedure

## Research Process

Follow these steps in order:

### Step 1: Read Memory Bank
- Read `llm_docs/memory/activeContext.md` for current context
- Read `llm_docs/memory/systemPatterns.md` for existing patterns
- Read `llm_docs/memory/techContext.md` for technical context

### Step 2: Clarify the Problem (MANDATORY if ambiguous)

**CRITICAL:** Before proceeding with research, apply the clarification protocol if:
- The problem statement is ambiguous or underspecified
- Constraints (time/space/latency/accuracy) are unclear
- Data characteristics or hardware limits are not specified

Ask 2-4 focused questions covering:
1. **Objective(s):** What exactly should the algorithm optimize or achieve?
2. **Constraints:** Time/space/latency/accuracy requirements? Hardware limits?
3. **Data:** What are the data characteristics, volume, and variability?
4. **Environment:** CPU/GPU? Batch/streaming? Determinism requirements?
5. **Boundaries:** Privacy/fairness requirements? Allowed libraries/frameworks?

**Wait for user answers before continuing.**

**Exception:** If the user provides a detailed problem specification or specific files, proceed directly to Step 3.

### Step 3: Read Explicitly Mentioned Materials
- Read any user-specified files completely (problem specs, examples, dataset schemas, baseline scripts)
- Use complete file reads (no offset/limit) for full context

### Step 4: Codebase Interface Analysis (Integration Surfaces)
- Identify and read relevant code components: processors, handlers, services, repositories/stores, DTOs/schemas, configs
- Map inputs and outputs (types, shapes, invariants) across boundaries
- Note async vs sync, error/exception contracts, threading/concurrency assumptions
- Document integration points with local path + line ranges only (no code blocks)

### Step 5: Formalize the Problem

Define precisely:
- **Inputs/Outputs:** Types, shapes, invariants
- **Objective function(s):** What is being optimized?
- **Constraints:** Hard and soft constraints
- **Metrics & Targets:** Accuracy/F1/IoU/latency/memory with target thresholds
- **Operating environment:** CPU/GPU, batch/streaming, max memory, concurrency
- **Failure modes:** Noise, adversarial inputs, edge cases, robustness requirements

### Step 6: Establish Baselines & Prior Art
- Identify a trivial baseline (simplest possible solution)
- Document any existing baseline in the repo (paths only)
- List relevant algorithm families and model classes applicable to this problem

### Step 7: Solution Space Exploration (3-5 Candidates)

For each candidate approach, analyze:
- **Description and rationale:** Why is this approach suitable?
- **Complexity:** Time/space complexity and expected scaling behavior
- **Data requirements:** Pre/post-processing needs
- **Hardware/runtime:** Assumptions and dependencies
- **Expected quality:** Accuracy vs baseline, risks, edge cases
- **Hyperparameters:** Tunable components and sensitivity

### Step 8: Downselect Criteria & Validation Plan
- Propose criteria to choose among candidates (metric threshold, latency budget, memory budget, simplicity, maintainability)
- Outline an experiment plan: dataset splits, evaluation loops, ablations, seeds, reproducibility

### Step 9: Output Document
- One document per research task
- Location: `llm_docs/research/`
- Filename: `YYYY-MM-DD-HHMM-research-algo-<kebab-topic>.md`
- No frontmatter. Keep content concise but complete for downstream planning

### Step 10: Diagrams (Gated)
- If a diagram would significantly improve understanding, ask for confirmation first
- Provide a one-line justification before producing any diagram

### Step 11: Final Handoff

Present a brief "Findings Summary" in chat with:
- Key candidate approaches (ranked by feasibility)
- Critical constraints or blockers identified
- Local file references for integration points

Ask if a diagram would be helpful (with one-line justification)

Confirm the document location and filename

Update Memory Bank: Add key findings to `llm_docs/memory/activeContext.md`

**⏸️ PAUSE:** The next agent (planning phase) will create the implementation plan based on this document—do not include implementation details.

## Output Document Template

```markdown
# Research — Algorithm: [Topic]

**Tags**: [select from taxonomy, extend as needed]

## 1. Problem Statement
- Restatement of the task and goals after clarification

## 2. Inputs, Outputs, Constraints
- Data types, shapes, invariants
- Hard constraints (must satisfy)
- Soft constraints (prefer to satisfy)
- Latency/memory budgets

## 3. Metrics & Targets
- Primary metric(s) and target threshold
- Secondary metric(s) if applicable
- How success will be measured

## 4. Codebase Interface Analysis

### System Context Overview
- Brief context of examined areas at a high level

### Findings by Area

#### Backend
- Where the algorithm plugs into processors/handlers
- References only: `path/to/file.py:10-25` — what those lines implement

#### Models / Inference / Pre- & Post-processing
- Entry points, pre/post steps, artifact paths
- References only with line ranges

#### Data Contracts / API Schemas
- Request/response structures, validators, typing
- References only with line ranges

#### Existing Classes Relevant to Algorithm
- Classes/functions that will interact with the new algorithm

### Architecture Documentation
- Current patterns and conventions to align with

### Contract Mismatches (Checklist)
- [ ] Async vs Sync mismatches across boundaries
- [ ] Request/response schema mismatches
- [ ] Return type/shape discrepancies
- [ ] Error/exception contract inconsistencies
- Include references (local path + line ranges) for each item

## 5. Baselines & Prior Art
- **Trivial baseline:** Simplest possible solution and expected performance
- **Existing repo baseline:** Path references if any
- **Relevant algorithm families:** List applicable approaches from literature

## 6. Candidate Approaches

### A) [Approach Name]
- **Description:** What it is and why it's suitable
- **Complexity:** Time O(?), Space O(?)
- **Data requirements:** Pre/post-processing needs
- **Hardware/runtime:** CPU/GPU, memory, dependencies
- **Expected quality:** vs baseline, confidence level
- **Risks/edge cases:** Known failure modes
- **Hyperparameters:** Key tunable components

### B) [Approach Name]
- ...

### C) [Approach Name]
- ...

## 7. Risks & Unknowns
- Open questions requiring clarification
- Assumptions that need validation
- Potential blockers

## 8. Experiment & Validation Plan
- Dataset splits (train/val/test ratios)
- Evaluation loop design
- Ablation studies planned
- Random seeds and reproducibility measures
- Success criteria for moving to implementation

## 9. References (Local Paths Only)
- `path/to/file.py:10-25` — Brief description
```

## Quality Guidelines

- Follow local workspace rules (code principles, ML guides, data science guides)
- Prefer OpenCV (`cv2`) for imaging work
- Prefer vectorized operations (NumPy) for numeric performance
- Consider numerical stability in algorithm comparisons
- Emphasize reproducibility (random seeds, fixed libraries, deterministic ops)
- Use strict type hints language when describing interfaces
