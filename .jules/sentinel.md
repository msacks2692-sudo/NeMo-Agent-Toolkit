## 2025-02-14 - Argument Injection in Subprocess Commands
**Vulnerability:** Subprocess calls to external binaries (`uv`, `pip`, `twine`) in `pypi_handler.py` and `rest_handler.py` passed untrusted/external values (package names, paths, queries) as positional arguments without the `--` separator.
**Learning:** Python`s `subprocess.run` does not inherently protect against argument injection if an attacker-controlled string starts with `-` or `--`, allowing them to inject arbitrary flags into the target binary.
**Prevention:** Always insert the `--` delimiter before passing any dynamic or external variable as a positional argument in `subprocess` command lists to enforce that subsequent items are treated strictly as positional data.
