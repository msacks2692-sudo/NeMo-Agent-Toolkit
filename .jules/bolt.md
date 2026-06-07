## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.
## 2024-10-25 - [Pre-compile Module Level Regexes]
**Learning:** To eliminate repeated compilation overhead in frequently called functions, pre-compile regular expressions at the module level using `re.compile()` rather than using dynamic compilation methods like `re.match()` or `re.search()` with string patterns inside the function.
**Action:** Always check for regex usage in hot paths and pre-compile them at the module level, ensuring they are placed after all absolute and relative imports to avoid Ruff E402 errors.
