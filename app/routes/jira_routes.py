from fastapi import APIRouter

from app.services.jira_service.jira_client import (
    get_issue,
    get_current_user,
)

router = APIRouter(prefix="/jira", tags=["jira"])


@router.get("/me")
async def get_jira_current_user():
    return await get_current_user()


@router.get("/{issue_key}")
async def get_jira_issue(issue_key: str):
    return await get_issue(issue_key)
