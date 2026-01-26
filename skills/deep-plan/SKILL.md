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

**Step 3: Finalize**
Only when the loop terminates (ZERO ambiguities remain), generate the "Analysis Output" tables below.

## 3. Analysis Output (Strict Tables)

You must output your analysis in the following **four** Markdown tables in this exact order. **Add 1 empty line before and after each table.**

### 🧩 Table 1: Ambiguity Resolution Matrix (歧义消除矩阵)

*   **Goal**: Eliminate ALL "TBD" (To Be Determined). Convert options to hard constraints.
*   **Strict Rule**: If technical details (timeouts, retries, specific libraries) are not locked, the plan is **REJECTED**.

| 决策点 (Ambiguity) | 选项/可能性 | 最终约束 | 理由 |
| :--- | :--- | :--- | :--- |
| *Example: Timeout* | *Default / 30s / 60s* | ***Fixed: 15s connect, 30s read*** | *Avoid resource exhaustion* |
| *Example: Library* | *Json / Orjson* | ***Fixed: Standard json*** | *Avoid new dependencies* |

### 🧪 Table 2: Property-Based Testing Spec (PBT 属性规约)

*   **Goal**: Define mathematical invariants that must hold true for ALL inputs (not just examples).
*   **Categories**: Idempotency (幂等性), Round-trip (可逆性), Invariant Preservation (守恒性), Commutativity (交换律).

| 功能模块 | PBT 属性类型 | 不变量描述 | 证伪策略 |
| :--- | :--- | :--- | :--- |
| *Example: Parser* | *Round-trip* | `decode(encode(x)) == x` | *Random Unicode strings* |
| *Example: Wallet* | *Invariant* | `balance >= 0` always | *Concurrent subtraction* |

### ⚖️ Table 3: Logic & Contract Audit (逻辑与契约审计)

*   **Data Flow**: Verify upstream/downstream parameter compatibility.
*   **System Risk**: Check for global state modification or OS-specific assumptions.

| 维度 | 检查项 | 状态 | 决策/规约 |
| :--- | :--- | :--- | :--- |
| **数据流** | 上游依赖 / 下游兼容 | Pass/Warn | (Must define specific data contract) |
| **一致性** | 函数签名 / 库调用 | Pass/Fail | (Check recursively against definitions) |
| **数据结构** | 硬编码 / 参数化 | Pass/Locked | (Must prioritize args/config over hardcoding) |
| **系统风险** | 副作用 / 环境兼容 | Pass/Warn | (Check global mechanisms & OS differences) |
| **复杂度** | 时间 / 空间 / OOM | Pass/Warn | (Assess loops & memory usage) |
| **并发与锁** | 读写冲突 / 死锁 | Pass/Warn | (Check file IO & shared resources) |
| **零决策** | 参数锁定 / 歧义消除 | Locked | (Must match Table 1) |

### 🛠️ Table 4: Physical Change Simulation (物理变更预演)

*   **Minimalist Check**: Confirm no changes to unrelated whitespace or comments.
*   **Ripple Effect**: Confirm imports and dependencies do not create circular references.

| 文件路径 | 定位 | 操作 | 简述 | 最小化验证 | 涟漪效应 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `path/to/file` | `func_name` | Modify | 增加重试逻辑 | ✅ 仅修改目标函数 | 无 |

## 4. Strict Schema Compliance (Implicit)

You MUST read `~/.claude/skills/deep-plan/output_schema.json` (if available) to understand the required verification depth.
**Do NOT output the JSON block.** Populate the Markdown tables to satisfy the schema's rigor.

## 5. Critical Rules
1.  **Stop & Think**: Do not generate this report if you haven't read the relevant files yet. Read them first.
2.  **Be Harsh**: The goal is to find problems, not to validate the plan. Play the "Devil's Advocate".
3.  **No Code Generation**: This step is pure analysis. Do not write implementation code here.

## 6. Explicit Stop Protocol (MANDATORY)
**CRITICAL**: You MUST generate ALL tables and analysis text in your response.

**After generating the analysis tables above, you MUST STOP.**
1.  Do **NOT** write any code.
2.  Do **NOT** apply any changes.
3.  Do **NOT** use the `AskUserQuestion` tool.
4.  Ends your response with a clear text question to the user:
    > "审计完成 (Audit Complete). [🟢开始执行 (Proceed)] / [🟡修改计划 (Revise)] / [🔴取消 (Cancel)]?"
