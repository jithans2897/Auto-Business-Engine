from sqlalchemy import Column, Integer, DateTime, Text
from datetime import datetime
from app.database.db import Base


class AIReport(Base):
    __tablename__ = "ai_reports"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer)
    total_resources = Column(Integer)
    total_cost = Column(Integer)
    recommendations = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)