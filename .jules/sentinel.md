## 2025-05-07 - [Path Traversal in Registry Handler]
**Vulnerability:** Found `os.path.join(tmp_dir, package.whl_name)` in `src/nat/registry_handlers/rest/rest_handler.py` when pulling packages.
**Learning:** `package.whl_name` was directly passed without sanitization, allowing an attacker to escape `tmp_dir` if the package name included directory traversal sequences.
**Prevention:** Always sanitize remote or untrusted file names using `os.path.basename()` before passing them to `os.path.join()`.
