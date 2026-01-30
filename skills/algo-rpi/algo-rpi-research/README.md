# Algo-RPI Research

Algorithm problem research and solution space exploration for the Algo-RPI workflow.

## Purpose

This skill formalizes algorithmic problems and explores solution approaches (classical algorithms, optimization, AI/ML). It produces rigorous problem definitions, candidate approach analysis, and validation plans for downstream planning and implementation.

## When to Use

Use this skill when you need to:
- Formalize an algorithmic problem with precise constraints and metrics
- Explore classical algorithms, optimization methods, or AI/ML solutions
- Analyze trade-offs between different algorithmic approaches
- Document the solution space before planning implementation
- Understand performance requirements and evaluation criteria

## Key Features

- **Mandatory clarification protocol** for ambiguous problem statements
- **Problem formalization** with inputs, outputs, constraints, metrics, and targets
- **Codebase interface analysis** to understand integration points
- **Solution space exploration** with 3-5 candidate approaches
- **Trade-off analysis** comparing complexity, quality, and resource requirements
- **Validation plan** with dataset splits, metrics, and reproducibility measures

## Output

Research document in `llm_docs/research/YYYY-MM-DD-HHMM-research-algo-<kebab-topic>.md` containing:
- Problem statement and formalization
- Codebase interface analysis
- Baselines and prior art
- Candidate approaches (3-5 options) with trade-offs
- Risks and unknowns
- Experiment and validation plan

## Invocation

```
/algo-rpi-research

Problem: [algorithmic task description]
Constraints: [time/space/latency/accuracy requirements]
Data: [characteristics, volume, variability]
Hardware: [CPU/GPU, memory limits]
Metrics: [target thresholds]
```

## Clarification Protocol

**CRITICAL:** This skill MUST ask clarifying questions before proceeding if:
- Problem statement is ambiguous or underspecified
- Constraints (time/space/latency/accuracy) are unclear
- Data characteristics or hardware limits are not specified

Questions will cover:
1. **Objective(s):** What should the algorithm optimize?
2. **Constraints:** Time/space/latency/accuracy requirements? Hardware limits?
3. **Data:** Characteristics, volume, variability?
4. **Environment:** CPU/GPU? Batch/streaming? Determinism?
5. **Boundaries:** Privacy/fairness? Allowed libraries/frameworks?

**Exception:** If you provide a detailed problem specification, the skill proceeds directly.

## Algorithmic Domains

The skill considers (but is not limited to):

**Classical Algorithms:** Arrays, strings, graphs, trees, DP, greedy, geometry, search, hashing

**Optimization:** ILP/MILP, network flows, convex optimization, heuristics, constraint programming

**AI/ML:** Supervised learning, deep learning (CNNs, RNNs, Transformers), probabilistic models, RL

**Vision & Imaging:** Filtering, transforms, segmentation, OCR, detection/tracking

**NLP:** Tokenization, classification, retrieval, summarization, generation, RAG

**Evaluation:** Dataset splits, metrics, statistical testing, reproducibility

## Example

```
/algo-rpi-research

Problem: Implement real-time object detection for video stream
Constraints: <30ms latency per frame, <2GB memory, 95%+ mAP
Data: 1080p video at 30fps, 20 object classes, indoor/outdoor scenes
Hardware: NVIDIA RTX 3080 GPU
Metrics: mAP@0.5, latency, memory usage
```

The skill will:
1. Ask clarifying questions about edge cases, lighting conditions, occlusion handling
2. Formalize the problem with precise input/output specifications
3. Analyze codebase integration points (video pipeline, inference handlers)
4. Explore candidates: YOLO variants, EfficientDet, custom lightweight CNNs
5. Compare trade-offs: accuracy vs speed vs memory
6. Propose validation plan with dataset splits and benchmarking

## Integration with Algo-RPI Workflow

This is the first phase of the Algo-RPI workflow:
1. **Research** (this skill) → Formalize problem, explore solutions
2. **Plan** (`algo-rpi-plan`) → Select approach, create implementation plan
3. **Implement** (`algo-rpi-implement`) → Execute plan with quantitative verification

## See Also

- `algo-rpi-plan/` — Algorithm planning skill
- `algo-rpi-implement/` — Algorithm implementation skill
- `rpi-research/` — General software research (use for non-algorithmic tasks)
- `coding-standards/` — Shared coding guidelines
