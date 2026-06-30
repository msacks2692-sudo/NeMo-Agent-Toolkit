## 2024-07-01 - [Path Traversal Fix]
**Vulnerability:** Path traversal in static file upload/download logic using `os.path.normpath` alone.
**Learning:** `os.path.normpath` resolves paths but doesn't remove `..` parts if they prefix the string (e.g. `../../b`), leaving it susceptible to traversal.
**Prevention:** Explicitly verify that `..` is not present in the path's parts `if '..' in path.split(os.sep)`.
