import datetime
import logging
import typing

import sqlalchemy as sa
from sqlalchemy import orm

from helpers.datetime import generate_utc_dt

logger = logging.getLogger(__name__)

METADATA: typing.Final = sa.MetaData()


class Base(orm.DeclarativeBase):
    metadata = METADATA


class NoIdModel(Base):
    __abstract__ = True

    created_at: orm.Mapped[
        typing.Annotated[
            datetime.datetime,
            orm.mapped_column(sa.DateTime(timezone=True), default=generate_utc_dt, nullable=False),
        ]
    ]


class BaseModel(NoIdModel):
    __abstract__ = True

    id: orm.Mapped[typing.Annotated[int, orm.mapped_column(primary_key=True, unique=True, autoincrement=True)]]

    def __str__(self) -> str:
        return f"<{type(self).__name__}({self.id=})>"
