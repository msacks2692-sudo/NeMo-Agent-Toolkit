## 2024-03-17 - Update Random Number Generation to be Cryptographically Secure
**Vulnerability:** Use of non-cryptographically secure random number generator (`random.choice`) for security-related logic (field resolution strategies in RedTeamingMiddleware).
**Learning:** SAST tools like Bandit will flag standard `random` module usage (B311 rule) as insecure for security logic, even if the specific operation is picking a random target field match.
**Prevention:** Always use `secrets.choice` or other `secrets` module functions instead of `random` for any security, defense, or red-teaming logic to provide defense-in-depth and eliminate SAST warnings.
