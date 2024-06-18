from typing import Optional, List

from schemas.base import Base


class Manager(Base):
    id: int
    user_id: int


class ManagerCreate(Base):
    user_id: int


class ManagerUpdate(Base):
    user_id: Optional[int] = None


class Managers(Base):
    managers: List[Manager]
