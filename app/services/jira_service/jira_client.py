import os

import httpx
from dotenv import load_dotenv

load_dotenv()

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")


async def get_issue(issue_key: str):
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}"

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            auth=(JIRA_EMAIL, JIRA_API_TOKEN),
            headers={
                "Accept": "application/json"
            }
        )

    response.raise_for_status()

    return response.json()

async def check_issue_permissions(issue_key: str):
    url = f"{JIRA_BASE_URL}/rest/api/3/mypermissions"

    params = {
        "issueKey": issue_key,
        "permissions": "BROWSE_PROJECTS"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            params=params,
            auth=(JIRA_EMAIL, JIRA_API_TOKEN),
            headers={
                "Accept": "application/json"
            }
        )

    response.raise_for_status()

    return response.json()

async def get_current_user():
    url = f"{JIRA_BASE_URL}/rest/api/3/myself"

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            auth=(JIRA_EMAIL, JIRA_API_TOKEN),
            headers={
                "Accept": "application/json"
            }
        )

    response.raise_for_status()

    return response.json()