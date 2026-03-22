## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2024-10-25 - [Async Iterable Parallelization in FunctionGroup]
**Learning:** When filtering a dictionary or list using async conditions (such as per-function inclusion checks in `FunctionGroup`), always use `asyncio.gather` instead of sequential `await` inside a loop to parallelize checks and prevent O(N) linear time blocking. However, explicitly pre-filter elements that can be synchronously excluded to preserve short-circuit evaluation, avoid eager evaluation of excluded items, and prevent unwanted side effects.
**Action:** Always pre-filter lists with synchronous checks before generating async tasks for `asyncio.gather`.
