from app.likes.likes_post.dao import DaoLike
from app.likes.likes_post.errors import ThisPostLikedError, NonePostForLikeError
from app.likes.likes_post.models import LikeStatus

async def like_dislike_post(user_id: int, post_id: int, status: LikeStatus):
    liked_this_post = await DaoLike.check_like_post(user_id, post_id)
    if liked_this_post is None:
        try:
            await DaoLike.like_dislike_post(user_id, post_id, status)
        except:
            raise NonePostForLikeError()
    elif liked_this_post.status == status:
        raise ThisPostLikedError()
    else:
        await DaoLike.change_status(user_id, post_id, status)