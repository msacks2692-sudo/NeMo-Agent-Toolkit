## 2025-05-23 - [CRITICAL] Unprivileged Container Execution & Network Isolation
**Vulnerability:** The `local-sandbox` container runs as `root` and uses `--network=host`. This allows executed code to modify container files, potentially escape to the host, and access host network services (like local databases or internal APIs).
**Learning:** Default Docker configurations often run as root and may use host networking for convenience, sacrificing security. "Sandboxes" must enforce strict isolation.
**Prevention:** Always define a non-root USER in Dockerfiles for applications. Use explicit port mapping (`-p`) instead of host networking (`--network=host`) to isolate the container's network stack.
