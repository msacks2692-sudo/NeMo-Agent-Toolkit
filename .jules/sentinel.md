## 2025-02-23 - Local Sandbox Network Exposure
**Vulnerability:** The `start_local_sandbox.sh` script used `--network=host`, exposing the unauthenticated code execution service on `0.0.0.0:6000` to the entire network.
**Learning:** Development tools intended for local use often default to permissive network settings (like `--network=host` or `0.0.0.0` binding) for convenience, but this creates critical RCE vulnerabilities if used on untrusted networks.
**Prevention:** Always bind local development services to `127.0.0.1` unless external access is explicitly required and secured. Use `-p 127.0.0.1:HOST_PORT:CONTAINER_PORT` instead of `--network=host`.
