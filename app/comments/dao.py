
from app.comments.models import Comment
from app.db import async_session_factory
from app.users.models import User
from sqlalchemy import select, insert


class DaoComment:
    model = Comment


    @classmethod
    async def add_comment(cls, **data):
        async with async_session_factory() as session:
            stmt = insert(cls.model).values(**data).returning(cls.model)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()

    @classmethod
    async def get_all(cls):
        async with async_session_factory() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()


    @classmethod
    async def get_comment_by_id(cls, comment_id: int):
        async with async_session_factory() as session:
            query = select(cls.model).where(cls.model.id == comment_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()




