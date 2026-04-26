## 2025-04-26 - Fix Path Traversal in Package Download
**Vulnerability:** Path Traversal / Arbitrary File Write during package download.
**Learning:** `os.path.join(tmp_dir, package.whl_name)` doesn't strip malicious path structures from `package.whl_name`. If `whl_name` was `../../../etc/passwd` or `/etc/passwd`, it would overwrite system files instead of saving to `tmp_dir`.
**Prevention:** To prevent path traversal vulnerabilities when saving uploaded or remote files, always sanitize user-provided file names using `os.path.basename()` before joining them with a target directory path (e.g., `os.path.join(tmp_dir, os.path.basename(package.whl_name))`).
