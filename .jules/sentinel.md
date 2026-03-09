## 2024-05-24 - Weak Random Number Generation in Security Middleware
**Vulnerability:** The `RedTeamingMiddleware` used Python's standard `random` module (`random.choice`) for resolving multiple field matches in attack payloads. The standard `random` module is not cryptographically secure and predictable.
**Learning:** Security testing tools and middlewares should use cryptographically secure randomness even for seemingly benign operations like target selection, as predictability could be exploited to evade or manipulate the testing outcomes.
**Prevention:** Always use the `secrets` module (e.g., `secrets.choice`, `secrets.randbelow`) instead of `random` for any logic within security-critical components like red teaming or defense middlewares.
