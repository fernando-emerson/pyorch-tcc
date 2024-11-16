from typing import Any
from typing import Generator
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import build_app
from src.database import Base
from src.database import Database

db = Database()

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Use connect_args parameter only with sqlite
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module", name="app")
def app_fixture() -> Generator[FastAPI, Any, None]:
    """
    Create a fresh database on each test case.
    """
    Base.metadata.create_all(engine)  # Create the tables.
    _app = build_app()
    yield _app
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="module", name="db_session")
def db_session_fixture() -> Generator[SessionTesting, Any, None]:  # type: ignore
    Base.metadata.create_all(engine)
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)

    def get_session():
        return session

    yield get_session  # use the session in tests.
    Base.metadata.create_all(engine)
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="module", name="client")
def client_fixture(
    app: FastAPI,
    db_session: SessionTesting,  # type: ignore
) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[db.get_db_session()] = _get_test_db
    with TestClient(app) as test_client:
        yield test_client
