# ADLC vs SDLC: How the Agent Development Lifecycle Differs

> Origin: https://atlan.com/know/ai-agent/adlc-vs-sdlc/
> Received via Telegram: 2026-11-14T10:10:58+00:00
> Author: Emily Winks (Atlan), published 2026-06-16, updated 2026-09-21
> Text extracted from the page HTML on 2026-11-14 (site navigation may remain).

ADLC vs SDLC: Agent Development Lifecycle Explained [2026] Skip to main content

# ADLC vs SDLC: How the Agent Development Lifecycle Differs

Emily WinksData Governance ExpertData Governance Specialist18+ years in information architecture, data governance, and enterprise data managementMasters, Library and Information Science, Queens College; Certificate in Archives, Records Management and Preservation; BA English, St. Joseph's CollegeAtlan Product EssentialsComputer Science Principles: Programming (LinkedIn)View LinkedIn ProfileUpdated:Sep 21, 2026|Published:Jun 16, 202622 min readSee Context Agents LiveGet the Context Layer Ebook

## Key takeaways

- ADLC ships probabilistic behavior; SDLC ships deterministic code. A different class of artifact.

- ADLC requires a context lifecycle: build, test, version, deploy, and observe governed context

- Over 40% of agentic AI projects will be canceled by 2027; most failures trace to context gaps, not model limits

- Most ADLC frameworks prescribe evaluation harnesses but skip what the harness evaluates against

## What is the difference between ADLC and SDLC?

ADLC (Agent Development Lifecycle) manages probabilistic, context-dependent AI agent behavior. SDLC (Software Development Lifecycle) manages deterministic code. The structural difference is not just in phases but in what each lifecycle treats as its primary engineering artifact and how it defines done. ADLC ships a trilogy of code, context layer, and evaluation suite; SDLC ships code. ADLC measures evaluation distributions; SDLC tests pass or fail. Most enterprise AI programs require both running in parallel.

### Three structural differences that explain the gap

- Artifact: SDLC ships code; ADLC ships code + context layer + evaluation suite as a trilogy

- Testing: SDLC measures pass/fail; ADLC measures evaluation distributions against quality thresholds

- Production model: SDLC ships versioned releases; ADLC continuously calibrates context in production

Is your data estate AI-agent ready?

Get the AI Labs Report

ADLC and SDLC are two engineering lifecycle frameworks with a critical distinction: SDLC ships deterministic code, while ADLC ships probabilistic agent behavior where output varies with context quality, model state, and tool availability. Atlan, Arthur.ai, Glean, and IBM have each formalized ADLC approaches because according to Gartner (June 2025), more than 40% of agentic AI projects will be canceled by end of 2027, mostly due to costs, unclear value, and risk controls that SDLC-only teams cannot provide. This guide covers 8 structural differences, a decision table for when to use each, and the context lifecycle discipline that most ADLC frameworks still omit.

Key comparison dimensions covered below:

- Artifact: What SDLC and ADLC each ship, and why they’re different classes of engineering product

- Testing: Binary pass/fail vs evaluation distributions

- Production model: Versioned releases vs continuous context calibration

- Why most ADLC implementations still fail, and what the fix requires

- How SDLC and ADLC work together in real enterprise programs

- The context lifecycle: the discipline ADLC requires and SDLC never needed

## ADLC vs SDLC: the three structural differences

The core difference between ADLC and SDLC comes down to what each lifecycle is designed to produce and validate. SDLC assumes the same input produces the same output every time. This is the deterministic foundation that makes binary testing meaningful. Agents don’t work this way. As Clay Bavor and Bret Taylor, Co-Founders of Sierra (2024), wrote: “traditional software is written in a programming language that is rule-based and deterministic, so the same input reliably produces the same output. Agents are goal-based and non-deterministic.”

Three structural differences define the gap:

- Artifact type: SDLC ships source code. ADLC ships a trilogy: code, context layer, and evaluation suite. Agents require governed business context at runtime, not just working code.

