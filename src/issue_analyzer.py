import spacy

from src.iqp import IQP

class IssueAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def analyze_issue(self, issue_text):
        """Analyzes a Jira issue and returns an IQP object."""
        summary = self.summarize_issue(issue_text)
        lexical_terms = self.extract_technical_entities(issue_text)
        bug_category = self.classify_bug_category(issue_text)
        # Semantic vector generation will be implemented later.
        semantic_vector = None
        return IQP(summary, lexical_terms, bug_category, semantic_vector)

    def summarize_issue(self, issue_text):
        """Summarizes the text of a Jira issue."""
        if not issue_text:
            return ""

        doc = self.nlp(issue_text)
        sentences = [sent.text for sent in doc.sents]
        # A simple summarization by taking the first few sentences.
        def extract_technical_entities(self, issue_text):
        """Extracts technical entities from the issue text."""
        if not issue_text:
            return []

        doc = self.nlp(issue_text)
        def classify_bug_category(self, issue_text):
        """Classifies the bug category based on keywords."""
        if not issue_text:
            return "Other"

        text = issue_text.lower()
        if any(keyword in text for keyword in ["ui", "frontend", "button", "click"]):
            return "UI/Frontend"
        if any(keyword in text for keyword in ["backend", "api", "server", "database"]):
            return "Backend/API"
        if any(keyword in text for keyword in ["performance", "slow", "lag"]):
            return "Performance"
        if any(keyword in text for keyword in ["security", "vulnerability"]):
            return "Security"
        if any(keyword in text for keyword in ["build", "deployment"]):
            return "Build/Deployment"

        return "Other"
