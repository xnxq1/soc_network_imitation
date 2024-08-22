import pytest
from httpx import AsyncClient

from app.tests.conftest import get_content

router_prefix = '/comments'


@pytest.mark.parametrize('comment_id, comment_parent_id, text, status_code',[
    (1, 1, 'tewtwqwre', 200),
    (2, 1, 'tewtwe', 200),
    (100, None, 'tewtwe', 409)
])
async def test_add_comment_to_comment(comment_id, comment_parent_id, text, status_code, authenticate_client: AsyncClient):
    url = f'{router_prefix}/add/comment/{comment_id}'
    response = await authenticate_client.post(url, json={'text': text})
    assert response.status_code == status_code
    if status_code == 200:
        response_text = get_content(response)
        assert response_text.get('parent_comment_id') == comment_parent_id
        assert response_text.get('text') == text



@pytest.mark.parametrize('post_id, text, status_code',[
    (1, 'tewtwe', 200),
    (-1, 'tewtwe', 422),
    (100, 'tewtwe', 406)
])
async def test_add_comment_to_post(post_id, text, status_code, authenticate_client: AsyncClient):
    url = f'{router_prefix}/add/post/{post_id}'
    response = await authenticate_client.post(url, json={'text': text})
    assert response.status_code == status_code
    if status_code == 200:
        response_text = get_content(response)
        assert response_text.get('post_id') == post_id
        assert response_text.get('text') == text




