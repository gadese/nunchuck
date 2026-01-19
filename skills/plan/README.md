# plan

`plan` is **AI-assisted planning discipline**.

It does not replace execution.
It makes bounded, auditable work easier to create, run, and review.

---

## The problem

Agents can be productive but inconsistent when work is not bounded.

Common failure modes:

* Starting implementation before agreeing on outcomes
* Losing track of what is in scope
* Mixing discovery, design, and execution
* Shipping changes without a clear review surface

The repository already supports structure, but only if:

* plans are created consistently
* progress is tracked explicitly
* execution is tied back to the plan
* review has a clear artifact to validate

---

## What plan is

`plan` is a **container of standalone skills** that work together.

It manages bounded work units with structured plans stored in `.plan/`.

These skills:

- keep plan state on disk (auditable, durable)
- encourage outcome-oriented, scoped milestones
- make control flow explicit (you choose which skill to run next)

Member skills:

* `plan-create`
* `plan-discuss`
* `plan-exec`

---

## What plan is not

`plan` is not:

* a project manager
* a ticketing system
* a replacement for implementation
* a substitute for judgment

It does not guarantee good decisions.
It only provides a structure that makes decisions and progress inspectable.

---

## How it works (conceptually)

`plan` separates concerns cleanly:

* **Structure on disk**

  * plan intent lives in `.plan/active.yaml`
  * the compiled active plan lives in `.plan/active/`
  * archived plans live in `.plan/archive/<id>/`
  * tasks and milestones are explicit
  * frontmatter is validated against JSON Schemas shipped inside each skill’s `assets/`
  * status and progress are derived from schema-validated frontmatter

* **Agentic reasoning**

  * choosing milestones and scope boundaries
  * selecting what to execute next
  * producing outputs and handoffs that reviewers can verify

To run the workflow, use:

- `plan-discuss` to stabilize intent in `.plan/active.yaml`
- `plan-create` to compile `.plan/active/`
- `plan-exec` to execute tasks and archive on completion

### Determinism note

The YAML frontmatter is the *authoritative state* and is checked under the hood on each `plan-exec` run.
The Markdown body is intentionally free-form and non-authoritative.

---

## Mental model

Think of `plan` as a *bounded work contract*.

It turns “do the thing” into:

* a set of outcomes
* a small number of milestones
* executable tasks with explicit completion criteria
* a review surface that can be validated after the fact

---

## Constraints (by design)

* Bounded scope
* Explicit progress tracking
* Durable artifacts in `.plan/`
* Reviewable outputs and handoffs

If `plan` ever feels like it is improvising scope, it is doing too much.

---

## When to use plan

Use `plan` when:

* the work spans multiple steps or files
* you want an auditable create → exec → review loop
* you need a reliable progress/status surface
* you want to reduce scope drift

Do not use `plan` to:

* replace careful technical decisions
* skip review
* justify unbounded exploration

---

## Why this exists

Most failures in agentic work are not capability failures — they are *process failures*.

`plan` exists to make the work unit itself explicit, so execution can be:

* scoped
* tracked
* reviewed
* repeated safely

---

## TLDR

`plan` is planning with guardrails.

It produces durable on-disk plans, executes against them, and leaves a clear review trail, nothing more.
