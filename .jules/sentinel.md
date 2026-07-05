## 2024-07-05 - Path Traversal in FastAPI Static File Endpoints
**Vulnerability:** Path traversal vulnerability in `sanitize_path` inside `src/nat/front_ends/fastapi/fastapi_front_end_plugin_worker.py`.
**Learning:** Using `os.path.normpath` alone is insufficient for sanitizing file paths, as it resolves but retains leading `..` components (e.g., `os.path.normpath("../etc/passwd")` returns `../etc/passwd`).
**Prevention:** Explicitly verify that `..` is not present in the path's parts (e.g., `'..' in path.split(os.sep)`) after using `os.path.normpath`.
