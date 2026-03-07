# Sentinel's Journal - Critical Learnings

This journal records CRITICAL security learnings, vulnerabilities, and patterns specific to this codebase.

## 2026-02-11 - Insecure Docker Networking
**Vulnerability:** The `start_local_sandbox.sh` script used `--network=host`, exposing the container to the host network and potentially allowing access to local services.
**Learning:** Default configurations in setup scripts are often overlooked but critical. Host networking breaks container isolation assumptions.
**Prevention:** Always use explicit port mapping (`-p 127.0.0.1:HOST:CONTAINER`) for local services to enforce network isolation and prevent remote access.
