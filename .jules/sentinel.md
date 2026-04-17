## 2025-04-17 - Path Traversal in File Download from External API
**Vulnerability:** Found a path traversal vulnerability in `src/nat/registry_handlers/rest/rest_handler.py` where a user-controlled file name `package.whl_name` was passed unsanitized into `os.path.join(tmp_dir, package.whl_name)`.
**Learning:** This could allow a malicious REST registry or middleman to dictate file paths, writing the file out of `tmp_dir` into sensitive locations (e.g., overriding system or local project files if `../../` was sent).
**Prevention:** To prevent path traversal vulnerabilities when saving uploaded or remote files, always sanitize user-provided file names using `os.path.basename()` before joining them with a target directory path.
