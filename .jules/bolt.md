## 2026-02-20 - [Milvus Retriever Performance]
**Learning:** `MilvusRetriever` was calling `list_collections` (O(N) network call) on every `search` operation to validate collection existence, which is a major bottleneck for high-throughput systems.
**Action:** Always verify if a validation check involves an expensive list operation. Use "Ask for Forgiveness" (try and catch error) or cache the validation result (schema) to avoid repeated network calls.
