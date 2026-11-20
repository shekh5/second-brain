# What it takes to set intelligence free — Fabian Hedin, CTO, Lovable

> Origin: https://youtu.be/pZWPq_ZAmM4?si=1xSrMgXP348wtFIx
> Received via Telegram: 2026-11-20T09:03:03+00:00
> Author: Fabian Hedin (CTO, Lovable), AI Engineer channel (CODE Summit 2026 talk, ~21 min, published 2026-11-19)
> Transcript note: YouTube transcript was blocked (bot check / transcript API refused). Saved instead: the video description and chapter list (via r.jina.ai), plus the README of the open-source project linked in the description (https://github.com/lovablelabs/oj). An ai.engineer talk write-up was not yet published.

## Video description

Lovable nearly failed after building a sophisticated multi agent framework, Fabian Hedin says. At CODE Summit 2026, its CTO explains what changed: durable agent runtimes, Git inspired histories and forkable computers that support long running coding agents. Sandbox checkpointing, copy on write memory, a Rust rewrite of Vite and verification feedback loops connect reliable software generation to product and business outcomes.

Speaker info: https://x.com/FabianHedin · https://www.linkedin.com/in/fabian-hedin-2377b0144 · https://github.com/lovablelabs/oj

## Chapters

- 0:00 Why Lovable's first agent framework failed
- 3:52 Building products and business outcomes
- 7:48 Removing the limits on agent runtime
- 8:51 Inboxes and agent communication
- 10:06 Git inspired histories and agent forks
- 11:10 Separating prompts from task history
- 13:03 Stateless workers and uninterrupted deployments
- 14:30 Checkpointing computers and fast resume
- 16:16 Forking sandboxes and copy on write memory
- 18:02 Rewriting Vite in Rust
- 19:13 Inner verification and feedback loops
- 20:07 Product feedback and business metrics

## Linked project: lovablelabs/oj (README excerpt)

"Experimental next generation frontend tooling. It optimizes for memory and cold start, where running many builds (CI, agents, multi-tenant) under Vite gets expensive. OJ is meant to run real production React apps without changes to their source."

Further points from the README:
- SSR mode streams HTML with `renderToReadableStream` instead of buffering; client hydrates through the normal dev pipeline so Fast Refresh and HMR keep working.
- In dev, server modules run in a small persistent Node process that re-evaluates only what changed, instead of rebuilding a bundle per request.
- Vite/Rollup-style plugins run through a persistent Node plugin host; OJ can read an app's existing `vite.config` and its plugins.
- "Runtime env" keys: instead of baking `import.meta.env` values into compiled code (which needs a dev-server restart to change), values are read at page load and can be set over a local-only HTTP endpoint. Useful "when the dev server starts before its backend does (a preview whose database comes up later)". Nothing is recompiled; open pages reload.
- Runs TanStack Start apps directly with no source changes.
- Includes `oj typecheck` (tsc on a Rust port of the TypeScript compiler).
- Benchmarks section (README, oj 0.2.46, vs Vite 8.3.5 on generated 1k–10k-module React apps): "Against Vite's default dev, oj starts faster at every size: cold 1.4x at 1k to 1.9x at 10k, warm 1.9x to 2.2x. Reload is level with it. Vite's experimental bundled dev starts faster than oj and reloads far faster ... Memory is oj's largest and most consistent win: a 136-201MB footprint against Vite's 306MB-1.7GB, from 2.5x less than default dev at 1k to 6.6x less at 10k."
