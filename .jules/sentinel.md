## 2025-02-18 - Fix Path Traversal Vulnerability in REST Registry Pull
**Vulnerability:** Path traversal via unsanitized package names received from a remote REST registry (`rest_handler.py`).
**Learning:** `os.path.join(tmp_dir, package.whl_name)` allowed writing arbitrary files if a malicious remote server provided a `whl_name` containing `../`. This highlights that remote registry responses must be treated as untrusted input.
**Prevention:** Always sanitize externally provided filenames using `os.path.basename()` before combining them with local paths (e.g., `os.path.join(tmp_dir, os.path.basename(package.whl_name))`).
