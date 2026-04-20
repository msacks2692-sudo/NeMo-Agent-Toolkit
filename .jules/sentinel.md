## 2025-02-28 - Path Traversal in Package Extraction
**Vulnerability:** A path traversal (Zip Slip/Arbitrary File Write) vulnerability existed in `src/nat/registry_handlers/rest/rest_handler.py` where a remotely provided `package.whl_name` was directly joined with `tmp_dir` using `os.path.join()`.
**Learning:** External registry servers could supply malicious filenames (e.g., `../../../etc/passwd` or absolute paths) which, when concatenated with `os.path.join()`, bypass the intended temporary directory boundary, leading to arbitrary file write.
**Prevention:** Always sanitize externally provided filenames when constructing paths for extraction or downloading by wrapping them in `os.path.basename()` (e.g., `os.path.join(tmp_dir, os.path.basename(package.whl_name))`).
