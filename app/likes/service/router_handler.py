from app.likes.dao import DaoLike
from app.likes.errors import ThisPostLikedError
from app.redis_conn import redis

async def check_like_user(user_id: int, post_id: int):
    liked_this_post = await DaoLike.check_like_user(user_id, post_id)
    if liked_this_post is not None:
        raise ThisPostLikedError()
    await redis.set(f'user_likes_{user_id}', post_id)
    print(await redis.get(f'user_likes_{user_id}'))