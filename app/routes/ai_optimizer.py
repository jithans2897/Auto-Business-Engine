from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.services.ai_optimizer import optimize_project

router = APIRouter(tags=["AI Optimization"])


@router.post("/ai/optimize/{project_id}")
def optimize(project_id: int, db: Session = Depends(get_db)):
    return optimize_project(db, project_id)