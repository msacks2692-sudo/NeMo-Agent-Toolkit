## 2024-07-01 - Path traversal vulnerability in sanitize_path
**Vulnerability:** Path traversal in static file endpoints because `os.path.normpath` alone is insufficient to prevent it.
**Learning:** `os.path.normpath` resolves but retains `..` tokens if the path structure allows it (e.g., `../../etc/passwd`). Relying solely on it is insecure.
**Prevention:** Explicitly verify that `..` is not present in the path's parts (e.g., `'..' in path.split(os.sep)`).
