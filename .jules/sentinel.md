
## 2025-04-10 - [Argument Injection in subprocess calls]
**Vulnerability:** Found argument injection vulnerabilities in `subprocess.run` calls within `PypiRegistryHandler` and `RestRegistryHandler` when executing `twine upload` and `uv pip install`.
**Learning:** When passing dynamic elements (like file paths or package names) to shell utilities via `subprocess.run`, if an element begins with a hyphen (e.g. `-malicious`), the utility may incorrectly interpret it as an option instead of a positional argument, leading to unexpected behavior or remote command execution (if a utility parses it as such). Also learned that `pip search` is deprecated via XML-RPC and should not be relied upon.
**Prevention:** Always insert the POSIX standard `--` delimiter in `subprocess.run` command lists before appending positional arguments to ensure tools interpret subsequent arguments strictly as positional operands.
