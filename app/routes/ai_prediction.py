from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.services.ai_prediction_engine import predict_project_growth

router = APIRouter(tags=["AI Prediction"])


@router.get("/ai/predict/project-growth/{project_id}")
def predict_growth(project_id: int, db: Session = Depends(get_db)):
    return predict_project_growth(db, project_id)