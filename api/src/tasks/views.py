from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.depends import get_db_session
from src.tasks.models import TaskState
from src.tasks.repo import TaskRepository
from src.tasks.service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_repository(
    db_session: Session = Depends(get_db_session),
) -> TaskRepository:
    return TaskRepository(db_session=db_session)


def get_service(
    repo: TaskService = Depends(get_repository),
) -> TaskService:
    return TaskService(repo=repo)


@router.get("/")
def get_all(service: TaskService = Depends(get_service)):
    return service.get_all()

@router.patch("/update-status/{taskid}/{status}")
def update_status(taskid: str, status: TaskState, service: TaskService = Depends(get_service)):
    return service.update_status(taskid=taskid, status=status)
