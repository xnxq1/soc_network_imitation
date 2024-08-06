from typing import List

from pydantic import EmailStr
from sqlalchemy import Computed, DefaultClause, text
from sqlalchemy.orm import Mapped, mapped_column, column_property, relationship

from app.models import CustomBase, intpk, str_10, str_20, Base
from app.posts.models import Post
class User(CustomBase):

    first_name: Mapped[str_10] = mapped_column(nullable=True)
    last_name: Mapped[str_10] = mapped_column(nullable=True)
    fullname = column_property(first_name + " " + last_name)
    age: Mapped[int]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]

    posts = relationship("Post")








