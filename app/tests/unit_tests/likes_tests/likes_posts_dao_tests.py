
import pytest

from app.likes.dao import DaoLikePost
from app.likes.models import LikeStatus

@pytest.mark.parametrize('user_id, post_id, status, normal_form',[
    (1, 4, LikeStatus.like, True),
    (1, 10, LikeStatus.like, False),
    (1, 1, LikeStatus.like, False),
    (100, 1, LikeStatus.like, False),
])
async def test_like_dislike_post(user_id, post_id, status, normal_form):
    try:
        await DaoLikePost.like_dislike(user_id=user_id, post_id=post_id, status=status)
        if not normal_form:
            assert False
    except:
        if normal_form:
            assert False



@pytest.mark.parametrize('user_id, post_id, exists',[
    (1, 1, True),
    (2, 3, True),
    (1, 100, False),
])
async def test_check_like_post(user_id, post_id, exists):
    like = await DaoLikePost.check_like(user_id=user_id, post_id=post_id)
    if exists:
        assert like is not None
        assert like.post_id == post_id
        assert like.user_id == user_id
    else:
        assert like is None