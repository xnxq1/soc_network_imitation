from fastapi import APIRouter, Depends, Path

from app.auth.auth import JWTUser
from app.comments.dao import DaoComment
from app.comments.schemas import SchemasCommentForAdd
from app.comments.service.router_handler import check_parent_comment_id, add_comment_to_post_service

router = APIRouter(prefix='/comments', tags=['Comments'])

@router.post('/add/post/{post_id}')
async def add_comment_to_post(body: SchemasCommentForAdd, post_id: int = Path(title='ID поста', ge=1), user=Depends(JWTUser.get_curr_user)):
    result = await add_comment_to_post_service(text=body.text, post_id=post_id, user_id=user.id)
    return result


@router.post('/add/comment/{comment_id}')
async def add_comment_to_comment(body: SchemasCommentForAdd, comment_id: int = Depends(check_parent_comment_id), user=Depends(JWTUser.get_curr_user)):
    result = await DaoComment.add_comment(text=body.text, parent_comment_id=comment_id, user_id=user.id)
    return result


@router.get("/temp")
async def xxx():
    return await DaoComment.get_all()