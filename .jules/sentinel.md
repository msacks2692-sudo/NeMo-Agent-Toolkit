## 2024-05-14 - [Path Traversal in Registry Download]
**Vulnerability:** Found a path traversal vulnerability in `src/nat/registry_handlers/rest/rest_handler.py` where `os.path.join(tmp_dir, package.whl_name)` was used. A malicious server could return a wheel name like `../../../../../../tmp/evil.whl` to write arbitrary files on the client.
**Learning:** External registry or API responses cannot be trusted for file names. They should be sanitized.
**Prevention:** Use `os.path.basename()` on any filename received from an external source before using it in a file path.
