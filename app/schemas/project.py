from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class ProjectStatus(str, Enum):
    ACTIVE = "ACTIVE"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    ARCHIVED = "ARCHIVED"

class ProjectCreate(BaseModel):
    name: str
    description: str
    status: str

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    status: ProjectStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True