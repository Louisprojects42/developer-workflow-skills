#!/usr/bin/env python3
"""Bounded filename-only project inventory. Never follows reparse points."""
import argparse
import json
import os
from pathlib import Path
import stat

EXCLUDE = {'.git', '.venv', 'venv', 'node_modules', 'dist', 'build', '.next',
           '__pycache__', '.cache', '.mypy_cache', '.pytest_cache', '.ruff_cache',
           'AppData', '.ssh', '.aws', '.trash', '.obsidian'}
MARKERS = {'package.json', 'pyproject.toml', 'Cargo.toml', 'go.mod', 'pom.xml',
           'build.gradle', 'README.md', 'readme.md', 'AGENTS.md', 'CLAUDE.md',
           'requirements.txt', 'Makefile'}

def linked(path):
    info = path.lstat()
    return stat.S_ISLNK(info.st_mode) or bool(getattr(info, 'st_file_attributes', 0) & 0x400)

def inventory(root, depth=3, max_entries=3000):
    root = Path(root).absolute()
    if depth < 0 or max_entries < 1:
        raise ValueError('depth must be nonnegative and max_entries positive')
    if linked(root) or not root.is_dir():
        raise ValueError('root must be an existing directory, not a link/junction')
    result = {'root':str(root), 'directories':[], 'markers':[], 'warnings':[], 'truncated':False}
    remaining = max_entries
    def walk(folder, level):
        nonlocal remaining
        try:
            entries = []
            with os.scandir(folder) as scan:
                for entry in scan:
                    if remaining <= 0:
                        result['truncated'] = True
                        break
                    remaining -= 1
                    entries.append(Path(entry.path))
            for path in sorted(entries, key=lambda p: p.name.casefold()):
                if path.name in EXCLUDE or path.name.startswith('.env'):
                    continue
                relative = path.relative_to(root).as_posix()
                try:
                    if linked(path):
                        result['warnings'].append({'path':relative,'reason':'link/junction skipped'})
                    elif path.is_dir():
                        result['directories'].append(relative)
                        if level < depth and remaining > 0:
                            walk(path, level + 1)
                        elif level < depth:
                            result['truncated'] = True
                    elif path.name in MARKERS:
                        result['markers'].append(relative)
                except OSError as exc:
                    result['warnings'].append({'path':relative,'reason':type(exc).__name__})
        except OSError as exc:
            result['warnings'].append({'path':folder.relative_to(root).as_posix(),'reason':type(exc).__name__})
    walk(root, 0)
    result['directories'].sort()
    result['markers'].sort()
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root')
    parser.add_argument('--depth', type=int, default=3, help='maximum nested directory levels to inspect')
    parser.add_argument('--max-entries', type=int, default=3000)
    args = parser.parse_args()
    try:
        print(json.dumps(inventory(args.root, args.depth, args.max_entries), indent=2))
    except (OSError, ValueError) as exc:
        parser.exit(2, str(exc) + '\n')
if __name__ == '__main__':
    main()
