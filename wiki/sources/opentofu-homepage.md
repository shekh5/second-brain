---
type: source
tags: [devops, infrastructure-as-code, opentofu, terraform]
sources: [opentofu-homepage]
created: 2026-11-21
updated: 2026-11-21
---

# OpenTofu — project homepage

- **Raw file:** `raw/articles/2026-11-21-opentofu.md`
- **Author / origin:** OpenTofu project (Linux Foundation), opentofu.org homepage. A project's own marketing page — claims are not independent. The raw file is a condensed capture.
- **Ingested:** 2026-11-21

## Summary
OpenTofu is an open-source [[infrastructure-as-code]] tool that calls itself a "drop-in
replacement for Terraform". It was forked by Gruntwork, Spacelift, Harness, env0, Scalr and others
after HashiCorp moved Terraform from an open-source licence to the Business Source License (BUSL),
and it is now run by the Linux Foundation. It reuses the Terraform provider/module ecosystem
(3,900+ providers, 23,600+ modules, via its own registry) and adds features Terraform lacks, such
as **client-side state encryption**, an `-exclude` flag and `for_each` over providers.

## Key takeaways
- **Why it exists:** licence change (Terraform → BUSL) — OpenTofu keeps the tool open source under neutral stewardship.
- **Drop-in:** same HCL, same providers and modules; switching mostly means swapping the binary (`tofu` instead of `terraform`).
- **Unique features:** state encryption at rest (v1.7, keys from PBKDF2, AWS KMS, GCP KMS, OpenBao), early variable evaluation in module sources (v1.8), `-exclude` and provider `for_each` (v1.9).
- **Compatibility is not promised forever:** the community picks which future Terraform features to add.
- Choosing between them is mostly about **licence risk**, not capability, per the page's FAQ.

## Concepts touched
[[opentofu]], [[terraform]], [[infrastructure-as-code]], [[opentofu-vs-terraform]]

## Open questions
- Exactly what the BUSL forbids (it mainly restricts offering competing hosted products) — the page only calls it "ambiguous".
- How far the two tools have drifted apart since the fork (state-file compatibility across versions).
