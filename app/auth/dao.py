from app.db import async_session_factory
from app.users.models import User
from sqlalchemy import select, insert
class DaoAuth:
    model = User

    @classmethod
    async def get_user_by_email(cls, email: str) -> model:
        async with async_session_factory() as session:
            query = select(cls.model).where(cls.model.email == email)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add_user_to_db(cls, **data):
        async with async_session_factory() as session:
            stmt = insert(cls.model).values(**data).returning(cls.model.id)

            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()