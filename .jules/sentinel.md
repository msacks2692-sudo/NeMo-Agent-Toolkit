## 2025-05-04 - [Path Traversal in Registry Package Pull]
**Vulnerability:** A path traversal vulnerability existed in the REST registry handler where `package.whl_name` was directly appended to `tmp_dir` using `os.path.join()`. This could allow a malicious registry server to return a package with a filename containing `../` to write arbitrary files outside the temporary directory.
**Learning:** `os.path.join()` does not protect against path traversal if the appended segments contain absolute paths or relative traversals (`../`).
**Prevention:** Always sanitize remote or user-provided filenames using `os.path.basename()` before combining them with directories to write local files.
