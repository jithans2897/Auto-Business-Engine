from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.agents.llm_react_agent import run_llm_agent

router = APIRouter(tags=["LLM AI Agent"])


@router.post("/ai/llm-agent/{project_id}")
def llm_agent(project_id: int, db: Session = Depends(get_db)):
    return run_llm_agent(db, project_id)