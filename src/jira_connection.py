import os
from jira import JIRA

class JiraConnection:
    def __init__(self):
        self.server = os.environ.get('JIRA_SERVER')
        self.username = os.environ.get('JIRA_USERNAME')
        self.api_token = os.environ.get('JIRA_API_TOKEN')
        self.jira = None

    def connect(self):
        """Connects to the Jira server."""
        if not all([self.server, self.username, self.api_token]):
            raise ValueError("JIRA_SERVER, JIRA_USERNAME, and JIRA_API_TOKEN environment variables must be set.")

        try:
            self.jira = JIRA(server=self.server, basic_auth=(self.username, self.api_token))
            print("Successfully connected to Jira.")
        except Exception as e:
            print(f"Failed to connect to Jira: {e}")
            self.jira = None

    def get_issue(self, issue_key):
        """Fetches an issue from Jira."""
        if not self.jira:
            print("Not connected to Jira. Call connect() first.")
            return None
        try:
            issue = self.jira.issue(issue_key)
            return issue
        except Exception as e:
            print(f"Failed to get issue {issue_key}: {e}")
            return None
