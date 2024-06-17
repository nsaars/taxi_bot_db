import typing
from datetime import datetime
from typing import Optional, List, Annotated

from app.schemas.base import Base


class Driver(Base):
    id: int
    user_id: int
    yandex_id: str
    callsign: str
    scores: float
    phone_number: str
    is_blocked: bool
    trusted: bool
    scores_updated_at: datetime

    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]


class DriverCreate(Base):
    user_id: int
    yandex_id: str
    callsign: str
    scores: Optional[float] = 0
    phone_number: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None


class DriverUpdate(Base):
    user_id: Optional[int] = None
    yandex_id: Optional[str] = None
    callsign: Optional[str] = None
    scores: Optional[float] = None
    phone_number: Optional[str] = None
    is_blocked: Optional[bool] = None
    trusted: Optional[bool] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    scores_updated_at: Optional[datetime] = None


class Drivers(Base):
    drivers: List[Driver]
