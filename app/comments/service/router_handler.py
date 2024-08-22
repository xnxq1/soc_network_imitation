from app.comments.dao import DaoComment
from app.comments.errors import NoneCommentError
from app.posts.errors import NonePostError


async def exist_comment_by_id(comment_id: int):
    comment = await DaoComment.get_comment_by_id(comment_id)
    if comment is None:
        raise NoneCommentError()
    return comment


async def check_parent_comment_id(comment_id: int) -> int:
    parent_comment = await exist_comment_by_id(comment_id)
    if parent_comment.parent_comment_id is not None:
        return parent_comment.parent_comment_id
    else:
        return parent_comment.id


async def add_comment_to_post_service(text: str, post_id: int, user_id: int):
    try:
        result = await DaoComment.add_comment(text=text, post_id=post_id, user_id=user_id)
        return result
    except:
        raise NonePostError()


