## 2025-02-09 - Local Sandbox Security Gap
**Vulnerability:** Local Code Execution Sandbox ran as root and used `--network=host`.
**Learning:** Default Docker configurations often default to root execution and some "convenient" flags like host networking break isolation completely.
**Prevention:** Explicitly create non-root user in Dockerfile and map ports instead of using host network. Handle cross-platform GID collisions (macOS vs Linux) using `|| true` and `-o`.
