from datetime import datetime

from fastapi import Query
from pydantic import BaseModel


class SchemasPost(BaseModel):
    id: int
    text: str
    likes: int = Query(..., ge=0)
    dislikes: int = Query(..., ge=0)
    author_id: int
    created_at: datetime
class SchemasPostForAdd(BaseModel):
    text: str


class SchemasPostForUser(SchemasPost):
    is_archived: bool
    is_changed: bool

