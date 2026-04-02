from app.models.project import Project
from app.models.resource import Resource


def monitor_system(db):
    projects = db.query(Project).all()
    resources = db.query(Resource).all()

    return {
        "projects": len(projects),
        "resources": len(resources)
    }