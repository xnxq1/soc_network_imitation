from app.db import async_session_factory
from sqlalchemy import select, insert, update, and_
from app.likes.likes_post.models import LikePost, LikeStatus


class DaoLike:
    model = LikePost
    @classmethod
    async def check_like_post(cls, user_id: int, post_id: int):
        async with async_session_factory() as session:
            query = select(cls.model).where(and_(cls.model.user_id == user_id, cls.model.post_id == post_id))
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def like_dislike_post(cls, user_id: int, post_id: int, status: LikeStatus):
        async with async_session_factory() as session:
            query = insert(cls.model).values(user_id=user_id, post_id=post_id, status=status)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_all(cls):
        async with async_session_factory() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def change_status(cls, user_id: int, post_id: int, status: LikeStatus):
        async with async_session_factory() as session:
            query = (update(cls.model)
                     .values(status=status)
                     .where(and_(cls.model.post_id==post_id), cls.model.user_id == user_id))
            await session.execute(query)
            await session.commit()
