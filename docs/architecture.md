# Architecture

Status: proposed. Components shown below are implementation targets.

## Product context
An infrastructure-as-code platform for reproducible application environments. Reusable Terraform modules and environment-level Terragrunt configuration are planned around state isolation, scoped identities, traceable changes and resource lifecycle management.

## Component view
```text
Environment configuration -> Terragrunt -> Terraform modules
                                              |
                                remote state / AWS sandbox
```

## Design decisions
- Module boundary versus environment composition
- Backend bootstrap and recovery
- Identity scope for planning versus applying

Record decisions and alternatives in [ADR 0001](adr/0001-system-boundaries.md). Define authoritative state, acknowledgement boundaries, identities, retry behavior and recovery ownership before implementing adapters.

## Interface boundary
`src/cloud_infrastructure_platform/interfaces.py` defines the initial application boundary. Return models and error contracts remain to be specified. These interfaces do not implement the component graph.

## Integration boundaries
Local adapters and synthetic fixtures precede external integrations. Every live adapter needs an explicit identity, permission scope, timeout strategy and observability contract. Separate user-supplied content from execution authority.

## Deployment design
Document topology, dependency versions, configuration and state persistence alongside the first executable delivery. Record what local environments cannot establish about availability, ordering or durability.

## Compatibility
Version interfaces and fixtures when their semantics change. Sibling projects are optional integrations, not implicit filesystem dependencies.
