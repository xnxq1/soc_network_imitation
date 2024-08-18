from app.errors import BaseCustomError


class ValidationError(BaseCustomError):
    message = "Не правильно введены данные"
    status_code = 409
