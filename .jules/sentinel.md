## 2024-06-17 - Insecure Path Normalization allows Path Traversal
**Vulnerability:** The `sanitize_path` function in `src/nat/front_ends/fastapi/fastapi_front_end_plugin_worker.py` only uses `os.path.normpath` which resolves but does not remove leading `..` components, potentially allowing path traversal to read/write arbitrary files outside the intended object store directory.
**Learning:** `os.path.normpath` is not sufficient for path sanitization. It leaves `../` sequences if they reach above the root or start of the path string. Explicitly checking for `..` is necessary.
**Prevention:** Verify that the normalized path does not start with `..` or contain `..` in its parts.
