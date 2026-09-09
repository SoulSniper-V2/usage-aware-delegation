---
name: usage-aware-delegation
description: Route substantial Codex coding, research, debugging, architecture, UI, and review work between direct execution and bounded native sub-agents using current model capability, reasoning effort, plan pressure, runtime capacity, and verification needs. Keep simple questions and tiny edits direct.
metadata:
  short-description: Route Codex work by capability and usage
---

# Usage-aware delegation

Choose the smallest execution shape that can reliably satisfy the user's request. The active coordinator owns intent, architecture, approvals, conflicts, integration, and final verification. Use a child only when model fit or independent overlap clearly repays startup, context transfer, supervision, aggregation, review, and rework costs.

This is a policy skill. It does not silently switch the active conversation's model, mutate global configuration, spend reset credits, bypass approvals, disclose credentials, or perform external actions that the user did not authorize.

## Decision order

Apply these priorities:

1. User instructions and explicit model, effort, direct-work, or delegation choices.
2. Safety, sandbox, approval, credential, privacy, and external-action boundaries.
3. Repository `AGENTS.md`, project instructions, and custom-agent configuration.
4. Observed runtime model catalog, supported efforts, native sub-agent tools, capacity, and usage signals.
5. This skill's task-evidence policy.
6. Benchmark and community priors.

An explicit request to work directly disables automatic delegation for the request. An explicit model/effort request is preserved when available; if it cannot be honored, use the nearest safe route and say what changed.

## Observe the current surface

When routing could materially affect the task, and a read-only runtime/account query is available and within the user's authorization, make one small runtime snapshot:

- active coordinator model and effort, if exposed;
- exact available model IDs and each model's supported efforts;
- native spawn, wait, follow-up, close/interrupt tools and reported concurrency;
- plan tier and primary/weekly used percentages, if a connected read-only usage tool exposes them.
- harness fit: available repository context, worktrees, tools, browser/device access,
  artifact inspection, approvals, and observable child lifecycle, if exposed.

Skip the query when it is unavailable, disallowed, or outside the user's scope, and record usage/capacity as `unknown`. Unknown is not zero usage, unlimited capacity, or proof that a model exists. Never infer current quota or actual model use from memory, internet benchmarks, a UI recommendation, or aggregate product-activity counts.

Resolve capability aliases against the current catalog:

- `frontier`: strongest available model for ambiguity, novelty, high consequence, long coherent reasoning, or independent review;
- `balanced`: strong general model for complex implementation, debugging, and synthesis;
- `economy`: lowest-cost adequate model for bounded, repeatable, read-heavy, or mechanically verifiable work.

## Behavioral and harness fit

Model choice is not a single intelligence ranking. When the task makes it
material, assess instruction following, long-task coherence, decomposition and
handoff quality, visual taste, vision/computer-use ability, tool selection,
source discipline, verification quality, latency, and coordination cost.
Treat public model opinions and benchmarks as priors until the current runtime
or a controlled comparison supplies evidence.

Evaluate the model separately from the harness. The harness determines which
files, tools, browsers, devices, worktrees, instructions, approvals, child
lifecycle controls, and verification surfaces are actually available. A
strong model in an unsuitable harness is not a proven route; a smaller model
with the right tools and a bounded objective may be the better route. Missing
dependencies, permissions, credentials, or external authority are environment
or authority failures, not evidence for a stronger model.

Use the task-specific matrix and acceptance patterns in
[task-routing.md](references/task-routing.md) for frontend/UI/3D, backend/API,
research/planning, mechanical work, debugging, independent review, and
orchestration. The matrix is a starting point, not a mandatory phase map.

## Usage pressure

Plan usage is shared and task-dependent. These are conservative local heuristics, not entitlement guarantees or a token-to-quota formula. Use the highest pressure across observed windows.

| Pressure | Signal when percentages exist | Routing adjustment |
|---|---|---|
| ample | windows comfortably below half used | normal gate; up to two children by default |
| watch | short window at least half used or weekly window around two-thirds used | direct by default; one child only for clear overlap or model fit; skip optional review |
| conserve | short window around three-quarters or weekly window around five-sixths used, or a recent sharp increase | direct unless delegation prevents likely expensive failure; one narrow economy child at most; no automatic frontier escalation |
| exhausted | runtime reports a limit or rejects dispatch for quota | continue locally if possible; stop optional work; never redeem, purchase, or reset automatically |
| unknown | no live signal | direct by default; one child maximum only with a strong benefit case |

