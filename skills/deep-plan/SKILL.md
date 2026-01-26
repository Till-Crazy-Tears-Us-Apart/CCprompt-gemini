---
name: deep-plan
description: Use when an implementation plan is proposed but requires a deep architectural audit for risks, side effects, and ambiguities before writing any code.
allowed-tools: Read, Grep, Glob, Bash
argument-hint: "[plan_summary (optional)]"
disable-model-invocation: true
---

# Deep Plan Audit Protocol

This skill enforces a rigorous **Zero-Decision** pre-implementation review. It follows a strict **Decision-First** logic: resolve ambiguities -> define invariants -> audit logic -> verify physical changes.

## 1. Execution Context
**Goal**: Eliminate ALL ambiguity and architectural risk before a single line of code is written.

## 2. Context Saturation & Interactive Ambiguity Resolution (Mandatory)

**Step 1: Active Context Saturation (Pre-Flight)**
Before identifying ambiguities, you MUST verify your knowledge completeness.
1.  **Self-Correction**: Ask "Do I have the *source definition* of every dependency involved?"
2.  **Recursive Read**: If you only see usages (e.g., `db.connect()`), you MUST read the definition (e.g., `class DBConnection`).
3.  **No Hallucinations**: You are FORBIDDEN from assuming implementation details (e.g., "It likely uses requests") without evidence.
4.  **Action**: Use `Read`, `Grep`, or `Glob` to saturate your context.

**Step 2: Recursive Ambiguity Elimination (Loop-Until-Saturated)**
You MUST execute the following loop until NO ambiguities remain:

1.  **Scan**: Identify current architectural decision points based on *saturated* context.
2.  **Check**: Are there unresolved ambiguities?
    *   **NO**: Break loop and proceed to "Step 3: Finalize".
    *   **YES**: Continue to next sub-step.
3.  **Ask**: Use `AskUserQuestion` to resolve *current layer* ambiguities.
    *   **Multi-Question Batching**: Present all currently visible ambiguities.
    *   **Language**: Simplified Chinese (简体中文).
    *   **Format**: Short header, reasonable options, recommended option marked.
4.  **Saturate (Again) - ACTION REQUIRED**:
    *   **Trigger**: Immediately upon receiving the user's choice.
    *   **Mandate**: You **MUST** invoke `Grep`/`Glob` targeting the specific keywords of the choice (e.g., if user selected "Redis", grep for "redis", "cache", "sentinel").
    *   **Read**: You **MUST** read any newly discovered configuration/utility files.
    *   **Blocker**: Do NOT proceed to Step 5 until these new tool outputs are visible in the context.
5.  **Repeat**: Go back to sub-step 1.

**Step 3: Finalize (Load Templates)**
Only when the loop terminates (ZERO ambiguities remain):
1.  **Action**: You **MUST** use the `Read` tool to read the template file: `skills/deep-plan/audit_template.md`.
2.  **Instruction**: Use the content of that file to structure your final report.

## 3. Analysis Output (Deferred Loading)

**CRITICAL CONSTRAINT**: You DO NOT have the output schema yet. You MUST read `skills/deep-plan/audit_template.md` in Step 3 to get it.

*   **Prohibition**: Do NOT invent your own tables.
*   **Prohibition**: Do NOT "guess" the schema.
*   **Requirement**: Use `Read` to load the schema dynamically ONLY after ambiguities are resolved.

## 4. Strict Schema Compliance (Implicit)

You MUST read `~/.claude/skills/deep-plan/output_schema.json` (if available) to understand the required verification depth.

## 5. Critical Rules
1.  **Stop & Think**: Do not generate this report if you haven't read the relevant files yet. Read them first.
2.  **Be Harsh**: The goal is to find problems, not to validate the plan. Play the "Devil's Advocate".
3.  **No Code Generation**: This step is pure analysis. Do not write implementation code here.

## 6. Explicit Stop Protocol (MANDATORY)
**CRITICAL**: You MUST generate ALL tables and analysis text in your response.

**After generating the analysis tables (loaded from template), you MUST STOP.**
1.  Do **NOT** write any code.
2.  Do **NOT** apply any changes.
3.  Do **NOT** use the `AskUserQuestion` tool.
4.  Ends your response with a clear text question to the user:
    > "审计完成 (Audit Complete). [🟢开始执行 (Proceed)] / [🟡修改计划 (Revise)] / [🔴取消 (Cancel)]?"
