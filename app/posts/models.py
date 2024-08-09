from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import CustomBase

class Post(CustomBase):

    text: Mapped[str]
    likes: Mapped[int] = mapped_column(default=0)
    dislikes: Mapped[int] = mapped_column(default=0)
    author_id: Mapped[int] = mapped_column(ForeignKey("User.id"))

