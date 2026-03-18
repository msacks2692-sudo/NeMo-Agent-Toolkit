## 2025-02-12 - Secure Random Number Generation
**Vulnerability:** Weak random number generation (`random.choice`) was used for security-related configuration (target field resolution strategy) in `RedTeamingMiddleware`.
**Learning:** Using standard pseudo-random number generators (`random`) in security contexts can lead to predictable behavior and fails SAST checks (like Bandit B311).
**Prevention:** Use cryptographically secure pseudo-random number generators (e.g., `secrets.choice`) for security-related modules to ensure defense-in-depth.
