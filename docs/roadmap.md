# Delivery roadmap

Status: planned. No delivery stage is complete.

### 1. Contracts and system boundaries

Design module boundaries, environment layout, naming, tags and a resource inventory. Decide which resources genuinely need reuse.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 2. Core implementation

Build a small network and application module with explicit inputs/outputs and validations. Pin tools/providers and commit provider lock files when introduced.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 3. Integrations and access controls

Design backend bootstrapping, encryption, locking, state isolation and recovery. Keep state and plan binaries out of Git.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 4. Recovery and operational behavior

Add plan-on-change CI, workload identity for cloud access and reviewed apply gates. Practice drift detection and an import/refactor operation.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 5. Release validation

Provision one bounded sandbox, test teardown and publish a cost/lifecycle report. Prove one environment cannot alter another environment’s state.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

## Future scope

- Policy checks for public exposure and missing tags
- Ephemeral preview environments with expiry
- Module contract testing
- Compare Terragrunt orchestration with simpler Terraform roots

Select and pin implementation dependencies when introduced. Scope is refined through architecture decisions; completion requires working behavior and verification evidence.
