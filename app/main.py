
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from fastapi.security import APIKeyCookie
from app.users.router import router as router_user
from app.posts.router import router as router_post
from app.auth.router import router as router_auth
from app.likes.router import router as router_like
from app.redis_conn import redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis.start_connection()
    yield
    await redis.close_connection()


app = FastAPI(lifespan=lifespan)
app.include_router(router_auth)
app.include_router(router_user)
app.include_router(router_post)
app.include_router(router_like)

