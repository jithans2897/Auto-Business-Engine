from fastapi import FastAPI
from app.database.db import engine
from app.models.project import Project
from app.routes.projects import router as projects_router
from app.database.db import Base 
from app.routes.resources import router as resources_router
from app.routes.analytics import router as analytics_router
from app.routes.ai_controller import router as ai_router
import threading
from app.agents.ai_monitor import monitor_projects
from app.models import ai_report
from app.models import resource
from app.routes.ai_reports import router as ai_reports_router
from app.routes.ai_strategy import router as ai_strategy_router
from app.routes.ai_optimizer import router as ai_optimizer_router
from app.automation.ai_scheduler import start_scheduler
from app.routes.ai_system_report import router as ai_report_router
from app.routes.ai_prediction import router as ai_prediction_router
from app.routes.ai_control_center import router as ai_control_router
from app.routes.ai_business import router as ai_business_router
from app.routes.ai_autonomous import router as autonomous_router
from app.routes.system_health import router as system_router
from fastapi.staticfiles import StaticFiles
from app.routes.react_agent import router as react_router
from app.routes.llm_agent import router as llm_router


app = FastAPI()
start_scheduler()

Base.metadata.create_all(bind=engine)

app.mount("/dashboard", StaticFiles(directory="app/dashboard"), name="dashboard")

app.include_router(projects_router)
app.include_router(resources_router)
app.include_router(analytics_router)
app.include_router(ai_router)
app.include_router(ai_reports_router)
app.include_router(ai_strategy_router)
app.include_router(ai_optimizer_router)
app.include_router(ai_report_router)
app.include_router(ai_prediction_router)
app.include_router(ai_control_router)
app.include_router(ai_business_router)
app.include_router(autonomous_router)
app.include_router(system_router)
app.include_router(react_router)
app.include_router(llm_router)

@app.get("/")
def home():
    return {"message": "Welcome to the Autonomous Business Engine API!"}

thread = threading.Thread(target=monitor_projects, daemon=True)
thread.start()