from typing import List

from pydantic import BaseModel


class SchemasCommentForAdd(BaseModel):
    text: str

class SchemasComment(BaseModel):
    id: int
    text: str
    likes: int
    dislikes: int
    user_id: int
    child_comments: List['SchemasComment'] = None

