---
type: comparison
tags: [devops, infrastructure-as-code, terraform, aws]
sources: [what-is-terraform]
created: 2026-11-21
updated: 2026-11-21
---

# Terraform vs AWS CloudFormation

Two [[infrastructure-as-code]] tools: [[terraform]] (HashiCorp) and CloudFormation (AWS's built-in service).

| Dimension | Terraform | AWS CloudFormation |
|---|---|---|
| Scope | Multi-cloud + SaaS via providers (src: [[what-is-terraform]]) | AWS only (src: [[what-is-terraform]]) |
| Language | HCL (src: [[what-is-terraform]]) | JSON or YAML (src: [[what-is-terraform]]) |
| State | You manage it, local or remote (src: [[what-is-terraform]]) | Managed automatically by AWS (src: [[what-is-terraform]]) |
| Preview | `terraform plan` (src: [[what-is-terraform]]) | Change sets (note: general knowledge, not from a source) |
| Cost | CLI free to use; licence is BUSL since 2023 (note: general knowledge, not from a source) | No charge for AWS resource types (note: general knowledge, not from a source) |

## When to pick Terraform
- You use more than one cloud, or want to manage DNS, GitHub, monitoring etc. with the same tool (src: [[what-is-terraform]]).
- You want reusable modules shared across teams (src: [[what-is-terraform]]).

## When to pick CloudFormation
- You are all-in on AWS and don't want to run or secure a state backend — AWS keeps the state for you (src: [[what-is-terraform]]).
- You want new AWS features supported natively by AWS (note: general knowledge, not from a source).

## Sources
- [[what-is-terraform]]
