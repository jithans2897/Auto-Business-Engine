from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.services.analytics_services import get_project_analytics

router = APIRouter(tags=["Analytics"])


@router.get("/projects/{project_id}/analytics")
def project_analytics(project_id: int, db: Session = Depends(get_db)):
    return get_project_analytics(db, project_id)