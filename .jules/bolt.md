## 2024-02-27 - [MilvusRetriever Optimization]
**Learning:** `list_collections()` and `describe_collection()` are called on every search in `MilvusRetriever`, causing N+1 network calls. Caching schema eliminates this overhead.
**Action:** Always look for repeated metadata fetching in database/service clients. Cache immutable or slowly-changing metadata.
