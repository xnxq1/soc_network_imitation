from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models import CustomBase


class Like(CustomBase):
    post_id: Mapped[int] = mapped_column(ForeignKey("Post.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))

