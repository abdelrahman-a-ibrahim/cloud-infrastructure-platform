# Verification plan

Runtime behavior tests will be added with the implementation. The current source integrity check does not provide runtime coverage.

## Required behavior coverage
- A reviewed plan explains every create/update/delete operation.
- No credentials, state snapshots or sensitive plans are tracked.
- Two environments use independent state and identity boundaries.
- Destroy is tested and residual billable resources are enumerated.

## Failure coverage
- Run concurrent operations against the same state.
- Change a tagged resource outside Terraform and inspect drift.
- Rename a module address without intending resource replacement.
- Interrupt a deployment and reconcile the resource inventory.

Add domain tests, adapter contract tests and integration tests as those components are implemented. Include relevant invalid input, unauthorized access, concurrency, retry and restart scenarios. Real dependency guarantees require real integration evidence; mocks alone cannot establish ordering, replication, consistency or durability.

See [reliability](../docs/reliability.md) for execution/reporting requirements.
