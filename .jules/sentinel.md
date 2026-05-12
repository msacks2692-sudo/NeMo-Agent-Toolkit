## 2024-05-12 - Path Traversal Vulnerability in Wheel Downloads
**Vulnerability:** Found a path traversal vulnerability in `src/nat/registry_handlers/rest/rest_handler.py` where a user-provided filename `package.whl_name` was unsafely joined with a directory path during file writing.
**Learning:** This existed because remote file inputs from the REST registry were trusted implicitly without sanitization.
**Prevention:** Always use `os.path.basename()` to strip any directory path components from user-supplied file names before writing them to the filesystem to prevent `../` attacks.
