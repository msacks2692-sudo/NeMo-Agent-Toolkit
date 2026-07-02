## 2024-05-24 - [Arbitrary Code Execution in Tool Utilities]
**Vulnerability:** Use of `eval()` on unsanitized string input in an LLM tool evaluation function (`calculator`).
**Learning:** Even internal tool utilities or test scaffolding can become attack vectors if they process untruncated string input. `eval()` should never be used for evaluating mathematical expressions when a safer AST parsing approach is available.
**Prevention:** Use `ast.parse(expression, mode='eval')` with an explicit mapping of allowed operators (e.g., `ast.Add`, `ast.Sub`) and node types (e.g., `ast.Constant`) to evaluate dynamic string expressions securely without executing arbitrary code.
