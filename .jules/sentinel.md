## 2024-05-28 - Zip Slip Vulnerability in REST Registry Handler
**Vulnerability:** Path traversal vulnerability when downloading packages from a remote REST registry. `package.whl_name` was used directly in `os.path.join` without sanitization.
**Learning:** External or remote registries can provide malicious file names (e.g., `../../../etc/passwd`). When saving these files locally, blindly joining the provided name with a temporary directory allows arbitrary file writes outside the intended sandbox.
**Prevention:** Always sanitize externally provided file names using `os.path.basename()` before combining them with local paths (e.g., `os.path.join(tmp_dir, os.path.basename(package.whl_name))`).
