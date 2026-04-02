import time
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.services.ai_engine import analyze_project
from app.models.project import Project
from app.models.ai_report import AIReport

def monitor_projects():
    while True:
        db: Session = SessionLocal()

        try:
            projects = db.query(Project).all()

            for project in projects:
                result = analyze_project(db, project.id)

                report = AIReport(
                    project_id=result['project_id'],
                    total_resources=result['total_resources'],
                    total_cost=result['total_cost'],
                    recommendations=", ".join(result['recommendations'])
                )

                db.add(report)
                db.commit()


                print("AI REPORT SAVED")
                print(result)

        finally:
            db.close()

        time.sleep(60)