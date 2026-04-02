from app.models.project import Project
from app.models.resource import Resource


def optimize_project(db, project_id):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return {"error": "Project not found"}

    resources = db.query(Resource).filter(Resource.project_id == project_id).all()

    total_cost = sum(r.cost_per_month for r in resources)

    changes = []

    # AI optimization logic
    if total_cost > 1000:
        for r in resources:
            if r.cost_per_month > 300:
                old_cost = r.cost_per_month
                r.cost_per_month = int(r.cost_per_month * 0.9)  # reduce by 10%

                changes.append({
                    "resource": r.name,
                    "old_cost_per_month": old_cost,
                    "new_cost_per_month": r.cost_per_month
                })

    db.commit()

    return {
        "project": project.name,
        "total_monthly_cost_before": total_cost,
        "optimization_changes": changes if changes else "No optimization needed"
    }