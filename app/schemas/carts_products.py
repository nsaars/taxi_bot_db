from typing import Optional, List

from schemas.base import Base


class CartsProducts(Base):
    id: int
    product_id: int
    cart_id: int
    office_id: int
    quantity: int


class CartsProductsCreate(Base):

    product_id: int
    cart_id: int
    office_id: int
    quantity: int


class CartsProductsUpdate(Base):
    product_id: Optional[int] = None
    cart_id: Optional[int] = None
    office_id: Optional[int] = None
    quantity: Optional[int] = None


class CartsProductsList(Base):
    carts_products: List[CartsProducts]
