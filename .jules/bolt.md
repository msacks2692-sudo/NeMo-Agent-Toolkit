## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2025-04-27 - [Optimize sentence boundary matching in red teaming middleware]
**Learning:** In the red teaming middleware (`_find_middle_sentence_index`), locating the sentence boundary closest to the string's midpoint using `list(re.finditer(...))` followed by `min()` forced a full $O(N)$ string scan and memory allocation. Since `re.finditer` returns matches in strictly increasing positional order, the distance to the midpoint strictly decreases and then strictly increases.
**Action:** When finding the closest spatial regex match to a target index, do not use `list()` and `min()`. Instead, lazily iterate over `re.finditer` and short-circuit (`break`) the loop as soon as the computed distance begins to increase, reducing complexity from $O(N)$ to $O(N/2)$ or better and eliminating memory allocation overhead.
