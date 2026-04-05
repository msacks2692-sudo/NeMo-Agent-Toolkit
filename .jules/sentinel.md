## 2025-02-18 - Argument Injection in subprocess.run
**Vulnerability:** Found `subprocess.run` calls passing dynamic user-provided strings (like package names and search queries) as positional arguments without a `--` separator.
**Learning:** Even without `shell=True`, a malicious string starting with a hyphen (like `--index-url=malicious-url`) can be interpreted by the target CLI as an option instead of a positional argument, leading to argument injection.
**Prevention:** Always use `--` to separate options from positional arguments when passing untrusted input to a CLI via `subprocess.run`.
