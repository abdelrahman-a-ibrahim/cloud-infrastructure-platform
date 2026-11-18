# Reliability and failure verification

Status: verification scenarios planned; no results recorded yet.

## Required scenarios
- Run concurrent operations against the same state.
- Change a tagged resource outside Terraform and inspect drift.
- Rename a module address without intending resource replacement.
- Interrupt a deployment and reconcile the resource inventory.

## Verification protocol
For each implemented scenario, document:
1. Commit, runtime versions, environment and topology.
2. Input workload and the expected invariant.
3. Baseline observations, fault injection and timestamps.
4. Observed errors, duplicate effects or state inconsistencies.
5. Recovery steps and measured time to restore behavior.
6. Resource cleanup and remaining limitations.

A simulator establishes application behavior within its assumptions. Real service ordering, consistency, failover and durability claims require verification against the selected dependencies. Distinguish those results in reports.

## Release evidence
- A reviewed plan explains every create/update/delete operation.
- No credentials, state snapshots or sensitive plans are tracked.
- Two environments use independent state and identity boundaries.
- Destroy is tested and residual billable resources are enumerated.

Store concise reports in [verification results](verification/README.md). Targets and illustrative fixture values must not be reported as measurements.
