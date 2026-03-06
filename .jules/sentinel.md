## 2025-05-18 - [MEDIUM] Fix weak random number generation
**Vulnerability:** The Red Teaming middleware used the `random` module for selecting fields (`random.choice(matches)`). The `random` module is pseudo-random and not secure for cryptographic use cases.
**Learning:** Security-related logic, such as randomized field selections in attack middlewares or defense middlewares, must use cryptographically secure random number generators (CSPRNG) like the `secrets` module instead of `random`.
**Prevention:** Replace instances of `import random` with `import secrets` and `random.choice()` with `secrets.choice()` when handling sensitive or attack/defense-related operations.
