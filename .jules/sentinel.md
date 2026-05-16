
## 2024-05-16 - Path Traversal in REST Registry Handler
**Vulnerability:** Path traversal vulnerability in `src/nat/registry_handlers/rest/rest_handler.py` where a downloaded package wheel (`package.whl_name`) could be extracted outside the designated temporary directory.
**Learning:** `os.path.join(tmp_dir, package.whl_name)` blindly concatenates paths without sanitizing the user/server-provided filename. A payload like `../../../etc/passwd` would overwrite arbitrary system files.
**Prevention:** To prevent path traversal vulnerabilities when saving uploaded or remote files, always sanitize user-provided file names using `os.path.basename()` before joining them with a target directory path (e.g., `os.path.join(tmp_dir, os.path.basename(package.whl_name))`).
