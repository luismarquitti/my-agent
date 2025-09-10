import unittest
from src.issue_analyzer import IssueAnalyzer

class TestIssueAnalyzer(unittest.TestCase):

    def test_summarize_issue(self):
        analyzer = IssueAnalyzer()
        issue_text = ("This is a test issue. It has multiple sentences. "
                      "The goal is to test the summarization feature. "
                      "This is the fourth sentence and should not be in the summary.")
        summary = analyzer.summarize_issue(issue_text)
        expected_summary = "This is a test issue. It has multiple sentences. The goal is to test the summarization feature. "
        self.assertEqual(summary, expected_summary)

    """    def test_extract_technical_entities(self):
        analyzer = IssueAnalyzer()
        issue_text = "The application crashes when using the new feature on a Google Chrome browser. The error is a 500 Internal Server Error."
        entities = analyzer.extract_technical_entities(issue_text)
        self.assertIn("Google Chrome", entities)

    def test_classify_bug_category(self):
        analyzer = IssueAnalyzer()
        self.assertEqual(analyzer.classify_bug_category("The button is not working on the UI"), "UI/Frontend")
        self.assertEqual(analyzer.classify_bug_category("The server is returning a 500 error"), "Backend/API")
        self.assertEqual(analyzer.classify_bug_category("The application is very slow"), "Performance")
        self.assertEqual(analyzer.classify_bug_category("There is a security vulnerability"), "Security")
        self.assertEqual(analyzer.classify_bug_category("The build is failing"), "Build/Deployment")
        self.assertEqual(analyzer.classify_bug_category("This is a random bug"), "Other")

    def test_analyze_issue(self):
        analyzer = IssueAnalyzer()
        issue_text = "The button is not working on the UI. The application crashes when using the new feature on a Google Chrome browser."
        iqp = analyzer.analyze_issue(issue_text)
        self.assertEqual(iqp.summary, "The button is not working on the UI. The application crashes when using the new feature on a Google Chrome browser. ")
        self.assertIn("Google Chrome", iqp.lexical_terms)
        self.assertEqual(iqp.bug_category, "UI/Frontend")

    def test_summarize_empty_text(self):
        analyzer = IssueAnalyzer()
        summary = analyzer.summarize_issue("")
        self.assertEqual(summary, "")
""

if __name__ == '__main__':
    unittest.main()
