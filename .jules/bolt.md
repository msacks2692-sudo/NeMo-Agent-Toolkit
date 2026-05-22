## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2025-02-12 - [Cache Dictionary Counters in Loops]
**Learning:** Performance measurements show that caching dictionary-based counters into local variables within nested loops and performing a single dictionary write at the end reduces overhead and improves execution time.
**Action:** Always cache dictionary counters into local variables before executing nested loops that frequently increment them, and perform a single write back to the dictionary afterwards.
