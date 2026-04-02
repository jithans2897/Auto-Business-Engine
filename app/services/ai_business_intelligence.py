from app.models.resource import Resource
from app.models.project import Project


def run_business_intelligence(db):

    resources = db.query(Resource).all()
    projects = db.query(Project).all()

    total_cost = sum(r.cost_per_month for r in resources)

    # Detect expensive resources
    expensive_resources = [
        {
            "name": r.name,
            "cost_per_month": r.cost_per_month
        }
        for r in resources if r.cost_per_month > 250
    ]

    # Detect underutilized resources
    underutilized = [
        {
            "name": r.name,
            "reason": "Cost high compared to system average"
        }
        for r in resources if r.cost_per_month > (total_cost / max(len(resources), 1))
    ]

    # Cost prediction (simple AI logic for now)
    predicted_next_month_cost = total_cost * 1.15

    # Strategy suggestions
    suggestions = []

    if expensive_resources:
        suggestions.append("Review expensive resources to reduce spending")

    if predicted_next_month_cost > total_cost:
        suggestions.append("Projected cost increase detected")

    return {
        "total_cost": total_cost,
        "predicted_next_month_cost": predicted_next_month_cost,
        "expensive_resources": expensive_resources,
        "underutilized_resources": underutilized,
        "ai_suggestions": suggestions
    }