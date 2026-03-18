## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.


## 2024-10-25 - [Optimize FunctionGroup function retrieval]
**Learning:** Function retrieval methods in `FunctionGroup` (`src/nat/builder/function.py`) previously used sequential `await self._fn_should_be_included(name)` checks in for-loops for all functions in a group. This caused O(N) linear time await blocking for functions depending on network/async filters. Using `asyncio.gather()` to parallelize per-function inclusion checks significantly improves performance when filters are asynchronous.
**Action:** When filtering a dictionary or list using async conditions, always use `asyncio.gather` instead of sequential `await` inside a loop.