- Testing method: SDLC tests pass/fail against expected outputs. ADLC measures evaluation distributions, asking “does the agent produce accurate, grounded, cost-viable output across a range of scenarios?”

- Production model: SDLC ships versioned releases. ADLC continuously calibrates context as the underlying business data evolves.

Quick comparison at a glance:

Dimension

SDLC

ADLC

What it engineers

Deterministic code

Probabilistic agent behavior

Primary artifact

Source code + tests

Code + context + evaluation suite

Testing approach

Binary pass/fail

Evaluation distributions + thresholds

Deployment model

Version-gated release

Continuous context calibration

Ownership

Software engineering team

Cross-functional: eng + data + AI ops

Governance requirement

Code review + audit trail

Context governance + drift monitoring

Failure mode

Regression, crash, wrong logic

Context drift, stale schema, hallucination

Complexity level

Well-understood and mature

Emerging, 2-3 years as named practice

### The AI Context Stack: What lives under the hood of every reliable agent

The context layer is the engineering artifact ADLC requires and SDLC never had. Get the brief that explains what it is, how it's structured, and why enterprise teams are building it now.

Get the AI Context Stack

## ADLC vs SDLC: What’s the difference?

The core difference between ADLC and SDLC appears not in the phase names (both have planning, development, testing, deployment, and monitoring) but in what each lifecycle treats as the primary engineering artifact and how each defines success. SDLC crystallized between the 1970s (Waterfall) and the 1990s-2000s (Agile). ADLC as a named discipline is 2-3 years old.

According to Gartner (August 2025), enterprise applications featuring task-specific AI agents will rise from less than 5% in 2025 to 40% by end of 2026. The organizations building those agents are discovering that SDLC governance was designed for a different class of artifact.

The confusion persists because ADLC and SDLC share surface vocabulary: planning, development, testing, deployment, monitoring. Most teams start ADLC by adding sprint cycles and evaluation scripts onto an existing SDLC process: surface adaptation without structural change. The result is a persistent gap between experimentation and production. According to McKinsey’s State of AI 2025 report, 62% of organizations are experimenting with AI agents but only about 23% are scaling in at least one function. That gap traces to teams applying SDLC gates to agents that need a different set of lifecycle disciplines.

As the same Sierra post (Clay Bavor and Bret Taylor, 2024) put it: “AI agents break all the rules we’ve come to expect from software…and they’ve broken the typical software development life cycle in the process.”

Understanding what is harness engineering, the evaluation infrastructure ADLC requires, is the practical first step for teams making this transition.

## What is SDLC?

SDLC, the Software Development Lifecycle, is the structured process by which software teams plan, build, test, and release code. The defining property of SDLC is deterministic behavior: the same function returns the same output given the same input. This makes binary testing meaningful and makes version-controlled releases reliable.

SDLC has spent 50 years accumulating tooling: Git for version control, Jira for project management, Jenkins and GitHub Actions for CI/CD, Terraform for infrastructure-as-code. Agile transformed it from waterfall sequences into iterative sprints, but the underlying assumption never changed: the artifact is code, and code behaves deterministically.

About 51% of respondents run agents in production, according to LangChain’s State of AI Agents report. Most of those teams built on organizations with mature SDLC practices. SDLC is the baseline every software team already owns. ADLC is not a replacement; it is an extension layer for the agentic components that SDLC cannot govern alone.

### Core components of SDLC

SDLC has six well-understood phases, each with purpose and tooling:

- Requirements and planning: Defined scope, user stories, acceptance criteria, all pre-specified before build begins

- Design and architecture: System design, data models, API contracts with deterministic interfaces throughout

- Implementation: Code written to spec; behavior is explicit and verifiable

- Testing and QA: Unit, integration, regression; binary pass/fail against expected outputs

- Deployment: Version-gated release, rollback capability, infrastructure-as-code

