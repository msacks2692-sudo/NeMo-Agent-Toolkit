
## 2025-03-01 - Prevent Path Traversal in Static File API
**Vulnerability:** Path traversal vulnerability in `sanitize_path` inside `add_static_files_route` in `src/nat/front_ends/fastapi/fastapi_front_end_plugin_worker.py`.
**Learning:** `os.path.normpath` resolves `..` components but retains them if they reach the root of the relative path, allowing paths like `../../etc/passwd` to bypass basic sanitization. Absolute paths are also allowed if not explicitly blocked.
**Prevention:** Explicitly check for absolute paths and `..` components starting the path (e.g. `sanitized_path.startswith("..")` or `os.path.isabs(sanitized_path)`) after normalization.
