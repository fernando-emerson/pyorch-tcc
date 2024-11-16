from celery import Task
from datetime import datetime
from core.database.session import database
from src.processes.models import TaskOutput
from src.processes.repo import AutomationProcessesRepository
from src.queue.models import TaskQueue
from src.queue.repo import TaskQueueRepository
from sqlalchemy.exc import SQLAlchemyError
import json


class CeleryTaskExecutionBackend(Task):

    def before_start(self, task_id, args, kwargs):
        """Atualiza a tarefa para o status 'IN_PROGRESS' antes de iniciar."""
        repository = TaskQueueRepository(db_session=database.get_db_session)
        repository.update_by_task_id(task_id=task_id, data={"status": "IN_PROGRESS"})

    def on_success(self, retval, task_id, args, kwargs):
        """Atualiza a tarefa com o status 'SUCCESS' e armazena o resultado."""
        tq_repo = TaskQueueRepository(db_session=database.get_db_session)
        pr_repo = AutomationProcessesRepository(db_session=database.get_db_session)

        tq_repo.update_by_task_id(
            task_id=task_id,
            data={
                "status": "SUCCESS",
                "result": retval.raw,
                "finished_at": datetime.now(),
            },
        )

        for task in retval.tasks_output:
            pr_repo.register_task_output(
                task_output=TaskOutput(
                    execution_id=task["execution_id"],
                    process_id=task["process_id"],
                    name=task["name"],
                    agent=task["agent"],
                    expected_output=task["expected_output"],
                    summary=task["summary"],
                    raw=task["raw"],
                    json_dict=task["json_dict"],
                    output_format=task["output_format"],
                )
            )

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """Atualiza a tarefa com o status 'FAILED' e armazena a mensagem de erro."""
        repository = TaskQueueRepository(db_session=database.get_db_session)
        repository.update_by_task_id(
            task_id=task_id,
            data={
                "status": "FAILED",
                "error_message": str(exc),
                "finished_at": datetime.now(),
            },
        )
