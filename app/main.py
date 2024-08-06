from fastapi import Depends, FastAPI
from fastapi.security import APIKeyCookie
from app.users.router import router as router_user
app = FastAPI()
app.include_router(router_user)
