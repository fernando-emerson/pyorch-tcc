from typing import Annotated
from fastapi import APIRouter, Depends, File, Form, UploadFile
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.automations.models import AutomationCreate, AutomationUpdate
from src.automations.repo import AutomationRepository
from src.automations.service import AutomationsService
from src.depends import get_db_session
from src.tasks.service import TaskService
from src.tasks.views import get_service as get_task_service

router = APIRouter(prefix="/automations", tags=["Automações"])


def get_repository(
    db_session: Session = Depends(get_db_session),
) -> AutomationRepository:
    return AutomationRepository(db_session=db_session)

def get_service(
    repo: AutomationRepository = Depends(get_repository),
    task_service: TaskService = Depends(get_task_service)
) -> AutomationsService:
    return AutomationsService(repo=repo, task_service=task_service)


@router.get("/")
def get_all(service: AutomationsService = Depends(get_service)):
    return service.get_all()


@router.post("/")
def create(
    name: Annotated[str, Form()],
    description: Annotated[str, Form()],
    status: Annotated[str, Form()],
    file: Annotated[UploadFile, File()],
    service: AutomationsService = Depends(get_service),
):
    return service.create(
        AutomationCreate(
            name=name,
            description=description,
            status=status,
            file=file,
        )
    )


@router.delete("/{id}")
def delete(
    id: int,
    service: AutomationsService = Depends(get_service),
):
    service.delete(id=id)


@router.get("/{id}")
def get(id: int, service: AutomationsService = Depends(get_service)):
    return service.get_by_id(id=id)


@router.put("/")
def update(
    automation: AutomationUpdate, service: AutomationsService = Depends(get_service)
):
    return service.update(automation)

@router.post("/execute/{id}")
def update(
    id: int, service: AutomationsService = Depends(get_service)
):
    return service.execute(id=id)
