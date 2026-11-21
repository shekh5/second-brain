---
type: comparison
tags: [devops, infrastructure-as-code, opentofu, terraform]
sources: [opentofu-homepage, what-is-terraform]
created: 2026-11-21
updated: 2026-11-21
---

# OpenTofu vs Terraform

[[opentofu]] is a fork of [[terraform]]; both are [[infrastructure-as-code]] tools with the same core workflow.

| Dimension | OpenTofu | Terraform |
|---|---|---|
| Licence | Open source (src: [[opentofu-homepage]]) | Business Source License since 2023 (src: [[opentofu-homepage]]) |
| Governance | Linux Foundation, community RFCs (src: [[opentofu-homepage]]) | HashiCorp (note: general knowledge — now part of IBM) |
| Language / workflow | HCL, `init/plan/apply` (src: [[opentofu-homepage]]) | HCL, `init/plan/apply` (src: [[what-is-terraform]]) |
| Providers & modules | Same ecosystem, own registry (search.opentofu.org) (src: [[opentofu-homepage]]) | Terraform Registry (note: general knowledge, not from a source) |
| State encryption | Built in, client-side (v1.7) (src: [[opentofu-homepage]]) | Relies on the remote backend's encryption (src: [[what-is-terraform]]) |
| Extra features | `-exclude`, provider `for_each`, early variable evaluation (src: [[opentofu-homepage]]) | HCP Terraform / Terraform Cloud integration (src: [[what-is-terraform]]) |

## When to pick OpenTofu
- You want open-source licensing and community governance, e.g. you build a product on top of the tool (src: [[opentofu-homepage]]).
- You need encrypted state or the extra features (src: [[opentofu-homepage]]).

## When to pick Terraform
- You already rely on Terraform Cloud / HashiCorp support (note: general knowledge, not from a source).
- You want the newest HashiCorp features as they ship — OpenTofu decides per feature (src: [[opentofu-homepage]]).
- For personal use either works (src: [[opentofu-homepage]]).

## Sources
- [[opentofu-homepage]]
- [[what-is-terraform]]
