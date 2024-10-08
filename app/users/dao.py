from sqlalchemy import select, insert, update, asc

from app.db import async_session_factory
from app.posts.models import Post, PostStatus
from app.users.models import User
from sqlalchemy.orm import selectinload, joinedload, contains_eager

class DaoUser:
    model = User


    @classmethod
    async def get_user_by_id(cls, user_id: int):
        async with async_session_factory() as session:
            query = select(cls.model).where(cls.model.id == user_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_user_with_posts(cls, user_id: int) -> model:
        async with async_session_factory() as session:
            query = (
                select(cls.model)
                .options(selectinload(cls.model.posts).selectinload(Post.post_status))

                .where(cls.model.id == user_id)
            )
            result = await session.execute(query)
            user = result.scalar_one_or_none()
            return user



    @classmethod
    async def get_all_users(cls):
        async with async_session_factory() as session:
            query = select(cls.model)
            res = await session.execute(query)
            return res.scalars().all()


    @classmethod
    async def update_user_data(cls, user_id, **data):
        async with async_session_factory() as session:
            stmt = update(cls.model).values(**data).where(cls.model.id == user_id).returning(cls.model)
            result = await session.execute(stmt)
            await session.commit()
            updated_user = result.scalar_one_or_none()
            if updated_user is not None:
                await session.refresh(updated_user)
            return updated_user
