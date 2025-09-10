---
applyTo: "**/*.py"
description: "Coding standards and best practices for Python code in this project."
---

### Python Guidelines

-   **Style:** Strictly adhere to **PEP 8**.
-   **Comments/Docstrings:** All publicly exported functions, classes, and methods must have complete docstrings. Use inline comments to explain complex logic that is not obvious.
-   **Typing:** Avoid unrestricted use of `Any`. Use type hints for clarity and safety, resorting to `Union` or `Optional` when appropriate.
-   **Immutability:** Prefer immutable data structures when it makes sense to avoid unexpected side effects.