## 2024-06-15 - [Path Traversal in FastAPI Object Store Static File Routes]
**Vulnerability:** The `sanitize_path` function in the FastAPI plugin worker used `os.path.normpath()` to resolve paths but failed to block inputs with leading parent directory references (like `../../etc/passwd`).
**Learning:** `os.path.normpath` resolves paths cleanly but retains leading `..` components when navigating outside the base path context, which allowed bypassing the intended directory restrictions.
**Prevention:** When derived from user input, always combine `os.path.normpath` with an explicit check (`startswith("..")` or containing `..` as a component) to explicitly block path traversal attempts.