- Maintenance: Bug fixes, patches, feature iterations; behavior change always requires code change

SDLC’s structural gap for agentic work: binary testing has no mechanism to evaluate probabilistic outputs, context grounding quality, or semantic accuracy. And critically, SDLC has no lifecycle primitive for context. Code doesn’t need governed, versioned business context at runtime. Agents do.

## What is ADLC?

ADLC, the Agent Development Lifecycle, is the structured practice for building, evaluating, and operating AI agents whose behavior is probabilistic, context-dependent, and continuously evolving. The term was coined primarily by Arthur.ai in 2024 and formalized by Glean (7-stage framework, May 2026), Salesforce (5-phase Agentforce model), IBM, and EPAM in 2025-2026. Multiple variants exist; the vocabulary is still standardizing.

One critical disambiguation: this page covers ADLC as “agent development lifecycle,” the framework for building AI agent systems. It does not cover “AI-SDLC” or “A-SDLC,” which refers to using AI tools to assist traditional software development (the Augment Code / CodeRabbit use case). These are distinct disciplines.

ADLC matters because according to Gartner (August 2025), 40% of enterprise applications will feature task-specific AI agents by end of 2026, up from less than 5% in 2025. The discipline is being formalized in real time because the existing SDLC toolkit cannot govern what agents actually need: context, evaluation, and continuous improvement as first-class concerns.

As Adam Wenchel, Co-Founder and CEO of Arthur.ai (2025), described it: “Going from functionally complete to reliable is where the work lies.”

### Core components of ADLC

ADLC covers a broader lifecycle than SDLC because the artifact is broader:

- Agent design and scoping: Define agent goals, tool inventory, and permission boundaries. Non-determinism requires explicit constraint design before the first line of code.

- Context engineering: Build, version, and govern the business context agents reason against. This is a continuous discipline, not a pre-launch checklist item. See what is context engineering for the full framework.

- Development and iteration (inner loop): Rapid prompt-test-evaluate cycles within a harness; token economics analysis happens here to catch cost failures before production

- Evaluation harness: Automated evaluation suite that measures output quality distributions, not binary correctness. Adam Wenchel, Co-Founder and CEO of Arthur.ai, described a well-curated eval suite as the single most important predictor of agentic system success. The agent harness is the infrastructure that makes this measurement possible.

- Deployment and monitoring (outer loop): Agents deployed as live services with drift monitoring, cost metering, and audit trails

- Governance and improvement: Continuous context calibration, agent performance reviews, rollback paths for context regressions

The 12-20 week typical first-production timeline for ADLC implementations (Sumatosoft, 2026) reflects how much additional infrastructure these phases require compared to a standard software sprint. Teams that treat context engineering as a checklist item rather than a continuous discipline at every ADLC phase are those whose agents pass development and fail in production. That is the pattern behind the 88% of agentic projects that never ship.

### Context Gap Calculator: How big is your agent's context gap?

ADLC evaluation harnesses can only measure what agents have access to. The Context Gap Calculator shows where your context layer has gaps that are silently degrading agent output quality.

Calculate Your Context Gap

## ADLC vs SDLC: A head-to-head comparison across 10 dimensions

The sharpest difference between ADLC and SDLC appears not in the phase names but in what each lifecycle treats as the primary engineering artifact and how each defines success. SDLC’s “definition of done” is a passing test suite and a deployed version. ADLC’s is a sustained evaluation distribution above a defined threshold, which requires a context layer that is governed, current, and versioned.

SDLC governs code behavior; ADLC governs agent behavior. These are different classes of engineering artifacts with different governance requirements.

Detailed comparison across 10 dimensions:

Dimension

SDLC

ADLC

Primary artifact

Source code

Code + context layer + evaluation suite

Behavior model

Deterministic: same input, same output

Probabilistic: output varies with context and model state

Testing method

Binary pass/fail (unit, integration, regression)

Evaluation distributions measured against quality thresholds

