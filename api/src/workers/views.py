from fastapi import APIRouter, Depends
from src.worker import celery

router = APIRouter(prefix="/workers", tags=["Workers"])


@router.get("/")
def get_all():
    inspect_output = celery.control.inspect()
    stats = inspect_output.stats()
    active_tasks = inspect_output.active()
    workers =  [{"name": node, "id": idx + 1} for idx, node in enumerate(stats.keys()) if stats is not None]

    for worker in workers:
        if active_tasks:
            worker["active_tasks"] = active_tasks[worker["name"]] or []

    return workers
