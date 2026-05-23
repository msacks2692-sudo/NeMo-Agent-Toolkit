## 2025-05-23 - Path Traversal in Package Downloads
**Vulnerability:** A remote package registry could return a `whl_name` containing directory traversal characters (e.g., `../../../etc/passwd`), allowing arbitrary file write during package pull.
**Learning:** `os.path.join` does not sanitize inputs; if the second argument is an absolute path or contains traversal characters, it can escape the intended directory.
**Prevention:** Always sanitize remote or user-provided filenames using `os.path.basename()` before appending them to a local directory path.
