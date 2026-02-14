## 2024-05-23 - [Redundant Milvus Metadata Calls]
**Learning:** `MilvusRetriever` was making `list_collections` (O(N)) and `describe_collection` (network call) for *every* search query. This is a significant bottleneck for high-throughput applications.
**Action:** Implemented instance-level schema caching in `MilvusRetriever` to fetch metadata only once per collection.
