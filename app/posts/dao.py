from sqlalchemy import select, insert, update
from sqlalchemy.orm import joinedload

from app.db import async_session_factory
from app.posts.models import Post, PostStatus
from app.posts.schemas import SchemasPost


class DaoPost:
    model = Post
    model_status = PostStatus
    @classmethod
    async def get_all_posts(cls, archived: bool = False):
        async with async_session_factory() as session:
            query = (select(cls.model)
                     .join(cls.model_status, cls.model_status.id == cls.model.id)
                     .where(cls.model_status.is_archived == archived))
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_post_by_id(cls, post_id):
        async with async_session_factory() as session:
            query = select(cls.model).where(cls.model.id == post_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()


    @classmethod
    async def add_post(cls, user_id, **data) -> SchemasPost:
        async with async_session_factory() as session:
            stmt = insert(cls.model).values(author_id=user_id, **data).returning(cls.model)
            result = await session.execute(stmt)
            await session.commit()
            result = result.scalar_one()
            await session.refresh(result)
            await DaoPost.add_post_status(result.id)

            return result

    @classmethod
    async def archiving_unarchiving_post(cls,post_id, archived: bool = False):
        async with async_session_factory() as session:
            stmt = update(cls.model_status).values(is_archived=archived).where(cls.model_status.id == post_id)
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def add_post_status(cls, post_id):
        async with async_session_factory() as session:
            stmt = insert(cls.model_status).values(id=post_id, is_archived=False, is_changed=False)
            await session.execute(stmt)
            await session.commit()
