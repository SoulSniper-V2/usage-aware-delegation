#!/usr/bin/env python3
"""Dependency-free contract checks for the published skill package."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "usage-aware-delegation"


def check(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []

    required = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "CONTRIBUTING.md",
        ROOT / "CHANGELOG.md",
        ROOT / ".gitignore",
        ROOT / ".github" / "workflows" / "validate.yml",
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        SKILL / "references" / "model-routing.md",
        SKILL / "references" / "task-routing.md",
        SKILL / "references" / "usage-and-agents.md",
    ]
    for path in required:
        check(path.is_file(), f"missing required file: {path.relative_to(ROOT)}", failures)

    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8") if (SKILL / "SKILL.md").is_file() else ""
    check(skill_text.startswith("---\n"), "SKILL.md must start with YAML frontmatter", failures)
    closing = skill_text.find("\n---", 4)
    check(closing != -1, "SKILL.md must have a closing frontmatter delimiter", failures)

    frontmatter = skill_text[4:closing] if closing != -1 else ""
    frontmatter_values: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if ":" in line and not line[:1].isspace():
            key, value = line.split(":", 1)
            frontmatter_values[key.strip()] = value.strip().strip('"')

    check(
        frontmatter_values.get("name") == "usage-aware-delegation",
        "frontmatter name must be usage-aware-delegation",
        failures,
    )
    description = frontmatter_values.get("description", "")
    check(bool(description), "frontmatter description must be present", failures)
    check(len(description) <= 1024, "frontmatter description must be at most 1024 characters", failures)

    agent_text = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8") if (SKILL / "agents" / "openai.yaml").is_file() else ""
    check("display_name:" in agent_text, "agents/openai.yaml needs display_name", failures)
    check("short_description:" in agent_text, "agents/openai.yaml needs short_description", failures)
    check("allow_implicit_invocation: true" in agent_text, "implicit invocation must be explicitly enabled", failures)

    for target in re.findall(r"\]\(([^)]+)\)", skill_text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        check((SKILL / target).resolve().is_file(), f"broken skill link: {target}", failures)

    check("/Users/" not in skill_text, "SKILL.md must not contain a machine-specific /Users path", failures)
    check("credential" in skill_text.lower(), "skill should state its credential boundary", failures)
    check("external actions" in skill_text.lower(), "skill should state its external-action boundary", failures)
    check("Behavioral and harness fit" in skill_text, "skill should cover behavioral and harness fit", failures)
    check("task-routing.md" in skill_text, "skill should link task-routing.md", failures)
    task_text = (SKILL / "references" / "task-routing.md").read_text(encoding="utf-8") if (SKILL / "references" / "task-routing.md").is_file() else ""
    for phrase in (
        "Model versus harness",
        "Task-shape matrix",
        "Stuck-loop fresh takeover",
        "completion events",
    ):
        check(phrase.lower() in task_text.lower(), f"task-routing.md missing required concept: {phrase}", failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print("usage-aware-delegation contract: PASS")
    print(f"checked {len(required)} required files and canonical skill links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
