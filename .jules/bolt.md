## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.
## 2025-05-29 - Pre-compile Regexes in ReAct Output Parser
**Learning:** In the ReAct Output Parser, complex regexes are dynamically compiled on every `.parse()` call. Repeated dynamic compilation of complex patterns introduces measurable CPU overhead in parsing loops.
**Action:** Always pre-compile regular expressions at the module level using `re.compile()` rather than using dynamic compilation methods like `re.search()` with string patterns inside frequently called functions.
