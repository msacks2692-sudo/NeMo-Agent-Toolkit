## 2026-04-04 - Prevent Argument Injection in Subprocess
**Vulnerability:** Argument injection via joined strings and missing `--` when passing lists to subprocess commands (e.g., `uv pip install`).
**Learning:** When passing lists of user-provided or dynamic arguments to a subprocess, joining them with spaces allows injecting malicious arguments. Further, using `--` indicates the end of command options, preventing injection even if an argument starts with `-`.
**Prevention:** Pass arguments as a list (using `.extend()`) and explicitly use `--` before variadic positional arguments.
