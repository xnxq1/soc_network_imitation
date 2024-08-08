from sqlalchemy import select, insert

from app.db import async_session_factory
from app.users.models import User
from app.users.schemas import SchemasUserForRegister
class DaoUser:
    model = User

    @classmethod
    async def get_user_by_email(cls, email: str) -> model:
        async with async_session_factory() as session:
            query = select(cls.model).where(cls.model.email == email)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_user_by_id(cls, user_id: int) -> model:
        async with async_session_factory() as session:
            query = select(cls.model).where(cls.model.id == user_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add_user_to_db(cls, **data):
        async with async_session_factory() as session:
            stmt = insert(cls.model).values(**data).returning(cls.model.id)

            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()

    @classmethod
    async def get_all_users(cls):
        async with async_session_factory() as session:
            query = select(cls.model)
            res = await session.execute(query)
            return res.scalars().all()