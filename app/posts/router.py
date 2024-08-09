from fastapi import APIRouter, Depends

from app.posts.dao import DaoPost
from app.posts.schemas import SchemasPost, SchemasPostForAdd
from app.posts.service.router_handler import PostHandler
from app.users.auth import JWTUser

router = APIRouter(prefix='/posts', tags=['Posts'])

@router.get("/all", dependencies=[Depends(JWTUser.get_curr_user)])
async def get_all_posts() -> list[SchemasPost]:
    posts = await DaoPost.get_all_posts()
    return posts

@router.post("/add")
async def add_post(post: SchemasPostForAdd, user=Depends(JWTUser.get_curr_user)) -> SchemasPost:
    post = await PostHandler.add_post_service(dict(post), user.id)
    return post