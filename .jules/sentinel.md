## 2025-02-12 - Critical Sandbox Vulnerability Fix
**Vulnerability:** The local code execution sandbox was configured to run as the `root` user inside the container and used `--network=host`, exposing the host's network stack and providing potential root access upon container escape.
**Learning:** Convenience features in Docker configurations (like host networking for easier connectivity or default root user for easier permission management) can catastrophically compromise the security of a sandbox environment intended to run untrusted code.
**Prevention:**
1. Always create and switch to a non-root user (e.g., `UID 1000`) in Dockerfiles for applications.
2. Avoid `--network=host`. Use explicit port binding (e.g., `-p 127.0.0.1:PORT:PORT`) to isolate the container network and bind to localhost only.
