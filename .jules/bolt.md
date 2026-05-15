## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.
## 2024-05-15 - [Cache dictionary counters in nested loops]
**Learning:** Performance measurements show that caching dictionary-based counters (like `total_candidates`) into local variables within nested loops and performing a single dictionary write at the end reduces overhead and improves execution time by approximately 10%.
**Action:** Always pre-allocate dictionary counts to local variables when tracking metrics inside performance-critical nested loops.
