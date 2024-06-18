import sqlalchemy as sa
from sqlalchemy import orm

from models.base import BaseModel


class Product(BaseModel):
    __tablename__ = "products"

    title: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    money_price: orm.Mapped[float] = orm.mapped_column(sa.Float, nullable=False)
    score_price: orm.Mapped[float] = orm.mapped_column(sa.Float, nullable=False)

    image: orm.Mapped[str | None] = orm.mapped_column(sa.String, nullable=True)
    description: orm.Mapped[str | None] = orm.mapped_column(sa.String, nullable=True)

    offices: orm.Mapped[list["Office"]] = orm.relationship(
        back_populates="products",
        secondary="products_offices",
        overlaps="carts"
    )

    carts: orm.Mapped[list["Cart"]] = orm.relationship(
        back_populates="products",
        secondary="carts_products",
        overlaps="offices"
    )


class Office(BaseModel):
    __tablename__ = "offices"

    products: orm.Mapped[list["Product"]] = orm.relationship(
        back_populates="offices",
        secondary="products_offices",
        overlaps="carts"
    )

    carts: orm.Mapped[list["Cart"]] = orm.relationship(
        back_populates="offices",
        secondary="carts_products",
        overlaps="products"
    )

    address: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    title: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    manager_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("managers.id", ondelete='SET NULL'),
                                                    nullable=True)


class Settings(BaseModel):
    __tablename__ = "settings"

    allow_credits: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, default=True, nullable=False)


class State(BaseModel):
    __tablename__ = "states"

    user_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("users.id"))
    title: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    data: orm.Mapped[str] = orm.mapped_column(sa.JSON, nullable=True)
