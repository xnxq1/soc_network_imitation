from fastapi import Query
from pydantic import BaseModel, EmailStr

from app.posts.schemas import SchemasPost, SchemasPostForUser


class SchemasUserWithPost(BaseModel):
    first_name: str | None
    last_name: str | None
    fullname: str
    age: int
    email: EmailStr
    posts: list[SchemasPostForUser]


class SchemasUserForUpdate(BaseModel):

    first_name: str = None
    last_name: str = None
    age: int | None = Query(..., gt=0)

class SchemasUser(BaseModel):
    first_name: str | None
    last_name: str | None
    fullname: str
    age: int
    email: EmailStr

