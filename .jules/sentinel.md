## 2025-02-12 - Insecure random number generation in security middleware
**Vulnerability:** The Red Teaming middleware used the `random` module (`random.choice`) to select fields to attack. The `random` module is not cryptographically secure and could allow predictable selection of attack fields.
**Learning:** Security-related modules and middlewares must use cryptographically secure random number generators (e.g., `secrets` module) for any random operations. The `secrets` module was already properly used in the Defense middleware.
**Prevention:** Use `secrets.choice` instead of `random.choice` for resolving strategies and other random selections within security tooling or middlewares.
