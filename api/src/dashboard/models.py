from datetime import datetime
from decimal import Decimal
from datetime import timedelta
from typing import Optional, Union
from pydantic import BaseModel, field_validator


class DashboardStats(BaseModel):
    triggered: int
    total_automations: int
    saved_hours: Union[Decimal, None] = None
    average_time: Union[None, int] = None
    success: int
    waiting: int
    failures: int
    last_execution: Union[datetime, None] = None

    @field_validator("average_time", mode="before")
    def to_int(cls, v):
        if v:
            return v.seconds
        return v
