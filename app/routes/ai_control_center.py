from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.services.ai_control_center import system_overview
from app.services.ai_control_center import run_ai_control_center

router = APIRouter(tags=["AI Control Center"])


@router.get("/ai/control-center")
def control_center(db: Session = Depends(get_db)):
    return system_overview(db)

@router.get("/ai/control-center")
def ai_control_center(db: Session = Depends(get_db)):
    return run_ai_control_center(db)