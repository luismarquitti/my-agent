---
description: "Performs a senior-level code review on the selected code, based on project standards."
---
@workspace

You are a senior software architect. Review the selected Python code (`{{selection}}`) for the 'Jira Bug Analysis Agent' project.
Your review should focus on the following aspects, as defined in `copilot-instructions.md` and `code-rules.instructions.md`:
1.  **Coding Standards (PEP 8, Docstrings, Type Hints):** Identify any violations.
2.  **Potential Bugs:** Suggest improvements for error handling, race conditions, or flawed logic.
3.  **Modularity and Design:** Evaluate the clarity, cohesion, and coupling of the code.
4.  **Improvement Suggestions:** Propose refactorings to optimize performance or maintainability.

Present your feedback in Markdown format, with code examples when appropriate.