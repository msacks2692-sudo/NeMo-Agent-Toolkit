## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.
## 2024-10-25 - [Pre-compile repeated regexes in agent loop]
**Learning:** In the ReAct agent's output parsing (`ReActOutputParser.parse`), regular expressions were being compiled at runtime via `re.search` on every execution loop. This causes unnecessary overhead during text parsing, particularly when dealing with long streams or repeated LLM output evaluation.
**Action:** Always pre-compile frequently used regular expressions using `re.compile` at the module level (ensuring they are placed below module imports) instead of inside tight execution loops like parsers or output evaluators.
