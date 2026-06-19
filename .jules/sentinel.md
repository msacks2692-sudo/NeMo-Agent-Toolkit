
## 2024-06-19 - Path Traversal bypass with os.path.normpath
**Vulnerability:** Path traversal vulnerability due to relying solely on `os.path.normpath` for path sanitization.
**Learning:** `os.path.normpath` collapses `a/../b` correctly, but it does NOT remove or collapse leading `..` traversal segments (e.g., `../../../etc/passwd` remains `../../../etc/passwd` and `a/../../../etc/passwd` resolves to `../../etc/passwd`). Relying on it as the sole safety mechanism allows an attacker to escape the intended directory.
**Prevention:** Always explicitly check for the presence of `..` segments *after* normalizing the path, such as checking if `".." in sanitized_path.split(os.path.sep)`.
