from fastapi import Query
from pydantic import BaseModel


class SchemasPost(BaseModel):
    text: str
    likes: int = Query(..., ge=0)
    dislikes: int = Query(..., ge=0)
    author_id: int

class SchemasPostForAdd(BaseModel):
    text: str

