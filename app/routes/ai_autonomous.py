from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.services.ai_autonomous_engine import run_autonomous_system

router = APIRouter(tags=["Autonomous AI Engine"])


@router.post("/ai/autonomous-run")
def autonomous_ai_run(db: Session = Depends(get_db)):
    return run_autonomous_system(db)