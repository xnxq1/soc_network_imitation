from pydantic import EmailStr
from sqlalchemy import Computed, DefaultClause, text
from sqlalchemy.orm import Mapped, mapped_column, column_property

from app.models import CustomBase, intpk, str_10, str_20, Base


class User(CustomBase):

    first_name: Mapped[str_10] = mapped_column()
    last_name: Mapped[str_10] = mapped_column()
    fullname = column_property(first_name + " " + last_name)
    age: Mapped[int]
    email: Mapped[str]
    hashed_password: Mapped[str]










