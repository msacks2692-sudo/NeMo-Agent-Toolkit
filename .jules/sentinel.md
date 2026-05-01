## 2025-05-01 - Path Traversal in Package Pull
**Vulnerability:** A path traversal vulnerability existed in `RestRegistryHandler.pull` where the `whl_name` provided by a remote registry response was joined directly with `tmp_dir` using `os.path.join(tmp_dir, package.whl_name)`.
**Learning:** This could allow an attacker-controlled registry to return a package with a filename like `../../../etc/shadow`, which would result in the arbitrary writing or overwriting of files outside of the intended `.tmp/nat-pull` directory on the client's machine.
**Prevention:** Always sanitize filenames obtained from remote sources or user input before using them in file system operations. Using `os.path.basename()` is a simple and effective way to strip any directory traversal sequences.
