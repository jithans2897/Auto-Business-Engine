from pydantic import BaseModel
from datetime import datetime


class ResourceCreate(BaseModel):
    name: str
    type: str
    project_id: int
    cost_per_month: float 


class ResourceResponse(BaseModel):
    id: int
    name: str
    type: str
    status: str
    cost_per_month: float
    project_id: int
    created_at: datetime
    updated_at: datetime


    class Config:
        from_attributes = True