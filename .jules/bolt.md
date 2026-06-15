## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.
## 2024-05-18 - [Optimize dictionary metric updates]
**Learning:** Caching dictionary-based counters into local variables within nested loops and performing a single dictionary write at the end reduces overhead and improves execution time.
**Action:** Identify loop-bound dictionary lookups and updates, and hoist them into local variables where possible, syncing back to the dictionary outside the loop.
