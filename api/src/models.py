

from sqlalchemy import Column, Integer, String
from src.database import Base

class Bot(Base):
    __tablename__ = "bots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    version = Column(String)
    technology = Column(String)

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    bot_id = Column(Integer)
    args = Column(String)


class TaskQueue(Base):
    __tablename__ = "task_queue"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(String)
    bot_id = Column(Integer)
    status = Column(String)
