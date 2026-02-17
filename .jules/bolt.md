## 2025-05-20 - Milvus Retriever Search Bottleneck
**Learning:** `MilvusRetriever.search` was performing `list_collections()` and `describe_collection()` on every call, causing 2 extra network roundtrips per search. This is a common "check before use" anti-pattern.
**Action:** Always cache immutable metadata like collection schemas. Verify "check" methods like `_validate_collection` aren't being called redundantly in hot paths.

## 2025-05-20 - Pytest Conftest Dependency Hell
**Learning:** `tests/conftest.py` imports `nat.builder.builder` which pulls in complex dependencies (`finetuning`), breaking simple unit tests in environments with missing optional deps.
**Action:** Temporarily rename `conftest.py` when running isolated unit tests or ensure optional dependencies are installed.
