from app.models.project import Project
from app.models.resource import Resource


def generate_system_report(db):
    projects = db.query(Project).all()
    resources = db.query(Resource).all()

    total_projects = len(projects)
    total_resources = len(resources)

    total_cost = sum(r.cost_per_month for r in resources)

    high_cost_projects = []

    for project in projects:
        project_resources = [
            r for r in resources if r.project_id == project.id
        ]

        project_cost = sum(r.cost_per_month for r in project_resources)

        if project_cost > 1000:
            high_cost_projects.append({
                "project_id": project.id,
                "project_name": project.name,
                "monthly_cost": project_cost
            })

    insights = []

    if total_cost > 5000:
        insights.append("System cost is growing fast")

    if total_projects > 5:
        insights.append("Platform scaling detected")

    if not insights:
        insights.append("System operating normally")

    return {
        "system_overview": {
            "total_projects": total_projects,
            "total_resources": total_resources,
            "total_monthly_cost": total_cost
        },
        "high_cost_projects": high_cost_projects,
        "ai_insights": insights
    }