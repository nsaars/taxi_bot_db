from typing import Optional, List

from app.schemas.base import Base


class Cart(Base):
    id: int
    driver_id: int


class CartCreate(Base):
    driver_id: int


class CartUpdate(Base):
    driver_id: Optional[int] = None


class Carts(Base):
    carts: List[Cart]
