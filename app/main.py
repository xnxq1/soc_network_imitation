
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.comments.models import Comment
from app.likes.models import LikePost, LikeComment
from app.posts.models import Post
from app.users.router import router as router_user
from app.posts.router import router as router_post
from app.auth.router import router as router_auth
from app.likes.router import router_like, router_dislike
from app.comments.router import router as router_comment
from app.redis_conn import redis_post, redis_comm
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.tasks import count_like

scheduler = AsyncIOScheduler()
scheduler.add_job(count_like, IntervalTrigger(seconds=10), kwargs={
    'main_model': Post, 'like_model': LikePost, 'target_column': 'post_id','status': 'like'})
scheduler.add_job(count_like, IntervalTrigger(seconds=10), kwargs={
    'main_model': Post, 'like_model': LikePost, 'target_column': 'post_id','status': 'dislike'})
scheduler.add_job(count_like, IntervalTrigger(seconds=10), kwargs={
    'main_model': Comment, 'like_model': LikeComment, 'target_column': 'comment_id','status': 'like'})
scheduler.add_job(count_like, IntervalTrigger(seconds=10), kwargs={
    'main_model': Comment, 'like_model': LikeComment, 'target_column': 'comment_id','status': 'dislike'})

@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_post.start_connection()
    await redis_comm.start_connection()
    scheduler.start()
    yield
    await redis_post.close_connection()
    await redis_comm.close_connection()






app = FastAPI(lifespan=lifespan)

app.include_router(router_auth)
app.include_router(router_user)
app.include_router(router_post)
app.include_router(router_like)
app.include_router(router_dislike)
app.include_router(router_comment)


