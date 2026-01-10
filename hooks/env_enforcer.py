#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@FileName    : env_enforcer.py
@Description : UserPromptSubmit hook that injects CRITICAL environment constraints.
               This acts as a "reminder" to the model before it generates any commands.
@Author      : Till-Crazy-Tears-Us-Apart
@CreationDate: 2026-01-10
"""

import sys

# Using triple quotes to define the multi-line string for clarity.
# Only injecting the critical "Environment Constraints" section to save tokens.
REMINDER_TEXT = """<system_reminder>
[CRITICAL ENVIRONMENT CONSTRAINTS]
1. **Shell**: Use POSIX Bash syntax.
2. **Python**: Prepend `export PYTHONIOENCODING="utf-8"` for ALL scripts.
3. **Mamba/Conda**: MUST follow 4-step activation: `source "~/miniforge3/Scripts/activate"` > `eval "$(mamba.exe shell hook --shell=bash)"` > `mamba activate <env>` > `<command>`.
4. **Paths**: Use relative paths ONLY.
</system_reminder>"""

def main():
    """
    Prints the reminder text to stdout, which will be injected into the context.
    """
    sys.stdout.buffer.write(REMINDER_TEXT.encode('utf-8'))
    sys.exit(0)

if __name__ == "__main__":
    main()
