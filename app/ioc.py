import typing

from sqlalchemy.ext.asyncio import AsyncEngine
from that_depends import BaseContainer, providers

from app.db.resource import create_sa_engine, create_session
from repositories.repositories import (
    UserRepository,
    AdminRepository,
    ManagerRepository,
    EmployeeRepository,
    ProductRepository,
    OfficeRepository,
    ProductsOfficesRepository,
    DriverRepository,
    CartRepository,
    CartsProductsRepository,
    SettingsRepository,
    StateRepository
)


class IOCContainer(BaseContainer):
    database_engine = providers.AsyncResource(create_sa_engine)
    session = providers.AsyncContextResource(create_session, engine=typing.cast(AsyncEngine, database_engine))

    user_repo = providers.Factory(UserRepository, session=session)
    admin_repo = providers.Factory(AdminRepository, session=session)
    manager_repo = providers.Factory(ManagerRepository, session=session)
    employee_repo = providers.Factory(EmployeeRepository, session=session)
    product_repo = providers.Factory(ProductRepository, session=session)
    office_repo = providers.Factory(OfficeRepository, session=session)
    products_offices_repo = providers.Factory(ProductsOfficesRepository, session=session)
    driver_repo = providers.Factory(DriverRepository, session=session)
    cart_repo = providers.Factory(CartRepository, session=session)
    carts_products_repo = providers.Factory(CartsProductsRepository, session=session)

    settings_repo = providers.Factory(SettingsRepository, session=session)
    state_repo = providers.Factory(StateRepository, session=session)

