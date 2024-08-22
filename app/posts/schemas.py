from datetime import datetime
from typing import List

from fastapi import Query
from pydantic import BaseModel

from app.comments.schemas import SchemasComment


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


class SchemasPostWithComments(SchemasPost):
    comments: List[SchemasComment]

