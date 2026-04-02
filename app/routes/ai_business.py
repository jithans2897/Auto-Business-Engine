from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.services.ai_business_intelligence import run_business_intelligence

router = APIRouter(tags=["AI Business Intelligence"])


@router.get("/ai/business-intelligence")
def ai_business_intelligence(db: Session = Depends(get_db)):
    return run_business_intelligence(db)