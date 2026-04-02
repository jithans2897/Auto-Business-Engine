from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.agents.react_agent import react_agent_loop

router = APIRouter(tags=["ReAct AI Agent"])


@router.post("/ai/react/{project_id}")
def run_react_agent(project_id: int, db: Session = Depends(get_db)):
    return react_agent_loop(db, project_id)