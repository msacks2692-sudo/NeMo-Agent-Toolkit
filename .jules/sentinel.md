## 2025-05-18 - [Secure Local Sandbox Container]
**Vulnerability:** The local code execution sandbox container was running as root and binding to `0.0.0.0` with host networking (`--network=host`), exposing the RCE service to external networks and increasing the risk of container escape.
**Learning:** Default Docker configurations often run as root and bind to all interfaces. "Local" tools must explicitly bind to `127.0.0.1` and use non-root users to minimize attack surface.
**Prevention:** Always use `USER <non-root>` in Dockerfiles for services. Use `-p 127.0.0.1:port:port` instead of `--network=host` or `0.0.0.0` binding for local-only services.
