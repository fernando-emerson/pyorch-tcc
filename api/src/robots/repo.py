from src.robots.models import RobotModel
from sqlalchemy.orm import Session


def get(db_session: Session):
    return db_session.query(RobotModel).all()


def create(db_session: Session, RobotModel: RobotModel):
    with db_session() as session:
        session.add(RobotModel)
        session.commit()
        session.refresh(RobotModel)
        return RobotModel


def get_by_id(db_session: Session, robot_id: int):
    return db_session.query(RobotModel).filter(RobotModel.id == robot_id).first()


def update(db_session: Session, robot_id: int, RobotModel):
    db_session.query(RobotModel).filter(RobotModel.id == robot_id).update(RobotModel)
    db_session.commit()
    return db_session.query(RobotModel).filter(RobotModel.id == robot_id).first()


def delete(db_session: Session, robot_id: int):
    db_session.query(RobotModel).filter(RobotModel.id == robot_id).delete()
    db_session.commit()
    return True
