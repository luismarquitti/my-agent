# Current Code State - AI Agent for Jira Issue and Code Analysis

*Last updated: 2025-09-10 10:00*

## General Architecture

This project will be architected as a system of agent-based microservices, with two main components in Python: an Analysis Agent for processing Jira issues and an Investigation Agent for code search and analysis. The initial communication will be internal, with the goal of generating a diagnostic report.

## File Structure

-   `/src`: Contains the main source code.
    -   `main.py`: Main entry point of the system.
-   `/tests`: Contains the tests.
    -   `test_analysis_agent.py`: Initial test file for the Analysis Agent.
-   `/docs`: Folder for technical and design documentation.
-   `/scripts`: Contains automation scripts.
    -   `index_codebase.py`: Placeholder script for the code indexing pipeline.
-   `.github/`: Contains configuration files for GitHub Copilot and GitHub Actions.
-   `.gemini/`: Contains configuration and context files for the Gemini CLI.
-   `PLAN.md`: Project development plan.
-   `CODE_STATE.md`: Snapshot of the current code state and architectural decisions.
-   `CHANGELOG.md`: Record of changes and interactions of the AI agent.
-   `requirements.txt`: Python dependencies.

## Main Components (Initial State)

### `src/main.py`

-   **Responsibility:** System entry point. Currently, a stub.
-   **Dependencies:** None explicit yet.
-   **How it works:** (Placeholder) Will be responsible for orchestrating the execution of the two agents.

## Suggested Technical Next Steps

-   Install the initial Python dependencies (e.g., `jira-python`, `spacy`, `transformers`).
-   Start implementing the connection to the Jira API in `src/main.py`.
-   Define the initial data schema for the Investigation Query Package (IQP).