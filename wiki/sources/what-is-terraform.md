---
type: source
tags: [devops, infrastructure-as-code, terraform]
sources: [what-is-terraform]
created: 2026-11-21
updated: 2026-11-21
---

# Introduction to Terraform — GeeksforGeeks

- **Raw file:** `raw/articles/2026-11-21-what-is-terraform.md`
- **Author / origin:** GeeksforGeeks DevOps tutorial (author not shown, updated 2026-11-19). The raw file is a condensed paraphrase of the article, not the verbatim text.
- **Ingested:** 2026-11-21

## Summary
A beginner tutorial on Terraform, HashiCorp's **Infrastructure as Code** (IaC) tool. Instead of
clicking around a cloud console, you describe the servers, networks and buckets you want in text
files, and Terraform works out how to create or change them. Its engine compares your files with a
**state file** (its record of what really exists) and calls cloud APIs through **provider** plugins.
Reusable **modules** package groups of resources. The usual workflow is `init → plan → apply`,
and in production the state should live in a shared remote store with locking.

## Key takeaways
- **Declarative:** you describe the end state, Terraform figures out the steps.
- **Three parts:** core (computes the diff), providers (talk to each platform's API), state (maps code to real resources).
- **State is critical:** local state is fine for learning; teams need **remote state** with locking and encryption (e.g. S3 + DynamoDB).
- **`plan` before `apply`:** preview every change before making it.
- **Multi-cloud**, unlike AWS CloudFormation (AWS only, state managed by AWS).
- Use **provisioners** (run scripts after creation) sparingly — they make runs less predictable.

## Concepts touched
[[infrastructure-as-code]], [[terraform]], [[terraform-vs-cloudformation]]

## Open questions
- "Often replaces resources instead of modifying them in place" — true only for some attribute changes; many changes are in-place updates. Worth checking against the Terraform docs.
- The article doesn't mention HashiCorp's 2023 licence change to the BUSL, which matters when choosing a tool (OpenTofu is the open-source fork).
