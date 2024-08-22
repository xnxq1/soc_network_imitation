
import pytest
from httpx import AsyncClient


router_prefix_like = '/like'
router_prefix_dislike = '/dislike'

@pytest.mark.parametrize('post_id, status_code',[
    (3, 200),
    (1, 409),
    (0, 422),
    (55, 409),

])
async def test_like_post(post_id, status_code, authenticate_client: AsyncClient):
    url = f'{router_prefix_like}/post/{post_id}'
    response = await authenticate_client.get(url=url)
    assert response.status_code == status_code


@pytest.mark.parametrize('post_id, status_code',[
    (3, 200),
    (1, 200),
    (0, 422),
    (55, 409),

])
async def test_dislike_post(post_id, status_code, authenticate_client: AsyncClient):
    url = f'{router_prefix_dislike}/post/{post_id}'
    response = await authenticate_client.get(url=url)
    assert response.status_code == status_code



@pytest.mark.parametrize('comment_id, status_code',[
    (2, 200),
    (1, 409),
    (0, 422),
    (55, 409),

])
async def test_like_comment(comment_id, status_code, authenticate_client: AsyncClient):
    url = f'{router_prefix_like}/comment/{comment_id}'
    response = await authenticate_client.get(url=url)
    assert response.status_code == status_code


@pytest.mark.parametrize('comment_id, status_code',[
    (3, 200),
    (1, 200),
    (0, 422),
    (55, 409),

])
async def test_dislike_comment(comment_id, status_code, authenticate_client: AsyncClient):
    url = f'{router_prefix_dislike}/comment/{comment_id}'
    response = await authenticate_client.get(url=url)
    assert response.status_code == status_code