from sqlalchemy import select, insert, update

from app.db import async_session_factory
from app.posts.models import Post
from app.posts.schemas import SchemasPost


class DaoPost:
    model = Post
    @classmethod
    async def get_all_posts(cls, archived: bool = False):
        async with async_session_factory() as session:
            query = select(cls.model).where(cls.model.is_archived == archived)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_post_by_id(cls, post_id):
        async with async_session_factory() as session:
            query = select(cls.model).where(cls.model.id == post_id)
            result = await session.execute(query)
            return result.scalar_one()


    @classmethod
    async def add_post(cls, user_id, **data) -> SchemasPost:
        async with async_session_factory() as session:
            stmt = insert(cls.model).values(author_id=user_id, **data).returning(cls.model)
            result = await session.execute(stmt)
            await session.commit()
            result = result.scalar_one()
            await session.refresh(result)
            return result

    @classmethod
    async def archiving_unarchiving_post(cls, post_id, archived: bool = False):
        async with async_session_factory() as session:
            stmt = update(cls.model).values(is_archived=archived).where(cls.model.id == post_id)
            await session.execute(stmt)
            await session.commit()
