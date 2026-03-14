## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2025-03-14 - [Parallelize async function inclusion checks]
**Learning:** Function retrieval methods in `FunctionGroup` (`src/nat/builder/function.py`) use `asyncio.gather()` to parallelize per-function inclusion checks (`_fn_should_be_included`), significantly improving performance when filters are asynchronous.
**Action:** When filtering or processing multiple asynchronous checks (like per-function or per-tool checks), avoid sequential `await` inside loops. Instead, aggregate the items and use `asyncio.gather` to resolve them concurrently to reduce overall latency.
