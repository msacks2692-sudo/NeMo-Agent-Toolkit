## 2025-05-15 - [CRITICAL] Code Execution Sandbox Running as Root
**Vulnerability:** The local code execution sandbox (`src/nat/tool/code_execution/local_sandbox/`) was running as root inside the Docker container and using host networking (`--network=host`).
**Learning:** Default Docker behavior runs as root. Convenience setups often skip user creation, leaving the container vulnerable to privilege escalation if a breakout occurs. Host networking exposes the container to the host's entire network stack.
**Prevention:** Always create a non-root user in Dockerfiles for services executing untrusted code. Use specific port bindings (`-p 127.0.0.1:port:port`) instead of host networking to isolate the container.
