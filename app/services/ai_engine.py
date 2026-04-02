from sqlalchemy.orm import Session
from app.models.resource import Resource


def analyze_project(db: Session, project_id: int):

    resources = db.query(Resource).filter(Resource.project_id == project_id).all()

    recommendations = []

    total_cost = sum(r.cost_per_month for r in resources)
    active_resources = [r for r in resources if r.status == "ACTIVE"]
    inactive_resources = [r for r in resources if r.status != "ACTIVE"]

    # AI logic rules (version 1)
    if total_cost > 500:
        recommendations.append("Project cost is high. Consider optimizing resources.")

    if len(inactive_resources) > 0:
        recommendations.append("There are inactive resources. Cleanup recommended.")

    if len(active_resources) > 5:
        recommendations.append("High infrastructure usage. Scaling strategy may be needed.")

    if total_cost == 0:
        recommendations.append("No cost detected. Check if resources are configured correctly.")

    return {
        "project_id": project_id,
        "total_resources": len(resources),
        "total_cost": total_cost,
        "recommendations": recommendations
    }