from jira import JIRA
import os
from dotenv import load_dotenv

load_dotenv()

JIRA_DOMAIN = os.getenv("JIRA_DOMAIN")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API = os.getenv("JIRA_API")
PROJECT_KEY = os.getenv("PROJECT_KEY", "TAP")

jira = JIRA(server=JIRA_DOMAIN, basic_auth=(JIRA_EMAIL, JIRA_API))

def create_jira_issue(summary: str, description: str, issue_type="Task") -> str:
    """
    Creates a Jira issue with given summary and description.
    Returns the ticket ID.
    """
    issue = jira.create_issue(fields={
        'project': {'key': PROJECT_KEY},
        'summary': summary,
        'description': description,
        'issuetype': {'name': issue_type}
    })
    return issue.key
