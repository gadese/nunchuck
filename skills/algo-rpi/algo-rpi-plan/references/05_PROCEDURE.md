# Procedure

## Planning Process

Follow these steps in order:

### Phase 1: Context Gathering & Initial Analysis

1. **Read Memory Bank**
   - Read `llm_docs/memory/activeContext.md` for current context
   - Read `llm_docs/memory/systemPatterns.md` for existing patterns
   - Read `llm_docs/memory/techContext.md` for technical context

2. **Understand the Algorithm Research Document**
   
   The research document is your primary source of truth:
   - Read the entire research document before any other action
   - Identify the recommended approach(es) and their rationale
   - Note algorithmic trade-offs: accuracy vs speed vs memory
   - Extract interface requirements from the Codebase Interface Analysis section
   - Understand dataset characteristics and evaluation methodology

3. **Read All Additional Inputs Fully**
   - Read all explicitly mentioned files in their entirety
   - Read dataset schemas, baseline scripts, and prior implementations
   - Never skip or partially read any provided input

4. **Gather Technical Context**
   - Identify relevant source files, datasets, and benchmarks
   - Surface integration points from the research's Codebase Interface Analysis
   - Document hardware/runtime assumptions:
     - Target hardware (CPU/GPU/TPU)
     - Memory budget and batch size constraints
     - Concurrency and parallelization requirements
     - Inference latency requirements

5. **Verify Understanding**
   - Cross-reference research requirements with actual materials
   - Identify discrepancies between research assumptions and reality
   - Note gaps that require clarification

6. **Synthesize and Clarify**
   
   **CRITICAL:** Present your understanding and confirm selected approach:

   Based on the algorithm research, I understand we need to implement [algorithm/approach] to achieve [goal].

   **Problem Definition:**
   - Input: [data type, shape, constraints]
   - Output: [expected output, format]
   - Key metric: [primary metric and target value]

   **Selected Approach (from research):**
   - Algorithm: [name/description]
   - Expected complexity: O([time]) time, O([space]) space
   - Key trade-offs: [accuracy vs speed vs memory considerations]

   **Integration Points:**
   - [Interface with file:line reference]
   - [Data contract with file:line reference]

   **Hardware Constraints:**
   - Target: [CPU/GPU/TPU]
   - Memory budget: [limit]
   - Latency requirement: [target]

   **Questions requiring clarification:** (only if genuinely ambiguous)
   - [Technical question about algorithm parameters]
   - [Clarification on evaluation criteria]

   **⏸️ PAUSE:** Wait for user confirmation before proceeding to Phase 2.

   If no ambiguities exist, proceed to Phase 2.

### Phase 2: Design Convergence

1. **Confirm Algorithm Choice**
   
   If the research presents multiple viable approaches, present refined options:

   **Option A: [Algorithm Name]**
   - Approach: [Brief description]
   - Complexity: O([time]) time, O([space]) space
   - Pros: [Benefits, e.g., accuracy, simplicity]
   - Cons: [Drawbacks, e.g., memory usage, latency]
   - Research reference: Section [X]

   **Option B: [Algorithm Name]**
   - Approach: [Brief description]
   - Complexity: O([time]) time, O([space]) space
   - Pros: [Benefits]
   - Cons: [Drawbacks]
   - Research reference: Section [Y]

   **Recommendation:** Option [X] because [rationale grounded in research and constraints]

   **⏸️ PAUSE:** Which approach should we proceed with? Wait for user selection.

2. **Sketch Algorithm Architecture**
   
   Define the system textually (no code blocks):
   - **Data Preparation:** Input validation, preprocessing, augmentation
   - **Core Algorithm:** Main computational logic, key operations
   - **Postprocessing:** Output transformation, filtering, formatting
   - **Evaluation:** Metrics computation, comparison logic
   - **Packaging:** Integration interfaces, API surface

3. **Define Interfaces and Invariants**
   - Input/output types and shapes (textual description)
   - Preconditions and postconditions
   - Error handling expectations
   - Integration boundaries with `path:line` references from research

### Phase 3: Plan Structure Development

Present the standard algorithm development phases for approval:

## Proposed Plan Structure

**Overview:** [1-2 sentence summary of the algorithm and its purpose]

**Development Phases:**
1. **P0: Baseline & Harness** — Establish baseline, dataset splits, metrics, and test/benchmark harness
2. **P1: Prototype** — Implement minimal viable algorithm and verify metrics at small scale
3. **P2: Evaluation** — Full evaluation, ablations, significance testing; compare to baseline
4. **P3: Optimization** — Profile, vectorize, parallelize, quantize/prune as applicable
5. **P4: Robustness** — Adversarial/edge-case tests, determinism, failure handling
6. **P5: Packaging** — Documentation, examples, reproducibility artifacts

Does this phasing make sense for your use case? Should I adjust the scope of any phase?

**⏸️ PAUSE:** Wait for structure approval before writing detailed plan.

### Phase 4: Detailed Plan Writing

Produce the final plan document following the output template below.

## Output Document Template

