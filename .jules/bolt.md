## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.
## 2024-05-14 - json.loads() micro-optimization warning
**Learning:** Do not attempt to micro-optimize Python's `json.loads()` with manual structural checks like `string.lstrip()[0]`. `json.loads()` is implemented in C and is already highly optimized for failures. Calling string methods like `lstrip()` on large JSON payloads creates a new string in memory, causing performance and memory degradation that contradicts the optimization goals.
**Action:** Always measure first before optimizing. Rely on built-in C-extensions like `json` instead of trying to outsmart them with Python-level string manipulation.
