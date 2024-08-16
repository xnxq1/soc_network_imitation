import asyncio
import json
import os

import pytest
from sqlalchemy import insert

from app.db import engine, async_session_factory
from app.models import Base, CustomBase
from app.posts.models import Post, PostStatus
from app.users.models import User


@pytest.fixture()
async def prepare_db():
    assert os.environ['MODE'] == 'TEST'
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def convert_json(model: str):
        with open(f'app/tests/{model}.json') as f:
            return json.load(f)

    users = convert_json('users')
    posts = convert_json('posts')
    poststatus = convert_json('poststatus')
    async with async_session_factory() as session:
        users_query = insert(User).values(users)
        posts_query = insert(Post).values(posts)
        poststatus_query = insert(PostStatus).values(poststatus)
        await session.execute(users_query)
        await session.execute(posts_query)
        await session.execute(poststatus_query)
        await session.commit()



@pytest.fixture()
async def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
