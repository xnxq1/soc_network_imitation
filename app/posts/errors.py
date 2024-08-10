from app.errors import BaseCustomError


class NonePostError(BaseCustomError):
    status_code = 406
    message = 'Пост не должен быть пустым'


class NotTheAuthorError(BaseCustomError):
    status_code = 406
    message = 'Вы не автор поста'


class WrongStatusError(BaseCustomError):
    status_code = 406
    message = 'Пост уже имеет данный статус'