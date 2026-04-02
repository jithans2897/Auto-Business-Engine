from app.models.project import Project
from app.models.resource import Resource


def system_overview(db):
    projects = db.query(Project).all()
    resources = db.query(Resource).all()

    total_projects = len(projects)
    total_resources = len(resources)

    total_cost = sum(r.cost_per_month for r in resources)

    high_risk_projects = []
    alerts = []

    for project in projects:
        project_resources = [r for r in resources if r.project_id == project.id]
        project_cost = sum(r.cost_per_month for r in project_resources)

        if project_cost > 1000:
            high_risk_projects.append(project.name)
            alerts.append(f"High cost detected in {project.name}")

    return {
        "system_status": "Operational",
        "total_projects": total_projects,
        "total_resources": total_resources,
        "total_system_cost": total_cost,
        "high_risk_projects": high_risk_projects,
        "alerts": alerts
    }

from app.agents.monitor_agent import monitor_system
from app.agents.finance_agent import analyze_costs
from app.agents.risk_agent import detect_risks
from app.agents.optimization_agent import run_optimization


def run_ai_control_center(db):
    monitor = monitor_system(db)
    finance = analyze_costs(db)
    risks = detect_risks(db)
    optimization = run_optimization(db)

    return {
        "monitor_agent": monitor,
        "finance_agent": finance,
        "risk_agent": risks,
        "optimization_agent": optimization
    }