## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.
## 2024-10-25 - [Optimize loop dictionary accesses]
**Learning:** Performance measurements in `trajectory_builder.py` show that caching dictionary-based counters (like `total_candidates` and `skipped_score_diff`) into local variables before nested loops and performing a single dictionary write at the end reduces overhead and improves execution time.
**Action:** When updating dictionary counters inside tight loops, extract the value to a local variable beforehand, update the local variable in the loop, and write it back to the dictionary afterwards to avoid repeated `.get()` and hash lookups.
