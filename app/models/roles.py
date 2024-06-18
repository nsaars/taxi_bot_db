import typing
import datetime
import sqlalchemy as sa
from sqlalchemy import orm

from helpers.datetime import generate_utc_dt, generate_utc_dt_naive
from models.base import BaseModel


class Driver(BaseModel):
    __tablename__ = "drivers"

    user_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("users.id"))

    phone_number: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    yandex_id: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    callsign: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    scores: orm.Mapped[float] = orm.mapped_column(sa.Float, default=0, nullable=False)
    is_blocked: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, default=False, nullable=False)
    trusted: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, default=True, nullable=False)

    first_name: orm.Mapped[str | None] = orm.mapped_column(sa.String, nullable=True)
    last_name: orm.Mapped[str | None] = orm.mapped_column(sa.String, nullable=True)
    middle_name: orm.Mapped[str | None] = orm.mapped_column(sa.String, nullable=True)

    scores_updated_at: orm.Mapped[
        typing.Annotated[
            datetime.datetime,
            orm.mapped_column(default=generate_utc_dt_naive, nullable=False),
        ]
    ]


class Admin(BaseModel):
    __tablename__ = "admins"

    user_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("users.id"))


class Manager(BaseModel):
    __tablename__ = "managers"

    user_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("users.id"))


class Employee(BaseModel):
    __tablename__ = "employees"

    user_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("users.id", ondelete='CASCADE'))
    office_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey("offices.id", ondelete='CASCADE'))
