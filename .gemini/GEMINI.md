# Gemini Global Context - AI Agent for Jira Issue and Code Analysis

## Project Overview

This is the repository for the AI agent that analyzes Jira issues and the source code. The project is built in Python and aims to automate the detection of the root cause of bugs.

## General Agent Architecture

The system is divided into two distinct Python agents:
1.  **Analysis Agent:** Responsible for interacting with the Jira API, extracting and summarizing information from issues, and generating an 'Investigation Query Package' (IQP).
2.  **Investigation Agent:** Receives the IQP and performs a multimodal search (semantic, lexical, and historical) on the source code, using an advanced RAG pipeline.

The code search will use a local vector database (ChromaDB/FAISS) and code-specific embedding models (GraphCodeBERT).

## Preferred Technology Stack

-   **Main Language:** Python 3.9+
-   **Key Libraries:** `jira-python`, `spacy`, `transformers`, `chromadb` (or `faiss-cpu`), `GitPython`, `ripgrep` (via subprocess).
-   **Testing Framework:** Pytest

## Coding Standards and Style Guide

-   Follow the **PEP 8** guidelines for Python code.
-   Use detailed **docstrings** (Sphinx or Google format) for all functions, classes, and modules.
-   Prefer **type hints** whenever possible for clarity and safety.
-   Keep the code modular with high cohesion and low coupling.
-   Prioritize robust error handling and clear logging.

## Gated Execution Protocols

Your main function is to assist me in the development of this agent. It is CRITICAL that you follow the execution protocols.

<PROTOCOL:PLAN>
### PLANNING MODE ACTIVATED
### Your only function in this mode is to investigate and formulate a step-by-step plan.
### You MUST NOT write, modify, or execute any code on the file system.
### Use the file reading and search tools to analyze the current state of the project.
### Present the plan in Markdown format for my approval.
</PROTOCOL:PLAN>

<PROTOCOL:IMPLEMENT>
### IMPLEMENTATION MODE ACTIVATED
### This mode is only activated after I have approved a plan.
### You are now authorized to use the WriteFile, Edit, and Shell tools to implement the approved plan.
### Follow the approved plan precisely. Do not deviate without my explicit confirmation.
</PROTOCOL:IMPLEMENT>