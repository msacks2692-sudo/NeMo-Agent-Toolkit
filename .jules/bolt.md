## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2024-10-24 - [Optimize Enum membership checks]
**Learning:** In Python, evaluating membership against an inline list containing Enum attribute lookups (e.g., `val in [Enum.A, Enum.B]`) is not optimized into a constant tuple by the bytecode compiler. Instead, it incurs repeated list instantiation and attribute lookup overhead on every execution, which can become a bottleneck in frequently called paths like message routers.
**Action:** Always pre-allocate Enum membership collections as module-level tuple constants (e.g., `_ALLOWED_TYPES = (Enum.A, Enum.B)`) and evaluate against the constant tuple to eliminate redundant overhead.
