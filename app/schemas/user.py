from typing import Optional, List

from schemas.base import Base


class User(Base):
    id: int
    telegram_id: int
    telegram_username: Optional[str]
    telegram_name: Optional[str]


class UserCreate(Base):
    telegram_id: int
    telegram_username: str = None
    telegram_name: str = None


class UserUpdate(Base):
    telegram_id: Optional[int] = None
    telegram_username: Optional[str] = None
    telegram_name: Optional[str] = None


class Users(Base):
    users: List[User]
