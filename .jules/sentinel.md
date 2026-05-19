
## 2024-05-19 - Path Traversal in File Downloads
**Vulnerability:** Found a Path Traversal vulnerability in the REST registry handler (`src/nat/registry_handlers/rest/rest_handler.py`). The application joined a user-controlled filename (`package.whl_name`) directly with a temporary directory (`tmp_dir`) when downloading packages from a remote registry.
**Learning:** This existed because we trusted the metadata returned from a remote (potentially compromised or spoofed) registry without sanitizing it before using it in a local file system operation (`os.path.join`).
**Prevention:** Always sanitize any untrusted or remote filenames using `os.path.basename()` before combining them with local paths.
