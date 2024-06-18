from typing import Optional, List

from schemas.base import Base


class Product(Base):
    id: int
    title: str
    money_price: float
    score_price: float
    image: Optional[str]
    description: str


class ProductCreate(Base):
    title: str
    money_price: float
    score_price: float
    image: Optional[str] = None
    description: Optional[str] = None


class ProductUpdate(Base):
    title: Optional[str] = None
    money_price: Optional[float] = None
    score_price: Optional[float] = None
    image: Optional[str] = None
    description: Optional[str] = None


class Products(Base):
    products: List[Product]
