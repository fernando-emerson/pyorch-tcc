from sqlalchemy import text
from sqlalchemy.orm import Session
from collections import namedtuple
from src.dashboard.models import DashboardStats

class FetchDashboardStatsService():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def execute(self) -> DashboardStats:
        with self.db_session() as session:
            rows = session.execute(text('SELECT * FROM dashboard_stats'))
            Record = namedtuple('Record', rows.keys())
            records = [Record(*r) for r in rows.fetchall()]
            stats = [DashboardStats(**record._asdict()) for record in records]
            return stats[0]
