## 2025-05-27 - Argument Injection Vulnerability via Unsanitized `host_id`
**Vulnerability:** Argument injection via user-supplied `host_id` in `subprocess.run(["ping", "-c", "3", host_id], ...)`
**Learning:** Even without `shell=True`, a command array `["ping", "-c", "3", host_id]` where `host_id` starts with a hyphen (e.g. `-V` or `--help`) will be interpreted by the program as a flag rather than a positional argument, potentially leading to unintended behavior or argument injection.
**Prevention:** When passing dynamic variables as positional arguments to CLI tools in `subprocess.run`, always insert `--` before the variables to force the program to interpret subsequent strings as positional arguments, not options (e.g., `["ping", "-c", "3", "--", host_id]`).
