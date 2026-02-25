# Sentinel Journal - Critical Learnings

## 2025-05-23 - Container Running as Root
**Vulnerability:** The `Dockerfile.sandbox` for the code execution sandbox was running as the `root` user by default. This meant that any code executed within the sandbox (which uses `exec()`) could potentially modify system files, install packages, or facilitate container escape attacks with root privileges.
**Learning:** Even in sandboxed environments, the principle of least privilege must be applied. Docker containers should not run as root unless absolutely necessary.
**Prevention:** Always include a `USER` instruction in Dockerfiles to switch to a non-root user (e.g., UID 1000) after installing necessary dependencies. Ensure file ownership is correctly set for the new user.
