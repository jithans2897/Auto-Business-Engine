from app.models.project import Project
from app.models.resource import Resource


def get_project_data(db, project_id):
    project = db.query(Project).filter(Project.id == project_id).first()
    resources = db.query(Resource).filter(Resource.project_id == project_id).all()

    total_cost = sum(r.cost_per_month for r in resources)

    return {
        "project": project.name,
        "total_cost": total_cost,
        "resources": [
            {"name": r.name, "cost": r.cost_per_month}
            for r in resources
        ]
    }


def optimize_resources(db, project_id):
    resources = db.query(Resource).filter(Resource.project_id == project_id).all()

    actions = []

    for r in resources:
        if r.cost_per_month > 300:
            r.cost_per_month *= 0.9
            actions.append(f"Reduced cost of {r.name}")

    db.commit()

    return {"actions": actions}