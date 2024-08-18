from app.posts.dao import DaoPost
from app.posts.errors import NonePostError, NotTheAuthorError, WrongStatusError, WrongPostError


class PostHandler:

    @staticmethod
    async def add_post_service(post: dict, user_id: int):
        if post.get('text') is None or len(post['text']) == 0:
            raise WrongPostError()
        result_post = await DaoPost.add_post(user_id, **post)
        return result_post

    @staticmethod
    async def change_status_archive_service(post_id: int, user_id: int, archived: bool = False):
        post = await DaoPost.get_post_by_id(post_id)
        if not post:
            raise NonePostError()
        post = post.__dict__
        if post['author_id'] != user_id:
            raise NotTheAuthorError()

        await DaoPost.archiving_unarchiving_post(post_id=post_id, archived=archived)