from fastapi import APIRouter, Depends, Response, Request
from app.users.schemas import SchemasUser, SchemasUserForUpdate, \
    SchemasUserWithPost
from app.users.dao import DaoUser
from app.users.service.router_handler import update_user_data_service
from app.auth.auth import JWTUser

router = APIRouter(prefix="/profile", tags=["Profile"])




@router.get("/all", dependencies=[Depends(JWTUser.get_curr_user)])
async def get_all_users() -> list[SchemasUser]:
    return await DaoUser.get_all_users()


@router.get("/me")
async def get_me(user=Depends(JWTUser.get_curr_user)) -> SchemasUserWithPost:
    return user

@router.patch("/changedata")
async def change_data_user(data: SchemasUserForUpdate, user=Depends(JWTUser.get_curr_user)) -> SchemasUser:
    user_data = await update_user_data_service(dict(data), user.id)
    return user_data


