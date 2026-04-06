## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2024-10-24 - [Regex lazy short-circuiting]
**Learning:** When searching for the closest match in a large string (e.g. `re.finditer` to find a midpoint sentence boundary), converting the generator to a list (e.g. `list(re.finditer(...))`) forces the regex engine to scan the entire string and materializes the matches in memory, causing O(N) overhead.
**Action:** Iterate lazily over the generator `re.finditer(...)` and short-circuit the loop using a `break` as soon as the distance logic indicates you've passed the optimal midpoint. Combine this with module-level regex compilation (`re.compile`) to cut execution time significantly on large strings without sacrificing readability.
