## YYYY-MM-DD - Path Traversal Vulnerability in Wheel Download
**Vulnerability:** Path traversal vulnerability in `src/nat/registry_handlers/rest/rest_handler.py` via `os.path.join(tmp_dir, package.whl_name)`.
**Learning:** `package.whl_name` was directly concatenated using `os.path.join` without sanitization. An attacker could use a filename like `../../../etc/passwd` to write files anywhere on the file system, as `os.path.join` replaces the base path with the absolute path if one is provided.
**Prevention:** Always sanitize user-provided filenames using `os.path.basename()` before combining them with directories.
