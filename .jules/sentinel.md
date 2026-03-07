## 2025-05-30 - Path Traversal in Registry Handler
**Vulnerability:** Path traversal in `RestRegistryHandler.pull` allowed arbitrary file overwrite via malicious `whl_name` in registry response.
**Learning:** `os.path.join` with absolute paths or `../` allows escaping the target directory. Trusting external filenames (even from a registry) is dangerous.
**Prevention:** Always validate filenames with `os.path.basename()` before joining them to a target directory.
