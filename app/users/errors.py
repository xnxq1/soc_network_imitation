from fastapi import HTTPException


class ThereIsAUserError(Exception):
    message = "Такой пользователь уже есть"
    status_code = 409

    def __init__(self):
        raise HTTPException(status_code=self.status_code, detail=self.message)


class ValidationError(Exception):
    message = "Не правильно введены данные"
    status_code = 409

    def __init__(self):
        raise HTTPException(status_code=self.status_code, detail=self.message)


class WrongDataForAuthError(Exception):
    message = "Неправильно введен пароль или почта"
    status_code = 401

    def __init__(self):
        raise HTTPException(status_code=self.status_code, detail=self.message)


class JWTCustomError(Exception):
    message = "У вас нет jwt токена или он неправильный"
    status_code = 401

    def __init__(self, message: str = None, status_code: str = None):
        msg = message if message else self.message
        code = status_code if status_code else self.status_code
        raise HTTPException(status_code=code, detail=msg)


