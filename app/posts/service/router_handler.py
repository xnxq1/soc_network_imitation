from app.posts.dao import DaoPost
from app.posts.errors import NonePostError


class PostHandler:

    @staticmethod
    async def add_post_service(post: dict, user_id: int):
        if len(post['text']) == 0:
            raise NonePostError()
        result_post = await DaoPost.add_post(user_id, **post)
        return result_post