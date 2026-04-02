from app.models.resource import Resource


def analyze_costs(db):
    resources = db.query(Resource).all()

    total_cost = sum(r.cost_per_month for r in resources)

    expensive_resources = [
        {
            "name": r.name,
            "cost_per_month": r.cost_per_month
        }
        for r in resources if r.cost_per_month > 300
    ]

    return {
        "total_monthly_cost": total_cost,
        "expensive_resources": expensive_resources
    }