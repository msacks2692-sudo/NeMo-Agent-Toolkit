## 2024-05-20 - Fix Path Traversal in Rest Handler Download
**Vulnerability:** The codebase had an unsafe `os.path.join(tmp_dir, package.whl_name)` when extracting downloaded packages in the rest handler, lacking validation on the external `whl_name`. This could allow attackers to perform arbitrary file writes via directory traversal attacks.
**Learning:** External or user-provided file names from web endpoints must be assumed unsafe and properly sanitized before being passed into OS file manipulation operations.
**Prevention:** To prevent this, always sanitize external file names using `os.path.basename()` before joining them with destination directories (e.g. `os.path.join(dest, os.path.basename(file_name))`) or use libraries built specifically to prevent insecure path resolutions.
