from fastapi import FastAPI

from app.routes.jira_routes import router as jira_router

app = FastAPI()

app.include_router(jira_router)