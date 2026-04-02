from app.services.ai_optimizer import optimize_project
from app.models.project import Project


def run_optimization(db):
    projects = db.query(Project).all()
    results = []

    for project in projects:
        result = optimize_project(db, project.id)
        results.append(result)

    return results