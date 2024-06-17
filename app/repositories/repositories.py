import dataclasses
from typing import Type

from app import models
from app.repositories.base import BaseRepository


@dataclasses.dataclass(kw_only=True)
class AdminsRepository(BaseRepository[models.Admin]):
    model: Type[models.Admin] = models.Admin


@dataclasses.dataclass(kw_only=True)
class ManagersRepository(BaseRepository[models.Manager]):
    model: Type[models.Manager] = models.Manager


@dataclasses.dataclass(kw_only=True)
class EmployeesRepository(BaseRepository[models.Employee]):
    model: Type[models.Employee] = models.Employee


@dataclasses.dataclass(kw_only=True)
class ProductsRepository(BaseRepository[models.Product]):
    model: Type[models.Product] = models.Product


@dataclasses.dataclass(kw_only=True)
class OfficesRepository(BaseRepository[models.Office]):
    model: Type[models.Office] = models.Office


@dataclasses.dataclass(kw_only=True)
class ManagersOfficesRepository(BaseRepository[models.ManagersOffices]):
    model: Type[models.ManagersOffices] = models.ManagersOffices


@dataclasses.dataclass(kw_only=True)
class ProductsOfficesRepository(BaseRepository[models.ProductsOffices]):
    model: Type[models.ProductsOffices] = models.ProductsOffices


@dataclasses.dataclass(kw_only=True)
class DriversRepository(BaseRepository[models.Driver]):
    model: Type[models.Driver] = models.Driver
