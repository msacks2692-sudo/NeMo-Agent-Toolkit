## 2024-06-22 - Path Traversal in FastAPI Static Files Route
**Vulnerability:** The `sanitize_path` function in the FastAPI plugin relied solely on `os.path.normpath()`, allowing malicious paths like `../../foo` or `/../../bar` to be processed and uploaded to the object store.
**Learning:** `os.path.normpath()` resolves paths but retains leading `..` elements if the path doesn't start from an absolute root, enabling path traversal if not explicitly checked.
**Prevention:** Always explicitly check for `..` parts in the normalized path or if the path starts with `..` when sanitizing file paths derived from user input.
