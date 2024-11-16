from typing import List
from fastapi import APIRouter, Depends
from src.logs.models import LogFileEntry
from src.logs.services.fetch_automation_logs_from_file import (
    FetchAutomationLogsFromFile,
)
from src.logs.services.fetch_logs_from_files import FetchLogsFromFile

router = APIRouter(prefix="/logs", tags=["Logs"])


@router.get("/file", response_model=List[LogFileEntry])
def get_all() -> List[LogFileEntry]:
    return FetchLogsFromFile().execute()


@router.get("/file/{automation_id}", response_model=List[LogFileEntry])
def get(automation_id: int) -> List[LogFileEntry]:
    return FetchAutomationLogsFromFile().execute(automation_id=automation_id)
