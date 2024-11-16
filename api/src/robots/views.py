from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.depends import get_db_session
from src.robots.models import RobotCreate, RobotModel
from src.robots import repo
from datetime import datetime

router = APIRouter()


@router.post("/")
def create(robot: RobotCreate, db_session: Session = Depends(get_db_session)):
    return repo.create(
        db_session,
        RobotModel=RobotModel(
            name=robot.name,
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        ),
    )
