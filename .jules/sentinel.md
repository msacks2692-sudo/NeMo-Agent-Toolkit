## 2025-02-24 - [Path Traversal Fix]
**Vulnerability:** A path traversal vulnerability existed in `src/nat/registry_handlers/rest/rest_handler.py` during `pull` operation where wheel file data retrieved over REST API from a remote registry was being written to local disk using unsanitized file names.
**Learning:** `os.path.join(tmp_dir, package.whl_name)` allowed any arbitrary relative paths like `../../foo.txt` embedded within `whl_name` to escape `tmp_dir` and write to arbitrary local locations (Zip slip style).
**Prevention:** Always use `os.path.basename()` to sanitize untrusted filenames before combining them using `os.path.join`.
