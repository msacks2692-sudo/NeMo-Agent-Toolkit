## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2025-05-18 - Optimize Set Operations on Python Dictionaries
**Learning:** Calling `.keys()` on a dictionary before generating a set is slower than creating a set directly from the dictionary. By omitting `.keys()`, Python skips allocating the dict_keys view. Additionally, using `set(dict1).difference(dict2)` prevents generating a secondary set in memory before subtraction compared to `set(dict1) - set(dict2)`. Combining these strategies yields roughly ~25-45% speedups depending on set sizes.
**Action:** Avoid explicit `.keys()` usage when generating lists or sets, or when performing membership checks on dictionaries in hot paths across the repository.
