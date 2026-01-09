---
name: debug-protocol
description: Use this skill for diagnosing errors, analyzing test failures, and fixing bugs. Enforces a rigorous scientific method.
context: fork
input_schema:
  type: object
  properties:
    hypothesis:
      type: string
      description: A specific, falsifiable hypothesis about the bug's root cause.
    test_case:
      type: string
      description: The specific test case or reproduction step that fails.
    required_context:
      type: array
      items:
        type: string
      description: List of files or docs that MUST be read to establish ground truth (e.g., library docs, upstream caller).
  required:
    - hypothesis
    - test_case
---

# Debugging & Testing Protocols

## 1. Context Awareness & Verification (Forked Agent)
**WARNING**: You are running in a **forked context** to ensure objectivity.

### 1.1 Anti-Hallucination Protocol
*   **Assumption Ban**: You DO NOT have access to the full conversation history. You DO NOT know the state of the code.
*   **Verification**: You **MUST** read the code and documentation (using `Read` or `context7`) to verify every assumption.
    *   *Example*: "I assume `func_a` returns an int" -> **WRONG**.
    *   *Correction*: "I will read `func_a` to verify its return type."
*   **Dependency Check**: If your hypothesis involves a library or framework (e.g., Numba), you MUST verify its specific constraints/docs first.

---

## 2. Core Philosophy
*   **Test Integrity**: The source code is the primary suspect. Question the test only with strong evidence.
*   **Hypothesis-Driven**: Form a falsifiable hypothesis before changing code.
*   **No Whack-a-Mole**: Do not blindly try fixes.

---

## 3. Debug Probe Lifecycle (Mandatory 6-Step)

**Core Principle**: A debug probe (print/log) is the bridge between hypothesis and fix. It must **NOT** be removed until the fix is verified by the full test suite.

**Mandatory Workflow**:
1.  **Insert**: Based on your explicit `hypothesis`, insert a probe to gather evidence.
2.  **Observe**: Run the `test_case`. Analyze the probe's output.
    *   *Requirement*: Explicitly state how the output supports or refutes your hypothesis.
3.  **Fix**: Implement the fix *while keeping the probe*.
4.  **Verify**: Rerun the `test_case` *with the probe* to verify the fix.
    *   *Requirement*: Use the probe's new output to prove the fix worked.
5.  **Confirm**: Run the full test suite (or at least all related tests) to check for regressions.
6.  **Clean Up**: Remove the probe ONLY after Step 5 passes.

---

## 4. Diagnostic Escalation Protocol

**Trigger**: Two consecutive runs yield the exact same error output.

**Action (Stop-Look-Think)**:
1.  **Stop**: Do NOT try a different code fix immediately.
2.  **Escalate**: Admit information is insufficient. The only valid move is to add *more* probes or use a debugger.
3.  **Refine**: Form a new, more specific hypothesis based on the lack of change.
4.  **Iterate**: Rerun to gather *new* evidence, not to hope for a pass.

---

## 5. Testing Strategy
*   **Phase 1 (Fast)**: Run specific relevant tests (the `test_case`).
*   **Phase 2 (Gate)**: Run full suite (`pytest`) before declaring victory.
*   **Pytest Verbosity**: On first run, ask user if they want `-v` or `--tb=long`.
