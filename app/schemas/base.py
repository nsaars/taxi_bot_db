from typing import Optional, List

import pydantic
from pydantic import BaseModel


class Base(BaseModel):
    model_config = pydantic.ConfigDict(from_attributes=True)


class ProductSchema(BaseModel):
    id: Optional[int]
    title: str
    image: Optional[str]
    description: Optional[str]
    money_price: float
    score_price: float
    # offices: List[int]


class ProductUpdate(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    money_price: Optional[float] = None
    score_price: Optional[float] = None
    # offices: Optional[List[int]] = None


class Products(BaseModel):
    products: List[ProductSchema]


class OfficeSchema(BaseModel):
    id: Optional[int]
    address: str
    # managers: List[int]
    # products: List[int]
    employees: List[int]


class OfficeUpdate(BaseModel):
    address: Optional[str] = None
    managers: Optional[List[int]] = None
    products: Optional[List[int]] = None
    employees: Optional[List[int]] = None


class Offices(BaseModel):
    offices: List[OfficeSchema]


class ManagersOfficesSchema(BaseModel):
    manager_id: Optional[int]
    office_id: Optional[int]


class ManagersOfficesUpdate(BaseModel):
    manager_id: Optional[int] = None
    office_id: Optional[int] = None


class ManagersOfficesList(BaseModel):
    managers_offices: List[ManagersOfficesSchema]


class ProductsOfficesSchema(BaseModel):
    id: Optional[int]
    product_id: int
    office_id: int
    quantity: int


class ProductsOfficesUpdate(BaseModel):
    id: Optional[int] = None
    product_id: Optional[int] = None
    office_id: Optional[int] = None
    quantity: Optional[int] = None


class ProductsOfficesList(BaseModel):
    products_offices: List[ProductsOfficesSchema]
