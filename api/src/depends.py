from src.database import Database


def get_db_session():
    db = Database()
    return db.session
