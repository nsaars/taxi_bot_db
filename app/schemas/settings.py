from typing import Optional, List

from schemas.base import Base


class Settings(Base):
    allow_credits: bool


class SettingsCreate(Base):
    allow_credits: Optional[bool] = True


class SettingsUpdate(Base):
    allow_credits: Optional[bool] = None


class SettingsList(Base):
    settings: List[Settings]
