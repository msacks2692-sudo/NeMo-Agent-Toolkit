## 2025-02-23 - Prevent Path Traversal in Static File API
**Vulnerability:** Path traversal vulnerability in `sanitize_path` within FastAPI static file upload/download endpoints where `os.path.normpath` alone did not prevent leading `..` traversals.
**Learning:** `os.path.normpath` handles internal traversals but leaves leading `..` components intact. Solely relying on it or checking if the path equals `.` is insufficient for sanitization.
**Prevention:** Check for `..` components directly in the path split by `os.sep` (e.g., `".." in path.split(os.sep)`) after normalizing the path to comprehensively catch traversal attempts without falsely blocking safe dot characters inside filenames.