```markdown
# Algorithm Implementation Plan — [Topic]

**Tags:** [select from taxonomy]

## 1. Problem Statement
- **Input:** [data type, shape, constraints]
- **Output:** [expected output, format]
- **Objective:** [what the algorithm must achieve]

## 2. Quantitative Targets
| Metric | Target | Baseline | Notes |
|--------|--------|----------|-------|
| [Primary metric] | [value] | [current] | [context] |
| Latency | [ms] | [current] | [hardware context] |
| Memory | [MB/GB] | [current] | [constraints] |

## 3. Selected Approach
- **Algorithm:** [Name and brief description]
- **Complexity:** O([time]) time, O([space]) space
- **Rationale:** [Why this approach was selected from research options]
- **Key Trade-offs:** [What we're optimizing for vs. accepting]

## 4. Integration Points
From research Codebase Interface Analysis:
- `path/to/file.py:10-25` — [Interface description]
- `path/to/data.py:40-67` — [Data contract description]

## 5. Hardware & Runtime Assumptions
- **Target hardware:** [CPU/GPU/TPU]
- **Memory budget:** [limit]
- **Batch size:** [expected range]
- **Concurrency:** [threading/multiprocessing requirements]

## 6. Out of Scope
- [Explicit item we are NOT doing]
- [Another exclusion]

## 7. Implementation Phases

### P0: Baseline & Harness
**Objective:** Establish evaluation infrastructure and baseline performance

**Deliverables:**
- Dataset splits (train/val/test) with fixed seeds
- Baseline implementation or reference results
- Metrics computation pipeline
- Benchmark harness with timing instrumentation

**Success Criteria:**
- [ ] Baseline metrics documented: [metric] = [value]
- [ ] Dataset splits reproducible with seed [X]
- [ ] Benchmark harness measures [latency/throughput/memory]

### P1: Prototype
**Objective:** Implement minimal viable algorithm

**Deliverables:**
- Core algorithm implementation (minimal, correct)
- Unit tests for critical paths
- Initial integration with harness

**Success Criteria:**
- [ ] Algorithm produces correct output on test cases
- [ ] Metrics within [X]% of target on small subset
- [ ] All unit tests pass

### P2: Evaluation
**Objective:** Full evaluation and comparison

**Deliverables:**
- Full dataset evaluation results
- Ablation studies (if applicable)
- Statistical significance testing
- Comparison report vs baseline

**Success Criteria:**
- [ ] [Primary metric] ≥ [target] on test set
- [ ] Results statistically significant (p < 0.05)
- [ ] Ablations document contribution of key components

### P3: Optimization
**Objective:** Meet performance targets

**Deliverables:**
- Profiling report identifying bottlenecks
- Optimized implementation (vectorized/parallelized)
- Memory optimization if needed

**Success Criteria:**
- [ ] Latency ≤ [target] ms
- [ ] Memory usage ≤ [target] MB
- [ ] No regression in accuracy metrics

### P4: Robustness
**Objective:** Handle edge cases and ensure reliability

**Deliverables:**
- Edge case test suite
- Determinism verification (fixed seeds produce identical results)
- Error handling for malformed inputs
- Adversarial input testing (if applicable)

**Success Criteria:**
- [ ] All edge case tests pass
- [ ] Deterministic across [N] runs with same seed
- [ ] Graceful failure on invalid inputs

### P5: Packaging
**Objective:** Production-ready delivery

**Deliverables:**
- API documentation
- Usage examples
- Reproducibility artifacts (requirements, seeds, configs)
- Integration guide

**Success Criteria:**
- [ ] Documentation covers all public interfaces
- [ ] Example runs successfully end-to-end
- [ ] Results reproducible from artifacts

## 8. Risks & Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk 1] | [Impact] | [Strategy] |

## 9. Reproducibility Checklist
- [ ] Random seeds documented and fixed
- [ ] Dependency versions pinned
- [ ] Dataset version/hash recorded
- [ ] Hardware configuration documented

## 10. References
- Research: `llm_docs/research/[file].md`
- Baseline: `path/to/baseline.py:line-range`
- Dataset: `path/to/data/`
```

### Final Steps

1. **Present the plan summary in chat** with quantitative targets
2. **Confirm the document location and filename**
3. **Update Memory Bank:** Add design decisions to `llm_docs/memory/activeContext.md`
4. **Handoff:** The next agent (implementation phase) will execute this plan

## Quality Guidelines

- **Quantify Everything:** Metric targets, latency budgets, memory constraints must be explicit
- **Emphasize Reproducibility:** Seeds, fixed versions, deterministic operations where possible
- **Define Evaluation Rigorously:** Dataset splits, metrics, baseline comparators, ablations, significance tests
- **Align with Research:** Interfaces and integration must match the research Codebase Interface Analysis
- **Be Incremental:** Each phase must be independently testable
- **Prefer Established Libraries:** OpenCV (`cv2`) for imaging, NumPy for vectorization
- **Avoid Premature Optimization:** Complete P2 evaluation before P3 optimization
- **Local References Only:** Use local file paths with line ranges; no external permalinks
