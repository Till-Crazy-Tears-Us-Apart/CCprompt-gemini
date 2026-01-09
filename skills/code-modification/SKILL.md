---
name: code-modification
description: Use this skill when modifying, refactoring, or optimizing code. Enforces strict engineering standards and project-specific constraints.
context: fork
input_schema:
  type: object
  properties:
    intent:
      type: string
      description: The goal of the code modification (e.g., "Fix NPE in auth service").
    risk_analysis:
      type: string
      description: Analysis of potential ripple effects, framework integrity (JIT/Numba), and performance risks.
    target_files:
      type: array
      items:
        type: string
      description: List of files targeted for modification.
    call_chain_analysis:
      type: array
      items:
        type: string
      description: Explicit list of upstream callers and downstream dependencies that MUST be checked.
    verification_plan:
      type: string
      description: How you will verify library signatures and framework compatibility (e.g., "Check numba docs", "Verify function signature").
  required:
    - intent
    - risk_analysis
    - target_files
    - call_chain_analysis
    - verification_plan
---

# Code Modification Standards

## 1. Context Awareness Warning (Forked Agent)
**WARNING**: You are running in a **forked context** to ensure objectivity.
*   **Amnesia Risk**: You DO NOT know the full state of the project.
*   **Verification**: You MUST independently discover the call chain and dependencies. Do NOT rely on memory.

---

## 2. Core Engineering Principles (Mandatory)

### 2.1 Data Flow & Hierarchy (Downstream Adapts)
*   **Principle**: Modifications should flow downstream. **Downstream consumers must adapt to upstream changes** (data structures, APIs), unless the upstream itself is buggy.
*   **Action**: Trace the data flow. If you change a core data structure, you MUST update all consumers.

### 2.2 Configuration Over Hardcoding
*   **Principle**: **Avoid hardcoding**. Use constants, config files, or function arguments.
*   **Exception**: If existing mechanisms explicitly prevent configuration (rare), you MUST inform the user before proceeding.

### 2.3 Framework Integrity (Numba, JIT, Decorators)
*   **Principle**: **Do NOT break cross-file frameworks**.
    *   **Numba/JIT**: Ensure all utilized Python features are supported by the compiler (nopython mode).
    *   **Decorators**: Respect existing metaprogramming patterns.
*   **Check**: If modifying a JIT-compiled function, verify compatibility with the specific Numba version in use.

### 2.4 Performance & Resource Management
*   **Principle**: **Do NOT degrade performance**.
    *   **Optimized Code**: Respect existing optimizations (numpy vectorization, memory views, JAX arrays).
    *   **Action**: If a change might introduce overhead (e.g., converting a view to a copy, breaking a loop fusion), you MUST justify it or find an alternative.

### 2.5 Strict Library Verification (No Assumptions)
*   **Principle**: **Verify, Don't Guess**.
    *   **Ban**: Do not assume a function exists or has a specific signature just because it "should".
    *   **Action**: You MUST read the library code (if local) or use `context7` / documentation tools to verify signatures before writing code.

### 2.6 Incremental & Modular Change
*   **Principle**: **Minimize Blast Radius**.
    *   **Strategy**: Use incremental, additive changes where possible. Avoid "Big Bang" rewrites.
    *   **Override Protocol**: If a total rewrite/override is necessary, you MUST **PAUSE** and explicitly ask for user permission, explaining why incremental change is impossible.

### 2.7 Ripple Effect & Minimalism
*   **Principle**: **Global Consistency & Minimal Noise**.
    *   **Ripple**: Analyze the call chain. Ensure logical consistency across the entire project.
    *   **Minimalism**: Do NOT touch unrelated comments, formatting, whitespace, or variable names. ONLY change what is necessary for the task.

---

## 3. Workflow Protocol

**Phase 1: Discovery & Tracing (Mandatory)**
1.  **Map Dependencies**: Based on your `call_chain_analysis`, use `grep` or `glob` to locate all files that import or call the `target_files`.
2.  **Verify Signatures**: Read the definitions of any external functions you intend to use.

**Phase 2: Framework Compliance Check**
1.  **JIT Check**: If modifying code under `@jit` or `@numba`, verify the new logic is supported in `nopython` mode.
2.  **Array Check**: Ensure `numpy` / `jax` array operations do not trigger unintended copies or device transfers.

**Phase 3: Execution (Read-Plan-Edit)**
1.  **Pre-Read**: Read the file to be edited.
2.  **Edit**: Apply the change.
3.  **Post-Read**: Verify the change was applied correctly.

**Phase 4: Validation**
1.  Run the tests specified in your plan.