Do not predict turns remaining. If before/after telemetry is available, report a measured account-wide delta with its timestamp. Otherwise report only the pressure category or that usage was unavailable.

## Classify the task

Assess these axes qualitatively: ambiguity, scope, coupling, verification difficulty, consequence, context burden, latency priority, independent parallelism, instruction-following fit, long-task coherence, visual/taste or computer-use fit, tool/source fit, and verification fit. Also identify read-only work, disjoint writes, shared mutable state, and external actions.

Keep work direct when it is a question, explanation, tiny edit, one-command probe, one-file mechanical change, tightly coupled sequence, overlapping write, shared build/device operation, approval-bound action, or a child would spend more time receiving and returning context than doing useful work.

Consider delegation only when all are true:

1. Native sub-agent support is exposed and not disabled.
2. The child has one self-contained objective and observable acceptance criteria.
3. It has read-only scope or disjoint mutable paths.
4. Expected model-fit or overlap benefit exceeds child startup, context replay, supervision, aggregation, review, and likely rework.
5. It has a bounded validation budget and stop condition.

Direct tool/process concurrency comes before child agents for independent safe commands. Keep semantic dependencies, overlapping writes, builds, simulators/devices, approvals, Git mutation, deployments, uploads, submissions, messages, and other external effects serial.

Delegation is not automatically a quota-saving trick. A high-cost coordinator that supervises many cheap children can consume more than a direct run.

## Model and effort policy

Choose task evidence first, then resolve the capability tier and effort. Start here:

| Work shape | Route |
|---|---|
| literal edit, exact repeated pattern, small inventory | economy/medium; direct if tiny |
| bounded implementation with deterministic tests | economy/high or balanced/medium |
| read-heavy exploration, extraction, docs, test discovery | economy/medium; balanced/medium for broad synthesis |
| explicit latency-first ordinary work | balanced/medium, or the catalog's supported fast tier |
| stable cross-file feature | balanced/medium; economy/high if tightly bounded |
| unknown cross-system bug | balanced/high or frontier/medium |
| architecture, security/privacy/auth, payments, destructive migration, production-critical decision | frontier/medium or balanced/high plus an independent frontier review |
| high-consequence independent review | frontier/medium or balanced/high, fresh context, read-only |
| large low-consequence deterministic scan/deep work | economy/xhigh or economy/max when supported |

Effort rules:

- `medium` is the automatic floor for meaningful work;
- `low` is for a tiny task or explicit speed/compatibility request;
- `high` is for difficult bounded reasoning, high coupling, consequence, or verification;
- `xhigh` is for broad evidence coverage or a classified failure after scope is sound;
- `max` is for bounded deep work with deterministic verification and an accepted latency/token budget;
- `ultra` is never automatic. If the user explicitly chooses native Ultra, follow its runtime semantics and do not stack skill-managed parallelism.

Increase effort within the same tier before changing tiers when the boundary is sound. Escalate the model only when ambiguity, coupling, consequence, or verification needs exceed the current tier. Missing dependencies, permissions, credentials, network services, or external authority are not model evidence.

## Overrides and actual execution

The active coordinator cannot change its own model/effort through this skill. For a child, pass exact `model` and `reasoning_effort` only when the current spawn surface accepts those fields and its tool policy permits automatic overrides. If the surface requires inheritance, preserve the inherited settings and label the result `recommended` versus `observed`.

Never pass `frontier`, `balanced`, or `economy` to a tool that expects an exact model ID. Do not edit global `config.toml` or enable/disable agents as a hidden side effect.

Use these evidence levels:

- `recommended`: policy selected a route;
- `configured`: a runtime/project setting supports it;
- `dispatched`: the native tool accepted the child;
- `observed`: runtime returned model/effort and terminal status;
- `verified`: artifact, scope, and acceptance checks passed;
- `blocked`: required capability, artifact, permission, or acceptance evidence is missing.

