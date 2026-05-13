## 2024-10-24 - [Optimize JSON validation]
**Learning:** When optimizing JSON validation, use a 'try-parse first' strategy instead of blanket string replacements (e.g., replacing single quotes with double quotes) before parsing. This prevents corrupting valid JSON that legitimately contains the replaced characters and avoids performance overhead on the happy path.
**Action:** Always attempt to parse the original string first. Only fallback to quote replacement and a second parse attempt if the initial parse fails and single quotes are actually present in the string.
## 2024-10-24 - [Mocking dynamically accessed dependencies]
**Learning:** When mocking complex external modules (like `nemo_microservices`) to run pytest in restricted environments, simple class mocks fail if the code heavily relies on dynamic or nested attribute access.
**Action:** Create a mock module class inheriting from `types.ModuleType` that implements `__getattr__` to recursively return new instances of itself. This allows arbitrary nested attribute access during test collection without triggering `AttributeError`.
