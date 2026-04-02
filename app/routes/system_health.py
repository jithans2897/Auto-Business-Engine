from fastapi import APIRouter
import os

router = APIRouter(tags=["System"])


@router.get("/system/health")
def system_health():
    return {
        "status": "running",
        "environment": os.getenv("APP_ENV"),
        "ai_mode": os.getenv("AI_MODE")
    }