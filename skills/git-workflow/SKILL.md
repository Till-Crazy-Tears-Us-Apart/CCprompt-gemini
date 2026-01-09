---
name: git-workflow
description: Use this skill for all version control tasks, including committing, branching, pushing, and reviewing history.
input_schema:
  type: object
  properties:
    action:
      type: string
      enum: [commit, push, branch, log, status]
      description: The git operation to perform.
    commit_type:
      type: string
      enum: [feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert]
      description: The conventional commit type (only for action='commit').
    commit_scope:
      type: string
      description: The scope of the change (e.g., auth, api, ui). Optional.
    commit_message:
      type: string
      description: The concise commit subject (max 50 chars).
  required:
    - action
---

# Git Workflow & Safety Protocols 

## 1. Safety & Confirmation

### 1.1 Dangerous Operations
**Explicit user confirmation is REQUIRED for:**
*   `git commit` (unless user pre-authorized)
*   `git push`
*   `git reset --hard`
*   `git clean -fd`
*   Checking out a different branch (if current has changes)

### 1.2 Command Standards
*   **Atomic Commits**: One logical change per commit.
*   **No Parallel Git**: Git relies on the index lock. Never run multiple git commands in parallel.
*   **Rollback Protocol**: `checkout` rollbacks require confirmation.

---

## 2. Conventional Commits Specification

**Format**: `<type>(<scope>): <subject>`

| Type | Description |
| :--- | :--- |
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only changes |
| `style` | Changes that do not affect the meaning of the code (white-space, formatting, etc) |
| `refactor` | A code change that neither fixes a bug nor adds a feature |
| `perf` | A code change that improves performance |
| `test` | Adding missing tests or correcting existing tests |
| `build` | Changes that affect the build system or external dependencies |
| `ci` | Changes to our CI configuration files and scripts |
| `chore` | Other changes that don't modify src or test files |
| `revert` | Reverts a previous commit |

---

## 3. Branching Strategy
*   **Feature Branches**: `feat/short-description`
*   **Bugfix Branches**: `fix/issue-id-description`
*   **Chore Branches**: `chore/description`
