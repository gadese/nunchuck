# Algorithm Research Phase Only

Execute only the algorithm research phase to formalize problem and explore solutions.

## When to Use

Use this pipeline when you need to:
- Formalize an algorithmic problem with precise constraints and metrics
- Explore classical algorithms, optimization methods, or AI/ML solutions
- Analyze trade-offs between different algorithmic approaches
- Document the solution space before planning implementation
- Understand performance requirements and evaluation criteria

## Process

### Phase 1: Algorithm Research
**Skill:** `algo-rpi-research`

**Objective:** Formalize the algorithmic problem and explore candidate solution approaches.

**Steps:**

1. **Read Memory Bank**
   - Read `llm_docs/memory/activeContext.md` for current context
   - Read `llm_docs/memory/systemPatterns.md` for existing patterns
   - Read `llm_docs/memory/techContext.md` for technical context

2. **Clarify the Problem (MANDATORY if ambiguous)**
   
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

3. **Read Explicitly Mentioned Materials**
   - Read any user-specified files completely (problem specs, examples, dataset schemas, baseline scripts)

4. **Codebase Interface Analysis**
   - Identify and read relevant code components: processors, handlers, services, DTOs, schemas, configs
   - Map inputs and outputs (types, shapes, invariants) across boundaries
   - Note async vs sync, error/exception contracts, threading/concurrency assumptions
   - Document integration points with local path + line ranges

5. **Formalize the Problem**
   
   Define precisely:
   - **Inputs/Outputs:** Types, shapes, invariants
   - **Objective function(s):** What is being optimized?
   - **Constraints:** Hard and soft constraints
   - **Metrics & Targets:** Accuracy/F1/IoU/latency/memory with target thresholds
   - **Operating environment:** CPU/GPU, batch/streaming, max memory, concurrency
   - **Failure modes:** Noise, adversarial inputs, edge cases, robustness requirements

6. **Establish Baselines & Prior Art**
   - Identify a trivial baseline (simplest possible solution)
   - Document any existing baseline in the repo (paths only)
   - List relevant algorithm families and model classes applicable to this problem

7. **Solution Space Exploration (3-5 Candidates)**
   
   For each candidate approach, analyze:
   - **Description and rationale:** Why is this approach suitable?
   - **Complexity:** Time/space complexity and expected scaling behavior
   - **Data requirements:** Pre/post-processing needs
   - **Hardware/runtime:** Assumptions and dependencies
   - **Expected quality:** Accuracy vs baseline, risks, edge cases
   - **Hyperparameters:** Tunable components and sensitivity

8. **Downselect Criteria & Validation Plan**
   - Propose criteria to choose among candidates (metric threshold, latency budget, memory budget, simplicity, maintainability)
   - Outline an experiment plan: dataset splits, evaluation loops, ablations, seeds, reproducibility

9. **Output Document**
   - Location: `llm_docs/research/`
   - Filename: `YYYY-MM-DD-HHMM-research-algo-<kebab-topic>.md`
   - No frontmatter, concise but complete

10. **Update Memory Bank**
    - Add key findings to `llm_docs/memory/activeContext.md`

**Output:** Research document with problem formalization, candidate approaches, and validation plan

**⏸️ PAUSE POINT:** Present candidate approaches ranked by feasibility. Research phase complete.

---

## Output Format

The research document follows this structure:

```markdown
# Research — Algorithm: [Topic]

**Tags**: [taxonomy tags]

## 1. Problem Statement
Restatement of the task and goals after clarification

## 2. Inputs, Outputs, Constraints
Data types, shapes, invariants, hard/soft constraints, latency/memory budgets

## 3. Metrics & Targets
Primary metric(s) and target threshold, secondary metrics, success measurement

## 4. Codebase Interface Analysis
System context, findings by area (backend, models/inference, data contracts), architecture documentation, contract mismatches

## 5. Baselines & Prior Art
Trivial baseline, existing repo baseline, relevant algorithm families

## 6. Candidate Approaches
A) [Approach Name] - Description, complexity, data requirements, hardware/runtime, expected quality, risks, hyperparameters
B) [Approach Name] - ...
C) [Approach Name] - ...

## 7. Risks & Unknowns
Open questions, assumptions, potential blockers

## 8. Experiment & Validation Plan
Dataset splits, evaluation loop, ablations, seeds, reproducibility, success criteria

## 9. References (Local Paths Only)
File paths with line ranges and descriptions
```

---

## Quick Reference

**Invoking research only:**
```
/algo-rpi-research

Problem: [algorithmic task description]
Constraints: [time/space/latency/accuracy requirements]
Data: [characteristics, volume, variability]
Hardware: [CPU/GPU, memory limits]
Metrics: [target thresholds]
```

---

## Next Steps

After research is complete, you can:
1. Review candidate approaches and select one
2. Invoke `/algo-rpi-plan` with research document to create implementation plan
3. Archive research for future reference
4. Share research with team for approach selection
