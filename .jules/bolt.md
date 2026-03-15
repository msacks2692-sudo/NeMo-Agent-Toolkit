## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.

## 2024-10-25 - [Optimize Milvus Collection Checks and Schema Caching]
**Learning:** Checking collection existence in Milvus via `list_collections()` and iterating is O(N) in both network transfer and memory. Additionally, fetching `describe_collection` on every search introduces an unnecessary network roundtrip per query since collection schemas are static during runtime.
**Action:** Use `has_collection(collection_name)` for O(1) existence checks. Introduce an instance-level cache (`self._collection_schemas`) for `describe_collection` results to eliminate redundant network calls on subsequent searches.
