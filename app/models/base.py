import datetime
import logging
import typing

import sqlalchemy as sa
from sqlalchemy import orm

from app.helpers.datetime import generate_utc_dt

logger = logging.getLogger(__name__)

METADATA: typing.Final = sa.MetaData()


class Base(orm.DeclarativeBase):
    metadata = METADATA


class BaseModel(Base):
    __abstract__ = True

    id: orm.Mapped[typing.Annotated[int, orm.mapped_column(primary_key=True)]]
    created_at: orm.Mapped[
        typing.Annotated[
            datetime.datetime,
            orm.mapped_column(sa.DateTime(timezone=True), default=generate_utc_dt, nullable=False),
        ]
    ]
    updated_at: orm.Mapped[
        typing.Annotated[
            datetime.datetime,
            orm.mapped_column(sa.DateTime(timezone=True), default=generate_utc_dt, nullable=False),
        ]
    ]

    def __str__(self) -> str:
        return f"<{type(self).__name__}({self.id=})>"


class User(BaseModel):
    __tablename__ = "users"

    name: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    phone_number: orm.Mapped[str | None] = orm.mapped_column(sa.String, nullable=True)
    # telegram_username: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    telegram_id: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, nullable=True)
    email: orm.Mapped[str | None] = orm.mapped_column(sa.String, nullable=True)


class Driver(BaseModel):
    __tablename__ = "drivers"

    user_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("users.id"))
    yandex_id: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    callsign: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    scores: orm.Mapped[float] = orm.mapped_column(sa.Float, default=0, nullable=False)


class Admin(BaseModel):
    __tablename__ = "admins"

    user_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("users.id"))


class Manager(BaseModel):
    __tablename__ = "managers"

    user_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("users.id"))

    offices: orm.Mapped[list["Office"]] = orm.relationship(
        back_populates="managers",
        secondary="managers_offices",
    )


class Employee(BaseModel):
    __tablename__ = "employees"

    user_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("users.id"))
    office_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("offices.id"))


class Product(BaseModel):
    __tablename__ = "products"

    title: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    image: orm.Mapped[str | None] = orm.mapped_column(sa.String, nullable=True)
    description: orm.Mapped[str | None] = orm.mapped_column(sa.String, nullable=True)
    money_price: orm.Mapped[float] = orm.mapped_column(sa.Float, nullable=False)
    score_price: orm.Mapped[float] = orm.mapped_column(sa.Float, nullable=False)

    offices: orm.Mapped[list["Office"]] = orm.relationship(
        back_populates="products",
        secondary="products_offices",
    )


class Office(BaseModel):
    __tablename__ = "offices"

    managers: orm.Mapped[list["Manager"]] = orm.relationship(
        back_populates="offices",
        secondary="managers_offices",
    )

    products: orm.Mapped[list["Product"]] = orm.relationship(
        back_populates="offices",
        secondary="products_offices",
    )

    address: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    employees: orm.Mapped[list["Employee"]] = orm.relationship("Employee", lazy="noload", uselist=True)


class ManagersOffices(BaseModel):
    __tablename__ = "managers_offices"

    id: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, nullable=True)

    manager_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("managers.id", ondelete="CASCADE"),
        primary_key=True,
    )
    office_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("offices.id", ondelete="CASCADE"),
        primary_key=True,
    )


class ProductsOffices(BaseModel):
    __tablename__ = "products_offices"

    id: orm.Mapped[int | None] = orm.mapped_column(sa.Integer, nullable=True)

    product_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("products.id", ondelete="CASCADE"),
        primary_key=True,
    )
    office_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("offices.id", ondelete="CASCADE"),
        primary_key=True,
    )

    quantity: orm.Mapped[int] = orm.mapped_column(sa.Integer, nullable=False)
