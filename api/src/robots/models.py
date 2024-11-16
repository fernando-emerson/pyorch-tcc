from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer, String
from src.database import Base


class RobotModel(Base):
    __tablename__ = "robots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    storage_url = Column(String)


class RobotCreate(BaseModel):
    name: str
