from typing import Optional, List

from app.schemas.base import Base


class ProductsOffices(Base):
    id: int
    product_id: int
    office_id: int
    quantity: int
    reserved_quantity: int


class ProductsOfficesCreate(Base):
    product_id: int
    office_id: int
    quantity: int
    reserved_quantity: Optional[int] = 0


class ProductsOfficesUpdate(Base):
    product_id: Optional[int] = None
    office_id: Optional[int] = None
    quantity: Optional[int] = None
    reserved_quantity: Optional[int] = None


class ProductsOfficesList(Base):
    products_offices: List[ProductsOffices]
