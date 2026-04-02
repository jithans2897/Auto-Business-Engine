from app.models.project import Project
from app.models.resource import Resource


def detect_risks(db):
    projects = db.query(Project).all()
    risks = []

    for project in projects:
        resources = db.query(Resource).filter(
            Resource.project_id == project.id
        ).all()

        cost = sum(r.cost_per_month for r in resources)

        if cost > 2000:
            risks.append({
                "project": project.name,
                "risk": "High spending"
            })

    return risks