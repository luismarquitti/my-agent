---
description: "Generates a detailed implementation plan for a new feature in the project, following the phased methodology."
variables:
  name: feature_description
  description: "The description of the feature to be implemented."
---
@workspace

You are a Senior AI Systems Architect. I need an implementation plan for the following feature: "{{feature_description}}".

Based on the architecture and standards defined in this project (consulting `PLAN.md`, `CODE_STATE.md`, and `copilot-instructions.md`), please generate a detailed implementation plan in Markdown format, following the phased structure:

1.  **Feature Overview:** A brief summary of the feature.
2.  **Implementation Phases:** Divide the feature into logical phases (e.g., Design, Core Implementation, Tests, Documentation).
3.  **Detailed Tasks per Phase:** For each phase, list the specific tasks to be performed, with `[ ]` checkboxes.
4.  **Affected/New Components:** Identify existing modules and files that will be modified and new ones that will be created.
5.  **Acceptance Criteria:** Define how the success of the implementation will be measured.

Remember to adhere to the **Gated Execution Protocols** defined in `.gemini/GEMINI.md`. This is a **planning** prompt, so **DO NOT GENERATE CODE** in this response.