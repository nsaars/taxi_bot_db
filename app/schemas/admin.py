from typing import Optional, List

from schemas.base import Base


class Admin(Base):
    id: int
    user_id: int


class AdminCreate(Base):
    user_id: int


class AdminUpdate(Base):
    user_id: Optional[int] = None


class Admins(Base):
    admins: List[Admin]
