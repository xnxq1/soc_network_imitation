import asyncio
import json
import os

import pytest
from sqlalchemy import insert

from app.db import engine, async_session_factory
from app.models import Base, CustomBase
from app.posts.models import Post, PostStatus
from app.users.models import User
from httpx import AsyncClient, ASGITransport
from app.main import app as fastapi_app
@pytest.fixture(autouse=True, scope='session')
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



# @pytest.fixture(scope='session')
# async def event_loop(request):
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()
#

@pytest.fixture(scope='function')
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url='http://test') as ac:
        yield ac


@pytest.fixture(scope='function')
async def authenticate_client():
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url='http://test') as ac:
        await ac.post(url='auth/login', json={
        'email': 'test@test.com', 'password': 'test'})
        assert ac.cookies.get('access_token') is not None
        yield ac


def get_content(response):
    response_text = response.content
    response_text = json.loads(response_text)
    return response_text


async def check_auth(async_client: AsyncClient, url):
    response = await async_client.get(url=url)
    assert response.status_code == 401

