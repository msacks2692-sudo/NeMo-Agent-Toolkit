## 2025-02-18 - Milvus Schema Caching
**Learning:** `MilvusRetriever` was performing `list_collections` and `describe_collection` on every search operation, causing significant overhead (N+1-like issue).
**Action:** Always check `__init__` or long-lived object state for caching opportunities on static metadata (like DB schemas) to avoid redundant network calls in hot paths like `search`.
