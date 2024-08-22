import enum

from sqlalchemy import ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.models import CustomBase


class LikeStatus(enum.Enum):
    like = 'like'
    dislike = 'dislike'




class LikePost(CustomBase):
    post_id: Mapped[int] = mapped_column(ForeignKey('Post.id'), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('User.id'), nullable=False)
    status: Mapped[LikeStatus] = mapped_column(nullable=False)

    __table_args__ = (
        Index("idx_post_user", "post_id", "user_id"),
        UniqueConstraint('post_id', 'user_id', name='post_user_uc'),
    )


class LikeComment(CustomBase):
    comment_id: Mapped[int] = mapped_column(ForeignKey('Comment.id'), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('User.id'), nullable=False)
    status: Mapped[LikeStatus] = mapped_column(nullable=False)

    __table_args__ = (
        Index("idx_comment_user", "comment_id", "user_id"),
        UniqueConstraint('comment_id', 'user_id', name='comment_user_uc'),
    )