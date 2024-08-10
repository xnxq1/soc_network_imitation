from fastapi import APIRouter, Depends, Response, Request
from app.auth.schemas import SchemasUserForRegister, SchemasUserForAuth
from app.auth.service.router_handler import Auth_user
from app.auth.auth import JWTCookies

router = APIRouter(prefix="/auth", tags=["auth"])



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