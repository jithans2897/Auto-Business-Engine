from apscheduler.schedulers.background import BackgroundScheduler
from app.database.db import SessionLocal
from app.services.ai_optimizer import optimize_project
from app.models.project import Project

scheduler = BackgroundScheduler()


def run_ai_cycle():
    db = SessionLocal()
    projects = db.query(Project).all()

    print("\nAI Autonomous Cycle Running...")

    for project in projects:
        result = optimize_project(db, project.id)
        print(f"Optimized Project {project.id}: {result}")

    db.close()


def start_scheduler():
    scheduler.add_job(run_ai_cycle, "interval", seconds=60)
    scheduler.start()