Evaluation criteria

Does the code do what the spec says?

Does the agent produce accurate, grounded, cost-viable output?

Deployment cadence

Version-gated releases

Continuous deployment with context calibration cycles

Context requirement

None: behavior is encoded in code

First-class: governed, versioned business context required at runtime

Governance scope

Code review, audit trail, access control

Context governance + drift monitoring + token economics + agent accountability

Failure mode

Bug, crash, regression, logic error

Context drift, stale schema, semantic hallucination, cost overrun

Maturity indicator

Code coverage %, regression suite pass rate

Eval distribution stability, context freshness score, cost per task

Industry framework

ISO/IEC 12207, CMMI, Agile/Scrum

Arthur.ai (3-phase), Glean (7-stage), Salesforce (5-phase), Microsoft Learn

### A real-world example: Token economics caught by ADLC, invisible to SDLC

A financial services team built a contract analysis agent. The code passed every SDLC gate: unit tests, security review, staging deployment. By SDLC standards, it was done. ADLC evaluation, specifically the token economics phase of the inner development loop, revealed that the initial prompt design would be economically unviable at production volume. The agent was “functionally complete” by SDLC standards and economically non-viable by ADLC standards. This distinction was only visible through the evaluation harness ADLC builds into its inner loop.

The same evaluation phase surfaced that responses hallucinated contract terms when the context layer returned stale schema. Neither failure mode (cost overrun nor semantic hallucination) is detectable with binary pass/fail testing. This is what Arthur.ai’s ADLC framework names as “going from functionally complete to reliable,” the gap that SDLC has no gate for.

The governance scope question (“what are we governing?”) is what separates ADLC from SDLC in practice. SDLC governs code correctness. ADLC governs agent behavior, which is inseparable from context quality.

## Why do most ADLC implementations still fail?

Most ADLC implementations fail not because teams skip evaluation but because they evaluate without the context infrastructure that makes evaluation meaningful. According to Atlan’s harness engineering research (2026), 88% of AI agent projects never reach production. The named ADLC failure modes (bad prompts, poor orchestration, weak evaluation) are symptoms. The root cause is context absence.

Agents in failed ADLC implementations are evaluated against raw database schema rather than governed, versioned business semantics. When the harness tests whether an agent can answer a question accurately, the answer depends entirely on whether the context layer reflects current business reality. A schema-grounded agent fails not because the evaluation harness is wrong, but because what the harness is evaluating against is wrong.

This is where the “context lifecycle” concept matters. Context must be built, tested, versioned, deployed, observed, and improved alongside the code; not treated as a pre-launch configuration step. When Glean launched their 7-stage ADLC framework (May 2026), they placed “Context” as Stage 4. But treating context as a phase rather than a lifecycle discipline means it gets skipped when timelines compress. That is exactly what happens in the majority of teams that never reach production.

Atlan AI Labs (2026) found a 38% improvement in SQL accuracy when agents were grounded in governance metadata versus raw schema, across 522 query evaluations with statistical significance at p<0.0001. Customers who layered governed context also reported up to 5x improvement in query accuracy. These are not marginal improvements; they represent the difference between an agent that passes ADLC evaluation and one that does not.

The context architecture for AI agents that makes this possible is what most ADLC frameworks prescribe without specifying: governed context as a versioned artifact, with the same engineering discipline applied to it as to code.

The forward-looking stakes are direct: according to Gartner (2025), by 2030, 50% of AI agent deployment failures will be due to insufficient governance platform runtime enforcement. Governance failure in ADLC is not a compliance checkbox; it is the mechanism by which the 40%+ cancellation rate Gartner predicted becomes real.

Teams that understand how agents forget, including the difference between session forgetting and organizational context absence, are the ones that build ADLC implementations with the context lifecycle discipline required to avoid this failure mode.

## How do ADLC and SDLC work together in enterprise AI programs?

