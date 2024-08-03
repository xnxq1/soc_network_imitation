from typing import Annotated

from fastapi import Query
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, declared_attr, registry
from sqlalchemy import String

intpk = Annotated[int, mapped_column(primary_key=True)]
str_10 = Annotated[str, 10]
str_20 = Annotated[str, 20]


class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            intpk: Integer,
            str_10: String(10),
            str_20: String(20),

        }
    )


class CustomBase(Base):

    __abstract__ = True
    id: Mapped[intpk]

    @declared_attr
    def __tablename__(cls):
        return cls.__name__

