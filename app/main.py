from fastapi import Depends, FastAPI
from fastapi.security import APIKeyCookie
from app.users.router import router as router_user
from app.posts.router import router as router_post
from app.auth.router import router as router_auth
app = FastAPI()
app.include_router(router_auth)
app.include_router(router_user)
app.include_router(router_post)

