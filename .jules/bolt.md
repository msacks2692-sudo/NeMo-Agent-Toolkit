## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2024-10-25 - [Optimize regex compilation for think tags]
**Learning:** Functions that parse generated text (like `remove_r1_think_tags`) are called repeatedly in tight reasoning loops or generation steps. Compiling regular expressions locally inside these functions introduces redundant overhead, even with Python's internal regex caching, which can add up in high-throughput or heavily iterated agent pipelines.
**Action:** Always pre-compile frequently used regular expressions at the module level (e.g., `_PATTERN = re.compile(..., re.DOTALL)`) in utility modules, and ensure that dependent modules do not inadvertently re-compile or inline the regex locally but either import the pre-compiled pattern or implement a fast proxy method calling the pre-compiled regex object.
