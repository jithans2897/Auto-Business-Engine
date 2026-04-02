from sqlalchemy.orm import Session
from app.models.resource import Resource
from app.schemas.resource_schema import ResourceCreate
from sqlalchemy import func
from app.models.resource import Resource


def create_resource(db: Session, resource: ResourceCreate):
    new_resource = Resource(
        name=resource.name,
        type=resource.type,
        project_id=resource.project_id,
        cost_per_month=resource.cost_per_month,
        status="ACTIVE"
    )

    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)

    return new_resource


def get_resources(db: Session):
    return db.query(Resource).all()


def get_resources_by_project(db: Session, project_id: int):
    return db.query(Resource).filter(Resource.project_id == project_id).all()

def get_project_summary(db: Session, project_id: int):
    total_resources = db.query(Resource).filter(
        Resource.project_id == project_id
    ).count()

    active_resources = db.query(Resource).filter(
        Resource.project_id == project_id,
        Resource.status == "ACTIVE"
    ).count()

    total_cost = db.query(func.sum(Resource.cost_per_month)).filter(
        Resource.project_id == project_id
    ).scalar()

    if total_cost is None:
        total_cost = 0

    return {
        "project_id": project_id,
        "total_resources": total_resources,
        "active_resources": active_resources,
        "total_monthly_cost": total_cost
    }