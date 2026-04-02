from sqlalchemy import Column, Float, Integer, String, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.db import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    status = Column(String, default="ACTIVE")

    cost_per_month = Column(Float, default=0.0)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project")