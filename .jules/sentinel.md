
## 2024-05-24 - Path Traversal Prevention in sanitize_path
**Vulnerability:** The `sanitize_path` function in the FastAPI front end relied solely on `os.path.normpath` which resolves `..` but retains them if they reach the root of the relative path, allowing path traversal.
**Learning:** `os.path.normpath` alone is insufficient to prevent path traversal vulnerabilities when sanitizing user-provided paths.
**Prevention:** Always explicitly check the normalized path for leading `..` components or `..` anywhere in the path parts after normalization to ensure path traversal cannot occur.
