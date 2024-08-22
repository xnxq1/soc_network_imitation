import pytest

from app.comments.dao import DaoComment


@pytest.mark.parametrize('comment_id, exists',[
    (1, True),
    (10, False),
    (2, True),
])
async def test_get_comment_by_id(comment_id, exists):
    comment = await DaoComment.get_comment_by_id(comment_id)
    if exists:
        assert comment is not None
    else:
        assert comment is None




@pytest.mark.parametrize('post_id, parent_comment_id, text, user_id',[
    (1, None, 'tetwt', 1),
    (None, 2,  'tetwt', 1),
])
async def test_add_comment(post_id, parent_comment_id, text, user_id):
    comment = await DaoComment.add_comment(post_id=post_id, parent_comment_id=parent_comment_id, text=text, user_id=user_id)
    assert comment.post_id == post_id
    assert comment.parent_comment_id == parent_comment_id
    assert comment.text == text
    assert comment.user_id == user_id