In most enterprise AI programs, SDLC and ADLC run in parallel. Software components that power the agent infrastructure follow SDLC governance; the agent behavior layer requires ADLC discipline. The governance gap opens when teams apply SDLC gates to agentic components that need context lifecycle management.

SDLC and ADLC are not mutually exclusive. Most enterprise AI programs have both software components (SDLC-governed) and agentic components (ADLC-governed). Choosing which to apply to which components is the core decision; getting it wrong in either direction creates problems.

### Data pipeline development (SDLC) feeding the agent context layer (ADLC)

ETL pipeline code, data quality tests, and version-controlled schema definitions are SDLC artifacts. Context versioning, agent evaluation against updated schema, and drift detection when pipeline changes propagate are ADLC disciplines. When combined, agents stay grounded when the underlying data changes, because context lifecycle synchronizes with code lifecycle. This is the context architecture for AI agents in practice.

### API and tool development (SDLC) exposed as agent tools (ADLC)

API specs, contract tests, CI/CD deployment, and security review are SDLC work. Tool integration testing within the evaluation harness, permission boundary validation, and cost metering per tool call are ADLC work. Teams that confuse these domains either under-test agent tool usage (applying only SDLC security gates) or over-engineer standard API development (applying ADLC evaluation to code that behaves deterministically). Choosing the right agentic framework for enterprise is part of this architectural decision.

### When to use each

Condition

SDLC sufficient

ADLC required

Both required

Deterministic rule-based automation

✓

Agent with natural language goals

✓

AI agent built on software infrastructure

✓

Production agent with multiple tools

✓

Regulatory environment with audit requirements

✓

SDLC is sufficient when building infrastructure tools, APIs, pipelines, or automation where behavior is fully specified and outputs are deterministic.

ADLC is required when building any agent that takes natural language goals, uses LLMs, makes tool calls, or operates in environments where context quality determines output quality.

Both simultaneously are required for any enterprise AI program where agents consume or expose software infrastructure, which is effectively every production deployment.

The organizational version of this problem is agent sprawl: what happens when different teams apply different lifecycle disciplines (or no discipline at all) to a proliferating agent fleet. Agent sprawl is context sprawl. Each agent with its own ungoverned context creates the same governance failure that ADLC was designed to prevent.

### AI Agent Context Readiness Checklist: Is your team ready for ADLC production?

Before deploying agents into production, verify that your context lifecycle is in place. This checklist covers the infrastructure decisions that determine whether your ADLC implementation succeeds or joins the 88% that never ship.

Check Your Context Readiness

## Real stories from real customers: Context lifecycle in production

"We're excited to build the future of AI governance with Atlan. All of the work that we did to get to a shared language at Workday can be leveraged by AI via Atlan's MCP server...as part of Atlan's AI Labs, we're co-building the [semantic layer](https://atlan.com/know/semantic-layer/) that AI needs with new constructs, like context products."

Joe DosSantos, VP of Enterprise Data & Analytics, Workday

Watch Now

"Atlan is our context operating system to cover every type of context in every system including our operational systems. For the first time we have a single source of truth for context."

Sridher Arumugham, Chief Data Analytics Officer, DigiKey

Watch Now

## Why the context lifecycle is ADLC’s missing piece

Atlan treats context as the lifecycle artifact that ADLC requires and SDLC never had: something that must be built, tested, versioned, deployed, and continuously improved with the same engineering discipline applied to code. Most ADLC implementations treat context as pre-launch configuration: upload a schema, write system prompts, move on. When the business changes, the context does not update automatically, and the agent drifts.

Context drift produces the exact failures Gartner predicts will cancel 40%+ of agentic projects: unclear value (from degraded accuracy), rising costs (from inefficient prompts), and ungoverned behavior (from stale or missing business context). This pattern shows up consistently in enterprise team conversations: “The agent is easy to build now; getting business context into it is the hard part” (recurring theme across data teams in financial services, retail, and healthcare).

