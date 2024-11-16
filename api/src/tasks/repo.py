from sqlalchemy.orm import Session

from src.tasks.models import Task, TaskState
from sqlalchemy import update


class TaskRepository:

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def get_all(self):
        with self.db_session() as session:
            return session.query(Task).order_by(Task.started_at.desc()).all()

    def get_by_taskid(self, taskid: str):
        with self.db_session() as session:
            return session.query(Task).filter(Task.task_id == taskid).first()

    def update_status(self, taskid: str, status: TaskState):
        with self.db_session() as session:
            stmt = (
                 update(Task)
                 .where(Task.task_id == taskid)
                 .values(status=status)
            )

            session.execute(stmt)
            session.commit()

    def create(self, task: Task):
        with self.db_session() as session:
            session.add(task)
            session.commit()
            session.refresh(task)
            return task

    def update(self, taskid: str, data: dict):
        with self.db_session() as session:
            task = session.query(Task).filter(Task.task_id == taskid).first()
            for key, value in data.items():
                setattr(task, key, value)
            session.commit()
            session.refresh(task)
            return task

    def get_last_execution_by_automation_id(self, automation_id: str):
        with self.db_session() as session:
            row = (
                session.query(Task)
                .filter(Task.automation_id == automation_id)
                .order_by(Task.started_at.desc())
            ).first()

            return row
