---
description: Failure conditions and recovery strategies for the brainstorm skill.
index:
  - No Problem Description Provided
  - User Provides No Constraints
  - User Fixates on One Approach
  - Web Search Returns No Useful Results
  - Narrowing Stalls
  - Problem Too Broad for One Session
  - User Wants to Skip to Implementation
  - Problem Outside Skill Scope
  - Memory Bank Files Missing
  - Context Window Exhaustion
  - Conversation Drift
  - Novel Problem With No Direct Literature
---

# Failures — Error Handling and Recovery

## No Problem Description Provided

**Symptoms:** User invokes `/brainstorm` with no arguments or context.

**Recovery:**
1. Ask: "What problem or domain would you like to explore?"
2. Do not proceed until a problem statement is provided
3. If user provides only a vague topic, ask one follow-up to scope it

---

## User Provides No Constraints

**Symptoms:** User describes a problem but provides no constraints (compute, latency, data, accuracy).

**Recovery:**
1. Proceed with DIVERGE phase, noting that constraints are assumed to be flexible
2. Circle back to constraints during the first NARROW round when trade-offs make them relevant
3. Frame as: "This trade-off depends on your constraints. What are your limits on [compute/latency/data]?"

---

## User Fixates on One Approach

**Symptoms:** User commits to a single approach immediately, before exploring alternatives.

**Recovery:**
1. Acknowledge the choice: "That's a reasonable starting point"
2. Still execute DIVERGE — present alternatives before allowing convergence
3. If user insists after seeing alternatives, respect the choice
4. Document the tunnel vision risk in the output document

---

## Web Search Returns No Useful Results

**Symptoms:** Web search returns irrelevant, outdated, or no results for the problem domain.

**Recovery:**
1. Fall back to training knowledge, noting the gap
2. Use context7 as a secondary source for library-specific information
3. Note in the output document that web search was inconclusive
4. Adjust confidence level of recommendations accordingly

---

## Narrowing Stalls

**Symptoms:** User cannot decide between options, repeatedly asks for more information without converging.

**Recovery:**
1. Propose a default recommendation with explicit rationale
2. Offer a pragmatic frame: "If you had to ship next week, which would you pick?"
3. If still stuck, suggest converging on top 2 and deferring the final choice to prototyping
4. Do not force a decision — document the ambiguity in the output

---

## Problem Too Broad for One Session

**Symptoms:** Problem has multiple independent sub-problems that each require their own exploration.

**Recovery:**
1. Identify and name the sub-problems explicitly
2. Ask user which sub-problem is most critical or blocking
3. Brainstorm the most critical sub-problem first
4. Note the remaining sub-problems in the output document for future sessions
5. Suggest separate `/brainstorm` sessions for each remaining sub-problem

---

## User Wants to Skip to Implementation

**Symptoms:** User wants to jump directly to coding without completing the brainstorm.

**Recovery:**
1. Briefly explain that brainstorming saves rework downstream
2. Respect user autonomy — do not block them
3. Write a partial output document capturing what was explored so far
4. Suggest the user can return to brainstorming if they hit a dead end
5. Hand off to the appropriate implementation skill

---

## Problem Outside Skill Scope

**Symptoms:** Problem is not related to algorithms, AI, or ML (e.g., UI design, project management, DevOps).

**Recovery:**
1. Acknowledge the limitation: this skill is scoped to algorithm and AI/ML solution brainstorming
2. If the problem has an algorithmic component, offer to brainstorm that subset
3. Otherwise, suggest general-purpose exploration or redirect to appropriate tools
4. Do not proceed with a disclaimer-laden brainstorm — it wastes the user's time

---

## Memory Bank Files Missing

**Symptoms:** Fresh project with no `activeContext.md`, `systemPatterns.md`, or `techContext.md`.

**Recovery:**
1. Skip Memory Bank read gracefully — no error, no warning wall
2. Note briefly that no prior context was available
3. Rely entirely on user-provided context during CLARIFY phase
4. Proceed normally through the funnel

---

## Context Window Exhaustion

**Symptoms:** Conversation reaches 4+ narrowing rounds with substantial research. Agent responses become less coherent or lose earlier context.

**Recovery:**
1. At round 4, proactively summarize the current state: problem, directions explored, current candidates
2. Suggest converging: "We've explored extensively. Ready to converge on your top candidates?"
3. If context is clearly degrading, write a partial output document and offer to continue in a new session
4. The partial document preserves the exploration work and serves as input for the next session

---

## Conversation Drift

**Symptoms:** User goes off-topic during the brainstorm, discussing unrelated problems or tangential concerns.

**Recovery:**
1. Gently redirect: "We started exploring [original problem]. Should we continue with that, or has the problem changed?"
2. If the problem has genuinely changed, restart CLARIFY with the new framing
3. If the user is tangentially exploring, note the tangent and steer back: "That's interesting context. Let's factor it into our narrowing of [original problem]"
4. Do not abruptly cut off — the tangent may contain useful constraint information

---

## Novel Problem With No Direct Literature

**Symptoms:** Detected during DIVERGE when web search yields no established approaches for the full problem.

**Recovery:**
1. **Decompose:** Break the problem into core sub-problems and research each independently
2. **Cross-pollinate:** Search for the same sub-problems in adjacent industries and domains (e.g., a robotics perception problem may have analogues in autonomous driving, medical imaging, or industrial inspection)
3. **Compose:** Identify how partial solutions from different domains can be combined — map which sub-problems each covers and where gaps remain
4. **Adapt:** For each candidate, explicitly note what is proven (borrowed from existing domain) vs. what requires novel integration work (the "glue" between components)
5. **Flag risk:** Novel integration points are the highest-risk parts of the solution. The output document should clearly mark these as requiring prototyping and validation
6. **Reframe:** Present options around adaptation effort and integration risk, not just algorithm quality
