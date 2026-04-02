from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.ai_report import AIReport

router = APIRouter(tags=["AI Reports"])


@router.get("/ai/reports")
def get_reports(db: Session = Depends(get_db)):
    return db.query(AIReport).all()