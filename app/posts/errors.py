from app.errors import BaseCustomError


class NonePostError(BaseCustomError):
    status_code = 406
    message = 'Пост не должен быть пустым'