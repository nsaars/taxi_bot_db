import sqlalchemy as sa
from sqlalchemy import orm

from app.models.base import NoIdModel, BaseModel


class ProductsOffices(BaseModel):
    __tablename__ = "products_offices"

    product_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("products.id", ondelete="CASCADE"),
        primary_key=True,
    )
    office_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("offices.id", ondelete="CASCADE"),
        primary_key=True,
    )

    quantity: orm.Mapped[int] = orm.mapped_column(sa.Integer, nullable=False)
    reserved_quantity: orm.Mapped[int] = orm.mapped_column(sa.Integer, default=0, nullable=False)


class CartsProducts(BaseModel):
    __tablename__ = "carts_products"

    product_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("products.id", ondelete="CASCADE"),
        primary_key=True,
    )
    cart_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("carts.id", ondelete="CASCADE"),
        primary_key=True,
    )

    office_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("offices.id", ondelete="CASCADE"),
        primary_key=True,
    )

    quantity: orm.Mapped[int] = orm.mapped_column(sa.Integer, nullable=False)
