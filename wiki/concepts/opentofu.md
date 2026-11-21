---
type: concept
tags: [devops, infrastructure-as-code, opentofu, terraform]
sources: [opentofu-homepage]
created: 2026-11-21
updated: 2026-11-21
---

# OpenTofu

**In one line:** the open-source, Linux Foundation fork of [[terraform]] — same language and
providers, plus a few extra features such as encrypted state (src: [[opentofu-homepage]]).

## How it works
It works exactly like Terraform: HCL files, providers, modules, a state file, and the
`init → plan → apply` workflow (src: [[opentofu-homepage]]). The command is `tofu` instead of
`terraform` (note: general knowledge, not from a source).

```
 2014  Terraform (open source, MPL)
 2023  HashiCorp relicenses Terraform → BUSL
          │
          └──► fork: OpenTofu (Gruntwork, Spacelift, Harness, env0, Scalr…)
               └─ Linux Foundation stewardship, stays open source
```
(src: [[opentofu-homepage]]; dates are general knowledge, not from the source)

Features unique to OpenTofu (src: [[opentofu-homepage]]):
| Version | Feature | Why it helps |
|---|---|---|
| 1.7 | **State encryption** (client-side, keys from PBKDF2, AWS KMS, GCP KMS, OpenBao) | The state file often contains secrets; now it's encrypted at rest |
| 1.8 | Variables/locals in module sources and versions | Bump many module versions with one change |
| 1.9 | `-exclude` flag on plan/apply | Skip resources for testing or staged rollouts |
| 1.9 | `for_each` on providers | One provider config per region without copy-paste |

## Why it matters / when to use it
- When you want IaC under a true open-source licence and neutral governance (src: [[opentofu-homepage]]).
- When state encryption matters (note: general knowledge — Terraform's state is plain JSON unless the backend encrypts it).
- Switching carries some risk for companies, reduced by Linux Foundation stewardship and the goal of feature parity (src: [[opentofu-homepage]]).

## Trade-offs
| Pro | Con |
|---|---|
| Open source, community-governed (src: [[opentofu-homepage]]) | Future Terraform features aren't guaranteed to arrive (src: [[opentofu-homepage]]) |
| Reuses Terraform providers and modules (3,900+ / 23,600+) (src: [[opentofu-homepage]]) | Smaller vendor behind it than HashiCorp/IBM (note: general knowledge, not from a source) |
| Extra features: state encryption, `-exclude` (src: [[opentofu-homepage]]) | Using OpenTofu-only features makes going back to Terraform harder (note: general knowledge, not from a source) |

## Real-world examples
- Homepage examples: create an S3 bucket, manage Cloudflare DNS records, set up GitHub repos with branch protection — all as code (src: [[opentofu-homepage]]).
- Backed by Harness, Gruntwork, Spacelift, env0, Scalr and 180+ community contributors; Buildkite, Cloudflare and Datadog sponsor services (src: [[opentofu-homepage]]).

## Related
[[terraform]] — the tool it forked from
[[opentofu-vs-terraform]] — side-by-side choice
[[infrastructure-as-code]] — the underlying idea

## Sources
- [[opentofu-homepage]]
