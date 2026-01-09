---
name: change-logging
description: Use this skill when completing large-scale edits or when the user requests a change log/summary to facilitate manual context compression.
---

# Change Logging & Context Compression

## 1. Workflow: Compress-Reset-Review
This skill is part of a manual context management strategy designed to handle long sessions.

1.  **Compress**: When context is full or a major milestone is reached, generate a **Change Log** using the template below.
    *   *Goal*: Capture all "state changes" (code modifications, decisions, open issues) in a single file.
2.  **Reset (User Action)**: The user will manually reset the session context.
3.  **Review (User Action)**: The user will instruct the new session to read the generated log.
    *   *Requirement*: The log must be **self-contained**. Do not reference "previous conversation" or "as discussed above".

---

## 2. Change Log Specification

**Action**: Create a markdown file in `temp_log/` (e.g., `temp_log/_temp_refactor_v1.md`).

**Content Template**:

```markdown
# [Change Summary Title]
> Generated for Context Reset on [Date]

## 1. High-Level Summary
*   **Goal**: [What was the primary objective?]
*   **Status**: [Completed / In-Progress / Blocked]
*   **Next Steps**: [What should the next session do immediately?]

## 2. Detailed Modifications
### 2.1 [File Path 1]
*   **Change**: [Description of modification]
*   **Reason**: [Why it was done]
*   **Verification**: [How it was tested (e.g., "Passed test_auth.py")]

### 2.2 [File Path 2]
...

## 3. Critical Context for Next Session
*   **Open Issues**: [Known bugs or unfinished TODOs]
*   **Decisions**: [Key architectural decisions made]
*   **Environment**: [Any new deps installed?]
```

## 3. Constraints
*   **Self-Contained**: Write as if explaining to a new developer who has zero knowledge of the previous chat history.
*   **Objective**: No adjectives ("great", "efficient"). Just facts.
*   **Traceable**: Reference specific file paths and function names.
