from app.models.project import Project
from app.models.resource import Resource


def predict_project_growth(db, project_id):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return {"error": "Project not found"}

    resources = db.query(Resource).filter(Resource.project_id == project_id).all()

    current_monthly_cost = sum(r.cost_per_month for r in resources)

    # Simple prediction model (growth estimation)
    growth_rate = 0.12  # 12% projected growth

    month_1 = int(current_monthly_cost * (1 + growth_rate))
    month_2 = int(month_1 * (1 + growth_rate))
    month_3 = int(month_2 * (1 + growth_rate))

    risk_level = "LOW"

    if current_monthly_cost > 2000:
        risk_level = "MEDIUM"

    if current_monthly_cost > 5000:
        risk_level = "HIGH"

    return {
        "project": project.name,
        "current_monthly_cost": current_monthly_cost,
        "predicted_growth": {
            "next_month": month_1,
            "month_2": month_2,
            "month_3": month_3
        },
        "risk_level": risk_level
    }