import dataclasses
from typing import Type

from import models
from repositories.base import BaseRepository


@dataclasses.dataclass(kw_only=True)
class UserRepository(BaseRepository[models.User]):
    model: Type[models.User] = models.User


@dataclasses.dataclass(kw_only=True)
class AdminRepository(BaseRepository[models.Admin]):
    model: Type[models.Admin] = models.Admin


@dataclasses.dataclass(kw_only=True)
class ManagerRepository(BaseRepository[models.Manager]):
    model: Type[models.Manager] = models.Manager


@dataclasses.dataclass(kw_only=True)
class EmployeeRepository(BaseRepository[models.Employee]):
    model: Type[models.Employee] = models.Employee


@dataclasses.dataclass(kw_only=True)
class ProductRepository(BaseRepository[models.Product]):
    model: Type[models.Product] = models.Product


@dataclasses.dataclass(kw_only=True)
class OfficeRepository(BaseRepository[models.Office]):
    model: Type[models.Office] = models.Office


@dataclasses.dataclass(kw_only=True)
class ProductsOfficesRepository(BaseRepository[models.ProductsOffices]):
    model: Type[models.ProductsOffices] = models.ProductsOffices


@dataclasses.dataclass(kw_only=True)
class DriverRepository(BaseRepository[models.Driver]):
    model: Type[models.Driver] = models.Driver


@dataclasses.dataclass(kw_only=True)
class CartRepository(BaseRepository[models.Cart]):
    model: Type[models.Cart] = models.Cart


@dataclasses.dataclass(kw_only=True)
class CartsProductsRepository(BaseRepository[models.CartsProducts]):
    model: Type[models.CartsProducts] = models.CartsProducts


@dataclasses.dataclass(kw_only=True)
class SettingsRepository(BaseRepository[models.Settings]):
    model: Type[models.Settings] = models.Settings


@dataclasses.dataclass(kw_only=True)
class StateRepository(BaseRepository[models.State]):
    model: Type[models.State] = models.State

