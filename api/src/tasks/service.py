from datetime import datetime
from typing import Any
from src.tasks.models import Task, TaskCreate, TaskState
from src.tasks.repo import TaskRepository


class TaskService:

    def __init__(self, repo: TaskRepository) -> None:
        self.repo = repo

    def get_all(self):
        return self.repo.get_all()

    def get_last_execution_by_automation_id(self, automation_id: str):
        return self.repo.get_last_execution_by_automation_id(automation_id=automation_id)

    def create(self, task: TaskCreate):
        return self.repo.create(Task(
            task_id=task.task_id,
            priority=task.priority,
            progress=task.progress,
            automation_id=task.automation_id,
            status=task.status
        ))

    def update_status(self, taskid: str, status: TaskState):
        self.repo.update_status(taskid=taskid, status=status.value)

    def on_success(self, taskid: str, result: Any):
        self.repo.update(taskid=taskid, data={
            "status": TaskState.FINISHED.value,
            "result": result,
            "finished_at": datetime.now(),
            "progress": 100
        })

    def on_failure(self, taskid: str, exc: str):
        self.repo.update(taskid=taskid, data={
            "status": TaskState.ERROR.value,
            "message": exc,
            "finished_at": datetime.now(),
            "progress": 50
        })
