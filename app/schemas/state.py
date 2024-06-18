from typing import Optional, Dict, List

from schemas.base import Base


class State(Base):
    id: int
    user_id: int
    title: Optional[str] = None
    data: Optional[Dict] = None


class StateCreate(Base):
    user_id: int
    title: Optional[str] = None
    data: Optional[Dict] = None


class StateUpdate(Base):
    title: Optional[str] = None
    data: Optional[Dict] = None


class States(Base):
    states: List[State]
