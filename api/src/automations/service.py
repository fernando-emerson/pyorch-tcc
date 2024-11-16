import os
import shutil
import subprocess
import uuid
import zipfile

from src.automations.models import AutomationCreate, AutomationUpdate
from src.automations.repo import AutomationRepository
from src.automations.tasks import run_task
from src.tasks.models import TaskCreate, TaskPriority, TaskState
from src.tasks.service import TaskService


class AutomationsService:

    def __init__(self, repo: AutomationRepository, task_service: TaskService) -> None:
        self.repo = repo
        self.task_service = task_service

    def get_by_id(self, id: int):
        """Retrieve an automation by its ID."""
        return self.repo.get(id=id)

    def get_all(self):
        """Retrieve all automations."""
        return self.repo.get_all()

    def create(self, automation: AutomationCreate):
        """Create a new automation."""
        created = self.repo.create(automation.model_dump(exclude=["file"]))

        if automation.file is not None:
            destination = f"upload/{created.id}/{automation.file.filename}"
            relative_path = os.path.dirname(destination)

            if not os.path.exists(destination):
                os.mkdir(relative_path)

            with open(destination, "wb+") as file_object:
                shutil.copyfileobj(automation.file.file, file_object)

            # Descompactar o ZIP
            with zipfile.ZipFile(destination, "r") as zip_ref:
                zip_ref.extractall(relative_path)

            # Verificar se o arquivo requirements.txt existe
            requirements_path = os.path.join(relative_path, "requirements.txt")
            if not os.path.exists(requirements_path):
                raise FileNotFoundError("Arquivo requirements.txt não encontrado.")

            # Criar o ambiente virtual
            result = subprocess.run(
                ["python", "-m", "venv", "venv"], check=True, cwd=relative_path
            )

            if result.returncode != 0:
                raise Exception("Erro ao criar ambiente virtual")

        return created

    def execute(self, id: int):
        automation = self.repo.get(id=id)
        taskid = str(uuid.uuid1())

        self.task_service.create(
            task=TaskCreate(
                status=TaskState.WAITING.value,
                priority=TaskPriority.HIGH.value,
                progress=0,
                automation_id=automation.id,
                task_id=taskid,
            )
        )

        run_task.apply_async(args=(f"upload/{id}",), task_id=taskid)

        return {"state": "enqueued", "taskid": taskid}

    def delete(self, id: int):
        """Delete an automation by its ID."""
        self.repo.delete(id)

    def update(self, data: AutomationUpdate):
        """Update an existing automation."""
        self.repo.update(id=data.id, data=data.model_dump(exclude=["id", "file"]))
        return self.get_by_id(id=data.id)
