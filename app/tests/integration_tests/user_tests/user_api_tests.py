import json

import pytest
from httpx import AsyncClient
from app.tests.conftest import get_content, check_auth
router_prefix = '/profile'




async def test_get_all_users(authenticate_client: AsyncClient, async_client: AsyncClient):
    url = f'{router_prefix}/all'
    response = await authenticate_client.get(url=url)
    assert response.status_code == 200
    response_text = get_content(response)
    for el in response_text:
        assert el.get('hashed_password') is None

    await check_auth(async_client, url)


async def test_get_info_about_me(authenticate_client: AsyncClient, async_client: AsyncClient):
    url = f'{router_prefix}/me'
    response = await authenticate_client.get(url=url)
    assert response.status_code == 200
    response_text = get_content(response)
    assert response_text is not None
    assert response_text.get('email') == 'test@test.com'
    assert response_text.get('hashed_password') is None

    await check_auth(async_client, url)


async def test_get_info_about_me_with_posts(authenticate_client: AsyncClient, async_client: AsyncClient):
    url = f'{router_prefix}/me_with_posts'
    response = await authenticate_client.get(url=url)

    assert response.status_code == 200
    response_text = get_content(response)

    assert response_text is not None
    assert response_text.get('email') == 'test@test.com'
    assert response_text.get('hashed_password') is None

    posts = response_text.get('posts')
    assert posts is not None
    if len(posts) > 0:
        for el in posts:
            assert el.get('post_status') is not None

    await check_auth(async_client, url)


@pytest.mark.parametrize('first_name, last_name, age, status_code',[
    ('test', 'test', 18, 200),
    ('test', 'test', -1, 422),
    ('test', 'tttttttttttttest', 11, 409),
    (None, 'test', 55, 200),
])
async def test_change_data_user(
        first_name, last_name, age, status_code,
        authenticate_client: AsyncClient, async_client: AsyncClient):
    url = f'{router_prefix}/changedata'
    response = await authenticate_client.patch(url=url, json={
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
    })

    assert response.status_code == status_code
    if status_code == 200:
        response_text = get_content(response)
        assert response_text.get('hashed_password') is None
        if first_name is None:
            assert response_text.get('first_name') == 'test'
        else:
            assert response_text.get('first_name') == first_name
        assert response_text.get('last_name') == last_name
        assert response_text.get('age') == age
