from app.comments.dao import DaoComment
from app.comments.errors import NoneCommentError


async def check_parent_comment_id(parent_comment_id: int) -> int:
    parent_comment = await DaoComment.get_comment_by_id(parent_comment_id)
    if parent_comment is None:
        raise NoneCommentError()

    if parent_comment.parent_comment_id is not None:
        return parent_comment.parent_comment_id
    else:
        return parent_comment.id
