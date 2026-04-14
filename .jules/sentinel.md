## 2025-02-27 - Fix Path Traversal in REST Handler
**Vulnerability:** A path traversal vulnerability existed in `src/nat/registry_handlers/rest/rest_handler.py` where a user-provided filename from an external response (`package.whl_name`) was directly passed to `os.path.join(tmp_dir, ...)`.
**Learning:** `os.path.join` is vulnerable to path traversal if the second argument is an absolute path or contains directory traversal sequences (`../`), causing the file to be written outside the intended directory.
**Prevention:** Always sanitize externally provided filenames using `os.path.basename()` before appending them to a directory path using `os.path.join()`.
