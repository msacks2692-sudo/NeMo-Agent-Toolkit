## 2024-06-18 - Path Traversal Vulnerability in FastAPI Front End
**Vulnerability:** The `sanitize_path` function in `fastapi_front_end_plugin_worker.py` only used `os.path.normpath`, allowing path traversal sequences to slip through.
**Learning:** `os.path.normpath` does not prevent path traversal if the resulting path still contains relative path navigation elements (e.g. `..`).
**Prevention:** Always explicitly check if `..` is still present in the sanitized path, for instance by splitting with `os.path.sep` and checking for `..` parts.
