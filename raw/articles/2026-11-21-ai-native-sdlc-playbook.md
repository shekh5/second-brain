# The AI-native SDLC playbook — Claude

> Origin: https://claude.com/resources/articles/the-ai-native-sdlc-playbook
> Received via Telegram: 2026-11-21T18:20:43+00:00
> Author: Louis Claxton (Anthropic), published 2026-08-21, ~40 min read. Products covered: Claude Enterprise, Claude Code, Claude Tag.
> Capture note: the fetch tool would only return a summary of this long article, not its full text. This file holds that summary.

## Core argument
The article's central claim is that "Code is no longer the bottleneck." AI can now write code far faster than traditional approval gates, reviews, and handoffs can process it. The bottleneck has moved to the human-speed steps before and after the build: planning, review and testing, and deployment. Controls designed for human-written code can't keep up with agent-written diffs, so the process itself needs to be rebuilt.

## The six stages
- **Plan:** Capture ideas as a version-controlled `intent.md` file, drafted with Claude and reviewed by a product owner.
- **Design:** Turn the approved intent into a `spec.md` in a single session, with organizational skills (brand, security, compliance, UX) applied while the spec is written.
- **Build:** Start in plan mode and commit a `plan.md` before any code is written. Use `CLAUDE.md` files, skills, and hooks as guardrails, and run parallel sessions in git worktrees.
- **Test:** Give Claude a way to verify its own work, such as tests, builds, or screenshots. Run continuous evals in CI, and treat configuration changes like code.
- **Deploy:** Use AI-driven PR reviews governed by `REVIEW.md`, with humans still approving. Hooks act as approval gates, and CI/CD runs non-interactively with sandboxed credentials. The agent can act up to the production gate but cannot pass it.
- **Maintain:** Monitoring triggers, recurring security scans, and Claude Tag in incident channels can start the loop without a person initiating it. Findings re-enter the process as new `intent.md` files.

## Governance themes
- Each stage commits an artifact that the next stage reads. Together these form the audit trail.
- Humans stay accountable for judgment calls, and their attention concentrates at the gates.
- Policies are enforced through deterministic hooks and managed settings, not only through advisory skills.
- The article includes an example enterprise managed-settings configuration, presented as a starting point to adapt.

Closing line: "The loop keeps running. Human judgement stays above it."
