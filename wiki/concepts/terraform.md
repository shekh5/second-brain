---
type: concept
tags: [devops, infrastructure-as-code, terraform]
sources: [what-is-terraform, opentofu-homepage]
created: 2026-11-21
updated: 2026-11-21
---

# Terraform

**In one line:** HashiCorp's [[infrastructure-as-code]] tool — you write the desired infrastructure
in HCL files, and Terraform plans and applies the changes on any cloud (src: [[what-is-terraform]]).

## How it works
```
   .tf files (HCL)      terraform.tfstate
        │                     │
        └──────►  CORE  ◄─────┘   compares desired vs recorded state
                   │
                   ▼  "plan": the list of changes
              PROVIDERS (aws, azurerm, kubernetes, …)
                   │   turn changes into API calls
                   ▼
             real infrastructure
```

- **Core:** reads the config, compares it with the state, calculates what must change (src: [[what-is-terraform]]).
- **Providers:** plugins that translate resources into API calls for AWS, Azure, Kubernetes, etc. (src: [[what-is-terraform]]).
- **State (`terraform.tfstate`):** Terraform's record mapping each resource in code to the real thing. Without it Terraform can't tell what already exists (src: [[what-is-terraform]]).
  - *Local state:* simple, but no locking — risky for teams (src: [[what-is-terraform]]).
  - *Remote state:* shared, locked, encrypted. Backends: S3 (+ DynamoDB for locks), Terraform Cloud, Azure Blob, Google Cloud Storage (src: [[what-is-terraform]]).
  - **Locking** stops two people running `apply` at once and corrupting the state (note: general knowledge, not from a source).
- **HCL:** HashiCorp Configuration Language; resources are written as blocks (src: [[what-is-terraform]]).
- **Modules:** reusable bundles of resources with inputs (variables) and outputs; can be versioned, nested, and shared via a private registry (src: [[what-is-terraform]]).
- **Provisioners:** run scripts after a resource is created — use sparingly (src: [[what-is-terraform]]).

### Main commands
| Command | What it does |
|---|---|
| `init` | set up the folder, download providers |
| `plan` | preview changes (nothing is touched) |
| `apply` | make the changes |
| `destroy` | delete everything in the state |
| `import` | bring an existing resource under Terraform |
| `refresh` | update state to match reality |
(src: [[what-is-terraform]])

## Why it matters / when to use it
Pick it when you need one tool across several clouds or SaaS platforms, and want infra changes
reviewed as code (src: [[what-is-terraform]]). Always run `plan` and read it before `apply`
(note: general knowledge, not from a source).

## Trade-offs
| Pro | Con |
|---|---|
| Multi-cloud, huge provider ecosystem (src: [[what-is-terraform]]) | You manage the state file yourself — lose or corrupt it and Terraform loses track (src: [[what-is-terraform]]) |
| `plan` shows changes before they happen (src: [[what-is-terraform]]) | Some changes destroy and recreate a resource, which can mean downtime or data loss if unnoticed (note: general knowledge, not from a source) |
| Modules give reuse across teams (src: [[what-is-terraform]]) | Provisioners make runs less predictable (src: [[what-is-terraform]]) |
| | Since 2023 under the Business Source License, not open source — which led to the [[opentofu]] fork (src: [[opentofu-homepage]]) |

## Real-world examples
- Typical team setup: state in S3 with a DynamoDB lock table, modules shared through a private registry (src: [[what-is-terraform]]).
- Defining VPCs and storage buckets as HCL blocks (src: [[what-is-terraform]]).

## Related
[[infrastructure-as-code]] — the idea Terraform implements
[[terraform-vs-cloudformation]] — vs AWS's own tool
[[opentofu-vs-terraform]] — vs its open-source fork

## Sources
- [[what-is-terraform]]
- [[opentofu-homepage]]
