from app.models.resource import Resource
from app.models.project import Project
from app.core.logger import logger


def run_autonomous_system(db):

    actions_taken = []
    resources = db.query(Resource).all()
    projects = db.query(Project).all()

    action = f"Reduced cost of resource {r.name}"
    actions_taken.append(action)
    logger.info(action)

    # Detect and adjust expensive resources
    for r in resources:
        if r.cost_per_month > 400:
            r.cost_per_month = r.cost_per_month * 0.9
            actions_taken.append(
                f"Reduced cost of resource {r.name}"
            )

    # Detect risky projects
    for project in projects:
        project_resources = db.query(Resource).filter(
            Resource.project_id == project.id
        ).all()

        total_cost = sum(r.cost_per_month for r in project_resources)

        if total_cost > 2000:
            actions_taken.append(
                f"Project {project.name} flagged for optimization"
            )

    db.commit()

    return {
        "status": "Autonomous AI executed",
        "actions": actions_taken
    }
    
