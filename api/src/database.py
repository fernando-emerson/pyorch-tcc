from contextlib import contextmanager
import typing
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from src.config import settings
from sqlalchemy.orm import DeclarativeBase
import sqlalchemy


class Database:
    def __init__(self):
        self._engine = create_engine(
            url=f"{settings.DB_SCHEMA}://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}",
            pool_size=settings.DB_POOL_SIZE,
            max_overflow=settings.DB_POOL_OVERFLOW,
            pool_pre_ping=True,
            pool_recycle=300,
        )
        self._session_factory = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=True,
                bind=self._engine,
            ),
        )

    @contextmanager
    def session(self):
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


class DBTable(DeclarativeBase):
    metadata: sqlalchemy.MetaData = sqlalchemy.MetaData()


Base: typing.Type[DeclarativeBase] = DBTable

db = Database()
