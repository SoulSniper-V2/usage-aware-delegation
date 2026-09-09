# Usage-aware delegation

[![Validate](https://github.com/SoulSniper-V2/usage-aware-delegation/actions/workflows/validate.yml/badge.svg)](https://github.com/SoulSniper-V2/usage-aware-delegation/actions/workflows/validate.yml)

Route substantial Codex work between direct execution and bounded native sub-agents using model capability, reasoning effort, plan pressure, runtime capacity, and verification needs.

This is a community-maintained Codex skill. It is a policy layer, not a new model, agent runner, quota meter, or replacement for user approval.

## Why this exists

Delegation is useful when a child has a genuinely independent objective, a better model fit, or safe parallel work. It is wasteful when a task is tiny, tightly coupled, approval-bound, or easier to finish directly.

Usage-aware delegation gives Codex a repeatable decision policy:

- keep questions, tiny edits, and tightly coupled sequences direct;
- delegate only when model-fit or independent overlap repays startup and coordination cost;
- resolve capability aliases against the models the current runtime actually exposes;
- choose reasoning effort from task evidence instead of treating max as a default;
- reduce optional workers and reviews when observed plan pressure is high;
- keep architecture, approvals, credentials, integration, conflicts, and final verification with the coordinator;
- distinguish a recommended route from a child that was actually dispatched, observed, and verified.

## Quick start

After installation, start a new Codex turn or session so the skill catalog refreshes.

Use it explicitly when you want to see the policy applied:

    Use $usage-aware-delegation. Inspect this repository, then choose a direct or bounded delegated route. Keep the final integration and verification with me.

It can also be invoked implicitly when the current Codex runtime honors the included agent metadata.

## Install

### Codex built-in installer

From a Codex session, invoke the built-in $skill-installer skill and provide this GitHub tree URL:

    https://github.com/SoulSniper-V2/usage-aware-delegation/tree/main/skills/usage-aware-delegation

### GitHub CLI

With a recent GitHub CLI that supports skills:

    gh skill install SoulSniper-V2/usage-aware-delegation usage-aware-delegation

### Skills CLI

The Vercel Skills CLI can install the canonical skill directory for Codex:

    npx skills add SoulSniper-V2/usage-aware-delegation --skill usage-aware-delegation -a codex -g

Use project scope instead of -g when the skill should live only in the current repository.

### Manual copy

Clone the repository and copy the canonical skill directory into the configured Codex skills directory. If the installation uses a non-default CODEX_HOME, use that directory instead of ~/.codex.

    git clone https://github.com/SoulSniper-V2/usage-aware-delegation.git
    mkdir -p ~/.codex/skills
    cp -R usage-aware-delegation/skills/usage-aware-delegation ~/.codex/skills/usage-aware-delegation

## How it routes work

The policy evaluates the request in this order:

1. Honor the user's explicit direct-work, model, effort, and delegation choices.
2. Preserve safety, sandbox, approval, credential, privacy, and external-action boundaries.
3. Follow repository instructions and custom-agent configuration.
4. Observe the runtime's actual model catalog, supported efforts, native lifecycle tools, capacity, and usage signals.
5. Apply task evidence and coordination economics.
6. Use benchmarks and community reports only as supporting priors.

The central gate is simple:

    Delegate only when model-fit or independent-overlap benefit clearly exceeds startup,
    context transfer, supervision, aggregation, review, and likely rework cost.

Direct tool/process concurrency is preferred for independent safe commands. Semantic dependencies, overlapping writes, builds, simulators, devices, approvals, Git mutations, deployments, uploads, submissions, messages, and other external effects remain serial.

## Model and effort policy

The skill uses capability aliases rather than hard-coding a model name:

| Alias | Use for | Current-family prior when available |
| --- | --- | --- |
| frontier | Ambiguity, novelty, high consequence, long coherent reasoning, or independent review | strongest available model, such as GPT-6 Astra |
| balanced | Complex implementation, cross-file synthesis, debugging, and quality-sensitive normal work | strong general model, such as GPT-5.6 Sol |
| economy | Bounded exploration, extraction, testing, and repeatable low-consequence work | fast lower-cost model, such as GPT-5.6 Luna |

GPT-5.6 Terra is a useful latency/read-heavy option when the runtime exposes it. These are routing priors, not promises that a model is available or entitled on a particular plan. The skill resolves aliases against the live catalog and records the actual route when the runtime reports it.

Reasoning effort follows the smallest sufficient setting:

| Effort | Default use |
| --- | --- |
| low | Tiny work or an explicit speed/compatibility request |
| medium | Meaningful bounded work and ordinary implementation |
| high | Difficult, coupled, consequential, or verification-heavy work |
| xhigh | Broad evidence coverage after the task boundary is sound |
| max | Bounded deep work with deterministic verification and an accepted token/latency budget |
| ultra | Never automatic; only when the user explicitly chooses the native runtime semantics |

Luna max means the Luna model with max reasoning effort. It is not a separate model.

## Plan pressure

Plan usage is shared and task-dependent. When a runtime exposes account-wide usage percentages, the skill treats them as a signal rather than a turn counter or token-to-quota formula:

| Pressure | Routing adjustment |
| --- | --- |
| ample | Normal benefit gate; up to two children when the work clearly repays it |
| watch | Direct by default; one child for clear overlap or model fit; skip optional review |
| conserve | Direct unless delegation avoids likely expensive failure; one narrow economy child at most |
| exhausted | Continue locally if possible; stop optional work; never reset or purchase automatically |
| unknown | Direct by default; one child maximum only with a strong benefit case |

The skill never invents remaining turns, treats unknown usage as zero, or silently spends reset credits.

## Roles and lifecycle

Children receive a compact contract with:

- one objective and exact scope;
- read-only or disjoint ownership;
- relevant context without a full transcript replay;
- observable acceptance checks;
- separate child-count, wall-time, token, and validation budgets;
- a no-recursion rule and a stop condition.

Supported roles are explorer, researcher, worker, tester, reviewer, and advisor. The coordinator inspects returned artifacts, changed paths, commands, exit codes, and terminal status. A child report is not proof that a patch or test passed.

On a no-op or failure, the coordinator classifies the problem as scope, reasoning, verification, environment, permission, or authority failure. It narrows and retries at most once when that addresses the classified issue. It escalates model or effort only for demonstrated reasoning or verification failure; missing credentials or dependencies are not model evidence.

## Safety boundaries

This skill does not:

- silently switch the active conversation's model or effort;
- edit global Codex configuration as a hidden side effect;
- bypass approvals, sandbox restrictions, credentials, or repository instructions;
- retrieve or disclose passwords, cookies, API keys, MFA codes, or private session data;
- purchase or redeem credits, reset quotas, or claim quota savings;
- authorize a child to post, send, submit, deploy, upload, delete, or contact anyone without user authorization;
- use a recommendation as proof of actual model execution;
- allow recursive workers, overlapping writers, or an always-on companion by default.

An explicit user choice wins when it is available and safe. If the runtime requires inherited child settings, the skill labels the choice as recommended rather than claiming an override was observed.

## Routing notice and evidence levels

When routing materially affects the task, the skill can emit a compact notice:

    Routing: delegated | recommendation: exact-model/effort | observed: metadata or unavailable | reason: one sentence

It distinguishes these states:

| State | Meaning |
| --- | --- |
| recommended | The policy selected a route |
| configured | A runtime or project setting supports it |
| dispatched | The native tool accepted a child |
| observed | Runtime returned model, effort, and terminal status |
| verified | Artifact, scope, and acceptance checks passed |
| blocked | Required capability, artifact, permission, or acceptance evidence is missing |

## Repository layout

    .
    ├── skills/
    │   └── usage-aware-delegation/
    │       ├── SKILL.md
    │       ├── agents/
    │       │   └── openai.yaml
    │       └── references/
    │           ├── model-routing.md
    │           └── usage-and-agents.md
    ├── tests/
    │   └── test_skill_contract.py
    ├── .github/
    │   └── workflows/
    │       └── validate.yml
    ├── CHANGELOG.md
    ├── CONTRIBUTING.md
    ├── LICENSE
    └── README.md

The skill directory is the source of truth. The root README explains the package to humans; it is intentionally not duplicated inside the skill directory.

## Validate locally

The contract test uses only the Python standard library:

    python3 tests/test_skill_contract.py

When the Codex skill creator is installed, also run its validator against the canonical directory:

    python3 /path/to/codex/skills/.system/skill-creator/scripts/quick_validate.py skills/usage-aware-delegation

For a clean contribution, check the patch itself:

    git diff --check

## Contributing

Read CONTRIBUTING.md before opening a pull request. Keep policy changes small and explain the evidence behind new routing rules. Model names, plan behavior, usage limits, and native tool schemas can change; verify current first-party documentation before turning a current model into a hard-coded requirement.

Please preserve the distinction between:

- a policy recommendation and an observed runtime route;
- account-wide usage telemetry and this task's actual cost;
- a benchmark or community report and a verified Codex result;
- a missing dependency or permission and a model capability failure.

## Versioning

Releases use a lightweight semantic-versioning convention. Bump the version in CHANGELOG.md when the routing contract or installation surface changes, and describe any behavior that could change child count, model selection, effort, usage pressure, or external-action boundaries.

## Current references

The default policy is informed by the current Codex documentation for [sub-agents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [plan pricing and usage](https://learn.chatgpt.com/docs/pricing), [reasoning effort](https://developers.openai.com/api/docs/guides/reasoning), and model references for [GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra), [GPT-5.6 Sol](https://developers.openai.com/api/docs/models/gpt-5.6-sol), [GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra), and [GPT-5.6 Luna](https://developers.openai.com/api/docs/models/gpt-5.6-luna). Re-check those sources before relying on current availability, pricing, or limits.

This project is not affiliated with or endorsed by OpenAI.

## License

Released under the MIT License. See LICENSE.
