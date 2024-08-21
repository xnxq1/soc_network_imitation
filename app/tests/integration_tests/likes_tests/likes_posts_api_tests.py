
import pytest
from httpx import AsyncClient


router_prefix_like = '/like/post'
router_prefix_dislike = '/dislike/post'

@pytest.mark.parametrize('post_id, status_code',[
    (3, 200),
    (1, 409),
    (0, 422),
    (55, 409),

])
async def test_like_post(post_id, status_code, authenticate_client: AsyncClient):
    url = f'{router_prefix_like}/{post_id}'
    response = await authenticate_client.get(url=url)
    assert response.status_code == status_code


@pytest.mark.parametrize('post_id, status_code',[
    (3, 200),
    (1, 200),
    (0, 422),
    (55, 409),

])
async def test_dislike_post(post_id, status_code, authenticate_client: AsyncClient):
    url = f'{router_prefix_dislike}/{post_id}'
    response = await authenticate_client.get(url=url)
    assert response.status_code == status_code