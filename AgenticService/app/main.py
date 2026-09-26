from fastapi import FastAPI

from app.routes.jira_routes import router as jira_router
from app.routes.test_ollama_routes import router as ollama_test_router

app = FastAPI()

app.include_router(jira_router)
app.include_router(ollama_test_router)