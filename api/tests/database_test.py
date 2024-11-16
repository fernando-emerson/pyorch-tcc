from src.database import Database
from sqlalchemy import text


def test_database_connection():
    db = Database()
    with db.session() as session:
        assert session is not None
        assert session.execute(text("SELECT 1")).scalar() == 1
