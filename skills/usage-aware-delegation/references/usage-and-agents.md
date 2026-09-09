# Usage and agent lifecycle reference

Use this reference when a task is large enough that plan pressure, context replay, worker count, or completion state can change the route.

## What can be measured

Prefer runtime-provided telemetry. When available, capture a before and after snapshot containing:

- plan tier;
- primary/short-window and secondary/weekly used percentages;
- reset timestamp or remaining window, if exposed;
- credit balance/availability, without account identifiers;
- exact model and effort observed on the coordinator and each child;
- child count, terminal state, wall time, changed paths, commands, and exit codes.

Keep the snapshot local to the current task. Do not store account IDs, cookies, API keys, passwords, MFA codes, private prompt text, or raw session logs in a routing ledger. Do not infer actual model use from a model recommendation, a UI label, or aggregate product activity that is not tied to the current dispatch.

If a usage tool is absent, disallowed, or outside the user's scope, mark usage `unknown`. Do not turn unknown into a generous budget. An observed percentage is still account-wide and may include other sessions; describe it as a signal, not an isolated task cost.

## Coordination economics

Estimate the net benefit qualitatively:

```text
net benefit = model-fit or overlap benefit
              - child startup
              - context transfer/replay
              - coordinator supervision
              - aggregation and review
              - likely rework
```

Delegate only when the result is clearly positive. The root often remains active for the entire delegated task, so its turns can dominate plan usage even when workers are inexpensive. A child that writes code can still be a poor route if the coordinator has to reread all of it, repair it, and review it.

Good delegation candidates are:

- independent read-only repository mapping or symbol/test discovery;
- bounded current-doc or compatibility research;
- disjoint implementation slices with clear file ownership;
- a targeted reproduction or test run that does not share mutable build/device state;
- a fresh, read-only review of a high-consequence result.

Poor candidates are:

- one-file changes, short commands, simple answers, and exact edits;
- dependent steps where the child result immediately determines the next local action;
- overlapping writers or shared build/simulator/device state;
- an always-on companion, role queue, or many small status polls;
- delegation used solely to “save tokens” while an expensive coordinator keeps supervising;
- work requiring user approval, credentials, or an external mutation that the user did not authorize.

## Pressure adjustments

Use the most constrained observed window:

| Pressure | Child policy | Effort policy | Review policy |
|---|---|---|---|
| ample | up to two children if the gate clears | medium default; high for task evidence | add when risk justifies |
| watch | zero or one child | medium first; avoid max/frontier unless risk demands it | optional review usually skipped |
| conserve | direct by default; one narrow economy child only for clear benefit | medium or lower supported effort; no automatic frontier escalation | review only for high consequence |
| exhausted | no optional child; continue local or report limit | do not retry quota failure with a stronger model | no optional review |
| unknown | one child maximum and only with a strong gate | medium floor; no quota claims | only when high consequence |

Pressure changes the number of children and optional work before it changes safety requirements. A security or destructive-data task still needs an appropriate capability tier; if that tier is unavailable, report the block instead of silently using an inadequate worker.

## Capsule schema

Use this compact handoff, replacing bracketed fields. Keep child count, wall-clock time, token allowance, and validation/recovery as separate budgets; do not derive a token allowance from a plan percentage:

```text
You are the [role] for the current task.

Objective: [one concrete outcome]
Scope: [exact files/subsystem/source set]
Relevant context: [minimum facts and decisions]
Ownership: [read-only OR exact mutable paths; conflict key]
Constraints: [preserve unrelated changes, approvals, sandbox, credentials, external actions]
Deliverable: [patch/findings/artifact/test evidence]
Acceptance: [observable checks and commands]
Budget: child_count [number]; time_budget [bounded duration]; token_budget [only if runtime exposes one]; validation_budget [checks and one recovery at most]
Stop: return immediately when acceptance is met, or return a concise blocker after the budget.
Delegation: do not spawn children. Do not broaden scope. Report changed paths, commands, exit codes, evidence, and unresolved risks.
```

For a reviewer, set `Ownership: read-only`, require fresh context, and include the exact diff or paths to inspect. For an explorer/researcher, explicitly prohibit edits. For a worker, name each path it may change and require it to preserve all unrelated user changes.

## Native lifecycle

Use the current surface's actual tools; names and schemas vary by release. The usual lifecycle is:

1. check capacity and the current request's child budget;
2. spawn only ready, self-contained children;
3. continue useful non-overlapping local work;
4. wait when a required result is needed, using bounded waits rather than busy polling;
5. inspect the artifact and terminal result;
6. send at most one focused recovery input or continue locally if that will not duplicate work;
7. close completed children when the surface requires it;
8. before final response, refresh status and stop genuinely running optional children that cannot change the result.

Do not treat a pending label, timeout, or stale parent status as proof of failure. Do not interrupt a child that has completed merely to change its display. If lifecycle state cannot be verified, say so.

## Verification levels

Use a compact ledger for each child:

| Field | Meaning |
|---|---|
| `recommended` | policy selected a model/effort |
| `configured` | a runtime/project default supports it |
| `dispatched` | a spawn request was accepted |
| `observed` | model/effort and terminal status came from runtime metadata |
| `artifact` | expected patch/report/test output exists |
| `verified` | acceptance checks passed and scope was reviewed |
| `blocked` | a required capability, artifact, permission, or acceptance check is missing |

Never promote a child from `recommended` to `observed` merely because its role was named. Never promote an agent report to `verified` without inspecting the artifact and evidence.

## Safe recovery

On a no-op, missing artifact, or failed check:

- first classify whether the problem is task scope, model reasoning, verification, environment, permission, or external authority;
- narrow the capsule and retry once only if that can resolve the specific issue;
- escalate effort/model only for a demonstrated reasoning or verification failure;
- fix or report environment/permission/authority gaps without escalating the model;
- stop after the single recovery attempt unless the user explicitly expands the budget.

Do not start a second worker that can edit the same paths while the first is unresolved. Do not hide a partial child result behind a confident final statement.
