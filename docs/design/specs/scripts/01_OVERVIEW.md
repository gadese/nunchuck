# Overview

This section defines the **canonical CLI contract** for internal skills.

A skill is treated as a **command-line interface** with a small, stable surface that agents and humans can reliably discover, validate, and execute.

This canon exists to ensure that skills are:

* Deterministic
* Inspectable
* Cross-platform
* Extensible without structural drift

This is an **internal design spec**. It optimizes for correctness, longevity, and agent reasoning, not for public SDK ergonomics.
