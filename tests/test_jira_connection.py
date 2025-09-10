import unittest
from unittest.mock import patch
from src.jira_connection import JiraConnection

class TestJiraConnection(unittest.TestCase):

    @patch.dict('os.environ', {'JIRA_SERVER': 'https://your-jira-instance.atlassian.net', 'JIRA_USERNAME': 'user@example.com', 'JIRA_API_TOKEN': 'your_api_token'})
    def test_init_with_env_vars(self):
        conn = JiraConnection()
        self.assertEqual(conn.server, 'https://your-jira-instance.atlassian.net')
        self.assertEqual(conn.username, 'user@example.com')
        self.assertEqual(conn.api_token, 'your_api_token')

    def test_init_without_env_vars_raises_error(self):
        with self.assertRaises(ValueError):
            conn = JiraConnection()
            conn.connect()

if __name__ == '__main__':
    unittest.main()
