## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.
## 2024-10-25 - [Optimize regex closest-match search]
**Learning:** To find the closest match in a string using regex (e.g., matching a sentence boundary closest to the midpoint), avoid using `list(re.finditer(...))` followed by `min()` as it forces an $O(N)$ memory allocation and a full string scan.
**Action:** Pre-compile the regex at the module level. Then, iterate through `re.finditer(...)` and short-circuit (`break`) the loop as soon as the calculated distance from the target point begins to increase, yielding significant memory and execution time improvements on large strings.
