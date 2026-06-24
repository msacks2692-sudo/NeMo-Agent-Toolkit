## 2024-06-24 - Pre-compile regexes in parsers and content guards
**Learning:** In the ReAct parser and content guard components, `re.search` is used with dynamic string patterns or repeatedly during parsing, especially inside loops and hot paths like `parse()`. This repeatedly compiles regex patterns, causing measurable overhead.
**Action:** When a regex is known at design time and doesn't change, pre-compile it using `re.compile()` at the module level. I will precompile `re.search` in `src/nat/agent/react_agent/output_parser.py` and `src/nat/middleware/defense/defense_middleware_content_guard.py`.

## 2024-06-24 - Module Level Regex Compilation Needs to Follow PEP8
**Learning:** When moving regular expression pre-compilation from functions to the module level, the new `re.compile()` constants must be placed strictly *after* all local, relative, and absolute imports to avoid `E402 Module level import not at top of file` Ruff errors.
**Action:** In `src/nat/middleware/defense/defense_middleware_content_guard.py` and future tasks, ensure new variables or precompiled constants are declared only after all imports have concluded.
