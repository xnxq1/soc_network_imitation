import enum

from sqlalchemy import ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.models import CustomBase


class LikeStatus(enum.Enum):
    like = 'like'
    dislike = 'dislike'


class LikePost(CustomBase):
    post_id: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[LikeStatus] = mapped_column(nullable=False)

    __table_args__ = (
        Index("idx_post_user", "post_id", "user_id"),
    )