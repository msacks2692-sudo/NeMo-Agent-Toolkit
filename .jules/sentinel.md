## 2025-02-18 - Path Traversal in REST Handler
**Vulnerability:** Found a path traversal vulnerability when saving downloaded wheels in `rest_handler.py` because `package.whl_name` was directly joined with `tmp_dir`.
**Learning:** External or remote filenames must not be trusted and must be sanitized.
**Prevention:** Always use `os.path.basename()` to sanitize filenames before joining them with a target directory path.
