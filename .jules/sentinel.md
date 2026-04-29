## 2024-05-14 - Fix Path Traversal in REST Registry Handler
**Vulnerability:** Found a path traversal vulnerability in `src/nat/registry_handlers/rest/rest_handler.py` where a downloaded package wheel file was saved using the raw `package.whl_name` combined with a temporary directory path (`os.path.join(tmp_dir, package.whl_name)`). This would allow a malicious server to respond with a `whl_name` like `../../../etc/passwd` to write files anywhere on the system.
**Learning:** `os.path.join` does not sanitize file names, and will use an absolute path or traverse upward if the second argument begins with `/` or `../`.
**Prevention:** Always sanitize user-provided or externally-provided file names using `os.path.basename()` before passing them into `os.path.join()` or writing them to disk.
