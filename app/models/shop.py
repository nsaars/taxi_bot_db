import sqlalchemy as sa
from sqlalchemy import orm

from models.base import BaseModel


class Cart(BaseModel):
    __tablename__ = "carts"

    driver_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("drivers.id"))

    products: orm.Mapped[list["Product"]] = orm.relationship(
        back_populates="carts",
        secondary="carts_products",
        overlaps="offices"
    )

    offices: orm.Mapped[list["Office"]] = orm.relationship(
        back_populates="carts",
        secondary="carts_products",
        overlaps="products"
    )
