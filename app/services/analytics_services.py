from sqlalchemy.orm import Session
from app.models.resource import Resource


def get_project_analytics(db: Session, project_id: int):
    resources = db.query(Resource).filter(Resource.project_id == project_id).all()

    total_resources = len(resources)

    total_cost = sum(r.cost_per_month for r in resources)

    active_resources = len([r for r in resources if r.status == "ACTIVE"])
    inactive_resources = len([r for r in resources if r.status != "ACTIVE"])

    return {
        "project_id": project_id,
        "total_resources": total_resources,
        "total_monthly_cost": total_cost,
        "active_resources": active_resources,
        "inactive_resources": inactive_resources
    }