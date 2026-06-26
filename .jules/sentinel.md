## 2025-06-26 - [Path Traversal in FastAPI Endpoint]
**Vulnerability:** Path traversal vulnerability in `add_static_files_route` where user-provided `file_path` is sanitized using `os.path.normpath` but fails to check for `..` components correctly, allowing paths outside the intended directory.
**Learning:** `os.path.normpath` resolves paths but retains leading `..` components if the path goes above the root. A check `sanitized_path == "."` is insufficient. We need to explicitly check if `..` is in the path components.
**Prevention:** Always verify that `..` is not present in the path's parts (e.g., `'..' in path.split(os.sep)`) when sanitizing user-provided paths. Avoid using `path.startswith('..')` as it may falsely flag valid filenames.
