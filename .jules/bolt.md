## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2024-05-18 - Missing documentation comments for performance improvements
**Learning:** The prompt explicitly stated "✅ **Always do:** Add comments explaining the optimization" as a boundary. I forgot to include this in my initial code modifications.
**Action:** When acting as the Bolt performance persona, always add a comment explaining *why* the optimization was made (e.g. "Performance Optimization: Pre-compile regexes to avoid repeated recompilation on every parse call") directly in the source code where the change was made.
