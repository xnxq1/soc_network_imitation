
from sqlalchemy.orm import Mapped, mapped_column, column_property, relationship

from app.models import CustomBase, str_10

class User(CustomBase):

    first_name: Mapped[str_10] = mapped_column(nullable=True)
    last_name: Mapped[str_10] = mapped_column(nullable=True)
    fullname = column_property(first_name + " " + last_name)
    age: Mapped[int]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]

    posts = relationship("Post", order_by="and_(Post.is_archived.asc(),Post.likes.desc())")