A recommendation never proves model execution. A child report never proves an artifact or test passed until inspected.

## Roles and worker budget

Use only roles that pay for themselves:

- `explorer`: read-only repository map, trace, symbols, tests, config, or dependencies;
- `researcher`: bounded current-doc, version, or source verification;
- `worker`: one owned implementation slice;
- `tester`: reproduction or targeted verification;
- `reviewer`: fresh-context, read-only independent review;
- `advisor`: one focused higher-tier question for a likely blocker or high-consequence choice.

Default to zero children for small work, one child for a material bounded sidecar, and at most two children under ample pressure. Increase fan-out only when objectives and writes are disjoint, capacity and lifecycle are observable, pressure is acceptable, and the coordinator has an aggregation and verification step. Reduce to one under watch/conserve and never exceed observed runtime capacity. If capacity is unknown, use one child maximum. Keep these budgets distinct: `child_count` limits concurrent/total children, `time_budget` limits the child's wall-clock attempt, `token_budget` is used only when the runtime exposes a real per-child budget, and `validation_budget` limits checks/recovery. Never invent token limits from plan percentages. Do not pre-create queues, permanent companions, or recursive workers. Leaves must not delegate.

## Child capsule

Give every child a short, self-contained contract:

```text
Role: explorer | researcher | worker | tester | reviewer | advisor
Objective: one concrete outcome
Scope: exact files, subsystem, or source set
Relevant context: minimum facts and decisions
Ownership: read-only or exact mutable paths; conflict key
Constraints: preserve unrelated changes, approvals, sandbox, credentials, and external-action boundaries
Deliverable: artifact, patch, findings, or test evidence
Acceptance: observable checks and required commands
Budget: child_count [number], time_budget [bounded duration], token_budget [only if runtime exposes one], validation_budget [checks and one recovery at most]
Stop: return when acceptance is met, or a concise blocker after one recovery attempt
Delegation: do not spawn children; do not broaden scope; report paths, commands, exit codes, evidence, and risks
```

Use fresh context for independent review. Require explorers and researchers to avoid edits. Give workers exact path ownership. Ask for compact reports so the coordinator does not repeatedly replay raw logs or an entire repository.

## Lifecycle and recovery

1. Decide the route once for the current bounded stage and emit at most one compact routing notice.
2. Dispatch ready independent children together only when their boundaries are disjoint.
3. Continue useful non-overlapping local work; do not duplicate a child's assignment.
4. Wait only when a required result is needed. Use bounded waits, not busy polling.
5. Inspect the returned artifact, actual changed paths, terminal status, commands, and acceptance evidence.
6. On a no-op or failure, classify it as scope, reasoning, verification, environment, permission, or authority failure. Narrow and retry once only when that addresses the classified issue.
7. Escalate model/effort only for a demonstrated reasoning or verification failure. Carry the failed check into the next capsule.
8. Stop optional children after required acceptance is proven. For a stuck loop, preserve the current state, classify the failure, and use one bounded fresh takeover before escalating model or effort. Refresh lifecycle state and inspect artifacts; a quiet token stream is not proof of failure and a progress message is not proof of completion. Close/interrupt genuinely running optional children using the available lifecycle tool. Do not claim completed history was deleted.

Never start a second writer on unresolved overlapping paths. Preserve normal approval and sandbox boundaries. A child cannot expand authorization because it has a tool.

## Reporting

When routing matters, keep the notice compact:

`Routing: <direct|delegated> | recommendation: <exact model>/<effort> | observed: <metadata or unavailable> | reason: <one sentence>`

At completion, report the actual route, evidence level, acceptance checks, usage evidence, and remaining uncertainty. Do not claim quota savings, speedup, quality improvement, a model switch, or successful cleanup without corresponding evidence.

If behavioral fit or harness access changed the route, name that factor and
the acceptance evidence it requires. For a UI route, this may be a rendered
browser/device check; for backend work, contracts and error paths; for research,
a dated source ledger; for orchestration, terminal child state and ownership.

For deeper task-specific routing, read [model-routing.md](references/model-routing.md) and [task-routing.md](references/task-routing.md). For usage measurement, coordination economics, and lifecycle details, read [usage-and-agents.md](references/usage-and-agents.md).
