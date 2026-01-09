#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@FileName    : tabu_reminder.py
@Description : A UserPromptSubmit hook to inject core directives and technical constraints.
@Author      : Claude Code
@CreationDate: 2026-01-08
"""

import sys

# Using triple quotes to define the multi-line string for clarity.
REMINDER_TEXT = """<core_directives>
[System Command: STRICT ENFORCEMENT REQUIRED]
---
1. **Tool Execution Protocol**:
   - Execute strictly **SERIALLY** (one by one).
   - Maintain **SILENCE** during tool usage (no intermediate chatter).
   - **Verify First**: Read file before Edit; Check path before Command.
   - **Parameter Integrity**: All multi-word parameters MUST use `snake_case` (e.g., `file_path`, not `file-path`). Check `-` vs `_` carefully.

2. **Communication Discipline**:
   - **Objectivity**: No adjectives, no emotion, no flattery. Facts only.
   - **No Assumption**: Do not assume code works; do not assume user is right.
   - **No Fabrication**: Report truncated stdout truthfully. Monitor Bash timeouts explicitly.

3. **Engineering Mindset**:
   - **Safety**: Do not introduce tech debt to pass tests.
   - **Systemic**: Analyze ripple effects before modifying.

4. **Environment Constraints**:
   - **Shell**: Use POSIX Bash syntax.
   - **Python**: Prepend `export PYTHONIOENCODING="utf-8"` for scripts.
   - **Mamba/Conda**: MUST follow 4-step activation: `source "~/miniforge3/Scripts/activate"` > `eval "$(mamba.exe shell hook --shell=bash)"` > `mamba activate <env>` > `<command>`.
   - **File Paths**: Use relative paths only; avoid absolute paths unless specified.
---
</core_directives>"""

def main():
    """
    Prints the reminder text to stdout, which will be injected into the context
    by the Claude Code hook system for UserPromptSubmit events.
    """
    # Remove leading newline, encode to utf-8, and write to stdout
    sys.stdout.buffer.write(REMINDER_TEXT.lstrip('\n').encode('utf-8'))
    sys.exit(0)

if __name__ == "__main__":
    main()
