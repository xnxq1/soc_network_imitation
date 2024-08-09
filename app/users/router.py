from fastapi import APIRouter, HTTPException, Depends, Response, Request
from app.users.schemas import SchemasUserForRegister, SchemasUser, SchemasUserForAuth
from app.users.dao import DaoUser
from app.users.service.hasher import Hasher
from app.users.service.router_handler import Auth_user
from app.users.errors import ThereIsAUserError, ValidationError, WrongDataForAuthError
from app.users.auth import JWTBase, JWTCookies, JWTUser

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
async def register_user(responce: Response, user_data: SchemasUserForRegister) -> str:

    user_id = await Auth_user.register_user_service(dict(user_data))
    return JWTCookies.set_cookie_jwt(responce, user_id)


@router.post("/login")
async def login_user(responce: Response, user: SchemasUserForAuth) -> str:

    user_id = await Auth_user.login_user_service(dict(user))
    return JWTCookies.set_cookie_jwt(responce, user_id)


@router.post("/logout")
async def logout_user(request: Request, responce: Response) -> None:
    JWTCookies.delete_cookie_jwt(request, responce)


@router.get("/all", dependencies=[Depends(JWTUser.get_curr_user)])
async def get_all_users() -> list[SchemasUser]:
    return await DaoUser.get_all_users()


@router.get("/me")
async def get_all_users(user=Depends(JWTUser.get_curr_user)) -> SchemasUser:
    return user

