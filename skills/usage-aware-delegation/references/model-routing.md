# Model routing reference

This reference supports `usage-aware-delegation` when a task needs more detail than the entrypoint. The catalog and plan rules can change; resolve the current runtime first and treat these as policy priors.

## Capability aliases

Do not route by the alias alone. Resolve an alias to an exact model ID from the current Codex model catalog or collaboration-tool schema, then confirm the effort is supported.

| Alias | Select when | Current-family prior when available |
|---|---|---|
| `frontier` | ambiguity, novelty, high consequence, long coherent reasoning, adversarial or independent review | strongest available model, such as Astra |
| `balanced` | difficult normal implementation, cross-file synthesis, broad debugging, read-heavy work where quality matters | strong general model, such as Sol; Terra can be the latency/read-heavy choice |
| `economy` | mechanical, repeatable, bounded exploration, extraction, testing, or low-consequence implementation | fast lower-cost model, such as Luna |

The prior is not a promise that a named model exists or is entitled to the user. If the preferred family is unavailable, use the fallback graph below and record the actual route.

## Routing matrix

| Task evidence | First choice | Second choice | Keep local when |
|---|---|---|---|
| exact one-file edit or established repeated pattern | economy/medium | economy/low on explicit speed request | child startup or context transfer exceeds the work |
| clear bounded implementation with deterministic tests | economy/high | balanced/medium | the change is tightly coupled to the coordinator's next judgment |
| large read-only inventory, extraction, or test discovery | economy/medium | economy/xhigh for broad coverage | the result is needed immediately for the next local command |
| current docs/version/source lookup | economy/medium | balanced/medium for synthesis or contradictions | lookup is one or two direct reads |
| explicit fast ordinary implementation | balanced/medium or catalog fast tier | economy/high | latency is not actually the user's priority |
| stable cross-file feature | balanced/medium | economy/high if bounded and well-tested | architecture is still being decided |
| unknown cross-system bug | balanced/high | frontier/medium | the blocker is missing access, dependency, or authority |
| architecture, security, auth, privacy, payments, destructive migration | frontier/medium | balanced/high plus independent frontier review | requirements or authority are unresolved |
| high-risk independent review | frontier/medium, fresh context | balanced/high | the work is cosmetic, deterministic, and low consequence |
| low-consequence deep deterministic scan or implementation | economy/xhigh or economy/max | balanced/medium | max would expand the work beyond the acceptance boundary |

## Effort ladder

Use the lowest effort that is sufficient for the evidence. Effort labels are relative to each model, not a shared IQ scale.

| Effort | Policy |
|---|---|
| `low` | explicit speed/compatibility request or tiny work; do not make it the automatic default for meaningful work |
| `medium` | default for real bounded work and ordinary implementation |
| `high` | difficult bounded reasoning, high coupling, consequence, or verification |
| `xhigh` | broad evidence coverage or a classified failure after the scope was already sound |
| `max` | bounded deep work with deterministic verification and an accepted latency/token budget |
| `ultra` | never automatic; only explicit user choice and no stacked skill-managed delegation |

Increase effort before changing model when the current model is adequate and the task boundary is sound. Change model when the task's ambiguity, coupling, consequence, or verification needs exceed the tier. Do not use max or a frontier model to compensate for ambiguous requirements, missing files, absent credentials, unavailable dependencies, or blocked permissions.

## Fallback graph

Preserve intent instead of preserving an effort label:

```text
frontier/medium or high -> balanced/high or medium
balanced/high          -> frontier/medium for consequence, economy/xhigh for bounded coverage
balanced/medium        -> economy/high for bounded work, frontier/medium for ambiguity
economy/max            -> balanced/medium
economy/xhigh          -> economy/high or balanced/medium
economy/high           -> economy/medium, then balanced/medium if evidence requires
balanced/low           -> economy/medium unless low was explicitly required
```

The exact fallback must be selected from the current catalog. If no suitable model/effort is available, continue locally or report the block; do not invent a model ID or silently downgrade a user-required route.

## Override handling

An explicit user model or effort choice is a hard preference subject to availability and safety. Project instructions and custom-agent configuration are next. Automatic policy is last.

The active conversation's model/effort cannot be changed by this skill. A child override is valid only when the native spawn surface accepts the exact fields and its current tool instructions permit them. If the tool inherits the parent, send the child with inherited settings and report `recommended` versus `observed` separately.

`Luna max` is the Luna model with `max` reasoning. There is no implied separate “Luna Max” model. `Ultra` may include platform-managed delegation; automatic policy must not stack another layer on it.

## Source anchors

Use current first-party documentation before making a claim about availability or pricing:

- [Codex sub-agents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Codex pricing](https://learn.chatgpt.com/docs/pricing)
- [Codex configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Reasoning guide](https://developers.openai.com/api/docs/guides/reasoning)
- [Astra prompting and latest-model guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra)
- [Astra model reference](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [Sol model reference](https://developers.openai.com/api/docs/models/gpt-5.6-sol)
- [Terra model reference](https://developers.openai.com/api/docs/models/gpt-5.6-terra)
- [Luna model reference](https://developers.openai.com/api/docs/models/gpt-5.6-luna)

Community and GitHub sources are supporting evidence only. Do not use a benchmark score, repository star count, Reddit report, or X post as proof that a route is available, cheaper on a plan, faster in Codex, or correct for the current task.
