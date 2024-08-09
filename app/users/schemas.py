from fastapi import Query
from pydantic import BaseModel, EmailStr

from app.posts.models import Post
from app.posts.schemas import SchemasPost


class SchemasUserForAuth(BaseModel):
    email: EmailStr
    password: str


class SchemasUserForRegister(SchemasUserForAuth):

    first_name: str = None
    last_name: str = None
    age: int = Query(..., gt=0)


class SchemasUser(BaseModel):
    first_name: str | None
    last_name: str | None
    fullname: str
    age: int
    email: EmailStr
    posts: list[SchemasPost]


class SchemasUserForUpdate(BaseModel):

    first_name: str = None
    last_name: str = None
    age: int | None = Query(..., gt=0)
