## 2025-02-18 - Path Traversal Vulnerability in REST Handler
**Vulnerability:** Path traversal vulnerability due to unsanitized external filename (`package.whl_name`) being used in `os.path.join`.
**Learning:** External filenames provided via API must be sanitized before use in local paths to prevent writing to unintended locations on the filesystem.
**Prevention:** Always sanitize filenames from external sources using `os.path.basename` before joining them with destination directories.
