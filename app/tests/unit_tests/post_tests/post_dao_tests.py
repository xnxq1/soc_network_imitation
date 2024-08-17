import pytest

from app.posts.dao import DaoPost


async def test_get_all_posts():
    posts = await DaoPost.get_all_posts()
    assert posts is not None
    for el in posts:
        assert isinstance(el, DaoPost.model)


@pytest.mark.parametrize('post_id, exists',[
    (1, True),
    (2, True),
    (1010, False)
])
async def test_get_post_by_id(post_id, exists):
    post = await DaoPost.get_post_by_id(post_id)

    if exists:
        assert post is not None
        assert post.id == post_id
    else:
        assert post is None

@pytest.mark.parametrize('user_id, text',[
    (1, 'text 1'),
    (1, 'text 2'),
])
async def test_add_post(user_id, text):
    post = await DaoPost.add_post(user_id, text=text)
    assert post is not None
    assert post.text == text
    assert post.author_id == user_id


@pytest.mark.parametrize('post_id, archived',[
    (1, True),
    (1, False),
])
async def test_archiving_unarchiving_post(post_id, archived):
    await DaoPost.archiving_unarchiving_post(post_id, archived)
    post_status = await DaoPost.get_post_status_by_id(post_id)
    assert post_status.is_archived == archived
    assert post_status.id == post_id

