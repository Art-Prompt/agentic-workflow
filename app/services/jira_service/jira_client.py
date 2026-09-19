import os

import httpx
from dotenv import load_dotenv
import json

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

def parseIssueDescription(issue_description_content):
    issue_description_text = ""
    
    for node in issue_description_content:
        type = node.get("type", "")
        content = node.get("content", "")

        if type == "paragraph" or type == "heading":
            for item in content:
                item_text = item.get("text", "")
                issue_description_text += item_text + "\n"
        
        if type == "orderedList":
            for item in content:
                item_list = item.get("content", [])
                for sub_item in item_list:
                    sub_item_content = sub_item.get("content", [])
                    orderedList_bullet_points = ""
                    for sub_sub_item in sub_item_content:
                        sub_sub_item_text = sub_sub_item.get("text", "")
                        orderedList_bullet_points += sub_sub_item_text
                
                    issue_description_text += orderedList_bullet_points + "\n"
                    
        if type == "bulletList":
            for item in content:
                item_list = item.get("content", [])
                for sub_item in item_list:
                    sub_item_content = sub_item.get("content", [])
                    bulletList_bullet_points = ""
                    for sub_sub_item in sub_item_content:
                        sub_sub_item_text = sub_sub_item.get("text", "")
                        bulletList_bullet_points += sub_sub_item_text
                    
                    issue_description_text += bulletList_bullet_points + "\n"

    return issue_description_text

async def get_ticket_description(issue_key: str):
    response = await get_issue(issue_key)

    issue_description = response.get("fields", {}).get("description", "")
    issue_description_content = issue_description.get("content", [])

    description_data = json.loads(json.dumps(issue_description_content))
    
    issue_description_text = parseIssueDescription(description_data)
                        
    return issue_description_text