from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database.db import SessionLocal
from app.schemas.resource_schema import ResourceCreate, ResourceResponse
from app.services import resource_service
from app.database.db import get_db

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/resources", response_model=ResourceResponse)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    return resource_service.create_resource(db, resource)


@router.get("/resources", response_model=list[ResourceResponse])
def get_resources(db: Session = Depends(get_db)):
    return resource_service.get_resources(db)


@router.get("/projects/{project_id}/resources", response_model=list[ResourceResponse])
def get_project_resources(project_id: int, db: Session = Depends(get_db)):
    return resource_service.get_resources_by_project(db, project_id)

@router.get("/projects/{project_id}/summary")
def project_summary(project_id: int, db: Session = Depends(get_db)):
    return resource_service.get_project_summary(db, project_id)