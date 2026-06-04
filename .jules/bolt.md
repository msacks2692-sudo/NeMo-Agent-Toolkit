## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.
## 2024-10-25 - [Pre-compile Regexes]
**Learning:** In frequently called methods like agent output parsers, dynamic regex compilation (e.g., using `re.search()` with inline strings) introduces measurable overhead. Profiling showed that dynamic search takes ~0.306s for 100k iterations compared to ~0.236s for pre-compiled regexes.
**Action:** When working with repetitive parsing loops, always define `re.compile()` constants at the module level.
