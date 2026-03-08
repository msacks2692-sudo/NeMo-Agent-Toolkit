## 2024-05-14 - Use Cryptographically Secure PRNGs for Security Logic
**Vulnerability:** Weak random number generation using the standard `random` module for field resolution strategy (`"random"`) in `RedTeamingMiddleware`.
**Learning:** The standard `random` module is not cryptographically secure and should not be used for security-related configurations or logic, such as field resolution strategies in red teaming or defense middlewares. Predictable randomness could lead to reproducible attack patterns.
**Prevention:** Use cryptographically secure pseudo-random number generators (e.g., `secrets.choice`) instead of the standard `random` module for any logic that dictates security behavior, testing, or mitigation.
