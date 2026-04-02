from app.models.resource import Resource
from app.models.project import Project


def generate_strategy(db, project_id):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return {
            "error": "Project not found"
        }
    resources = db.query(Resource).filter(Resource.project_id == project_id).all()

    total_cost = sum(r.cost_per_month for r in resources)
    resource_count = len(resources)

    risk_score = "Low"
    priority = "Normal"
    action = "Project running normally"

    if total_cost > 500:
        risk_score = "Medium"
        action = "Optimize resource allocation"
        priority = "High"

    if total_cost > 1000:
        risk_score = "High"
        action = "Immediate cost reduction required"
        priority = "Critical"

    efficiency = 100 - (total_cost / 20)

    return {
        "project": project.name,
        "risk_score": risk_score,
        "total_cost": total_cost,
        "resources": resource_count,
        "efficiency": round(efficiency, 2),
        "priority": priority,
        "recommended_action": action
    }