Atlan’s Context Engineering Studio is designed as the IDE for the complete ADLC context lifecycle: bootstrap (build the governed context substrate), simulate (test agents against it before production), ship (expose via the Atlan MCP server to Claude, ChatGPT, Gemini, Cursor, and Copilot Studio), and observe (monitor context freshness, drift, and agent behavior in production). The Enterprise Data Graph is the shared, living substrate of assets, lineage, policies, and relationships that agents query at every ADLC phase, not just at launch.

The proof is in the measurement: Atlan AI Labs (2026) found a 38% SQL accuracy improvement when agents queried governance metadata instead of raw schema, across 522 controlled query evaluations. Teams that build an agent harness with governed context as a first-class input are the ones whose ADLC evaluations catch real failures instead of passing agents that will drift in production.

As more enterprise applications gain agentic capabilities (the 40% by 2026 that Gartner projects), the organizations that formalize ADLC and treat context lifecycle as first-class will close the production gap. The vocabulary for these decisions is stabilizing now. The teams that learn it are the ones whose agents ship.

Book a Demo

## FAQs about ADLC vs SDLC

### 1. What is the difference between ADLC and SDLC?

ADLC manages probabilistic, context-dependent AI agent behavior; SDLC manages deterministic code. Three structural differences define the gap: ADLC ships code plus context plus evaluation as a trilogy of artifacts (SDLC ships code only); ADLC measures evaluation distributions (SDLC tests pass/fail); ADLC requires continuous context calibration in production (SDLC ships versioned releases). Most enterprise AI programs require both running in parallel: SDLC for the infrastructure, ADLC for the agent behavior layer.

### 2. Can SDLC handle AI agent development without modification?

SDLC can handle the software infrastructure that agents run on, but it cannot manage agent behavior. SDLC binary pass/fail testing has no mechanism to evaluate probabilistic outputs, context grounding quality, or semantic accuracy. Teams that apply SDLC gates to agentic components systematically under-test the parts most likely to fail in production. The result is agents that pass development but drift within weeks of deployment.

### 3. What is ADLC in AI?

ADLC (Agent Development Lifecycle) is the structured practice for building, evaluating, and operating AI agents. Unlike SDLC, which assumes deterministic behavior, ADLC manages agents whose outputs vary with context quality, model state, and tool availability. The term was coined by Arthur.ai in 2024 and formalized by Glean, Salesforce, IBM, and EPAM in 2025-2026. Multiple variants exist; the vocabulary is still standardizing across the industry.

### 4. What does “non-deterministic” mean in agent development?

Non-deterministic means the same input can produce different outputs depending on context quality, model state, prompt phrasing, and tool availability. Sierra’s co-founders Clay Bavor and Bret Taylor put it this way: traditional software is rule-based and deterministic, so the same input reliably produces the same output; agents are goal-based and non-deterministic. This breaks SDLC’s core assumption that tests can be binary pass/fail, because there is no single “correct” output to test against.

### 5. Can you use SDLC and ADLC in the same project?

Yes. Most enterprise AI programs require both. Software components that power agent infrastructure follow SDLC governance; the agent behavior layer requires ADLC discipline. The governance gap opens when teams apply SDLC gates to agentic components that need context lifecycle management. Running them in parallel is the standard pattern for mature enterprise AI programs. The key is knowing which components belong under which lifecycle.

### 6. How do you test an AI agent in ADLC?

ADLC testing uses evaluation harnesses that measure output quality distributions rather than binary pass/fail. The harness runs the agent against a curated set of test cases and measures accuracy, cost per task, and context grounding quality against defined thresholds. Adam Wenchel of Arthur.ai has called a well-curated eval suite the single most critical factor for guaranteeing success in an agentic system. The harness evaluates against governed context, not raw schema, which is why context infrastructure is a prerequisite for meaningful evaluation.

### 7. What is drift monitoring in ADLC?

