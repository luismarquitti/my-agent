# Project: AI Agent for Jira Issue and Code Analysis

## Project Overview

This repository contains the implementation of an AI Agent designed to automate the analysis of Jira issues and investigate the codebase to identify the root cause of bugs. It uses an architecture of two specialized agents: an **Analysis Agent** to interpret Jira issues and an **Investigation Agent** to perform hybrid searches (semantic, lexical, and historical) in the source code.

The development methodology of this project is AI-assisted, using control files (`PLAN.md`, `CODE_STATE.md`, `CHANGELOG.md`) and specific configurations for GitHub Copilot and the Gemini CLI, all contained in this repository.

## Project Structure

-   `/src`: Contains the main source code of the agent.
-   `/tests`: Contains unit and integration tests.
-   `/docs`: Contains additional documentation and guides.
-   `/scripts`: Contains automation scripts, such as the indexing pipeline.
-   `PLAN.md`: The strategic development plan for the project.
-   `CODE_STATE.md`: A "snapshot" of the current architecture and code state.
-   `CHANGELOG.md`: The history of significant changes and AI interactions.

## Immediate Next Steps

Consult `PLAN.md` for the next tasks and `CODE_STATE.md` for a detailed description of the current state.

## Reusable Prompts Guide

This repository contains a series of reusable prompts that can be used for different AI-assisted development tasks. Below is a list of available prompts and their descriptions:

1. **Prompt review-code**
   - Description: Performs a senior-level code review on the selected code, based on project standards.
   - Location: `.github/prompts/review-code.prompt.md`

2. **Prompt analyze-issue**
   - Description: Analyzes the text of a Jira issue and extracts structured information for the Analysis Agent.
   - Location: `.github/prompts/analyze-issue.prompt.md`

3. **Prompt plan-feature**
   - Description: Generates a detailed implementation plan for a new feature in the project, following the phased methodology.
   - Location: `.github/prompts/plan-feature.prompt.md`

4. **Prompt generate-tests**
   - Description: Generates unit tests for the selected Python code using Pytest, covering important scenarios.
   - Location: `.github/prompts/generate-tests.prompt.md`