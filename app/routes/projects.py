from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectResponse
from typing import Optional
from app.schemas.project import ProjectStatus
from app.services import project_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/projects", response_model=ProjectResponse)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return project_service.create_project(db, project)
  
@router.get("/projects/search", response_model=list[ProjectResponse])
def search_projects(query: str, db: Session = Depends(get_db)):
    return project_service.search_projects(db, query)

@router.get("/projects", response_model=list[ProjectResponse])
def get_projects(
    status: Optional[ProjectStatus] = None,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    return project_service.get_projects(db, status, limit, offset)

@router.get("/projects/{project_id}", response_model=ProjectResponse)
def update_projects(project_id: int, updated_project: ProjectCreate, db: Session = Depends(get_db)):
    return project_service.update_project(db, project_id, updated_project)
      
@router.put("/projects/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, updated_project: ProjectCreate, db: Session = Depends(get_db)):
    return project_service.update_project(db, project_id, updated_project)

@router.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project_service.delete_project(db, project_id)
    return {"message": "Project deleted"}
   



