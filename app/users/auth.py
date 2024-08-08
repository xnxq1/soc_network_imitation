from datetime import datetime, timedelta

from jose import jwt, JWTError

from app.config import settings
from fastapi import Response, Request, Depends

from app.users.dao import DaoUser
from app.users.errors import JWTCustomError

class JWTBase:

    @classmethod
    def encode_jwt_token(cls, data: dict) -> str:
        data = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=15)
        data.update({'exp': expire})
        token = jwt.encode(data, key=settings.SECRETKEY, algorithm=settings.ALGORITHM)

        return token

    @classmethod
    def decode_jwt_token(cls, token: str):
        try:
            print(token)
            payload = jwt.decode(token, settings.SECRETKEY, settings.ALGORITHM)
            return payload
        except JWTError as e:
            raise JWTCustomError(message=f'{e}')


class JWTCookies(JWTBase):

    @classmethod
    def set_cookie_jwt(cls, responce: Response, user_id: int) -> str:
        token = cls.encode_jwt_token({'sub': str(user_id)})
        responce.set_cookie(key='access_token', value=token, httponly=True)
        return token


    @classmethod
    def get_cookie_jwt(cls, request: Request):
        token = request.cookies.get('access_token')
        if not token:
            raise JWTCustomError()
        return token


class JWTUser(JWTCookies):
    @classmethod
    def check_expire(cls, payload: dict):
        expire = payload['exp']
        if not expire or int(expire) < datetime.utcnow().timestamp():
            raise JWTCustomError(message='Токен устарел')

    @classmethod
    async def get_curr_user(cls, request: Request):
        token = cls.get_cookie_jwt(request)
        payload = cls.decode_jwt_token(token)
        cls.check_expire(payload)
        sub = payload['sub']
        if not sub:
            raise JWTCustomError(message='Нет такого пользователя')

        user = await DaoUser.get_user_by_id(int(sub))
        if not user:
            raise JWTCustomError(message='Нет такого пользователя')
        return user