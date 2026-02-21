## 2024-05-22 - Unauthenticated Local Code Execution Exposure
**Vulnerability:** The local code execution sandbox (`local_sandbox`) ran as root and bound to all network interfaces (`--network=host`), exposing an unauthenticated Python execution endpoint to the local network.
**Learning:** Development tools often default to convenience (root, host network) over security, creating risks even in "local" setups.
**Prevention:** Always run containers as non-root users and bind sensitive local services explicitly to `127.0.0.1`.
