from fastapi import Query
from pydantic import BaseModel, EmailStr


class SchemasUserForRegister(BaseModel):

    first_name: str | None
    last_name: str | None
    age: int = Query(..., gt=0)
    email: EmailStr
    password: str