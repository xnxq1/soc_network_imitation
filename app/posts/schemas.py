from datetime import datetime

from fastapi import Query
from pydantic import BaseModel


class SchemasPostStatus(BaseModel):

    is_archived: bool
    is_changed: bool


class SchemasPost(BaseModel):
    id: int
    text: str
    likes: int = Query(..., ge=0)
    dislikes: int = Query(..., ge=0)
    author_id: int
    created_at: datetime


class SchemasPostWithStatus(SchemasPost):
    post_status: list[SchemasPostStatus]


class SchemasPostForAdd(BaseModel):
    text: str


class SchemasPostForUser(SchemasPostWithStatus):
    pass



