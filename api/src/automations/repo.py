from src.automations.models import AutomationCreate, AutomationModel
from sqlalchemy.orm import Session


class AutomationRepository:

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def get(self, id: int):
        with self.db_session() as session:
            return (
                session.query(AutomationModel)
                .filter(AutomationModel.id == id)
                .one_or_none()
            )

    def get_all(self):
        with self.db_session() as session:
            return session.query(AutomationModel).all()

    def create(self, data: dict):
        with self.db_session() as session:
            automation = AutomationModel(**data)
            session.add(automation)
            session.commit()
            session.refresh(automation)
            return automation

    def delete(self, id: int):
        with self.db_session() as session:
            session.query(AutomationModel).filter(AutomationModel.id == id).delete()
            session.commit()
            return True

    def update(self, id: int, data: dict):
        with self.db_session() as session:
            session.query(AutomationModel).filter(AutomationModel.id == id).update(data)
            session.commit()
