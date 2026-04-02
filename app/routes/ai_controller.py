from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.services.ai_engine import analyze_project

router = APIRouter(tags=["AI Engine"])


@router.get("/ai/projects/{project_id}/analyze")
def run_ai_analysis(project_id: int, db: Session = Depends(get_db)):
    return analyze_project(db, project_id)