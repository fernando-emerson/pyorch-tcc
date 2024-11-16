from __future__ import annotations
from typing import Any, List, Optional, Union
from fastapi import UploadFile
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from src.database import Base
from pydantic import BaseModel, field_validator
from sqlalchemy.orm import relationship


class AutomationModel(Base):
    __tablename__ = "automations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    status = Column(String)
    args = Column(String)
    kwargs = Column(String)
    env_variables = Column(String)
    slug = Column(String)

    @classmethod
    def create(cls, data: AutomationCreate):
        return cls(
            name=data.name,
            description=data.description,
            status=data.status,
            args=data.args,
            kwargs=data.kwargs,
            env_variables=data.env_variables,
            slug=data.slug,
        )


class AutomationCreate(BaseModel):
    name: str
    description: str
    status: str
    kwargs: Union[str, None] = None
    env_variables: Union[str, None] = None
    file: UploadFile = None
    slug: Union[str, None] = None

    def __init__(self, **data: Any) -> None:
        if "name" in data:
            data["slug"] = data["name"].lower().replace(" ", "-")
        super().__init__(**data)


class AutomationUpdate(BaseModel):
    id: int
    name: str
    description: str
    status: str
    file: Optional[UploadFile] = None
    slug: Union[str, None] = None

    def __init__(self, **data: Any) -> None:
        if "name" in data:
            data["slug"] = data["name"].lower().replace(" ", "-")
        super().__init__(**data)