Drift monitoring in ADLC tracks changes in agent output quality over time as the underlying context, data, or model changes. When a data pipeline updates schemas or business definitions change, agents grounded in stale context begin producing degraded outputs. Drift monitoring detects these regressions before users do and triggers context recalibration. This has no equivalent in SDLC because traditional software does not depend on runtime context quality for correctness.

### 8. What is token economics in the agent development lifecycle?

Token economics in ADLC is the analysis of the cost per task that an agent incurs at production volume. A prompt design that works in development may become economically unviable at scale, a failure mode invisible to SDLC binary pass/fail gates. Token economics analysis happens in the inner development loop, before deployment, and is one of the evaluation dimensions that has no equivalent gate in SDLC because traditional software does not have per-inference cost profiles.

## Sources

Gartner, “Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027,” June 2025. https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027

Gartner, “Gartner Predicts 40 Percent of Enterprise Apps Will Feature Task-Specific AI Agents by 2026,” August 2025. https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025

Gartner, “Gartner Unveils Top Predictions for IT Organizations and Users in 2026 and Beyond,” October 2025. https://www.gartner.com/en/newsroom/press-releases/2025-10-21-gartner-unveils-top-predictions-for-it-organizations-and-users-in-2026-and-beyond

Sierra AI, “The Agent Development Life Cycle,” Clay Bavor and Bret Taylor, 3 June 2024. https://sierra.ai/blog/agent-development-life-cycle

Arthur.ai, “The Agent Development Lifecycle (ADLC): Rethinking the Venerable SDLC for AI Agents,” Adam Wenchel, 2025. https://www.arthur.ai/blog/introducing-adlc

Glean, “Introducing the Agent Development Lifecycle (ADLC),” Arvind Jain, May 2026. https://www.glean.com/blog/agent-dev-lifecycle-2026

Sumatosoft, “What is ADLC? A 2026 Guide to Governing Probabilistic AI Systems,” 2026. https://sumatosoft.com/blog/what-is-adlc-agentic-development

Atlan, “What Is Harness Engineering?” 2026. https://atlan.com/know/what-is-harness-engineering/

Atlan, “AI Agents for Software Engineering,” 2025. https://atlan.com/know/ai-agents-for-software-engineering/

Atlan AI Labs, “Research Shows How Enhanced Metadata Delivers 38% Better AI Accuracy,” 2026. https://atlan.com/know/enhanced-metadata-improves-query-accuracy/

McKinsey, “The State of AI in 2025: Agents, Innovation, and Transformation,” 2025. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

Share this article

Atlan is the Context Layer for AI. It translates business knowledge, including data definitions, working procedures, and governance policies, into context AI can actually use. This knowledge lives in a single Enterprise Data Graph that every team and AI agent can reach.In Atlan's AI Labs benchmark, adding this context improved AI's text-to-SQL accuracy by 38%.Atlan is recognized as a Leader across multiple Gartner reports and Forrester Waves, and is trusted by over 400 enterprises representing $10T+ in market cap, including Mastercard, Workday, General Motors, CME Group, HubSpot, FOX, Virgin Media O2, and Elastic.

Get a Custom DemoSee How It Works

## Agent lifecycle: Related reads

What Is Harness Engineering? The engineering discipline behind evaluation harnesses that ADLC requires. How to Build an AI Agent Harness Practical guide to building the harness layer in the ADLC development phase. Agent Harness vs Agent Framework Understanding the third layer, context, that both harness and framework skip. How Agents Forget and How to Fix It The memory and context persistence problem ADLC monitoring must address. Context Architecture for AI Agents Deep technical reference for the context layer ADLC requires at every phase. What Is Context Engineering? The discipline that fills the gap between SDLC assumptions and ADLC requirements. Enterprise Context Layer for AI Why the context layer is ADLC infrastructure, not a runtime configuration. A Context Layer for the SDLC

## Bridge the context gap.Ship AI that works.

Book a DemoWatch Context Studio Demo
