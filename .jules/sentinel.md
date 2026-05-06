## 2024-05-18 - Path Traversal in REST API Registry Handler
**Vulnerability:** The `package.whl_name` provided by the remote registry in the `/pull` response was directly concatenated with `tmp_dir` using `os.path.join()`.
**Learning:** This allowed a malicious registry server to provide a payload like `../../../../etc/shadow` as the wheel name, causing the application to write downloaded wheel contents to arbitrary locations on the host file system.
**Prevention:** To prevent path traversal vulnerabilities when saving uploaded or remote files, always sanitize user-provided file names using `os.path.basename()` before joining them with a target directory path.
