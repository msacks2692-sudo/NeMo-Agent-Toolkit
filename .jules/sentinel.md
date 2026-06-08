## 2024-05-18 - [Prevent Argument Injection in Subprocess]
**Vulnerability:** User-provided variables (like package names or file paths) were passed directly to `subprocess.run` without `--` separation, allowing argument injection if a variable starts with `-` or `--`.
**Learning:** Even when using lists instead of `shell=True` in `subprocess.run`, CLI tools parse positional arguments starting with hyphens as flags. This can lead to unexpected behavior or security vulnerabilities (e.g., passing `--help` or malicious flags).
**Prevention:** Always use `--` to explicitly denote the end of command-line options before passing dynamic positional arguments to CLI tools.
