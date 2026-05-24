## 2025-05-24 - Pre-compiling Regex in Parsers
**Learning:** In the ReAct parser (`src/nat/agent/react_agent/output_parser.py`), dynamic regex compilation in the `parse()` method caused overhead on a critical path.
**Action:** Pre-compile regular expressions at the module level when they are used inside frequently executed parsing logic to eliminate repeated compilation cost.
