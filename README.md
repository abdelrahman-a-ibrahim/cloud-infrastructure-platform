# Cloud Infrastructure Platform

Reusable cloud infrastructure with Terraform and Terragrunt, isolated state and reviewed change plans.

**Status: In development** · Personal project by Abdelrahman Ahmed

## Overview

An infrastructure-as-code platform for reproducible application environments. Reusable Terraform modules and environment-level Terragrunt configuration are planned around state isolation, scoped identities, traceable changes and resource lifecycle management.

## Current state

The repository currently contains the system design, delivery requirements, a synthetic input fixture and initial Python interfaces. Runtime behavior, service integrations and deployment are planned. Interface methods raise `NotImplementedError`; there is no running application or published runtime benchmark yet.

## Planned capabilities

- Reusable Terraform modules with thin Terragrunt environment configuration.
- Environment-specific state isolation and controlled backend initialization.
- Input validation, standard ownership tags and resource inventory.
- Reviewed plans, short-lived deployment identity and drift detection.
- Import/refactor workflows, recovery procedures and predictable teardown.

Detailed scope is tracked in the [delivery roadmap](docs/roadmap.md) and [requirements](docs/requirements.md).

## Architecture

```text
Environment configuration -> Terragrunt -> Terraform modules
                                              |
                                remote state / AWS sandbox
```

This is the proposed component design. See [architecture](docs/architecture.md) for boundaries and [architecture decisions](docs/adr/0001-system-boundaries.md) for the choices still to resolve.

## Technology direction

Terraform · Terragrunt · AWS · State · IAM · Resource lifecycle.

These technologies describe the intended implementation. Dependencies and compatible versions will be pinned when introduced. Optional services are not required by the current source checks.

## Working with the source

```sh
git clone https://github.com/abdelrahman-a-ibrahim/cloud-infrastructure-platform.git
cd cloud-infrastructure-platform
python3 tools/check_project.py
```

Python 3.9+ is sufficient for the current standard-library source check. It parses Python and JSON and checks required project files. It does **not** run an application, validate deployment behavior or establish feature completion.

The initial application boundary is in [`src/cloud_infrastructure_platform/interfaces.py`](src/cloud_infrastructure_platform/interfaces.py). [`examples/scenario.json`](examples/scenario.json) provides a synthetic development input. Installation and runtime commands will be added with the first executable release.

## Quality and reliability

- A reviewed plan explains every create/update/delete operation.
- No credentials, state snapshots or sensitive plans are tracked.
- Two environments use independent state and identity boundaries.
- Destroy is tested and residual billable resources are enumerated.

These are acceptance targets. Failure scenarios are specified in [reliability verification](docs/reliability.md); [results](docs/verification/README.md) will be recorded as implementation progresses. Correctness and performance claims must reference an actual environment, workload and commit.

## Development roadmap

- [ ] Contracts and system boundaries
- [ ] Core implementation and behavior tests
- [ ] External adapters and scoped access
- [ ] Failure recovery and operational visibility
- [ ] Reproducible deployment and release validation

See [delivery stages and future scope](docs/roadmap.md). For deployment prerequisites and resource lifecycle, see [operations](docs/operations.md).

## Repository structure

```text
src/cloud_infrastructure_platform/       Initial application interfaces
examples/                  Synthetic development inputs
tests/                     Behavior verification plan
docs/architecture.md       Component design and boundaries
docs/requirements.md       Functional and quality requirements
docs/roadmap.md            Delivery stages and future scope
docs/reliability.md        Failure and recovery scenarios
docs/operations.md         Runtime and deployment plan
docs/verification/         Results as implementation progresses
tools/check_project.py     Source integrity check
```

## Development

Use focused feature branches, add behavior tests with implementation changes and update the relevant architecture decision when guarantees change. Read [CONTRIBUTING.md](CONTRIBUTING.md).

This is an independent personal project. Examples use synthetic data. See [NOTICE.md](NOTICE.md) for licensing status.

## References

- https://developer.hashicorp.com/terraform/docs
- https://docs.terragrunt.com/
