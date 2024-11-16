from pydantic import BaseModel
from src.database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String


class LogModel(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    robot_id = Column(Integer, ForeignKey("robots.id"))
    automation_id = Column(Integer, ForeignKey("automations.id"))
    started_at = Column(DateTime)
    finished_at = Column(DateTime)
    status = Column(String)
    traceback = Column(String)
    module = Column(String)
    func = Column(String)


class LogFileEntry(BaseModel):
    taskid: str
    automation_id: int
    message: str
    nivel: str
