from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.services.ai_decision_engine import generate_strategy

router = APIRouter(tags=["AI Strategy"])


@router.post("/ai/strategy/{project_id}")
def ai_strategy(project_id: int, db: Session = Depends(get_db)):
    return generate_strategy(db, project_id)