from celery import Task
from datetime import datetime
from src.database import db
from src.tasks.models import TaskState
from src.tasks.repo import TaskRepository
from src.tasks.service import TaskService


class CeleryTaskExecutionBackend(Task):

    def before_start(self, task_id, args, kwargs):
        """Atualiza a tarefa para o status 'IN_PROGRESS' antes de iniciar."""
        service = TaskService(repo=TaskRepository(db_session=db.session))
        service.update_status(taskid=task_id, status=TaskState.RUNNING)

    def on_success(self, retval, task_id, args, kwargs):
        """Atualiza a tarefa com o status 'SUCCESS' e armazena o resultado."""
        service = TaskService(repo=TaskRepository(db_session=db.session))
        service.on_success(taskid=task_id, result=retval)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """Atualiza a tarefa com o status 'FAILED' e armazena a mensagem de erro."""
        service = TaskService(repo=TaskRepository(db_session=db.session))
        service.on_failure(taskid=task_id, exc=exc)
