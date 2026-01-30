# Triggers

## When to Invoke

Invoke this skill when you need to:
- Formalize an algorithmic problem and explore solution approaches
- Research classical algorithms or AI/ML solutions for a specific task
- Analyze trade-offs between different algorithmic approaches
- Document the solution space before planning implementation
- Understand constraints, metrics, and evaluation criteria for algorithms

## Invocation Response

When invoked, respond with:

"I'm ready to perform algorithm problem research and solution space exploration as part of the Research-Plan-Implement workflow.

Please provide the problem statement, constraints, datasets, metrics, and any specific files or references. If the request is ambiguous, I will ask clarifying questions before proceeding to formalize the problem and explore candidate approaches."

Then wait for the user's query and apply the clarification protocol.

## Expected Inputs

- Problem statement or task description
- Constraints (time/space/latency/accuracy requirements)
- Data characteristics, volume, and variability
- Hardware environment (CPU/GPU, memory limits)
- Metrics and target thresholds
- Specific files or references (optional)

## Output Format

Research document in `llm_docs/research/YYYY-MM-DD-HHMM-research-algo-<kebab-topic>.md` containing:
- Problem formalization
- Codebase interface analysis
- Candidate approaches (3-5 options)
- Trade-off analysis
- Experiment and validation plan

## Clarification Protocol

**MANDATORY:** Ask clarifying questions when:
- The problem statement is ambiguous or underspecified
- Constraints (time/space/latency/accuracy) are unclear
- Data characteristics or hardware limits are not specified

Ask 2-4 focused questions covering:
1. **Objective(s):** What exactly should the algorithm optimize or achieve?
2. **Constraints:** Time/space/latency/accuracy requirements? Hardware limits?
3. **Data:** What are the data characteristics, volume, and variability?
4. **Environment:** CPU/GPU? Batch/streaming? Determinism requirements?
5. **Boundaries:** Privacy/fairness requirements? Allowed libraries/frameworks?

**Exception:** If the user provides a detailed problem specification or specific files, proceed directly to research.
