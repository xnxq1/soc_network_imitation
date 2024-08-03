from fastapi import FastAPI
from app.db import async_session_factory
from app.users.models import User
from sqlalchemy import delete, insert, update

app = FastAPI()

@app.get("/")
async def root():
    async with async_session_factory() as session:
        stmt = insert(User).values(
            {'first_name': 'vasya',
             'last_name': 'pupkin',
             'age': -11,
             'email': '123123',
             'hashed_password': '123', }
        )

        await session.execute(stmt)
        await session.commit()