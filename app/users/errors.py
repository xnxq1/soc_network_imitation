from fastapi import HTTPException


class BaseCustomError(Exception):
    message = "Unknown"
    status_code = 500
    def __init__(self):
        raise HTTPException(status_code=self.status_code, detail=self.message)


class ThereIsAUserError(BaseCustomError):
    message = "Такой пользователь уже есть"
    status_code = 409




class ValidationError(BaseCustomError):
    message = "Не правильно введены данные"
    status_code = 409



class WrongDataForAuthError(BaseCustomError):
    message = "Неправильно введен пароль или почта"
    status_code = 401




class JWTCustomError(BaseCustomError):
    message = "У вас нет jwt токена или он неправильный"
    status_code = 401

    def __init__(self, message: str = None, status_code: str = None):
        self.message = message if message else self.message
        self.status_code = status_code if status_code else self.status_code
        super().__init__()


