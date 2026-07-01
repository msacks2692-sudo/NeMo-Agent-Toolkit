## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2025-07-01 - [Pre-compile output parser regexes]
**Learning:** ReAct output parsers are called very frequently in the inner loop of the agent. Dynamically compiling regexes (like `re.search(r"...", text)`) on every parse call introduces unnecessary overhead.
**Action:** When working with agent output parsers or other frequently called string processing logic, always pre-compile regexes at the module level using `re.compile()`.
