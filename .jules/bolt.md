## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2024-04-08 - [Optimize Regex Match Distance Calculation]
**Learning:** Avoid compiling the same regex repeatedly within functions called frequently, and don't convert `re.finditer()` to a list when only searching for the closest match. Using `list(re.finditer(...))` followed by `min()` forces an O(N) memory allocation and a full string scan.
**Action:** Pre-compile the regex pattern at the module level. Iterate through `re.finditer(...)` and short-circuit (`break`) the loop as soon as the calculated distance from the target point begins to increase, yielding significant performance gains and reducing memory footprint on large strings.
