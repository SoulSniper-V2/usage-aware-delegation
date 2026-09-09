# Task routing and acceptance

Use this reference when the task's shape, user-visible quality, or runtime
harness matters more than a simple model-capability choice. It complements
model-routing.md; it does not replace runtime discovery or the direct-versus-
delegated benefit gate.

## Model fit is behavioral fit

Do not reduce model choice to a single intelligence or price ranking. Look for
observable fit along the axes that matter to the task:

- instruction following and intent preservation;
- long-task coherence and resistance to scope drift;
- decomposition and handoff quality;
- visual taste, layout judgment, and product sensitivity;
- vision, browser, GUI, 3D, or computer-use ability;
- tool selection, source discipline, and error recovery;
- verification quality, including knowing when a result is actually complete;
- latency, context use, and expected coordination cost.

These are priors until the current runtime or a controlled task comparison
shows otherwise. A public post, benchmark, or model label is not proof of
behavior in the current harness.

## Model versus harness

Evaluate the model and the harness separately. A harness may change:

- which files, tools, browsers, devices, worktrees, or services are available;
- how context, repository instructions, and agent configuration are supplied;
- whether subagents can be spawned, overridden, waited on, steered, or closed;
- whether approvals, sandboxing, credentials, and external actions are gated;
- whether progress, tool calls, artifacts, and terminal state are observable;
- whether the final result can be rendered, tested, deployed, or reviewed.

If a task fails because a dependency, permission, credential, tool, or external
authority is missing, classify that as environment or authority failure. Do not
escalate the model to compensate. If the task needs a capability the harness
does not expose, report the limitation and keep the safest useful route.

## Task-shape matrix

| Work shape | Route prior | Acceptance and verification |
| --- | --- | --- |
| Frontend, UI, design, 3D, or computer use | Balanced or frontier when visual judgment, ambiguity, or consequence is high; economy for mechanical changes | Inspect the rendered/browser/device result, interaction states, responsive behavior, accessibility, long content, and error/empty/loading states. |
| Backend, API, integrations, or data flow | Balanced/medium or high; frontier for architecture, auth, security, payments, destructive migration, or production-critical decisions | Run deterministic tests and contracts; exercise errors, retries, idempotency, auth/privacy, pagination, and integration behavior. |
| Deep research or planning | Economy/medium for bounded collection; balanced/high for synthesis; frontier when sources conflict or the decision is consequential | Keep a source ledger with URL, date/version, direct support, contradiction, confidence, and acceptance criteria. Do not turn a plan into proof of implementation. |
| Mechanical, repetitive, or exact inventory | Economy/medium or high; direct if tiny | Check the exact diff, count, formatter, generated output, or focused test. |
| Unknown cross-system debugging | Balanced/high; frontier only after a classified reasoning or verification failure | Reproduce the issue, record root-cause evidence, separate environment from reasoning, and add a regression check when possible. |
| High-consequence independent review | Fresh read-only frontier or balanced/high when the risk justifies its cost | Require findings tied to paths or behavior, severity, reproduction or evidence, and explicit missing-test notes. |
| Orchestration and decomposition | A model with demonstrated decomposition fit plus a harness with lifecycle and tool observability | Require one contract per child, ownership, stop conditions, terminal events, compact reports, aggregation, and final coordinator integration. |

The matrix is a starting point, not a mandatory phase map. A frontend task may
need a research child; a backend task may need a visual admin-console check; a
research task may be best handled directly when only two primary pages need to
be read.

## Useful workflow patterns

### Builder plus independent reviewer

Use this for a consequential or visually judgment-heavy change when the review
is likely to prevent expensive rework:

1. Give the builder one owned implementation slice.
2. Give a fresh-context reviewer read-only access to the diff, acceptance
   criteria, and relevant runtime evidence.
3. Keep the reviewer from editing the builder's paths.
4. Have the coordinator inspect both the artifact and the findings before
   integrating or authorizing external effects.

Do not add a reviewer to every tiny change or when pressure is conserve.

### Research to plan to build

Use this sequence when research changes the implementation decision:

1. Gather a bounded source set and record the source ledger.
2. Synthesize a plan with assumptions, contradictions, and acceptance checks.
3. Build only after the coordinator accepts the plan and owns the integration.

If research lanes are independent, direct tool concurrency comes before
reasoning subagents. If the build depends on the research, keep that handoff
serial and compact.

### Build to rendered check

For frontend, UI, 3D, or computer-use work, code completion is not acceptance.
After the build:

- launch the real local surface when possible;
- inspect representative desktop and narrow viewport or device states;
- exercise loading, empty, error, long-content, keyboard/touch, and dark-mode
  states when applicable;
- check visual hierarchy, interaction feedback, contrast, and localization
  resilience;
- record the rendered artifact or a concrete blocker.

Use the model or harness with the relevant vision/tool access, but never treat
that access as proof that the result looks correct.

### Build to tests and contract checks

For backend, API, security, data, and integration work, pair implementation with
deterministic checks:

- unit and contract tests;
- error, retry, timeout, and idempotency behavior;
- auth, privacy, secret, and permission boundaries;
- migrations and rollback or recovery behavior;
- integration or staging evidence when the user authorized it.

Do not let a low-cost worker make unreviewed architecture or security decisions
just because its code passes a shallow happy-path test.

### Stuck-loop fresh takeover

When an agent repeats a failed approach:

1. Capture the failed command, symptom, current branch/worktree, changed paths,
   and prior attempts.
2. Classify the failure as scope, reasoning, verification, environment,
   permission, or authority.
3. Start a fresh, bounded takeover with the failed evidence and one new
   acceptance target.
4. Preserve existing state unless the user explicitly authorizes a destructive
   restart or the repository's normal recovery process does so.
5. Allow one focused recovery attempt. Escalate model or effort only for a
   demonstrated reasoning or verification failure.

“Fresh takeover” means fresh reasoning context, not silently deleting history,
discarding user changes, or granting new permissions.

## Fan-out and long-running work

Increase fan-out only when all of these are observable:

- independent objectives and disjoint writes;
- enough runtime capacity for the requested concurrency;
- progress, child state, and artifacts can be inspected;
- plan pressure is not high or the expected failure avoided is worth the cost;
- each child has a bounded acceptance check and stop condition;
- the coordinator has a concrete aggregation and verification step.

Keep the default low: zero children for small work, one for a material sidecar,
and at most two under ordinary ample pressure. Never create a permanent
companion, waiting queue, or recursive child by default. A native Ultra mode
may own its own delegation semantics; do not stack skill-managed fan-out on it
unless the user explicitly asks.

For long-running work, prefer completion events, artifact checkpoints, and
terminal state over token-stream intuition. A quiet stream does not prove
failure, and a progress message does not prove completion. Refresh lifecycle
state, inspect the artifact, and run the acceptance checks.

## Compact routing checklist

Before dispatching, answer:

1. Is direct execution or direct tool concurrency already sufficient?
2. What behavior or harness capability makes a child better here?
3. Is the child objective self-contained and its ownership disjoint?
4. What exact artifact or test proves acceptance?
5. What are the child-count, wall-time, token, and validation budgets?
6. What happens if it is a no-op, loops, or hits an environment block?
7. Who owns integration, approvals, external actions, and final verification?

If these answers are not concrete, keep the work direct or report that the
required runtime evidence is unavailable.
