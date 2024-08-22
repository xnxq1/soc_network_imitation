from app.db import async_session_factory
from sqlalchemy import select, insert, update
from app.likes.models import LikePost, LikeComment


class DaoBaseLike:
    model = None

    @classmethod
    async def check_like(cls, **data):
        async with async_session_factory() as session:
            query = select(cls.model).filter_by(**data)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def like_dislike(cls, **data):
        async with async_session_factory() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_all(cls):
        async with async_session_factory() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def change_status(cls, status, **data):
        async with async_session_factory() as session:
            query = (update(cls.model)
                     .values(status=status)
                     .filter_by(**data))
            await session.execute(query)
            await session.commit()


class DaoLikePost(DaoBaseLike):
    model = LikePost


class DaoLikeComment(DaoBaseLike):
    model = LikeComment