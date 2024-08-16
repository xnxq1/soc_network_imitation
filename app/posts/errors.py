from app.errors import BaseCustomError


class WrongPostError(BaseCustomError):
    status_code = 406
    message = 'Пост не должен быть пустым'


class NonePostError(BaseCustomError):
    status_code = 406
    message = 'Поста с таким id не существует'


class NotTheAuthorError(BaseCustomError):
    status_code = 406
    message = 'Вы не автор поста'


class WrongStatusError(BaseCustomError):
    status_code = 406
    message = 'Пост уже имеет данный статус'