# ADR 0001: System boundaries and implementation approach

Status: proposed / decision not yet made.

## Context
Provision separate sandbox environments for WorkshopHub using reusable modules and thin Terragrunt environment configuration. Begin with a design and plan review; actual cloud resources are a later explicit milestone.

## Decision questions
- Module boundary versus environment composition
- Backend bootstrap and recovery
- Identity scope for planning versus applying

## Options
1. Small local implementation with synthetic adapters.
2. Integrated lab with real dependencies in a disposable environment.
3. A justified alternative to be supplied during design.

## Decision
Pending. Start by evaluating the smallest approach that can demonstrate the core invariant.

## Consequences to assess
Correctness, complexity, cost, recovery, trust boundaries, portability and maintenance burden.

## Evidence needed
A failure experiment, a working implementation slice and a comparison of the alternatives.

## Revisit when
Document a concrete load, team, correctness or operational constraint that invalidates the selected approach.
