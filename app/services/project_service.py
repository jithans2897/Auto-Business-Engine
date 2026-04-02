from sqlalchemy.orm import Session
from typing import Optional
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectStatus


def create_project(db: Session, project: ProjectCreate):
    new_project = Project(
        name=project.name,
        description=project.description,
        status=project.status
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


def get_projects(db: Session, status: Optional[ProjectStatus], limit: int, offset: int):
    query = db.query(Project)

    if status:
        query = query.filter(Project.status == status)

    return query.offset(offset).limit(limit).all()


def get_project_by_id(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()


def update_project(db: Session, project_id: int, updated_project: ProjectCreate):
    project = db.query(Project).filter(Project.id == project_id).first()

    project.name = updated_project.name
    project.description = updated_project.description
    project.status = updated_project.status

    db.commit()
    db.refresh(project)

    return project


def delete_project(db: Session, project_id: int):
    project = db.query(Project).filter(Project.id == project_id).first()

    db.delete(project)
    db.commit()

    return project

def search_projects(db: Session, query: str):
    return db.query(Project).filter(
        Project.name.ilike(f"%{query}%")
    ).all()