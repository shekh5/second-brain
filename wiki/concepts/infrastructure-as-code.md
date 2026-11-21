---
type: concept
tags: [devops, infrastructure-as-code, system-design]
sources: [what-is-terraform, opentofu-homepage]
created: 2026-11-21
updated: 2026-11-21
---

# Infrastructure as Code (IaC)

**In one line:** describe your servers, networks, databases and DNS in text files kept in git, and
let a tool create and update the real infrastructure to match.

## How it works
Instead of clicking through a cloud console, you write configuration files. A tool reads them,
compares them with what exists, and makes the changes (src: [[what-is-terraform]]).

```
  config files (git)  ──►  IaC tool  ──►  cloud APIs  ──►  real resources
        ▲                     │
        └──── review / PR     └── state: record of what exists
```

- **Declarative** style: you write *what* you want ("3 servers, 1 bucket"), not the steps to get there. The tool works out the steps (src: [[what-is-terraform]]).
- **Imperative** style (scripts that say "create this, then that") is the alternative (note: general knowledge, not from a source).
- Because the files live in version control, infra changes get history, review and rollback just like app code (src: [[what-is-terraform]]).

## Why it matters / when to use it
- Repeatable: the same files build dev, staging and prod the same way (note: general knowledge, not from a source).
- Fewer human errors than manual console clicks (src: [[what-is-terraform]]).
- Team collaboration through pull requests (src: [[what-is-terraform]]).
- Use it as soon as more than one person, or more than one environment, touches the infrastructure (note: general knowledge, not from a source).

## Trade-offs
| Pro | Con |
|---|---|
| Changes are reviewed, versioned and repeatable (src: [[what-is-terraform]]) | Learning curve: a new language (e.g. HCL) and tool (note: general knowledge, not from a source) |
| Limits **configuration drift** — real infra slowly differing from what was intended (src: [[what-is-terraform]]) | Manual console edits still cause drift unless the team stops making them (note: general knowledge, not from a source) |
| Same code can target many environments (note: general knowledge, not from a source) | The state record becomes critical data that must be protected and locked (src: [[what-is-terraform]]) |

## Real-world examples
- [[terraform]] — HashiCorp's multi-cloud declarative tool (src: [[what-is-terraform]]).
- [[opentofu]] — the open-source, Linux Foundation fork of Terraform; same language and providers (src: [[opentofu-homepage]]).
- IaC isn't only for clouds: OpenTofu's examples manage Cloudflare DNS records and GitHub repositories as code (src: [[opentofu-homepage]]).
- AWS CloudFormation (AWS only) and Azure ARM templates (Azure only) — single-cloud IaC tools (src: [[what-is-terraform]]). See [[terraform-vs-cloudformation]].

## Related
[[terraform]] — the most common IaC tool
[[ephemeral-environment]] — throw-away environments are only practical when infra is defined as code (note: general knowledge, not from a source)

## Sources
- [[what-is-terraform]]
- [[opentofu-homepage]]
