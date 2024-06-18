from typing import Optional, List

from schemas.base import Base


class Office(Base):
    id: int
    address: str
    title: str
    manager_id: Optional[int]


class OfficeCreate(Base):
    address: str
    title: str
    manager_id: int


class OfficeUpdate(Base):
    address: Optional[str] = None
    title: Optional[str] = None
    manager_id: Optional[int] = None


class Offices(Base):
    offices: List[Office]
