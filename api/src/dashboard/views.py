from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.dashboard.services.fetch_stats import FetchDashboardStatsService
from src.depends import get_db_session


router = APIRouter(prefix="/dashboard", tags=["Tasks"])


@router.get("/stats")
def get_stats(db_session: Session = Depends(get_db_session)):
    return FetchDashboardStatsService(db_session=db_session).execute()
