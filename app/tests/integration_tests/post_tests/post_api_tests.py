import pytest
from httpx import AsyncClient

from app.tests.conftest import get_content, check_auth

router_prefix = '/posts'


async def test_get_all_posts(authenticate_client: AsyncClient, async_client: AsyncClient):
    url = f'{router_prefix}/all'
    response = await authenticate_client.get(url=url)
    assert response.status_code == 200
    response_text = get_content(response)
    assert len(response_text) == 3

    await check_auth(async_client, url)


async def test_get_archived_posts(authenticate_client: AsyncClient, async_client: AsyncClient):
    url = f'{router_prefix}/archivedposts'
    response = await authenticate_client.get(url=url)
    assert response.status_code == 200
    response_text = get_content(response)
    assert len(response_text) == 1

    await check_auth(async_client, url)


@pytest.mark.parametrize('text, status_code',[
    ('fassafasfa', 200),
    (None, 422),
    ('', 406)
])
async def test_add_post(text, status_code, authenticate_client: AsyncClient):
    url = f'{router_prefix}/add'
    response = await authenticate_client.post(url=url, json={
        'text': text
    })
    assert response.status_code == status_code
    if status_code == 200:
        response_text = get_content(response)
        assert response_text.get('id') == 5
        assert response_text.get('author_id') == 1
    # response_text = get_content(response)
    # assert len(response_text) == 1



@pytest.mark.parametrize('post_id, status_code', [
    ('1', 200),
    ('100', 406),
    ('3', 406),
])
async def test_archiving_post(post_id, status_code, authenticate_client: AsyncClient,):
    url = f'{router_prefix}/archivingpost/{post_id}'
    response = await authenticate_client.get(url=url)
    assert response.status_code == status_code


@pytest.mark.parametrize('post_id, status_code', [
    ('1', 200),
    ('100', 406),
    ('3', 406),
])
async def test_unarchiving_post(post_id, status_code, authenticate_client: AsyncClient,):
    url = f'{router_prefix}/unarchivingpost/{post_id}'
    response = await authenticate_client.get(url=url)
    assert response.status_code == status_code