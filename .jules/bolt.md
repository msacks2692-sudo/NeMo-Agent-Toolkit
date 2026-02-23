## 2025-05-22 - [Optimistic Parsing]
**Learning:** Blindly sanitizing inputs (like replacing quotes) before parsing can break valid data and wastes CPU/memory on the happy path.
**Action:** Always attempt the strict/happy path parsing first (e.g., `json.loads`) and only apply sanitization/fallbacks in the exception handler.
