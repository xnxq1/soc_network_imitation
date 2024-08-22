from app.models import CustomBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Comment(CustomBase):
    post_id: Mapped[int] = mapped_column(ForeignKey('Post.id', ondelete='CASCADE'), nullable=True)
    parent_comment_id: Mapped[int] = mapped_column(ForeignKey('Comment.id', ondelete='CASCADE'), nullable=True)
    text: Mapped[str]
    likes: Mapped[int] = mapped_column(default=0)
    dislikes: Mapped[int] = mapped_column(default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey('User.id', ondelete='CASCADE'))

    post = relationship('Post', back_populates='comments')
    child_comments = relationship('Comment',
                                  cascade='all, delete',
                                  primaryjoin='Comment.id == Comment.parent_comment_id')



