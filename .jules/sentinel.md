
## 2025-05-20 - [Fix Path Traversal in Registry Handler]
**Vulnerability:** A Path Traversal / Arbitrary File Write vulnerability was present in `src/nat/registry_handlers/rest/rest_handler.py`. The `package.whl_name` variable, derived from the remote registry JSON payload, was joined directly with a temporary directory path using `os.path.join(tmp_dir, package.whl_name)`.
**Learning:** `os.path.join` is vulnerable to path traversal if the second argument is an absolute path or contains directory traversal sequences (like `../`). A malicious server response could force the file to be written outside the intended directory.
**Prevention:** Always sanitize untrusted filenames from remote sources using `os.path.basename()` before appending them to a local directory path to ensure the file is written to the intended location.
