## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.
## 2025-06-18 - Pre-compile Regexes in ReAct Parser
**Learning:** Compiling complex regular expressions dynamically inside frequently invoked functions like the ReAct agent's parser causes measurable overhead.
**Action:** Always pre-compile regular expressions at the module level using `re.compile()` for performance-critical parsing functions.
