#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@FileName    : injector.py
@Description : Centralized manager for injecting references into CLAUDE.md.
               Ensures idempotency and atomic updates.
@Author      : Till-Crazy-Tears-Us-Apart
@CreationDate: 2026-01-26
"""

import sys
import os
import json

CLAUDE_MD = "CLAUDE.md"

# Registry of content to be injected
# Format: { "tag_name": "relative_file_path" }
# The script will inject:
# <tag_name>
# @relative_file_path
# </tag_name>
REGISTRY = {
    "project_structure": ".claude/project_tree.md",
    "history_timeline": ".claude/history/timeline.md",
    "logic_tree": ".claude/logic_tree.md"
}

def inject_all(cwd):
    """Injects all registered references into CLAUDE.md."""
    claude_md_path = os.path.join(cwd, CLAUDE_MD)

    # Policy Check for Logic Index
    # ALWAYS (Default): Inject logic_tree
    # ASK/NEVER: Do not inject logic_tree (unless explicitly forced by environment, currently logic handled by caller)
    # The caller (SKILL) can force injection by setting LOGIC_INDEX_AUTO_INJECT=ALWAYS
    logic_policy = os.environ.get("LOGIC_INDEX_AUTO_INJECT", "ALWAYS")

    # Create local registry copy to modify
    active_registry = REGISTRY.copy()

    if logic_policy != "ALWAYS":
        if "logic_tree" in active_registry:
            del active_registry["logic_tree"]
            # print(f"[Injector] Skipping logic_tree injection (Policy: {logic_policy})")

    # Create CLAUDE.md if not exists
    if not os.path.exists(claude_md_path):
        with open(claude_md_path, 'w', encoding='utf-8') as f:
            f.write("# System Context\n\n")

    with open(claude_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    changes_made = False

    for tag, rel_path in active_registry.items():
        ref_line = f"@{rel_path}"

        # Check if already referenced (either by tag or direct link)
        if ref_line in new_content:
            continue

        # Build block
        # Ensure sufficient padding before the block
        prefix = "\n\n" if not new_content.endswith("\n\n") else ("\n" if not new_content.endswith("\n\n") else "")
        block = f"{prefix}<{tag}>\n\n{ref_line}\n\n</{tag}>\n"

        # Check if tag exists but content is different (simple append for now to be safe)
        if f"<{tag}>" not in new_content:
            new_content += block
            changes_made = True

    if changes_made:
        with open(claude_md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[Injector] Updated {CLAUDE_MD}")
    else:
        print(f"[Injector] No changes needed for {CLAUDE_MD}")

def main():
    # Force UTF-8
    sys.stdout.reconfigure(encoding='utf-8')
    cwd = os.getcwd()
    inject_all(cwd)

if __name__ == "__main__":
    main()
