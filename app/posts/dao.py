from sqlalchemy import select, insert

from app.db import async_session_factory
from app.posts.models import Post
from app.posts.schemas import SchemasPost


class DaoPost:
    model = Post
    @classmethod
    async def get_all_posts(cls):
        async with async_session_factory() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def add_post(cls, user_id, **data) -> SchemasPost:
        async with async_session_factory() as session:
            stmt = insert(cls.model).values(author_id=user_id, **data).returning(cls.model)
            result = await session.execute(stmt)
            await session.commit()
            result = result.scalar_one()
            await session.refresh(result)
            return result