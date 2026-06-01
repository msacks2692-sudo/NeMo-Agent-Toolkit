## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.
## 2025-02-12 - ReAct Output Parser Regex Bottleneck
**Learning:** Calling `re.search()` with complex string patterns inside the hot path of ReAct agent output parsing causes significant repeated compilation overhead. Pre-compiling the action, missing action, and missing action input patterns with `re.compile()` at the module level improved parse matching speed by ~24% during benchmarking.
**Action:** When working with agent output parsers or LLM text extractors, aggressively pre-compile any `re` patterns at the module level rather than calling `re.search` or `re.match` dynamically in the parse functions.
