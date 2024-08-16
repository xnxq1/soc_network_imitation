from app.db import async_session_factory
from sqlalchemy import select, insert, update, and_
from app.likes.models import LikePost


class DaoLike:
    model = LikePost
    @classmethod
    async def check_like_user(cls, user_id: int, post_id: int):
        async with async_session_factory() as session:
            query = select(cls.model).where(and_(cls.model.user_id == user_id, cls.model.post_id == post_id))
            result = await session.execute(query)
            return result.scalar_one_or_none()
