## 2025-02-28 - [Minimize Remote Operations in MilvusRetriever]
**Learning:** Repetitive calls to remote databases for metadata (e.g., fetching all collection names via `list_collections()` or fetching schemas via `describe_collection()`) severely degrade retrieval performance during continuous search operations.
**Action:** Use native, specific existence checks (like `has_collection(collection_name)`) and implement instance-level caching (via a dictionary) for metadata like collection schemas that rarely change during the lifespan of a retriever object.
