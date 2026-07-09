
## 2025-07-09 - Path Traversal via Remote Object Metadata in REST Client
**Vulnerability:** The REST registry client blindly passed the `.whl_name` parameter returned by the remote server to `os.path.join` for writing the wheel payload locally.
**Learning:** Even internal registries or expected formats can be compromised or misconfigured. `os.path.join` on absolute or traversed paths will silently navigate outside the intended download directory, allowing arbitrary file overwrite when downloading a package.
**Prevention:** When saving downloaded files where filenames come from an external or remote API response, explicitly extract the base filename using `os.path.basename` and validate against traversals (e.g., `..`) before writing to disk.
