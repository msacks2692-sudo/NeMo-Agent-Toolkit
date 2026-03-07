## 2025-10-24 - [Fix insecure random number generation]
**Vulnerability:** The red teaming middleware used the standard `random` module for field resolution strategies, which generates predictable values.
**Learning:** Security-critical functions or middlewares should avoid using predictable PRNGs. Cryptographically secure pseudo-random number generators (CSPRNGs) like the `secrets` module should be used instead.
**Prevention:** Use `secrets.choice` or `secrets.randbelow` instead of `random.choice` or `random.randint` when randomness affects security logic.
