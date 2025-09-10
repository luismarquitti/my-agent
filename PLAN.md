# Development Plan - AI Agent for Jira Issue and Code Analysis

## Project Overview

The goal of this project is to develop an AI agent that automates the analysis and diagnosis of bugs reported in Jira, correlating problem descriptions with the relevant source code. The system will be composed of two collaborative agents: the Analysis Agent (which processes Jira issues) and the Investigation Agent (which searches the code).

## Development Phases

### Phase 1: Foundation of the Analysis Agent and Initial Setup (TO DO)

-   [ ] Configure the Python development environment (venv, requirements.txt).
-   [ ] Implement the connection to the Jira REST API (using `jira-python`).
-   [ ] Develop the module for extracting and summarizing data from the Jira issue.
-   [ ] Implement custom Named Entity Recognition (NER) for software artifacts.
-   [ ] Implement bug category classification (UI/Backend/DB).
-   [ ] Generate the Investigation Query Package (IQP) with a summary, lexical terms, and a semantic vector.

### Phase 2: Core of the Investigation Agent (TO DO)

-   [ ] Configure the RAG pipeline for source code indexing (AST-chunking, GraphCodeBERT).
-   [ ] Implement the local vector database (ChromaDB/FAISS).
-   [ ] Develop the hybrid search strategy (semantic, lexical with ripgrep, historical with Git).
-   [ ] Implement advanced fusion and re-ranking of search results.
-   [ ] Generate the final diagnosis report in Markdown.

### Phase 3: Integration and Refinement (TO DO)

-   [ ] Integrate the Analysis Agent and the Investigation Agent into a complete workflow.
-   [ ] Create end-to-end integration tests.
-   [ ] Implement a feedback loop for continuous improvement of the AI models.
-   [ ] Develop a user interface for interaction (CLI or simple web).

## Immediate Next Steps

-   **Current Task:** Configure the Python development environment, including creating a virtual environment and the initial `requirements.txt` file.