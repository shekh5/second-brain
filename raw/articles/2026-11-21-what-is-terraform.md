# Introduction to Terraform — GeeksforGeeks

> Origin: https://www.geeksforgeeks.org/devops/what-is-terraform/
> Received via Telegram: 2026-11-21T18:19:33+00:00
> Author: not shown (GeeksforGeeks, DevOps section; page last updated 2026-11-19)
> Capture note: the fetch tool returned a condensed, paraphrased version of the article that keeps its structure, not the verbatim text.

## Overview
Terraform, created by HashiCorp, is an Infrastructure as Code (IaC) tool for building, changing, and managing infrastructure. It automates provisioning, supports version control and team collaboration, and helps reduce human error.

## Infrastructure as Code
IaC means managing infrastructure through configuration files instead of manual console clicks. Terraform's approach is declarative: you describe the desired end state, and it works out the steps. Because the files are version-controlled, infrastructure changes can be tracked like application code.

## Key Features
- Works across many providers, unlike single-cloud tools such as CloudFormation or ARM templates.
- Often replaces resources instead of modifying them in place, which helps limit configuration drift.
- Uses a state file as the record of real-world resources.
- Supports reusable modules.

## Architecture
- **Core (engine):** Reads configuration, compares it with current state, and calculates the required changes.
- **Providers:** Plugins that translate Terraform code into API calls for platforms such as AWS, Azure, or Kubernetes.
- **State file (`terraform.tfstate`):** Maps code to real resources. Teams usually store it remotely so everyone works from the same record.

## Core Elements
- **CLI:** Main commands are `init`, `validate`, `plan`, `apply`, and `destroy`.
- **Language:** Configuration uses HashiCorp Configuration Language (HCL), which is designed to be readable. Resources, such as VPCs or storage buckets, are defined in blocks.
- **Providers:** Define the resource types and data sources that Terraform can manage on a platform.
- **Modules:** Groups of related resources with inputs (variables), outputs, optional versioning, and support for nesting.
- **Provisioners:** Run scripts or copy files after resource creation. Use them sparingly, since they add complexity and reduce predictability.
- **State:** Lets Terraform compare current and desired infrastructure and apply only needed changes.
  - *Local state* is simple and suits learning or small projects, but it has no locking and is risky to share.
  - *Remote state* is the recommended production approach. It supports collaboration, locking, and encryption. Common backends include AWS S3 (often with DynamoDB for locking), Terraform Cloud, Azure Blob Storage, and Google Cloud Storage.
- **Private module registry:** Lets organizations host and share internal modules with access controls.

## Common Commands
- **`init`:** Initializes the working directory and downloads required providers.
- **`plan`:** Previews the changes that would be made.
- **`apply`:** Carries out the planned changes through cloud APIs.
- **`destroy`:** Removes all resources tracked in the state.
- **`import`:** Brings an existing resource under Terraform management.
- **`console`:** Opens an interactive shell for evaluating expressions.
- **`refresh`:** Updates state to match the actual infrastructure.

## Terraform vs. AWS CloudFormation
| Feature | Terraform | AWS CloudFormation |
|---|---|---|
| Scope | Multi-cloud | AWS only |
| Language | HCL | JSON or YAML |
| State | Managed by the user (local or remote) | Managed automatically by AWS |
