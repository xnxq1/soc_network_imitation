from fastapi import APIRouter, Depends, Path

from app.auth.auth import JWTUser
from app.likes.likes_post.dao import DaoLike
from app.likes.likes_post.service.router_handler import like_dislike_post
from app.likes.likes_post.models import LikeStatus
router_like = APIRouter(prefix='/like', tags=['Like'])
router_dislike = APIRouter(prefix='/dislike', tags=['Dislike'])

@router_like.get("/post/{post_id}")
async def like_post(post_id: int = Path(..., title="ID поста", ge=1), user=Depends(JWTUser.get_curr_user)):
    return await like_dislike_post(user.id, post_id, LikeStatus.like)

@router_dislike.get("/post/{post_id}")
async def dislike_post(post_id: int = Path(..., title="ID поста", ge=1), user=Depends(JWTUser.get_curr_user)):
    return await like_dislike_post(user.id, post_id, LikeStatus.dislike)


@router_like.get("/temp")
async def xxx():
    return await DaoLike.get_all()