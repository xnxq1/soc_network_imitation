from fastapi import APIRouter, Query, Depends, Path

from app.auth.auth import JWTUser
from app.likes.service.router_handler import check_like_user

router = APIRouter()


@router.get("/like/{post_id}")
async def like_post(post_id: int = Path(..., title="ID поста", ge=1), user=Depends(JWTUser.get_curr_user)):
    return await check_like_user(user.id, post_id)