## 2024-05-24 - Weak Random Number Generator in Security Logic
**Vulnerability:** Weak PRNG (`random.choice`) used in security/red-teaming configurations (`target_field_resolution_strategy` in `RedTeamingMiddleware`).
**Learning:** Security configurations should use cryptographically secure random number generators (`secrets`) to prevent predictability in attack simulations or defensive mechanisms.
**Prevention:** Use `secrets.choice` instead of `random.choice` for any security-related randomized decisions.
