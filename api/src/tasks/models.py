from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from src.automations.models import AutomationModel
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = "task_queue"

    id = Column(Integer, primary_key=True, index=True)
    finished_at = Column(DateTime)
    status = Column(String)
    message = Column(String)
    priority = Column(String)
    result = Column(Text)
    progress = Column(Integer)
    task_id = Column(String)

    automation_id: Mapped[int] = Column(
        Integer, ForeignKey("automations.id"), nullable=False
    )

    automation: Mapped["AutomationModel"] = relationship(
        "AutomationModel",
        foreign_keys=[automation_id],
        primaryjoin="AutomationModel.id == Task.automation_id",
        lazy="subquery",
    )

    started_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


class TaskCreate(BaseModel):
    status: str
    priority: str
    progress: int = 0
    automation_id: int
    task_id: str

class TaskState(Enum):
    RUNNING: str = "Executando"
    WAITING: str = "Aguardando"
    FINISHED: str = "Concluído"
    ERROR: str = "Falha"

class TaskPriority(Enum):
    HIGH: str = "Alta"
