## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2024-10-25 - [Optimize dictionary first element retrieval]
**Learning:** For dictionary operations in Python 3, getting the first element using `list(my_dict.keys())[0]` or `list(my_dict.values())[0]` creates a full copy of all keys/values into a new list, leading to O(N) time and memory complexity just to fetch one element. Instead, using `next(iter(my_dict))` and `next(iter(my_dict.values()))` performs the same logic in O(1) time without an intermediate list.
**Action:** Use `next(iter(dict))` when you need the first key, and `next(iter(dict.values()))` when you need the first value from a dictionary. Avoid `list(dict.keys())` completely when a list isn't necessary.
