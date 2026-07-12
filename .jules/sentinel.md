## 2024-05-24 - Path Traversal Vulnerability in Object Store Route
**Vulnerability:** Path traversal vulnerability in routes where user-provided paths were only sanitized with `os.path.normpath` but not checked for traversal sequences (`..`) before being passed to `object_store_client`.
**Learning:** `os.path.normpath` alone is insufficient to prevent path traversal when handling external paths, as it evaluates `..` but preserves it if it reaches the root of the relative path provided (e.g., `normpath("../../etc") == "../../etc"`).
**Prevention:** Explicitly check if `..` is present in the split parts of the normalized path (e.g., `".." in path.split(os.sep)`) to block traversal attempts when accepting user-provided paths for storage operations.
