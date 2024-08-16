from datetime import datetime

from sqlalchemy import ForeignKey, Computed
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import CustomBase, Base


class PostStatus(Base):
    __tablename__ = 'PostStatus'
    id: Mapped[int] = mapped_column(ForeignKey('Post.id'), primary_key=True)
    is_archived: Mapped[bool] = mapped_column(default=False)
    is_changed: Mapped[bool] = mapped_column(default=False)

class Post(CustomBase):

    text: Mapped[str]
    likes: Mapped[int] = mapped_column(default=0)
    dislikes: Mapped[int] = mapped_column(default=0)
    author_id: Mapped[int] = mapped_column(ForeignKey('User.id'))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    post_status = relationship('PostStatus', primaryjoin='Post.id == PostStatus.id')


