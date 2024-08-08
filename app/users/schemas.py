from fastapi import Query
from pydantic import BaseModel, EmailStr


class SchemasUserForAuth(BaseModel):
    email: EmailStr
    password: str


class SchemasUserForRegister(SchemasUserForAuth):

    first_name: str | None
    last_name: str | None
    age: int = Query(..., gt=0)


class SchemasUser(BaseModel):
    first_name: str | None
    last_name: str | None
    fullname: str
    age: int
    email: EmailStr