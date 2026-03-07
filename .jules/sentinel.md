## 2025-05-22 - Code Execution Sandbox Hardening
**Vulnerability:** The local code execution sandbox was running as root inside the container with `--network=host`, allowing full access to the host network stack and potentially the filesystem if a container escape occurred.
**Learning:** Development tools and "local sandboxes" often prioritize convenience over security, defaulting to permissive settings that can be dangerous if exposed or used with untrusted input.
**Prevention:** Always follow the principle of least privilege: run containers as non-root users and use explicit port mapping instead of host networking to isolate the container environment.
