#!/usr/bin/env python3
"""Validate this repository as a Codex Agent Skill.

Uses only the Python standard library.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"

REQUIRED = [
    SKILL,
    ROOT / "README.md",
    ROOT / "NOTICE.md",
    ROOT / "agents" / "openai.yaml",
    ROOT / "references" / "source_notes.md",
    ROOT / "references" / "book_coverage_matrix.md",
    ROOT / "tests" / "eval_cases.md",
]

FORBIDDEN_SUFFIXES = {".pdf", ".epub", ".mobi", ".azw", ".azw3"}
PATH_PATTERN = re.compile(
    r"`((?:references|scripts|agents|tests)/[^`\n]+)`"
)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter is not closed")

    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, text[end + 5 :]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for path in REQUIRED:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    if not SKILL.is_file():
        for message in errors:
            print(f"ERROR: {message}", file=sys.stderr)
        return 1

    try:
        skill_text = SKILL.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(skill_text)
    except (UnicodeDecodeError, ValueError) as exc:
        errors.append(str(exc))
        meta, body, skill_text = {}, "", ""

    for key in ("name", "description"):
        if not meta.get(key):
            errors.append(f"frontmatter is missing {key!r}")

    name = meta.get("name", "")
    if name and not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
        errors.append(
            "frontmatter name must contain lowercase letters, digits, and hyphens"
        )

    description = meta.get("description", "")
    if len(description) > 600:
        warnings.append(
            f"description is {len(description)} characters; keep it concise for triggering"
        )
    if body and len(body.strip()) < 500:
        errors.append("SKILL.md body is unexpectedly short")

    for raw_path in PATH_PATTERN.findall(skill_text):
        path_text = raw_path.rstrip(".,;:")
        target = ROOT / path_text
        if not target.exists():
            errors.append(f"SKILL.md references missing path: {path_text}")

    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if ".git" in rel.parts:
            continue

        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden source format committed: {rel}")

        if path.suffix.lower() in {".md", ".yaml", ".yml", ".py", ".txt", ".sh"}:
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                errors.append(f"not valid UTF-8: {rel}")
                continue
            if "\x00" in content:
                errors.append(f"NUL byte found in text file: {rel}")

    yaml_path = ROOT / "agents" / "openai.yaml"
    if yaml_path.is_file():
        yaml_text = yaml_path.read_text(encoding="utf-8")
        for token in ("interface:", "display_name:", "short_description:"):
            if token not in yaml_text:
                errors.append(f"agents/openai.yaml is missing {token!r}")

    if errors:
        for message in errors:
            print(f"ERROR: {message}", file=sys.stderr)
        for message in warnings:
            print(f"WARNING: {message}")
        print(f"\nValidation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    for message in warnings:
        print(f"WARNING: {message}")
    file_count = sum(1 for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts)
    print("Validation passed.")
    print(f"Skill name: {name}")
    print(f"Files checked: {file_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
