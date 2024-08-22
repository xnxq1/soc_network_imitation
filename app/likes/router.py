from fastapi import APIRouter, Depends, Path

from app.auth.auth import JWTUser
from app.likes.dao import DaoLikePost, DaoLikeComment
from app.likes.service.router_handler import LikeHandler
from app.likes.models import LikeStatus
router_like = APIRouter(prefix='/like', tags=['Like'])
router_dislike = APIRouter(prefix='/dislike', tags=['Dislike'])

@router_like.get("/post/{post_id}")
async def like_post(post_id: int = Path(..., title="ID поста", ge=1), user=Depends(JWTUser.get_curr_user)):
    like_handler = LikeHandler(DaoLikePost)
    return await like_handler.like_dislike(user_id=user.id, post_id=post_id, status=LikeStatus.like)

@router_dislike.get("/post/{post_id}")
async def dislike_post(post_id: int = Path(..., title="ID поста", ge=1), user=Depends(JWTUser.get_curr_user)):
    like_handler = LikeHandler(DaoLikePost)
    return await like_handler.like_dislike(user_id=user.id, post_id=post_id, status=LikeStatus.dislike)


@router_like.get("/comment/{comment_id}")
async def like_comment(comment_id: int = Path(..., title="ID комментария", ge=1), user=Depends(JWTUser.get_curr_user)):
    like_handler = LikeHandler(DaoLikeComment)
    return await like_handler.like_dislike(user_id=user.id, comment_id=comment_id, status=LikeStatus.like)

@router_dislike.get("/comment/{comment_id}")
async def dislike_comment(comment_id: int = Path(..., title="ID комментария", ge=1), user=Depends(JWTUser.get_curr_user)):
    like_handler = LikeHandler(DaoLikeComment)
    return await like_handler.like_dislike(user_id=user.id, comment_id=comment_id, status=LikeStatus.dislike)

@router_like.get("/all_likes_comments_posts")
async def all_1():
    return await DaoLikePost.get_all()

@router_like.get("/all_likes_comments")
async def all_2():
    return await DaoLikeComment.get_all()