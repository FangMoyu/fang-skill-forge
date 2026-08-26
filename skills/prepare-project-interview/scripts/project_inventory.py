#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import Counter
import json
import os
from pathlib import Path
import re
import sys


IGNORE_DIRS = {
    ".git", ".idea", ".vscode", ".superpowers", "__pycache__",
    "build", "dist", "node_modules", "target", "vendor",
}
LANGUAGES = {
    ".c": "C", ".cpp": "C++", ".cs": "C#", ".go": "Go",
    ".java": "Java", ".js": "JavaScript", ".jsx": "JavaScript",
    ".kt": "Kotlin", ".kts": "Kotlin", ".php": "PHP",
    ".py": "Python", ".rb": "Ruby", ".rs": "Rust",
    ".scala": "Scala", ".sql": "SQL", ".swift": "Swift",
    ".ts": "TypeScript", ".tsx": "TypeScript", ".vue": "Vue",
}
MANIFEST_NAMES = {
    "build.gradle", "build.gradle.kts", "Cargo.toml", "composer.json",
    "go.mod", "package.json", "pom.xml", "pyproject.toml",
    "requirements.txt", "settings.gradle", "settings.gradle.kts",
}
ENTRYPOINT_NAMES = {
    "app.java", "application.java", "main.go", "main.java", "main.kt",
    "main.py", "main.rs", "server.js", "server.ts",
}


def relative_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def safe_relative_subtree(filename: str | None, root: Path) -> str:
    if not filename:
        return "inaccessible"
    path = Path(filename)
    if not path.is_absolute():
        path = root / path
    try:
        relative = path.relative_to(root)
    except ValueError:
        return "inaccessible"
    parts = relative.parts
    if not 1 <= len(parts) <= 3:
        return "inaccessible"
    if any(
        part in {".", ".."}
        or len(part) > 40
        or not re.fullmatch(r"[A-Za-z0-9._-]+", part)
        for part in parts
    ):
        return "inaccessible"
    return Path(*parts).as_posix()


def is_entrypoint(path: Path) -> bool:
    name = path.name.lower()
    return name in ENTRYPOINT_NAMES or name.endswith("application.java")


def is_test(path: Path) -> bool:
    parts = {part.lower() for part in path.parts}
    name = path.name.lower()
    return (
        "test" in parts or "tests" in parts or name.startswith("test_")
        or name.endswith("test.java") or name.endswith("tests.java")
        or name.endswith("_test.go") or name.endswith("_test.py")
        or name.endswith(".test.ts") or name.endswith(".test.tsx")
    )


def is_migration(path: Path) -> bool:
    parts = {part.lower() for part in path.parts}
    return path.suffix.lower() == ".sql" and (
        "migration" in parts or "migrations" in parts
        or path.name.lower().startswith("v")
    )


def collect_inventory(
    project_root: str | Path,
    max_files: int = 20000,
) -> dict[str, object]:
    if max_files < 1:
        raise ValueError("max_files must be positive")
    root = Path(project_root).expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"project root is not a directory: {root}")

    languages: Counter[str] = Counter()
    manifests: list[str] = []
    entrypoints: list[str] = []
    tests: list[str] = []
    migrations: list[str] = []
    warnings: list[str] = []
    file_count = 0
    truncated = False

    try:
        top_level = [
            {"path": child.name, "type": "directory" if child.is_dir() else "file"}
            for child in sorted(root.iterdir(), key=lambda item: item.name.lower())
            if child.name not in IGNORE_DIRS and not child.is_symlink()
        ]
    except OSError as exc:
        top_level = []
        warnings.append(f"unable to list project root ({type(exc).__name__})")

    def on_walk_error(exc: OSError) -> None:
        subtree = safe_relative_subtree(exc.filename, root)
        warnings.append(
            f"unable to traverse subtree: {subtree} ({type(exc).__name__})"
        )
        nonlocal truncated
        truncated = True

    for current, dirnames, filenames in os.walk(
        root, onerror=on_walk_error, followlinks=False
    ):
        dirnames[:] = sorted(name for name in dirnames if name not in IGNORE_DIRS)
        current_path = Path(current)
        for filename in sorted(filenames):
            if file_count >= max_files:
                truncated = True
                break
            path = current_path / filename
            if path.is_symlink():
                continue
            file_count += 1
            relative = relative_posix(path, root)
            language = LANGUAGES.get(path.suffix.lower())
            if language:
                languages[language] += 1
            if path.name in MANIFEST_NAMES:
                manifests.append(relative)
            if is_entrypoint(path):
                entrypoints.append(relative)
            if is_test(Path(relative)):
                tests.append(relative)
            if is_migration(Path(relative)):
                migrations.append(relative)
        if truncated:
            break

    return {
        "schema_version": 1,
        "root": str(root),
        "file_count": file_count,
        "truncated": truncated,
        "languages": dict(sorted(languages.items())),
        "manifests": sorted(manifests),
        "entrypoint_candidates": sorted(entrypoints),
        "test_candidates": sorted(tests),
        "migration_candidates": sorted(migrations),
        "top_level": top_level,
        "warnings": warnings,
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a read-only structural inventory of a source repository."
    )
    parser.add_argument("project_root")
    parser.add_argument("--max-files", type=int, default=20000)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        inventory = collect_inventory(args.project_root, args.max_files)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(inventory, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

