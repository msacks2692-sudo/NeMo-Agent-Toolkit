## 2024-05-18 - Fix Path Traversal in Static Files Endpoints
**Vulnerability:** Path traversal possible in FastAPI static files endpoints via unsanitized file paths.
**Learning:** Even if a helper function `sanitize_path` exists and uses `os.path.normpath`, it retains `..` segments if not explicitly rejected. Endpoints must also actively call this sanitization before passing paths to the object store.
**Prevention:** Validate that `..` is not in `os.path.normpath` outputs, and consistently apply sanitization functions to user-controlled file paths in all endpoint handlers.
