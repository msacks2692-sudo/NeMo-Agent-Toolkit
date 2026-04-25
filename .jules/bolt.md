## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2024-10-25 - [Optimize finding middle sentence index to be O(N) short-circuited]
**Learning:** `list(re.finditer(...))` followed by `min()` forces a full string scan and an $O(N)$ memory allocation, which is severely inefficient for large strings when searching for the "closest" match. Since `finditer` yields sequentially, if searching for the match closest to the midpoint, the distance will strictly decrease then strictly increase.
**Action:** When finding a point closest to a known index using `re.finditer`, pre-compile the regex and iterate through it lazily. Stop the loop (`break`) as soon as the distance begins to increase to cap execution time and avoid full list allocation.
