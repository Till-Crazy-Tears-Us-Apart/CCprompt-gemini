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
2. **Environment Safety**: Python encoding and Mamba/Conda activation are handled AUTOMATICALLY by hooks. Do NOT manually inject them unless overriding.
3. **Paths**: Use relative paths ONLY.
4. **Behavior**: SILENT EXECUTION. No text between tool calls.
5. **Workflow**: Read-only -> Direct Act. Modification -> Plan & MUST use AskUserQuestion -> Silent Act.
6. **Protocol**: PROTOCOL COMMITMENT header MUST ONLY appear at the start of a SUBSTANTIVE text response.
</system_reminder>"""

def main():
    """
    Prints the reminder text to stdout, which will be injected into the context.
    """
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        # Python < 3.7 or safe fallback
        pass

    sys.stdout.buffer.write(REMINDER_TEXT.encode('utf-8'))
    sys.exit(0)

if __name__ == "__main__":
    main()
