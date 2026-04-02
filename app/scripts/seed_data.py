from app.database.db import SessionLocal
from app.models.project import Project
from app.models.resource import Resource


def seed():

    db = SessionLocal()

    # Clear old data (optional)
    db.query(Resource).delete()
    db.query(Project).delete()
    db.commit()

    # Create Projects
    project1 = Project(name="AI Startup", description="Automation system")
    project2 = Project(name="Ecommerce Platform", description="Online store")

    db.add_all([project1, project2])
    db.commit()

    # Create Resources
    resources = [
        Resource(name="Server", cost_per_month=500, project_id=project1.id),
        Resource(name="API Service", cost_per_month=300, project_id=project1.id),
        Resource(name="Database", cost_per_month=200, project_id=project2.id),
        Resource(name="Hosting", cost_per_month=150, project_id=project2.id),
    ]

    db.add_all(resources)
    db.commit()

    print("✅ Database seeded successfully!")


if __name__ == "__main__":
    seed()