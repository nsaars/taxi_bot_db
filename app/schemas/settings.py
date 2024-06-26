from typing import Optional, List

from app.schemas.base import Base


class Settings(Base):
    id: int
    allow_credits: bool


class SettingsCreate(Base):
    allow_credits: Optional[bool] = True


class SettingsUpdate(Base):
    allow_credits: Optional[bool] = None


class SettingsList(Base):
    settings: List[Settings]
