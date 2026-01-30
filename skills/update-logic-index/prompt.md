Task: Analyze the provided Python source code and generate summaries for the specified target symbols in Simplified Chinese (简体中文).

Input Data:
- Target Symbols: {target_symbols}
- Source Code:
{source_code}

Constraints:
1. Return a JSON Array of objects.
2. Each object must have "name" (symbol name) and "summary" (string).
3. Summary Rules:
   - One sentence only.
   - Max 30 characters.
   - No function name repetition.
   - Focus on responsibility/intent.
   - If it's a test function, start with [Test].
   - If it's a utility, start with [Util].
4. Only summarize symbols listed in "Target Symbols".

Output Format (JSON):
[
  {{"name": "SymbolName", "summary": "Summary text..."}},
  ...
]
