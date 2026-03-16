## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2024-10-25 - [Optimize vector db retrieval metadata lookups]
**Learning:** When working with vector databases like Milvus, avoid fetching the entire list of collections or repeatedly fetching collection schemas during query execution. In production workloads with numerous collections, a `list_collections()` API call followed by an O(N) client-side check can be extremely slow and memory intensive compared to an O(1) `has_collection()` direct existence check.
**Action:** Always use targeted APIs like `has_collection(name)` instead of bulk APIs like `list_collections()`. Introduce instance-level caching (e.g., `self._collection_schemas`) for static metadata like `describe_collection` to avoid redundant network overhead during frequent operations like `search`.
