#!/usr/bin/env python3
"""Validate the repository's platform-neutral Agent Skill structure."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
README = ROOT / "README.md"
LICENSE = ROOT / "LICENSE"
EXAMPLE = ROOT / "examples" / "status-report.md"


def fail(message: str) -> None:
    raise SystemExit(f"validation failed: {message}")


def main() -> None:
    for path in (SKILL, README, LICENSE, EXAMPLE):
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}")

    skill = SKILL.read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        fail("SKILL.md must start with YAML front matter")
    front_matter, separator, body = skill[4:].partition("\n---\n")
    if not separator:
        fail("SKILL.md has no closing YAML front matter delimiter")

    name = re.search(r"^name:\s*([^\n]+)$", front_matter, re.MULTILINE)
    description = re.search(r"^description:\s*(.+)$", front_matter, re.MULTILINE)
    if not name or name.group(1).strip() != "task-progress":
        fail("front matter name must be task-progress")
    if not description or len(description.group(1).strip()) < 20:
        fail("front matter description is missing or too short")

    required_sections = (
        "## Core rules",
        "## Checkpoint cadence",
        "## Status report format",
        "## Planning and scope",
        "## Files, tools, and verification",
        "## Blockers and recovery",
        "## Boundaries",
        "## Completion checklist",
    )
    for section in required_sections:
        if section not in body:
            fail(f"missing section: {section}")

    for marker in ("Status: <running | blocked | complete | failed>", "Current phase:", "Changed:", "Next:"):
        if marker not in body:
            fail(f"missing status field: {marker}")

    readme = README.read_text(encoding="utf-8")
    for marker in ("# Task Progress Skill", "## Install", "## Usage", "## Design limits"):
        if marker not in readme:
            fail(f"README is missing: {marker}")

    print("skill structure is valid")


if __name__ == "__main__":
    main()
