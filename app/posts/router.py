from fastapi import APIRouter, Depends

from app.posts.dao import DaoPost
from app.posts.schemas import SchemasPost, SchemasPostForAdd
from app.posts.service.router_handler import PostHandler
from app.auth.auth import JWTUser

router = APIRouter(prefix='/posts', tags=['Posts'])


@router.get("/all", dependencies=[Depends(JWTUser.get_curr_user)])
async def get_all_posts() -> list[SchemasPost]:
    posts = await DaoPost.get_all_posts()
    return posts


@router.get("/archivedposts", dependencies=[Depends(JWTUser.get_curr_user)])
async def get_archived_posts() -> list[SchemasPost]:
    posts = await DaoPost.get_all_posts(archived=True)
    return posts


@router.post("/add")
async def add_post(post: SchemasPostForAdd, user=Depends(JWTUser.get_curr_user)) -> SchemasPost:
    post = await PostHandler.add_post_service(dict(post), user.id)
    return post


@router.get("/archivingpost/{post_id}", dependencies=[Depends(JWTUser.get_curr_user)])
async def archiving_post(post_id: int):
    await DaoPost.archiving_unarchiving_post(post_id=post_id, archived=True)


@router.get("/unarchivingpost/{post_id}", dependencies=[Depends(JWTUser.get_curr_user)])
async def unarchiving_post(post_id: int):
    await DaoPost.archiving_unarchiving_post(post_id=post_id, archived=False)
