## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.
## 2025-03-08 - Optimize shallow copy overhead in retries
**Learning:** In highly-executed paths like exception handlers and retries, `tuple(args)` on an already immutable tuple and `dict(kwargs)` incur unnecessary overhead. Specifically, `tuple()` is redundant, and `kwargs.copy()` avoids global name lookup and function call overhead compared to `dict()`.
**Action:** Always prefer `.copy()` for dictionaries and avoid re-casting immutable types when creating shallow copies in performance-critical execution loops.
