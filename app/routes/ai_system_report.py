from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.services.ai_system_report import generate_system_report

router = APIRouter(tags=["AI Intelligence"])


@router.get("/ai/system-report")
def system_report(db: Session = Depends(get_db)):
    return generate_system_report(db)